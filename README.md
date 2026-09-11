# Krabbesøstre, hjemmeside

Statisk side. Ingen build, ingen database, ingen cookies.

**Siden hostes af GitHub Pages og udgives af sig selv.** Alt, der pushes til
`claude/github-repo-website-setup-2mur7j`, som er repoets default branch, er
live på krabbesostre.dk et par minutter senere. Der skal ikke lægges filer op
nogen steder i hånden.

Domænet er registreret hos one.com, som også står for mailen, men hjemmesiden
ligger ikke længere der. I one.coms DNS peger både `krabbesostre.dk` og
`www.krabbesostre.dk` på GitHubs fire adresser, og `CNAME`-filen i roden
fortæller GitHub, hvilket domæne siden hører til. **`CNAME` må ikke slettes**,
så falder domænet af.

Skal siden alligevel flyttes til en almindelig webhost en dag, står listen
over filer længere nede.

```
index.html          forsiden
bordreservation/    bookingsiden, indtil et nyt bookingsystem er valgt
nytaarskasse.html   nytårskassen, skjult indtil videre, se nedenfor
kontrolrapport.html fødevarekontrollen, lovpligtig visning af smileyrapporten
stil.css            designsystemet, deles af alle sider
robots.txt          giver alle robotter adgang, også AI, og peger på sitemap
sitemap.xml         de synlige sider, indsendes i Google Search Console
llms.txt            kort beskrivelse i almindeligt sprog til sprogmodeller
dokumenter/         kontrolrapporten som PDF
billeder/           optimerede WebP billeder
fonts/              Archivo og Newsreader (variable, hostet lokalt)
licenser/           SIL Open Font License for begge skrifter
src/                rå kildebilleder til tools/build_images.py (indgår ikke i sitet)
tools/              build_images.py, som klargør billeder til billeder/
```

## Hvis siden skal flyttes til en almindelig webhost

Alt herunder lægges i den mappe, hvor den nuværende `index.html` ligger hos
webhosten, med mappestrukturen bevaret. I alt 41 filer, cirka 4 MB.

```
index.html            forsiden
bordreservation/      hele mappen, ellers giver Book bord en fejlside
kontrolrapport.html   fødevarekontrollen, lovpligtig
nytaarskasse.html     skjult, men skal med, så et gemt link stadig virker
stil.css              designet, uden den ser siden helt forkert ud
robots.txt            skal ligge i roden, ellers finder robotterne den ikke
sitemap.xml           samme, den er nævnt i robots.txt
llms.txt              kort beskrivelse til sprogmodeller
billeder/             hele mappen
fonts/                hele mappen, ellers falder skrifterne tilbage til systemets
dokumenter/           kontrolrapporten som PDF
licenser/             skriftlicenserne, se nedenfor
```

Disse skal **ikke** med, de er arbejdsredskaber:

```
menukort-test.html  de elleve udkast til menuen, kun til jer
anmeldelser.json    bruges af scriptet, ikke af siden
README.md           denne fil, også dem i undermapperne
src/                rå kildebilleder
tools/              scripts
```

Store og små bogstaver skal passe præcist. Serveren skelner mellem
`Billeder` og `billeder`, og et forkert bogstav giver et billede, der ikke
vises, uden nogen fejlmeddelelse.

## Skriveregler for siden

