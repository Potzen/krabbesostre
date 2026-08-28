# Krabbesøstre, hjemmeside

Statisk side. Ingen build, ingen database, ingen cookies. Læg mappens indhold
op på en hvilken som helst webhost, så virker den.

```
index.html          forsiden
nytaarskasse.html   nytårskassen
stil.css            designsystemet, deles af begge sider
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

1. Bookinglink: alle knapper peger på krabbesostre.dk/bordreservation.
2. Tilmelding på forsiden: sæt jeres formular-URL ind i `ENDPOINT` nederst i
   index.html. Så længe den er tom, åbner knappen gæstens mailprogram.
3. Nytårskassen: `BETALING_NYTAAR` nederst i nytaarskasse.html kan sættes til
   et Stripe Payment Link eller MobilePay MyShop link. Tomt felt betyder, at
   bestillingen går gennem formularen og åbner gæstens mailprogram.
4. Kassens indhold er taget fra menukortet, ikke fra jer. Ret listen.
5. Leveringsdagen står som "inden nytårsaften". Sæt en konkret dag eller et
   tidsrum ind, når I ved, hvornår fragtmanden kører.

Instagram og Facebook er sat ind begge steder i footeren.

Kontaktadressen er contact@krabbesostre.dk og står i footeren på begge sider
samt i begge scripts.

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

## Kortet

Kortet under "Sådan finder I os" hentes først hos Google, når gæsten klikker
"Vis kort". Indtil da ingen cookies, derfor ingen cookiebanner. Tjek én gang
live, at Google tegner kortet; sandkassen her har ikke adgang til Google.

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
