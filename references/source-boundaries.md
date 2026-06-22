# Frontieres de source

## But
Eviter de "humaniser" une source entiere quand elle contient plusieurs roles : metadata, brouillon publiable, archive, preuve, score, post publie, taches ou consignes de publication.

## Quand l'ouvrir
Utiliser si l'entree ressemble a :
- une note Markdown avec frontmatter YAML;
- une note de creation ou de projet;
- un post X avec sections `Draft Final`, `Archive`, `Performance`, `Runtime`, `Méta-Analyse`;
- une version publiee, un quote-post, une citation, une transcription ou un extrait source;
- un document avec plusieurs versions concurrentes.

## Zones protegees
Ne pas reecrire sauf demande explicite :
- frontmatter YAML;
- liens, URLs, ids, dates de publication et chemins locaux;
- sections `Contexte`, `Source`, `Méta-Analyse`, `Runtime`, `Performance`, `Checklist`, `Exécution`, `Tasks`;
- scores, decisions editoriales, hypotheses de distribution et post-mortems;
- versions archivees qui servent de trace;
- texte marque comme publie, citation, transcription ou preuve exacte.

## Bloc editable
Chercher d'abord :
- `Draft Final`;
- `Version recommandée`;
- `Prêt à copier`;
- `texte_rewrite` fourni par l'utilisateur;
- le bloc explicitement designe dans la demande.

Si plusieurs versions existent, choisir seulement la version recommandee ou demander un arbitrage si le signal est contradictoire.

## Post publie
Si la source indique `statut_creation: publié`, `Publié`, `x_url` ou une trace de publication :
- traiter le texte comme artefact source;
- ne pas corriger silencieusement une faute presente dans la version publiee;
- signaler la faute si elle compte;
- proposer une variante corrigee seulement si l'utilisateur demande une republication, une reprise ou une version future.

## Notes Post X
Pour un post X a publier :
- retirer les labels editoriaux comme `[HOOK]`, `[CORPS]`, `[CTA]` seulement si la sortie demandee est copy-ready;
- garder le rythme court s'il sert la tension;
- ne pas transformer une repetition volontaire en synonymes;
- ne pas ajouter de faits, chiffres, sources ou exemples absents.

## Gate de sortie
Si la cible editable est floue, ne pas inventer le perimetre. Sortir un diagnostic court :
- bloc probable;
- zones protegees;
- question ou hypothese de travail.

La meilleure sortie peut etre : "je ne touche pas au texte publie; voici seulement une variante candidate".
