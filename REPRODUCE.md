# How this repository was made (Morocco)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Ministère de la Justice, portail Adala (La Constitution, version française) | <https://adala.justice.gov.ma/> | 2026-10-28 | Official text of the Constitution published by the Moroccan Ministry of Justice; no licence statement found |
| WIPO Lex: Code pénal, dahir n° 1-59-413, modifié jusqu à la loi n° 33-18 (MA088) | <https://wipolex-res.wipo.int/edocs/lexdocs/laws/fr/ma/ma088fr.pdf> | 2026-10-30 | Official text of law, not protected by Moroccan copyright: loi n° 2-00, article 8(a), excludes "les textes officiels de nature législative, administrative ou judiciaire" from protection. WIPO Lex states no licence on the PDF. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution du Royaume du Maroc (2011) | 1 | 2011-07-30 to 2011-07-30 |
| `code-penal` | Code pénal (dahir n° 1-59-413 du 28 joumada II 1382 (26 novembre 1962) portant approbation du texte du Code pénal), consolidé jusqu'à la loi n° 33-18 | 1 | 2019-03-11 to 2019-03-11 |

The build made 2 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 3 tags.

## Dates

Each commit is dated at noon (Africa/Casablanca) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Constitution of 2011 took effect on publication in the Bulletin officiel n° 5964 bis of 30 July 2011, as promulgated by Dahir n° 1-11-91 https://adala.justice.gov.ma/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `eb13423b94755cf9dd386b81d048248af49ac40a0e892cb968bf302684a500f6` (550383 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The Constitution has no later amendment, so the repository holds one version, the Constitution as promulgated, dated 2011-07-30, the day it appeared in the Bulletin officiel (n° 5964 bis); the dahir of promulgation is dated 2011-07-29.
- The French text is used because the Ministry of Justice portal publishes it as a text-layer PDF; the Arabic text is the authoritative one and was not available as text.
- Page numbers and title headings (TITRE ...) were removed; the promulgation dahir is not a unit.
- Code pénal: one version, the consolidated text through loi n° 33-18, dated 2019-03-11 (the date of dahir n° 1-19-44, which promulgated that law). It is not the 1962 text and later amendments (after 2019) are not applied.
- Code pénal units: one per article (art-001 is "Article premier"); Livre, Titre, Chapitre and Section headings are left out; the footnotes and their call numbers are dropped, so the notes naming each amending law are not kept. Articles 19 to 23 are missing from the WIPO Lex PDF text layer and articles 289 to 291 are repealed or not printed there, so they are not files.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
