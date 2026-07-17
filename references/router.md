# Routeur de décision

## But

Choisir le bon contexte, puis la bonne intensité avant de réécrire. Humaniser n'est pas toujours modifier beaucoup.

Ouvrir aussi `intensite-intervention.md`. Le contexte et l'intensité sont deux décisions distinctes.

## Étape 0 : frontière de source

Utiliser `source-boundaries.md` si l'entrée contient du frontmatter, plusieurs versions, une trace publiée, une citation, une transcription, un bloc source ou des métadonnées éditoriales.

Règles :
- isoler le bloc réellement éditable avant toute route de style;
- préserver les zones source et les preuves exactes;
- si la cible reste ambiguë, faire un diagnostic court plutôt qu'une réécriture globale.

Sortie autorisée : seulement sur le bloc éditable identifié.

## Étape 1 : route de contexte

### Route FR standard

Utiliser si le texte est majoritairement français et destiné à être lu par un humain.

Références minimales :
- `fr-first.md`;
- `register-gate.md`;
- `fr-patterns-boileau.md`;
- `typography-fr.md`;
- `voice-pass.md`.

### Route anglais

Utiliser si le texte est majoritairement anglais ou si l'utilisateur demande explicitement l'anglais.

Référence minimale :
- `en-patterns-legacy.md`.

Ne pas appliquer les règles typographiques françaises.

### Route technique

Utiliser si le texte contient code, commandes, URLs, slugs, clés JSON/YAML, Markdown sensible, données, procédure, documentation produit ou termes métier précis.

Références minimales :
- `technical-protection.md`;
- `typography-fr.md` si la prose finale est française.

Références complémentaires si la prose autour des tokens sonne IA :
- `fr-patterns-boileau.md`;
- `voice-pass.md`.

Règles :
- protéger le contrat technique avant le style;
- considérer la neutralité, la précision et la concision comme une voix humaine valide;
- humaniser seulement les phrases qui le nécessitent;
- choisir `retouche_ciblee` par défaut;
- appliquer les patterns anti-cadence uniquement à la prose autour des tokens.

### Route sensible

Utiliser si le texte touche au juridique, médical, financier, comptable, RH sensible, sécurité, conformité ou décision à risque.

Règles :
- préserver les formulations prudentes, réserves et conditions;
- choisir `retouche_ciblee` par défaut;
- ne pas rendre le texte plus affirmatif, plus simple ou plus chaleureux au prix du sens;
- signaler toute reformulation susceptible de modifier l'interprétation.

Sortie autorisée : seulement si la stabilité du sens est vérifiée.

### Overlay échantillon de voix

Utiliser si l'utilisateur fournit un extrait de sa voix, d'une marque ou d'un auteur.

Références minimales :
- `register-gate.md`;
- `fr-patterns-boileau.md`;
- `voice-pass.md`.

Règles :
- lire l'échantillon avant de réécrire;
- calibrer rythme, vocabulaire, transitions et aspérités;
- remplacer les tics IA par les patterns de l'auteur, pas par un naturel générique;
- ne pas copier les défauts qui nuisent au sens;
- ne pas utiliser l'échantillon pour justifier une expansion ou contourner les gates typographiques.

Cet overlay complète une route de contexte, il ne la remplace pas.

## Étape 2 : intensité

Choisir dans `intensite-intervention.md` :
- `no_op` si le texte fonctionne déjà;
- `retouche_ciblee` par défaut;
- `reecriture_structurelle` seulement si un défaut systémique est nommé;
- `audit_seul` si aucune réécriture n'est demandée.

## Arbitrage

En cas de conflit :
1. frontière de source;
2. stabilité du sens et prudence;
3. protection technique;
4. intensité minimale utile;
5. registre et voix;
6. finition typographique.

En cas de doute, choisir `retouche_ciblee`.
