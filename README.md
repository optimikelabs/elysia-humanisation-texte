# Humanisation de texte

Skill locale d'édition qui retire les marques d'écriture IA. La version active est **FR-first** : le français est le mode par défaut, l'anglais reste disponible en fallback.

Nom canonique : `elysia-humanisation-texte`.

## Source runtime

Le fichier qui fait foi pour l'agent est `SKILL.md`.

La profondeur vit dans `references/` :

- `router.md` : route document Markdown / FR / anglais / technique / sensible / no-op / audit anti-tics.
- `fr-first.md` : règles de base du mode français.
- `fr-patterns-boileau.md` : patterns français adaptés depuis Boileau.
- `register-gate.md` : choix du registre et anti-faux naturel.
- `voice-pass.md` : passe finale "qu'est-ce qui sonne encore IA ?".
- `typography-fr.md` : finition typographique française, sans casser Markdown/code/URLs.
- `technical-protection.md` : protection des tokens, champs, nodes, flags et termes système hybrides.
- `source-boundaries.md` : protection des documents Markdown complets, archives, frontmatter et versions publiees.
- `en-patterns-legacy.md` : couverture anglaise héritée.
- `output-contract.md` : forme de sortie attendue.
- `test-cases.md` : cas de validation.
- `real-corpus-canaries.md` : canaris techniques anonymisés.

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

## Personnaliser la skill

Cette skill est utilisable telle quelle, mais elle peut être adaptée à une voix, une marque ou un contexte métier.

### Comprendre le skill graph

La skill est organisée en deux couches :

- `SKILL.md` : point d'entrée runtime. Il doit rester court, activable et orienter l'agent vers les bons modules.
- `references/` : modules de profondeur. Chaque fichier porte une décision spécialisée : registre, typographie, protection technique, contrat de sortie, cas tests.

Quand vous personnalisez la skill, évitez de tout remettre dans `SKILL.md`. La bonne règle :

- nouveau déclencheur ou nouvelle route générale -> modifier `SKILL.md`;
- nouvelle règle de style ou de registre -> modifier `references/register-gate.md`;
- nouveaux tics ou patterns d'écriture -> modifier `references/fr-patterns-boileau.md` ou `references/en-patterns-legacy.md`;
- nouveaux termes métier à préserver -> modifier `references/technical-protection.md`;
- nouvelle forme de sortie -> modifier `references/output-contract.md`;
- nouveaux tests de non-régression -> modifier `references/test-cases.md` ou `references/real-corpus-canaries.md`.

Après modification, vérifiez au minimum :

1. Le frontmatter YAML de `SKILL.md` reste valide.
2. Tous les liens `references/...` cités dans `SKILL.md` existent.
3. Chaque route importante du `SKILL.md` pointe vers au moins une référence.
4. Un texte technique conserve ses commandes, URLs, champs, flags et valeurs exactes.
5. Un texte déjà naturel peut rester presque inchangé.

### 1. Adapter le nom

Dans `SKILL.md`, modifier le frontmatter :

```yaml
name: ma-skill-humanisation
description: |
  Humanisation de texte FR-first pour les contenus de mon équipe.
```

### 2. Ajuster le registre par défaut

Dans `references/register-gate.md`, ajouter ou modifier un registre :

```md
### Marque sobre
Pour : emails client, pages de service, documentation publique.
Faire : phrases courtes, verbes concrets, ton direct.
Éviter : humour forcé, effets de style, promesse vague.
```

### 3. Ajouter les termes métier à protéger

Dans `references/technical-protection.md`, compléter les termes hybrides ou les zones protégées :

```md
- `workspace_id`, `billing_status`, `sync_token`, `retry_after`;
- noms de workflows, endpoints, tables, champs et flags internes.
```

### 4. Remplacer les canaris

Dans `references/real-corpus-canaries.md`, remplacer les exemples anonymisés par 3 à 5 cas représentatifs de votre usage :

```md
## API produit
Tokens à préserver :
- `POST /v1/projects`
- `project_id`
- `status=archived`
- `retry_count < 3`

Risque testé :
- rendre le texte plus naturel en perdant un champ ou une valeur exacte.
```

### 5. Changer le niveau de diagnostic

Dans `references/output-contract.md`, ajuster le format de sortie :

