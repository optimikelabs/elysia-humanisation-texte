# Canaris techniques

## But
Rejouer des cas représentatifs sans dépendre d'un souvenir de thread. Ces canaris sont anonymisés et ne contiennent pas de secrets ni de clés.

## Critère commun
Une humanisation réussie améliore la phrase autour du contrat technique sans perdre ni traduire les tokens qui font foi.

## CLI / API
Tokens à préserver :
- `SERVICE_API_KEY`
- `report`, `apps`, `tasks`, `time-entry`, `gql`
- `webhook replay`
- `trycloudflare`
- `https://example.com/webhook`

Risque testé :
- résumer une liste de commandes et perdre un item comme `gql`.

## MCP / JSON-RPC
Tokens à préserver :
- `ToolsHandler::call_tool()`
- `top-level error`
- `JSON-RPC`
- `ExecuteAbilityAbility`
- `{}`
- `null`
- `type: object`
- `mcp-adapter-restfix`
- `example/mcp-adapter#111`

Risque testé :
- traduire ou lisser des noms de fonctions, réserves protocole et noms de fork.

## Workflow d'automatisation
Tokens à préserver :
- `rewrite_lead=false`
- `retry_count < 3`
- `needs_retry=true`
- `status_notes`
- `Postgres · Upsert Status`
- `paragraph_index`
- `sentence_hash`
- `parent_link`
- `output_contract`

Risque testé :
- rendre le plan plus clair en perdant les flags, champs ou seuils.

## Configuration d'outil local
Tokens à préserver :
- `ENABLE_QUERY_EMBEDDING = "false"`
- `SEARCH_MODE="files"`
- `APP_ENV_DIR="/path/to/.env"`
- `XDG_CACHE_HOME`
- `TRANSFORMERS_CACHE`
- `QUERY_EMBEDDER = "transformers"`
- `search mcp`

Risque testé :
- corriger la prose en cassant les valeurs exactes de config.

## Seuil de réussite
- Tous les tokens attendus restent présents.
- Aucune URL, variable ou valeur de config n'est modifiée.
- La prose autour devient plus claire.
- Aucun score anti-tics n'est affiché si l'utilisateur n'a pas demandé d'audit.
- Si le texte est déjà clair, la sortie peut être quasi inchangée.
