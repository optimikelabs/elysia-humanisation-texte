# Frontières de source

## But

Éviter d'humaniser une source entière quand elle contient plusieurs rôles : métadonnées, brouillon publiable, archive, preuve, score, texte publié, tâches ou consignes.

## Quand l'ouvrir

Utiliser si l'entrée ressemble à :
- un document Markdown avec frontmatter YAML;
- un brouillon éditorial ou une note de projet;
- un document avec sections `Draft Final`, `Archive`, `Performance`, `Analytics`, `Runtime` ou `Notes éditoriales`;
- une version publiée, une citation, une transcription ou un extrait source;
- plusieurs versions concurrentes.

## Zones protégées

Ne pas réécrire sauf demande explicite :
- frontmatter YAML;
- liens, URLs, ids, dates de publication et chemins;
- sections de contexte, source, analytics, performance, checklist, tâches et exécution;
- scores, décisions éditoriales, hypothèses et post-mortems;
- versions archivées qui servent de trace;
- texte marqué comme publié, citation, transcription ou preuve exacte.

## Bloc éditable

Chercher d'abord :
- `Draft Final`;
- `Version recommandée`;
- `Prêt à copier`;
- `texte_rewrite` fourni par l'utilisateur;
- le bloc explicitement désigné.

Si plusieurs versions existent, choisir la version recommandée. Si le signal reste contradictoire, formuler une hypothèse de travail et limiter l'intervention à la zone la plus probable.

## Texte publié

Si la source contient un statut ou une URL de publication :
- traiter le texte comme artefact source;
- ne pas corriger silencieusement une faute présente dans la version publiée;
- signaler la faute si elle compte;
- proposer une variante seulement pour une republication, une reprise ou une version future.

## Gate de sortie

Si la cible éditable reste floue, ne pas inventer le périmètre. Sortir un diagnostic court avec :
- bloc probable;
- zones protégées;
- hypothèse appliquée ou limite.