```md
Si l'utilisateur veut seulement le texte :
- donner uniquement `texte_rewrite`;
- ne pas expliquer les changements.
```

## Décision de version

`3.4.4` corrige la règle sur les parallélismes négatifs courts :

- ne plus traiter automatiquement `Pas X. Y.` ou `Ce n'est pas juste X. C'est Y.` comme un tic IA;
- préserver le parallélisme quand il appuie le propos, sert le hook, tranche une vraie distinction ou porte la voix de l'auteur;
- corriger seulement les parallélismes décoratifs, empilés, interchangeables ou répétés sans nécessité.

`3.4.3` améliore la `3.4.2` publique sans changer le moteur d'humanisation :

- rend le garde-fou Markdown de `3.4.2` plus réutilisable hors d'un workflow précis;
- remplace les cas de test trop typés par des cas publics : document Markdown complet, brouillon éditorial, post social, newsletter courte, archive publiée, trace de publication;
- généralise les marqueurs de publication à reconnaître : `published`, `publication`, `published_url`, `source_url`, `url`;
- rend les zones protégées plus lisibles pour un autre repo : `Brief`, `Notes éditoriales`, `Performance`, `Analytics`, `Checklist`, `Tasks`;
- clarifie que le comportement de `3.4.2` reste le coeur : isoler le bloc éditable avant réécriture, préserver frontmatter/URLs/archives/scores/tâches, et ne pas corriger silencieusement une version déjà publiée;
- transforme donc `3.4.2` d'une protection correcte mais encore trop contextualisée en une protection directement exploitable dans un repo public de contenus Markdown.

`3.4.2` ajoute un garde-fou sur les documents Markdown complets :

- isoler le bloc éditable avant de réécrire une note avec frontmatter, archives ou plusieurs versions;
- protéger frontmatter, notes éditoriales, scores, tâches, archives, URLs et traces publiées;
- ne pas corriger silencieusement une version déjà publiée;
- ajouter des canaris anonymisés pour les brouillons éditoriaux / Markdown.

`3.4.1` durcit le routage ajouté en `3.4.0` :

- route explicite pour les échantillons de voix;
- route technique capable d'utiliser les patterns anti-cadence sur la prose autour des tokens;
- priorité réaffirmée de `technical-protection.md` quand un pattern stylistique entre en conflit avec un token exact.

`3.4.0` renforce la passe finale de voix :

- calibration par échantillon d'auteur;
- garde-fou anti-faux-positifs;
- patterns modernes de cadence IA;
- checklist finale courte;
- score interne optionnel non affiché par défaut.

`3.3.1` ajoute un garde-fou sur le parallélisme négatif court :

- détecter les cadences sociales très reconnaissables comme `Pas X. Y.` ou `Ce n'est pas juste X. C'est Y.`;
- conserver l'opposition seulement quand elle tranche vraiment une idée;
- dire directement le point quand l'opposition est décorative.

`3.3.0` ajoute des canaris techniques rejouables :

- CLI/API;
- MCP / JSON-RPC;
- workflow d'automatisation;
- configuration d'outil local.

`3.2.1` ajoute un garde-fou issu d'un test technique :

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
- ancien monolithe anglais -> skill graph;
- français par défaut;
- Boileau utilisé comme inspiration, pas comme copie brute;
- ajout d'un gate de registre pour éviter le faux familier;
- conservation du fallback anglais.

## Sources

- Boileau : `https://github.com/alxbd/boileau`
- Wikipedia Signs of AI writing : `https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing`
- blader/humanizer : `https://github.com/blader/humanizer`
- stop-slop : `https://github.com/hardikpandya/stop-slop`
- Humanizer-zh : `https://github.com/op7418/humanizer-zh`

## Origines

Cette skill s'inspire de plusieurs signaux publics et de tests d'usage réels :

- patterns français anti-marques IA inspirés de Boileau;
- signaux `collectifweb/claude-skills/humanize`;
- détecteur Babeleur comme corpus de tics, sans en faire une métrique de score;
- tests techniques anonymisés pour éviter de casser les commandes, URLs, champs, flags et valeurs de configuration.

## Notes

Ne pas synchroniser automatiquement cette version vers d'autres runtimes sans test dédié.
