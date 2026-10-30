# Morocco: law history in git

The Constitution of the Kingdom of Morocco (2011) and the Code pénal as a git repository: one file per article, so `git blame` and `git log` work on the text. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ma/`.

**What is in it now**

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution du Royaume du Maroc, promulgated by Dahir n° 1-11-91 of 29 July 2011 | 1 | As promulgated; the Constitution has not been amended since |
| `code-penal/` | Code pénal (dahir n° 1-59-413 of 26 November 1962), consolidated to loi n° 33-18 | 1 | Oldest version available: the consolidated text, dated 11 March 2019 (608 articles) |

**Language.** The text is the **French version** published by the Ministry of Justice. Morocco's authoritative text is the Arabic one, which was not available as machine-readable text; for anything that matters, read the Arabic original in the Bulletin officiel.

## Dates and limits

- One version, dated **30 July 2011**, the day the text appeared in the Bulletin officiel n° 5964 bis. The promulgating dahir is dated 29 July 2011. The commit is credited to Dahir n° 1-11-91.
- The earlier Constitutions (1962 to 1996) are not in the record.
- Page numbers and the title headings (Titre premier to Titre XIV) are not kept. `preambule.md` holds the preamble; `art-001.md` is Article premier (Article 1).
- The dahir of promulgation is not a file.

## Code pénal

- The text is the consolidated version republished by WIPO Lex (MA088), taking in amendments up to loi n° 33-18 (dahir n° 1-19-44 of 11 March 2019). It is one version, not the 1962 original and not a history; later amendments are not applied.
- Articles 19 to 23 are missing from the WIPO Lex PDF's text layer, and articles 289 to 291 are not printed in it (repealed), so those have no file. Livre, Titre, Chapitre and Section headings, and the footnotes naming each amending law, are left out.
French is the working text; the Arabic is authoritative.
- Moroccan copyright law (loi n° 2-00, article 8(a)) excludes official legislative texts from protection; see `LICENSE`.

## Source

Constitution: Ministère de la Justice, portail Adala (https://adala.justice.gov.ma/), "La Constitution", French version, retrieved 28 October 2026. The portal states no licence.

Code pénal: WIPO Lex, https://wipolex-res.wipo.int/edocs/lexdocs/laws/fr/ma/ma088fr.pdf, retrieved 30 October 2026. The PDF states no licence.

No AI model wrote or changed legal text. This is not legal advice and not an official publication.
