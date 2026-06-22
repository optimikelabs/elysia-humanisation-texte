# Routeur de decision

## But
Choisir la bonne route avant de réécrire. Humaniser n'est pas toujours modifier beaucoup.

## Route document Markdown / archive
Utiliser si l'entrée contient du frontmatter, des sections Markdown, plusieurs versions, une trace publiee, une citation ou un bloc source.

Référence minimale :
- `source-boundaries.md`

Règles :
- isoler le bloc réellement éditable avant d'appliquer une route de style;
- préserver frontmatter, notes éditoriales, scores, archives, tâches, URLs et traces de publication;
- si le bloc éditable est un post social français, poursuivre avec `register-gate.md`, `fr-patterns-boileau.md`, `voice-pass.md` et `typography-fr.md`;
- si le bloc contient des tokens techniques, ouvrir aussi `technical-protection.md`;
- si la cible éditable reste ambiguë, faire un diagnostic court plutôt qu'une réécriture globale.

Sortie autorisée : oui seulement sur le bloc éditable; non pour une réécriture globale de la note.

## Route FR standard
Utiliser si le texte est majoritairement français et destiné à être lu par un humain.

Références minimales :
- `fr-first.md`
- `register-gate.md`
- `fr-patterns-boileau.md`
- `typography-fr.md`
- `voice-pass.md`

Sortie autorisée : oui, si le sens et le registre sont clairs.

## Route anglais
Utiliser si le texte est majoritairement anglais ou si l'utilisateur demande explicitement l'anglais.

Référence minimale :
- `en-patterns-legacy.md`

Sortie autorisée : oui, sans appliquer les règles typographiques françaises.

## Route échantillon de voix
Utiliser si l'utilisateur fournit un extrait de sa voix, d'une marque ou d'un auteur à imiter.

Références minimales :
- `register-gate.md`
- `fr-patterns-boileau.md`
- `voice-pass.md`

Règles :
- lire l'échantillon avant de réécrire;
- calibrer le rythme, le niveau de vocabulaire, les transitions et les aspérités;
- remplacer les tics IA par les patterns de l'auteur, pas par un naturel générique;
- ne pas copier les défauts qui nuisent au sens ou à la précision.

Sortie autorisée : oui, si l'échantillon est assez représentatif pour guider la voix.

## Route technique
Utiliser si le texte contient code, commandes, URLs, slugs, clés JSON/YAML, Markdown sensible ou termes métier précis.

Références minimales :
- `technical-protection.md`
- `typography-fr.md`

Références complémentaires si la prose autour des tokens sonne IA :
- `fr-patterns-boileau.md`
- `voice-pass.md`

Règles :
- préserver les blocs techniques;
- ne pas corriger la typographie dans le code, les URLs, les slugs et les clés;
- garder le jargon métier quand il est exact;
- garder les termes système hybrides quand ils nomment un objet réel du système;
- humaniser seulement les phrases d'explication.
- appliquer les patterns anti-cadence seulement aux phrases autour des tokens; `technical-protection.md` prime en cas de conflit.

Sortie autorisée : oui, avec prudence.

## Route sensible
Utiliser si le texte touche au juridique, médical, financier, RH sensible, sécurité, conformité ou décision à risque.

Règles :
- préserver les formulations prudentes;
- signaler toute reformulation qui pourrait changer le sens;
- préférer un diagnostic et des corrections minimales;
- ne pas rendre le texte plus affirmatif seulement pour qu'il sonne humain.

Sortie autorisée : seulement si le sens reste strictement stable.

## Route no-op
Utiliser si le texte est déjà naturel, précis et adapté à son contexte.

Règles :
- ne pas réécrire pour réécrire;
- signaler brièvement que les changements seraient cosmétiques;
- proposer au maximum 1 ou 2 micro-ajustements.

Sortie autorisée : oui, mais la meilleure sortie peut être quasi inchangée.

## Route audit anti-tics
Utiliser si l'utilisateur demande explicitement un audit, un score, une détection de tics IA, ou si le texte est long et visiblement généré.

Règles :
- le score reste optionnel et diagnostic;
- ne jamais promettre qu'un texte devient indétectable;
- utiliser les patterns externes comme inspiration, pas comme second canon.

Sortie autorisée : oui pour un diagnostic; réécriture seulement si demandée ou utile.
