# ÉLYSIA — Humanisation de texte

Skill locale d'édition qui retire les marques d'écriture IA. La version active est **FR-first** : le français est le mode par défaut, l'anglais reste disponible en fallback.

Nom canonique : `elysia-humanisation-texte`.

Ancien nom : `humanizer`.

## Source runtime

Le fichier qui fait foi pour l'agent est `SKILL.md`.

La profondeur vit dans `references/` :

- `router.md` : route FR / anglais / technique / sensible / no-op / audit anti-tics.
- `fr-first.md` : règles de base du mode français.
- `fr-patterns-boileau.md` : patterns français adaptés depuis Boileau.
- `register-gate.md` : choix du registre et anti-faux naturel.
- `voice-pass.md` : passe finale "qu'est-ce qui sonne encore IA ?".
- `typography-fr.md` : finition typographique française, sans casser Markdown/code/URLs.
- `technical-protection.md` : protection des tokens, champs, nodes, flags et termes système hybrides.
- `en-patterns-legacy.md` : couverture anglaise héritée.
- `output-contract.md` : forme de sortie attendue.
- `test-cases.md` : cas de validation.
- `real-corpus-canaries.md` : canaris techniques dérivés de notes réelles du coffre.

## Usage

Utiliser quand un texte :

- "sonne IA" ou "fait ChatGPT";
- est trop soutenu, trop vague, trop professoral ou trop promotionnel;
- doit garder son sens mais gagner en voix;
- sort d'une autre skill et a besoin d'une passe finale.

Le comportement attendu :

1. détecter la langue;
2. choisir le registre;
3. repérer les marqueurs IA les plus coûteux;
4. réécrire sans inventer de faits;
5. faire une passe finale de voix;
6. retourner le texte et un diagnostic bref.

## Décision de version

`3.3.0` ajoute des canaris réels rejouables :

- Rize CLI;
- WordPress MCP / GMA;
- MX Linking n8n;
- Smart Search MCP.

`3.2.1` ajoute un garde-fou issu d'un test Rize CLI réel :

- ne pas résumer une liste de commandes, options, endpoints ou capacités quand l'exhaustivité sert le diagnostic;
- vérifier qu'aucun item technique ne disparaît pendant la passe d'humanisation.

`3.2.0` renforce la route technique après tests sur des notes réelles du coffre :

- ajout de `technical-protection.md`;
- protection explicite des termes système hybrides (`payload`, `node`, `retry`, `lead`, `fixture`, etc.);
- préservation des noms de nodes, flags, champs, tables, fonctions, seuils et liens Markdown;
- humanisation limitée aux phrases autour du contrat technique.

`3.1.0` ajoute le routeur de décision, les règles typographiques fortes et l'audit anti-tics optionnel :

- route explicite avant réécriture : FR, anglais, technique, sensible, no-op ou audit;
- tiret cadratin, majuscule après deux-points et title case traités comme signaux visibles en texte final français;
- patterns Babeleur / collectifweb utilisés comme contre-check, sans devenir un second canon;
- score anti-tics réservé au diagnostic optionnel, jamais à la sortie par défaut;
- cas sensibles et textes déjà naturels protégés contre la réécriture agressive.

`3.0.0` marque la refonte FR-first et le renommage canonique :

- `elysia-humanisation-texte` devient le nom canonique;
- `humanizer` reste seulement un ancien nom utile pour comprendre l'historique;
- ancien monolithe anglais -> skill graph;
- français par défaut;
- Boileau utilisé comme inspiration, pas comme copie brute;
- ajout d'un gate de registre pour éviter le faux familier;
- conservation du fallback anglais.

## Sources

- Boileau : `https://github.com/alxbd/boileau`
- Wikipedia Signs of AI writing : `https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing`

## Origines et note de suivi

La skill possède une note de suivi locale dans le coffre ÉLYSIA :

- Obsidian : `obsidian://open?vault=%C3%89LYSIA&file=Efforts%2FProjets%2FInternes%2FProjet%20%C3%89lysia%2FSuivi%20%E2%80%94%20Skill%20elysia-humanisation-texte`
- Chemin Windows : `F:\OBSIDIAN\ÉLYSIA\Efforts\Projets\Internes\Projet Élysia\Suivi — Skill elysia-humanisation-texte.md`

Origines documentées : besoin interne ÉLYSIA, ancien usage `humanizer`, signaux `collectifweb/claude-skills/humanize`, détecteur Babeleur, puis reconstruction ÉLYSIA-native via `elysia-skill-forge`.

## Notes

Ne pas synchroniser automatiquement cette version vers d'autres runtimes sans test dédié. La source active locale est `C:\Users\micka\.agents\skills\elysia-humanisation-texte`.
