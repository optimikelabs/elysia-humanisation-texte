# Routeur de decision

## But
Choisir la bonne route avant de réécrire. Humaniser n'est pas toujours modifier beaucoup.

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

## Route technique
Utiliser si le texte contient code, commandes, URLs, slugs, clés JSON/YAML, Markdown sensible ou termes métier précis.

Référence minimale :
- `technical-protection.md`

Règles :
- préserver les blocs techniques;
- ne pas corriger la typographie dans le code, les URLs, les slugs et les clés;
- garder le jargon métier quand il est exact;
- garder les termes système hybrides quand ils nomment un objet réel du système;
- humaniser seulement les phrases d'explication.

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
Utiliser si Mike demande explicitement un audit, un score, une détection de tics IA, ou si le texte est long et visiblement généré.

Règles :
- le score reste optionnel et diagnostic;
- ne jamais promettre qu'un texte devient indétectable;
- utiliser les patterns externes comme inspiration, pas comme second canon.

Sortie autorisée : oui pour un diagnostic; réécriture seulement si demandée ou utile.
