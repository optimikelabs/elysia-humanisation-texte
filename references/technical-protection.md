# Protection technique

## But
Humaniser les phrases autour du système sans casser le contrat technique. Dans une note technique, certains mots anglais sont des objets du système, pas des tics IA.

## Zones protégées
Ne pas modifier :
- code, commandes, URLs, slugs, chemins, variables d'environnement;
- clés JSON/YAML/TOML, noms de champs, noms de tables et noms de colonnes;
- noms de fonctions, classes, composants, nodes, workflows et endpoints;
- listes de commandes, options, capacités, endpoints, checks ou statuts quand l'exhaustivité sert le diagnostic;
- extraits Markdown où le format fait partie de la preuve;
- valeurs exactes utiles au debug : statuts, flags, ids, versions, seuils, hashes.

## Termes hybrides à préserver
Préserver si le mot nomme un objet du système :
- `payload`, `node`, `workflow`, `retry`, `lead`, `backstop`, `seed`, `hint`, `fixture`, `runner`;
- `status_notes`, `needs_retry`, `retry_count`, `rewrite_lead`, `final_markdown`;
- `page_id`, `paragraph_index`, `sentence_hash`, `parent_link`, `output_contract`;
- `GraphQL`, `MCP`, `CLI`, `API`, `JSON-RPC`, `NDJSON`, `StyleSpec`.

## Ce qui peut être humanisé
Modifier seulement :
- les phrases d'explication autour des tokens;
- les transitions molles;
- les formulations inutilement abstraites;
- les répétitions qui ne portent pas d'information;
- les phrases qui annoncent au lieu de dire.

## Contrôle avant sortie
Comparer mentalement l'avant/après :
- les tokens techniques exacts sont-ils toujours présents ?
- une liste de commandes ou capacités a-t-elle perdu un item ?
- les chemins, URLs, flags et noms de champs sont-ils inchangés ?
- la phrase est-elle plus claire sans être moins exacte ?
- ai-je remplacé un terme système par un mot français ambigu ?

Si un doute subsiste, garder le terme original et améliorer seulement la phrase autour.
