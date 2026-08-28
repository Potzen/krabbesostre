#!/usr/bin/env python3
"""Henter Google-anmeldelser og skriver dem ind i index.html.

To trin, som kan køres hver for sig:

  python3 tools/hent_anmeldelser.py --hent     henter fra Google til anmeldelser.json
  python3 tools/hent_anmeldelser.py --byg      skriver anmeldelser.json ind i index.html
  python3 tools/hent_anmeldelser.py            gør begge dele

Til hentningen skal to ting sættes som miljøvariabler, så nøglen aldrig
havner i koden:

  export GOOGLE_API_NOEGLE="..."      nøgle fra Google Cloud, med Places API slået til
  export GOOGLE_PLACE_ID="..."        findes med Googles Place ID Finder

Bemærk: Places API giver højst fem anmeldelser, og Google vælger selv hvilke.
Googles vilkår tillader ikke, at data gemmes permanent, så scriptet skal køre
regelmæssigt, fx en gang i døgnet. Fryser man anmeldelserne fast for altid,
er man uden for vilkårene.

Stjernerne må IKKE lægges i sidens strukturerede data. Google forbyder, at man
mærker anmeldelser op, som man selv har hentet fra andre steder.
"""
import json, os, sys, html, urllib.request, urllib.parse
from datetime import date, datetime

HER = os.path.dirname(os.path.abspath(__file__))
ROD = os.path.dirname(HER)
DATA = os.path.join(ROD, "anmeldelser.json")
SIDE = os.path.join(ROD, "index.html")

START = "<!-- ANMELDELSER:START -->"
SLUT = "<!-- ANMELDELSER:SLUT -->"

MAANED = ["januar", "februar", "marts", "april", "maj", "juni",
          "juli", "august", "september", "oktober", "november", "december"]


def hent():
    noegle = os.environ.get("GOOGLE_API_NOEGLE")
    place = os.environ.get("GOOGLE_PLACE_ID")
    if not noegle or not place:
        sys.exit("Sæt GOOGLE_API_NOEGLE og GOOGLE_PLACE_ID først. Se toppen af filen.")

    url = "https://places.googleapis.com/v1/places/" + urllib.parse.quote(place)
    felter = "displayName,rating,userRatingCount,googleMapsUri,reviews"
    req = urllib.request.Request(url, headers={
        "X-Goog-Api-Key": noegle,
        "X-Goog-FieldMask": felter,
    })
    with urllib.request.urlopen(req, timeout=20) as r:
        svar = json.load(r)

    ud = []
    for a in svar.get("reviews", []):
        tekst = (a.get("originalText") or a.get("text") or {}).get("text", "").strip()
        if not tekst:
            continue
        ud.append({
            "navn": a.get("authorAttribution", {}).get("displayName", "").strip(),
            "stjerner": a.get("rating"),
            "tekst": tekst,
            "tidspunkt": a.get("publishTime", ""),
        })

    data = {
        "_om": "Hentet automatisk. Ret ikke i hånden.",
        "kilde": "Google",
        "profil": svar.get("googleMapsUri", ""),
        "opdateret": date.today().isoformat(),
        "score": svar.get("rating"),
        "antal": svar.get("userRatingCount"),
        "anmeldelser": ud,
    }
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"hentede {len(ud)} anmeldelser, score {data['score']} af {data['antal']}")


def dansk_dato(iso):
    """2026-07-14T... bliver til juli 2026"""
    if not iso:
        return ""
    try:
        d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return f"{MAANED[d.month - 1]} {d.year}"
    except Exception:
        return ""


def byg():
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)
    liste = data.get("anmeldelser") or []

    if not liste:
        blok = "\n"
        print("ingen anmeldelser i anmeldelser.json, afsnittet står tomt")
    else:
        kort = []
        for a in liste:
            navn = html.escape(a.get("navn") or "Gæst")
            tekst = html.escape((a.get("tekst") or "").strip())
            naar = html.escape(dansk_dato(a.get("tidspunkt")))
            st = a.get("stjerner")
            stjerner = ""
            if isinstance(st, (int, float)):
                hele = int(round(st))
                stjerner = (f'<span class="anm__stjerner" role="img" '
                            f'aria-label="{hele} ud af 5 stjerner">'
                            + "★" * hele + "☆" * (5 - hele) + "</span>")
            kort.append(
                '      <figure class="anm__kort">\n'
                f'        {stjerner}\n'
                f'        <blockquote>{tekst}</blockquote>\n'
                f'        <figcaption>{navn}'
                + (f'<span class="anm__naar">{naar}</span>' if naar else "")
                + "</figcaption>\n"
                "      </figure>"
            )

        hoved = ""
        if data.get("score") and data.get("antal"):
            score = str(data["score"]).replace(".", ",")
            hoved = (f'    <p class="anm__hoved">{score} af 5 '
                     f'på baggrund af {data["antal"]} anmeldelser på Google</p>\n')

        profil = html.escape(data.get("profil") or "")
        link = (f'    <p class="anm__kilde"><a href="{profil}" target="_blank" '
                'rel="noopener">Anmeldelserne kommer fra Google</a></p>\n') if profil else ""

        blok = (
            '\n<section class="section anmeldelser" aria-labelledby="anm-titel">\n'
            '  <div class="wrap">\n'
            '    <p class="eyebrow rv">Gæsterne</p>\n'
            '    <h2 class="rv" id="anm-titel">Sagt ved bordene</h2>\n'
            + hoved +
            '    <div class="anm__liste rv">\n'
            + "\n".join(kort) + "\n"
            "    </div>\n"
            + link +
            "  </div>\n"
            "</section>\n"
        )
        print(f"skrev {len(liste)} anmeldelser ind i index.html")

    with open(SIDE, encoding="utf-8") as f:
        s = f.read()
    i, j = s.index(START), s.index(SLUT)
    s = s[:i + len(START)] + blok + s[j:]
    with open(SIDE, "w", encoding="utf-8") as f:
        f.write(s)


if __name__ == "__main__":
    arg = sys.argv[1:] or ["--hent", "--byg"]
    if "--hent" in arg:
        hent()
    if "--byg" in arg:
        byg()
