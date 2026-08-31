# Krabbesøstre, hjemmeside

Statisk side. Ingen build, ingen database, ingen cookies. Læg mappens indhold
op på en hvilken som helst webhost, så virker den.

```
index.html          forsiden
nytaarskasse.html   nytårskassen
kontrolrapport.html fødevarekontrollen, lovpligtig visning af smileyrapporten
stil.css            designsystemet, deles af alle sider
robots.txt          giver alle robotter adgang, også AI, og peger på sitemap
sitemap.xml         de tre sider, indsendes i Google Search Console
llms.txt            kort beskrivelse i almindeligt sprog til sprogmodeller
dokumenter/         kontrolrapporten som PDF
billeder/           optimerede WebP billeder
fonts/              Archivo og Newsreader (variable, hostet lokalt)
licenser/           SIL Open Font License for begge skrifter
src/                rå kildebilleder til tools/build_images.py (indgår ikke i sitet)
tools/              build_images.py, som klargør billeder til billeder/
```

Kun `index.html`, `nytaarskasse.html`, `stil.css`, `billeder/`, `fonts/` og
`licenser/` skal lægges op på webhosten. `src/` og `tools/` er
arbejdsredskaber til jer/os, ikke en del af den offentlige side.

## Skriveregler for siden

Der bruges ingen tankestreger i teksterne, hverken korte eller lange. Skriv
med komma, punktum eller "til" i stedet (fx "12 til 21", "30. og 31.
december"). Tre produktnavne beholder deres bindestreg, fordi producenterne
selv staver dem sådan: Chassagne-Montrachet, Rose-Mary og Hancock Sport-Cola.

Priser står ikke på siden. Retter, vin, drikkevarer og nytårskassen nævnes
uden beløb.

## Skal udfyldes før den går live

1. Tilmelding på forsiden: sæt jeres formular-URL ind i `ENDPOINT` nederst i
   index.html. Så længe den er tom, åbner knappen gæstens mailprogram.
2. Nytårskassen: `BETALING_NYTAAR` nederst i nytaarskasse.html kan sættes til
   et Stripe Payment Link eller MobilePay MyShop link. Betalingsflowet er
   endnu ikke sat op, så feltet står tomt, og bestillingen går gennem
   formularen og åbner gæstens mailprogram.
3. Kassens indhold er taget fra menukortet, ikke fra jer. Indholdet er endnu
   ikke besluttet, så listen skal rettes, og der mangler billeder af kassen.
4. Leveringsdagen står som "inden nytårsaften". Sæt en konkret dag eller et
   tidsrum ind, når I ved, hvornår fragtmanden kører.

Klaret: Instagram og Facebook peger på jeres egne profiler, telefonnummeret
står i footeren, og bookinglinket krabbesostre.dk/bordreservation virker.

Kontaktadressen er contact@krabbesostre.dk og står i footeren på begge sider
samt i begge scripts. Bekræft, at det er den rigtige adresse. Telefonnummeret
29 43 00 52 står i footeren begge steder og i de strukturerede data på
forsiden.

## Nytårssiden

Siden har bevidst et andet lys end forsiden. Restauranten taler i kondenseret
versal signalskrift på lys bund; nytårskassen taler i graveret antikva på
mørk bund med messing som eneste accent. Samme skrifter, samme logo, samme
afstande, men et andet register, fordi det er en vare og ikke et sted.

Bunden er ikke fladt sort. Bag hele siden ligger et lærred, `canvas#stjerner`,
som tegner en kølig nathimmel foroven, levende lys forneden og et fint drys af
blinkende korn med en håndfuld større, der har en blød glorie. Kornene driver
langsomt opad og forskydes en anelse, når man ruller. Er reduceret bevægelse
slået til, tegnes billedet én gang og står helt stille.

Tallene ligger i `saetOp()` og `tegn()` nederst i nytaarskasse.html. Vil I have
flere eller færre stjerner, så ret divisoren i `antal`: lavere tal giver flere.
Farveovergangen ligger i `tegn()` som tre stop.

De øvrige farver ligger som variabler på `.nat` i stil.css: `--messing`
(accenten) og `--nat-linje` (hårlinjerne). Menulinje og footer får
nat-udgaven via klasserne `header--nat` og `footer--nat`.

Det store billede midt på siden vises i fuld højde og bliver ikke beskåret,
i modsætning til billedbåndene på forsiden. Reglen er `.nat .band img`.

Levering: hele Danmark for 150 kr., undtagen øer uden broforbindelse. Det står
tre steder på siden, og der er ingen afhentning på Thorupstrandvej.

## Fødevarekontrollen

Smileyrapporten skal være tilgængelig for gæsterne. Den ligger på
kontrolrapport.html, og der er link til siden i footeren på alle sider.
Selve arket vises som billede, `billeder/kontrolrapport.webp`, og kan
hentes som PDF i `dokumenter/kontrolrapport.pdf`.

Den viste rapport er fra 22. juli 2025. Når I får en ny kontrol, skal
begge filer skiftes ud: læg den nye PDF i dokumenter/ og lav et nyt
billede af den til billeder/. Alt-teksten på billedet nævner dato og
smiley, så den skal også rettes.

## Søgning og indeksering

Hver side erklærer sin egen adresse med `canonical`, og den skal altid passe
præcist med filnavnet. Erklærer en side en adresse, der ikke findes, risikerer
den slet ikke at blive indekseret. Det var faktisk tilfældet for nytårssiden og
kontrolrapporten, indtil det blev rettet.

Nederst på forsiden ligger et afsnit med strukturerede data. Det er den
usynlige beskrivelse, Google bruger til at vise åbningstider og kort, og som AI
læser. Tre ting skal holdes ved lige i det:

1. **Åbningstiderne** står med sæsonens datoer under `openingHoursSpecification`.
   De skal opdateres, når datoerne for næste sommer er på plads. Det samme gælder
   teksten i `manifest__fakta` øverst på forsiden og under Praktisk.
2. **Spørgsmål og svar** under Praktisk findes to steder: som synlig tekst og som
   `FAQPage` i de strukturerede data. Retter I det ene, skal I rette det andet,
   ellers står der noget forskelligt til gæsten og til Google.
3. **Nytårskassen** er beskrevet som en vare uden pris, fordi prisen ikke er
   fastsat. Når den er det, sættes et `offers`-afsnit ind med pris og valuta.

Koordinater er bevidst ikke angivet. Adressen er entydig nok til, at Google selv
finder punktet.

## Anmeldelser fra Google

Afsnittet "Sagt ved bordene" på forsiden bygges af
`tools/hent_anmeldelser.py` ud fra `anmeldelser.json`. Er listen tom,
vises afsnittet slet ikke. Skriv aldrig anmeldelser i hånden.

    export GOOGLE_API_NOEGLE="..."     nøgle fra Google Cloud, Places API slået til
    export GOOGLE_PLACE_ID="..."       findes med Googles Place ID Finder
    python3 tools/hent_anmeldelser.py

Nøglen står kun som miljøvariabel og må aldrig havne i en fil i repoet.

Tre ting at holde sig for øje:

1. **Places API giver højst fem anmeldelser**, og Google vælger selv hvilke.
   Skal alle med, kræver det Business Profile API, som skal søges hos Google
   og bruger login frem for nøgle. Visningen er den samme, så det kan bygges
   ovenpå senere uden at kaste noget væk.
2. **Anmeldelserne må ikke fryses fast.** Googles vilkår tillader ikke, at
   deres data gemmes permanent, så scriptet skal køre regelmæssigt, fx en
   gang i døgnet.
3. **Stjernerne må ikke i de strukturerede data.** Google forbyder, at man
   mærker anmeldelser op, som man selv har hentet andetsteds fra, og det kan
   udløse en straf. Stjernerne i søgeresultatet sætter Google selv.

## Kortet

Kortet under "Sådan finder I os" hentes først hos Google, når gæsten klikker
"Vis kort". Indtil da ingen cookies, derfor ingen cookiebanner. Tjek én gang
live, at Google tegner kortet; sandkassen her har ikke adgang til Google.

## Forsidens åbning

Der er intet topbillede. Siden begynder med logoet, som samtidig er sidens
`h1`, med navnet i billedets alt-tekst. Derfor må logoet aldrig blive et
almindeligt `img` igen uden at overskriften flytter et andet sted hen; en
side uden `h1` står svagt i Google.

Fordi der ikke er noget mørkt billede at ligge oven på, starter menulinjen
i sin lyse tilstand med `class="header is-stuck"` skrevet direkte i HTML.
Fjernes den klasse, bliver menuen hvid skrift på lyst papir og forsvinder.

Der er med vilje ingen knapper i åbningen. Alt ligger i menulinjen. Bemærk
at menuen skjuler punkter på små skærme: under 760 pixels vises kun Menu,
Nytårskasse og Book bord, og under 620 pixels viger ordet Krabbesøstre for
den lille krabbe, så der bliver plads. Tilføjes et punkt mere til menuen,
skal det tjekkes på en telefon, om der stadig er plads.

Delingsbilledet er `billeder/og-logo.webp`, logoet på papirbunden i 1200
gange 630 pixels, som er det format Facebook og beskedapps forventer.

## Bevægelse

Siden har et stille bevægelsessprog: topbilledet ånder langsomt ind ved
ankomst og glider en anelse ved rul, tekstblokke toner forskudt ind, og
menulinjen bliver til matteret glas, når man ruller. Alt sammen slås
automatisk fra for gæster, der har valgt reduceret bevægelse i deres system.

## Billeder

Beskæringen styres i stil.css med `object-position`. Vil I bytte et billede
ud, så læg den nye fil i billeder/, ret `src=` og juster beskæringen.
Logoet ligger i fire udgaver: logo.webp, logo-lys.webp (mørk bund),
krabbe.webp og krabbe-lys.webp (mærket i menulinjen og favicon).

Billeder der stadig mangler: gæster ved bordene indenfor, huset udefra i
fuld figur, et lodret nærbillede af en ret til mobil, aftenlys.

## Hvis priserne skal tilbage

Hver ret i index.html er en `article class="dish"`. Sæt
`<div class="dish__price">249</div>` ind som sidste element, og ret `.dish`
i stil.css fra `grid-template-columns:… 1fr` til `… 1fr auto`. Listerne
bruger `<span class="row__price">55</span>`. Husk også at sætte `offers`
tilbage i de strukturerede data nederst i index.html, hvis priserne vises.
