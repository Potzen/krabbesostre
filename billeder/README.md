# Billeder, der mangler

`index.html` og `nytaarskasse.html` peger på filerne herunder i `billeder/`.
Læg dem i denne mappe (som optimerede `.webp`, undtagen ikonerne) og commit.

## Logo og ikon
- `logo.webp`, `logo-lys.webp`
- `krabbe.webp`, `krabbe-lys.webp` (mærket i menulinjen)
- `favicon.png`, `apple-touch-icon.png`
- `og.webp` (deles på sociale medier)

## Forsiden
- `hero.webp`, `hero-mobil.webp`
- `strand.webp`
- `sostrene.webp`
- `menukort.webp`
- `krabbeklor.webp`, `rejer.webp`, `sild.webp`
- `sostrene-rod.webp`, `borddaekning.webp`, `pilning.webp`, `skur.webp`,
  `sister-ii.webp`, `kurv.webp`, `sostrene-vindue.webp`, `skilt.webp`
  (galleriet)

## Nytårskassen
- `bord-bred.webp`
- `anretning.webp`

## build_images.py
`tools/build_images.py` klargør en del af billederne ovenfor (beskæring,
skalering, WebP) ud fra råfiler i `src/`. Læg de rå kildebilleder i `src/`
(navnene fremgår af `JOBS`-listen i scriptet) og kør scriptet fra repo-roden:

```
pip install pillow
python3 tools/build_images.py
```

Scriptet dækker i dag ikke alle filerne ovenfor (bl.a. mangler logo, ikoner,
strand, menukort, og en del af galleriet). Dem skal I enten tilføje som nye
jobs i scriptet, eller lægge direkte i `billeder/` som færdige `.webp`-filer.

Ifølge `L_SMIG.md` (nu `README.md`) mangler der desuden helt nye motiver:
gæster ved bordene indenfor, huset udefra i fuld figur, et lodret nærbillede
af en ret til mobil, og et billede i aftenlys.
