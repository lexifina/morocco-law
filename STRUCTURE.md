# Structure du dépôt / Repository layout

Un dossier par texte, un fichier par article. Noms de dossiers en français, la langue dans laquelle les textes sont
publiés ici. / One folder per text, one file per article. Folder names are in French, the language of the texts held.

| Dossier | Contenu |
| --- | --- |
| `constitution/` | Constitution du Royaume du Maroc (2011) : `preambule.md`, `art-001.md` (article premier) … `art-180.md` |
| `codes/<code>/` | Codes : `codes/code-penal/`, `codes/code-des-obligations-et-contrats/` (DOC, 1913), `codes/code-de-commerce/`, `codes/code-de-procedure-civile/`, `codes/code-du-travail/`, `codes/code-des-droits-reels/` … |
| `dahirs/<année>/<numéro>-<objet>/` | Dahirs (y compris les dahirs portant loi), par année du texte |
| `lois/<année>/<numéro>-<objet>/` | Lois promulguées par dahir (`lois/1995/10-95-sur-l-eau/`), par année de promulgation |
| `decrets/<année>/<numéro>-<objet>/` | Décrets (`decrets/1998/2-97-487-…/`) |
| `arretes/<année>/<numéro>-<objet>/` | Arrêtés (ministériels, conjoints, viziriels, résidentiels) |
| `corpus.json` | La liste de tous les textes : dossier, nature, numéro, date retenue, titre, source, fichier, couche texte |

Dans chaque dossier de texte / In each text folder:

- `README.md` : titre, source, fichier source, numéro et date du Bulletin officiel quand la source les donne, date
  d'effet retenue et sa base, nature de la couche texte, nombre d'articles ;
- `preambule.md` : dahir de promulgation, visas et considérants (ce qui précède l'article premier) ;
- `art-NNN.md`, `art-NNN-bis.md`, `art-NNN-1.md` : un article par fichier (`art-001` est l'article premier) ;
- `signatures.md` : « Fait à … », contreseings ;
- `texte-integral.md` : le texte en un seul fichier, quand aucun article n'a pu être repéré.

Aucun dossier ne dépasse 1 000 entrées : les lois, dahirs, décrets et arrêtés sont rangés par année.

Dates : un commit par texte, à 12:00 (Africa/Casablanca) du jour d'effet retenu (trailers `In-force` et
`In-force-basis`). Ordre de préférence : la règle d'entrée en vigueur du texte appliquée à la date de l'édition générale
(arabe) du Bulletin officiel qu'il cite ; la date du Bulletin officiel donnée par la fiche FAOLEX ; la date d'entrée en
vigueur ou de publication de la fiche WIPO Lex ; à défaut, la date du texte (dahir de promulgation, décret, arrêté).
Codes consolidés : la date « version consolidée du … » imprimée par le Ministère de la Justice. Avant 1970 : commit daté
du 1er janvier 1970, jour réel dans le sujet et dans `In-force`.
