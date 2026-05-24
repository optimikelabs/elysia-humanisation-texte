# WARP.md

Guidance pour maintenir cette skill.

## Ce que c'est

`elysia-humanisation-texte` est une skill Agent Skills en Markdown. Depuis `3.0.0`, elle est FR-first et structurée en skill graph.

## Source de vérité

- `SKILL.md` : routeur runtime.
- `references/` : profondeur comportementale.
- `README.md` : aide humaine courte.

Ne pas recréer un gros monolithe dans `SKILL.md`. Si un comportement grossit, le mettre dans `references/` puis le lier depuis `SKILL.md`.

## Règles de maintenance

- Le français reste le défaut.
- L'anglais reste un fallback, pas le centre.
- Boileau est une inspiration externe, pas une seconde vérité.
- Le nom canonique reste `elysia-humanisation-texte`.
- Toute modification du frontmatter doit rester YAML valide.
- Après patch : valider YAML, liens de références, puis dry-run sur les cas de `references/test-cases.md`.

## Validation minimale

- YAML de `SKILL.md` parse.
- Tous les liens `references/*.md` existent.
- Le routeur mentionne : FR-first, registre, Boileau adapté, passe voix, typographie FR, fallback anglais.
- Les dry-runs couvrent : marketing FR, post X, email client, note stratégique, technique, créatif, anglais fallback.