Der bruges ingen tankestreger i teksterne, hverken korte eller lange. Skriv
med komma, punktum eller "til" i stedet (fx "12 til 21", "30. og 31.
december"). Tre produktnavne beholder deres bindestreg, fordi producenterne
selv staver dem sådan: Chassagne-Montrachet, Rose-Mary og Hancock Sport-Cola.

Priser står ikke på siden. Retter, vin, drikkevarer og nytårskassen nævnes
uden beløb.

## Skal udfyldes før den går live

Nyhedsbrevet er taget af siden, indtil der er en tjeneste, der kan tage imod
adresserne. Feltet stod nederst i afsnittet "Vi åbner igen til sommer" og lovede
gæsten besked, som ingen kunne give, fordi mailadresserne ingen steder blev
gemt. Afsnittet er nu én centreret spalte med en henvisning til bordreservation.

Skal det tilbage, så hent formularen, scriptet og `.signup`-reglerne frem fra
historikken og sæt `ENDPOINT` til tjenestens adresse, fx Mailchimp eller
MailerLite. Bemærk at `.signup`-reglerne **stadig står i stil.css**, fordi
nytårssidens bestillingsformular bruger de samme klasser. Dem skal der ikke
røres ved.

Nytårskassen er sat på pause, så de tre punkter, der hørte til den, venter,
indtil siden hentes frem igen: betalingsflowet i `BETALING_NYTAAR`, kassens
indhold, som stadig er taget fra menukortet og ikke fra jer, og leveringsdagen,
der står som "inden nytårsaften".

Klaret: Instagram og Facebook peger på jeres egne profiler, og telefonnummeret
står i footeren.

## Bordreservation

Bookingsystemet er ved at blive skiftet ud, så `bordreservation/index.html` er
indtil videre en almindelig side, der siger, at I åbner igen sommeren 2027 og
henviser til tilmeldingen på forsiden.

Den ligger som **mappe** og ikke som `bordreservation.html`, fordi adressen skal
blive ved med at være `krabbesostre.dk/bordreservation`. Det er den, der står på
Google, på Facebook og i alt, hvad der er delt indtil nu. Resten af sitet bruger
`.html` i adresserne; det her er den bevidste undtagelse.

Siden er sat til `noindex`, så den ikke konkurrerer med forsiden på jeres eget
navn i Google. Den er stadig med i menulinjen og i footeren på alle sider.

Når det nye bookingsystem er på plads, er der to muligheder:

1. Systemet har sin egen adresse: så peges de syv links i `index.html`,
   `kontrolrapport.html` og `nytaarskasse.html` derhen, og mappen kan slettes
2. Bookingen skal ligge på jeres eget domæne: så erstattes indholdet i
   `bordreservation/index.html` med systemets indlejringskode, og `noindex`
   fjernes

Links til siden står som `bordreservation/`, altså relativt, ikke som den fulde
adresse. Så virker de både på GitHub-forhåndsvisningen og på det rigtige domæne.
Den fulde adresse står kun ét sted, i `acceptsReservations` i de strukturerede
data nederst i index.html, hvor schema.org kræver en hel adresse.

Kontaktadressen er contact@krabbesostre.dk og står i footeren på begge sider
samt i begge scripts. Bekræft, at det er den rigtige adresse. Telefonnummeret
29 43 00 52 står i footeren begge steder og i de strukturerede data på
forsiden.

## Nytårssiden, skjult indtil videre

Kassen er ikke aktuel, så siden er taget ud af omløb. Den er **ikke slettet**,
og alt arbejdet på den står urørt. Fem steder holder den skjult:

1. `nytaarskasse.html` har `<meta name="robots" content="noindex, follow">`
   øverst, så søgemaskiner lader den være
2. menupunktet Nytårskasse er ude af menulinjen på forsiden og på
   kontrolrapporten
3. det samme punkt er ude af footeren
4. afsnittet "Havet med hjem" midt på forsiden er taget ud; der står en
   kommentar i index.html, hvor det stod
5. siden er ude af `sitemap.xml` og af `llms.txt`

Skal den frem igen, sættes de fem ting tilbage. Selve siden skal der ikke
røres ved. CSS-reglerne `.spot` og `.nav__nytaar` er med vilje ikke fjernet
fra stil.css, netop så afsnittet og menupunktet kan sættes tilbage uden andet
arbejde.

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

### Valget af API, besluttet september 2026

Der er to veje til de samme anmeldelser, og vi har valgt den anden:

**Places API** koster penge efter et gratis loft, kræver et betalingskort på
filen, virker med det samme og giver **højst fem anmeldelser**, som Google
selv vælger.

**Business Profile API** er gratis uden kort og giver **alle anmeldelser**,
men adgangen skal søges hos Google og tager fra få dage til flere uger. Den
bruger login frem for en nøgle.

Vi går efter Business Profile API, fordi alle anmeldelser er en del bedre end
fem, og fordi der ikke er travlt. Indtil adgangen er godkendt, står afsnittet
tomt på siden, og det gør ikke noget: er listen tom, vises afsnittet slet ikke.

### Projektet hos Google

    Projektnavn    krabbesostre-anmeldelser
    Projekt-ID     krabbesostre-anmeldelser
    Projektnummer  449891936278

Ingen af delene er hemmelige, de giver ikke adgang til noget. De står her,
så det rigtige projekt kan findes igen, og fordi ansøgningsskemaet spørger om
nummeret, ikke om navnet. Selve adgangen ligger i hemmelighederne under
repoets indstillinger og kommer aldrig i en fil.

Ansøgningen er sendt den 11. september 2026 gennem
https://support.google.com/business/contact/api_default med punktet
"Application for Basic API Access", fra den konto der ejer
virksomhedsprofilen.

    Sagsnummer  8-7819000041512
    Svartid     7 til 10 hverdage ifølge Google

Skal der rykkes, eller skal kvoten senere hæves, bruges samme skema og det
sagsnummer.

### Hvad der mangler, før det virker

1. Adgang skal søges hos Google fra samme konto som virksomhedsprofilen
2. `hent()` i scriptet skal skrives om. Den taler i dag med Places API og skal
   i stedet hente fra `https://mybusiness.googleapis.com/v4/accounts/*/locations/*/reviews`,
   som er det eneste sted, anmeldelser findes. Det er bevidst ikke skrevet
   endnu, for det kan ikke afprøves uden adgang
3. Login skal fornys automatisk. Det kræver, at projektets samtykkeskærm
   sættes i produktion, ellers udløber fornyelsesnøglen efter syv dage, og det
   natlige job går i stå hver uge
4. Hemmelighederne i repoet skal skifte navn, fra nøgle og Place ID til
   klient-id, klienthemmelighed og fornyelsesnøgle

Alt det øvrige er færdigt og bliver stående: visningen på forsiden, `--byg`,
og det natlige job i `.github/workflows/anmeldelser.yml`.

### To ting at holde sig for øje uanset API

1. **Anmeldelserne må ikke fryses fast.** Googles vilkår tillader ikke, at
   deres data gemmes permanent, så scriptet skal køre regelmæssigt, fx en
   gang i døgnet.
2. **Stjernerne må ikke i de strukturerede data.** Google forbyder, at man
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
at menuen skjuler punkter på små skærme: under 760 pixels vises kun Menu og
Book bord, og under 620 pixels viger ordet Krabbesøstre for den lille krabbe,
så der bliver plads. Den sidste regel stammer fra dengang, Nytårskasse også
stod i menuen. Nu hvor punktet er væk, er der plads til ordet igen fra cirka
420 pixels og op, hvis I vil have det frem. Tilføjes et punkt til menuen,
skal det tjekkes på en telefon, om der stadig er plads.

Delingsbilledet er `billeder/og-logo.jpg`, logoet på papirbunden i 1200
gange 630 pixels. Det skal blive ved med at være **JPEG**, ikke WebP:
Facebook, Messenger og flere beskedapps viser ikke WebP i deres
forhåndsvisning, og de melder ikke fejl, billedet udebliver bare.
Nytårssiden og kontrolrapporten bruger `billeder/og.jpg`.

Adresserne i `og:image` er absolutte og peger på krabbesostre.dk. Så
længe siden vises fra et andet sted, fx GitHub Pages, kan et delt link
ikke hente billedet, og forhåndsvisningen viser kun titel og adresse.
Det retter sig selv ved domæneskiftet. Når det er sket, skal Facebook
bedes hente siden igen på deres Sharing Debugger, for de gemmer den
gamle udgave i op til en måned.

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

## Menuen

Menuen er sat som en plakat: ingen fotos af retterne, navnene sat stort i
antikva, alt centreret i én smal spalte. Baggrunden er en undersøgelse af,
at billeder af mad ikke nødvendigvis øger lysten; et foto låser fantasien
fast på præcis den portion, mens ordet lader gæsten forestille sig sin egen.
Formen blev valgt blandt elleve udkast på menukort-test.html, hvor de øvrige
ti stadig ligger, hvis I vil se dem igen eller skifte mening.

Hele menuen ligger i `div class="plakat"` i index.html og styles af
`.plakat*` i stil.css. Retterne er `.plakat__ret` med navn og beskrivelse.
Dessert, drikkevarer og vin er `.plakat__afsnit` med en `.plakat__linje`
per vare; det, der står med småt under en vare, altså størrelse, land eller
tilbehør, er en `.plakat__sub` inde i linjen.

Beskrivelserne på de tre retter står også i de strukturerede data nederst
på siden som `hasMenu`. Retter I den ene, så ret den anden.

Fotoerne af retterne, krabbeklor.webp, rejer.webp og sild.webp, vises ikke
længere på siden. Filerne ligger stadig i billeder/, og krabbeklor.webp er
bevaret i `image` i de strukturerede data, så Google fortsat har et billede
af maden at vise i søgeresultatet, selvom siden selv er uden.

## Båndet med menukortet

Mellem historien og menuen ligger `figure class="band"` med billedet af det
trykte menukort på bordet. Det skiller de to afsnit og er det eneste billede
i menudelen. Billedet vises ubeskåret, som det altid har været, og skal blive
ved med det. Det er bevidst, at ordet Menukort kan læses på fotoet.

## Hvis priserne skal tilbage

Hver ret i index.html er en `div class="plakat__ret"`. Sæt prisen ind som
`<p class="plakat__pris">249</p>` efter beskrivelsen, og giv den en regel i
stil.css i samme sprog som `.plakat__sub`. På de øvrige varer skrives prisen
ind i `.plakat__sub` sammen med det, der allerede står der.

Husk også, at `offers` skal tilbage i de strukturerede data nederst i
index.html, og at skriveregelen om priser ovenfor skal rettes.
