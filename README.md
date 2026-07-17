# Humanisation de texte

Skill d'édition FR-first qui retire les marques d'écriture IA sans réécrire ce qui fonctionne déjà. La version `3.5.0` ajoute un routage séparé par contexte et intensité, un gate zéro cadratin en français et un contrôle de densité pour les textes techniques.

Nom canonique : `elysia-humanisation-texte`.

## Architecture

Le fichier runtime est `SKILL.md`. La profondeur vit dans `references/` :

- `router.md` : route de contexte;
- `intensite-intervention.md` : `no_op`, `retouche_ciblee`, `reecriture_structurelle`, `audit_seul`;
- `fr-first.md` : mode français;
- `fr-patterns-boileau.md` : patterns et faux positifs;
- `register-gate.md` : registre;
- `voice-pass.md` : passe finale et compression;
- `typography-fr.md` : gate typographique français;
- `technical-protection.md` : tokens, données et densité technique;
- `source-boundaries.md` : documents composites et archives;
- `en-patterns-legacy.md` : fallback anglais;
- `output-contract.md` : réponse utilisateur et état interne;
- `test-cases.md` : tests de comportement;
- `real-corpus-canaries.md` : canaris anonymisés;
- `source-map.md` : sources, règles reprises et règles rejetées.

## Changement de doctrine en 3.5.0

La skill ne choisit plus une route unique qui mélange le type de texte et le niveau de réécriture. Elle prend deux décisions :

1. contexte : français, anglais, technique, sensible, document source, échantillon de voix;
2. intensité : aucune modification, retouche ciblée, réécriture structurelle ou audit seul.

`retouche_ciblee` devient le défaut. La réécriture structurelle exige un défaut systémique nommé. Un texte technique peut rester neutre, dense et humain.

## Gates ajoutés

- aucun cadratin généré dans la prose finale française hors source exacte;
- remplacement fonctionnel par virgules, parenthèses, deux-points, point ou reformulation;
- aucune expansion utilisée comme stratégie d'humanisation;
- compression au-delà de 5 % de croissance mesurée en retouche ciblée sur un texte long;
- refus au-delà de 10 % sans objectif de développement ou raison sémantique précise;
- aucun nouveau gras, intertitre ou formatage décoratif;
- zéro marqueur détecté est un résultat valide;
- les états internes ne polluent plus la réponse utilisateur.

## Échantillon de voix

Un échantillon calibre le rythme, le vocabulaire, les transitions et les aspérités. Il ne justifie ni invention, ni expansion, ni copie mécanique des défauts.

```md
Échantillon de voix :
"""
Texte représentatif.
"""

Texte à humaniser :
"""
Brouillon à reprendre.
"""
```

## Personnalisation

- Nouvelle route générale : `SKILL.md` et `references/router.md`.
- Nouvelle intensité ou règle de densité : `references/intensite-intervention.md`.
- Nouveau registre : `references/register-gate.md`.
- Nouveau pattern : `references/fr-patterns-boileau.md`.
- Nouveau terme métier : `references/technical-protection.md`.
- Nouveau cas de non-régression : `references/test-cases.md` ou `references/real-corpus-canaries.md`.
- Nouvelle influence externe : `references/source-map.md`, avec règle reprise, risque et rejet explicite.

## Validation minimale

1. YAML de `SKILL.md` valide.
2. Liens `references/` résolus.
3. Chaque contexte et chaque intensité couverts par un test.
4. Tokens, listes, réserves et zones source préservés.
5. Gate zéro cadratin appliqué à la prose finale française.
6. Texte technique déjà clair laissé intact.
7. Sortie utilisateur sans état interne ni formatage ajouté.

## Versions

### 3.5.0

- routage à deux axes;
- retouche ciblée par défaut;
- gate zéro cadratin;
- budget de densité;
- seconde passe soustractive;
- protection contre le formatage ajouté;
- contrat de sortie clarifié;
- carte des sources auditée;
- canari d'analyse comptable technique.

### 3.4.6

- protection contre les scènes, anecdotes et mesures inventées;
- diagnostic séparé du texte final.

### 3.4.x

- calibration de voix;
- faux positifs sur staccato, répétitions, triades, aphorismes et métaphores;
- protection des documents Markdown, tokens et listes techniques.

## Sources

Voir `references/source-map.md` pour les décisions d'adoption et de rejet.
