# Typographie française

## Quand l'appliquer

Appliquer à toute prose finale générée en français : page, email, post, note ou document.

La règle sur le cadratin est une convention éditoriale de cette skill. Elle ne prétend pas résumer tous les usages admis par la typographie française.

## Zones protégées

Ne pas modifier sans demande explicite :
- code, commandes, URLs et slugs;
- clés JSON/YAML/TOML;
- chemins, identifiants et chaînes exactes;
- citations, transcriptions ou artefacts source qui doivent rester littéraux;
- texte volontairement ASCII.

## Gate zéro cadratin

Dans la prose finale française générée, ne jamais produire le caractère `—`.

Remplacer selon la fonction :
- incise ou apposition : virgules, cas majoritaire;
- précision secondaire qui rendrait les virgules ambiguës : parenthèses;
- rupture emphatique, annonce ou chute : deux-points ou point;
- articulation qui résiste à ces remplacements : reformuler la phrase.

Ne pas contourner la règle en remplaçant une incise par `–` ou `--`.

Le tiret demi-cadratin `–` reste possible dans une plage de valeurs, une convention bibliographique ou une source exacte, pas comme substitut stylistique au cadratin.

### Sources exactes

Si une citation, une transcription ou un dialogue fourni doit rester reproduit à l'identique, conserver son cadratin uniquement dans la zone protégée. Ne jamais en ajouter dans la prose autour.

Si l'utilisateur demande une réécriture libre du dialogue, préférer les guillemets, les virgules, les deux-points ou les retours à la ligne selon le support.

### Anglais

Cette règle ne s'applique pas à un texte final anglais, où l'em dash peut rester idiomatique.

### Contrôle littéral

Avant la sortie française, rechercher littéralement `—`. Toute occurrence hors zone protégée invalide la version. Vérifier aussi que `–` ou `--` n'a pas été utilisé pour esquiver la règle dans une incise.

## Autres points utiles

- Accents sur les majuscules dans le texte final : `État`, `À propos`, `Ça`.
- Espaces avant `:`, `;`, `?`, `!` si le support les accepte.
- Guillemets français si le niveau éditorial le justifie.
- Pas de virgule avant `et` dans une énumération simple.
- Cohérence des apostrophes dans un même texte.
- Après un deux-points, garder la minuscule sauf nom propre, sigle, citation directe ou titre volontaire.
- Dans les titres français, éviter le title case : seul le premier mot et les noms propres prennent une majuscule.
- Dans un post court, préserver le souffle par les retours à la ligne, les virgules, les parenthèses, les deux-points ou les points, pas par un cadratin ajouté.

## Gras Markdown

Ne pas ajouter de gras pour fabriquer de l'emphase, simuler une hiérarchie ou rendre un passage plus humain. Préserver le gras existant s'il sert une fonction réelle.

## Règle

La typographie finit le texte. Elle ne doit casser ni le sens, ni le registre, ni la compatibilité technique.
