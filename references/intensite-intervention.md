# Intensité d'intervention

## But

Humaniser ne signifie pas réécrire tout le texte. Cette référence choisit la plus petite intervention capable de retirer les marqueurs artificiels sans diluer l'information, allonger inutilement le texte ni effacer une voix déjà crédible.

Le routage se fait sur deux axes indépendants :

1. le contexte du texte : français, anglais, technique, sensible, document source, échantillon de voix;
2. l'intensité d'intervention : `no_op`, `retouche_ciblee`, `reecriture_structurelle` ou `audit_seul`.

## Intensités

### `no_op`

Utiliser si le texte est déjà naturel, précis et adapté à son contexte.

Faire :
- conserver le texte tel quel ou appliquer 1 à 2 micro-corrections certaines;
- accepter zéro marqueur détecté comme un résultat valide;
- signaler brièvement que les autres changements seraient cosmétiques.

Ne pas faire :
- chercher des défauts pour justifier l'exécution de la skill;
- varier des mots, casser un rythme ou ajouter des transitions sans bénéfice lisible.

### `retouche_ciblee`, intensité par défaut

Utiliser si les problèmes sont localisés : quelques formulations gonflées, connecteurs automatiques, calques, répétitions, tics de cadence ou défauts typographiques.

Règles :
- modifier seulement les segments concernés;
- laisser inchangés les paragraphes déjà humains et exacts;
- soustraire ou remplacer avant d'ajouter;
- préserver l'ordre des idées sauf nécessité locale;
- ne pas ajouter de chaleur, d'oralité, d'exemple ou de contexte pour donner une impression d'humanité;
- en texte technique, professionnel ou sensible, choisir cette intensité par défaut.

### `reecriture_structurelle`

Utiliser seulement si les marqueurs sont systémiques sur plusieurs paragraphes : plan scolaire artificiel, introduction et conclusion génériques, cadence uniformément manufacturée, répétition globale de la même idée, registre incohérent ou architecture qui empêche la compréhension.

Conditions :
- pouvoir nommer le défaut structurel avant de réécrire;
- conserver la couverture sémantique et les réserves du texte;
- ne pas transformer une faiblesse locale en refonte générale;
- ne pas inventer de nouvelle thèse, preuve, exemple, analogie ou anecdote;
- laisser intacts les blocs qui fonctionnent déjà.

Si le besoin structurel n'est pas certain, revenir à `retouche_ciblee`.

### `audit_seul`

Utiliser si l'utilisateur demande une détection, un diagnostic ou un score sans demander de réécriture.

Règles :
- identifier de 0 à 5 marqueurs réellement observés;
- distinguer les signaux faibles des clusters convaincants;
- ne pas modifier le texte;
- ne jamais promettre une indétectabilité.

## Double objectif : développer puis humaniser

Si l'utilisateur demande explicitement de développer, enrichir ou expliquer davantage le texte, traiter l'expansion comme un objectif séparé. Ne pas attribuer cette expansion à l'humanisation.

Ordre recommandé :
1. développer uniquement avec des informations fournies, vérifiables ou explicitement autorisées;
2. appliquer ensuite la route d'humanisation adaptée;
3. signaler brièvement que la longueur vient de l'objectif de développement, pas de la passe de voix.

Sans demande explicite de développement, l'expansion n'est pas autorisée comme stratégie d'humanisation.

## Couverture sémantique

Avant la sortie, vérifier que la version conserve :
- chaque affirmation utile;
- les conditions, limites, réserves et degrés de certitude;
- les exemples et contre-exemples présents;
- les étapes, éléments de liste et instructions nécessaires;
- les termes métier et tokens protégés;
- l'intention relationnelle, commerciale ou stratégique.

Une phrase plus courte qui supprime une condition n'est pas une amélioration.

### Invariants de décision

Pour un texte technique, métier ou sensible, vérifier aussi :
- la force des modalités : `peut`, `doit`, `devrait`, `interdit`, `uniquement si`;
- les négations, seuils, périodes, causalités et conditions cumulatives;
- les formulations métier qui portent un critère de décision;
- la distinction entre possibilité, obligation, recommandation et constat.

Ne pas remplacer une formulation décisionnelle précise par un synonyme plus général pour gagner quelques mots. La densité se gagne sur le métadiscours, les transitions, l'emphase et les répétitions.

### Diff minimal en retouche ciblée

Classer les blocs en `stable` ou `marque` :
- un bloc stable reste littéralement inchangé;
- dans un bloc marqué, ne modifier que les segments associés à un marqueur nommé;
- une correction sans justification locale est cosmétique et doit être retirée.

Si une sortie structurée ou une évaluation l'exige, conserver un `edit_ledger` interne avec le bloc, le marqueur, le segment source, le segment final et la justification.

## Budget de densité

Le budget sert de garde-fou, pas de cible stylistique visible.

Pour `retouche_ciblee` :
- viser une longueur égale ou inférieure au texte source;
- sur un texte de plus de 250 mots, si un comptage fiable est disponible, une hausse supérieure à 5 % déclenche une passe de compression;
- une hausse supérieure à 10 % est refusée, sauf demande explicite de développement ou nécessité précise de restaurer une ambiguïté, une condition ou un élément grammatical manquant;
- dans ce cas, garder en interne une raison courte : `expansion_reason`.

Pour un texte court, ne pas piloter par pourcentage. Examiner chaque proposition ajoutée : porte-t-elle une information déjà présente mais mal formulée ? Si non, la retirer.

## Passe finale soustractive

La seconde passe ne doit pas enrichir le texte. Elle sert à :
- retirer ce qui a été ajouté sans gain sémantique;
- raccourcir les transitions;
- rétablir un passage source perdu;
- vérifier la densité et la cohérence;
- restaurer une aspérité utile trop lissée.

Une addition reste possible uniquement pour réparer une perte de sens créée pendant la réécriture.

## Formatage

Ne pas ajouter par défaut :
- de gras Markdown;
- de nouveaux intertitres;
- de nouvelles listes;
- d'emojis;
- de citations mises en scène;
- de labels éditoriaux.

Préserver le formatage existant lorsqu'il porte une fonction réelle : libellé d'interface, hiérarchie demandée, documentation ou structure du support.
