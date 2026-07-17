# Canaris de corpus

## But

Rejouer des cas représentatifs sans dépendre d'un thread. Les exemples sont anonymisés et ne contiennent ni secret ni clé.

## Critère commun

Une humanisation réussie améliore la prose autour du contrat technique sans perdre, traduire, résumer ni sur-expliquer les éléments qui font foi.

## CLI et API

Tokens à préserver :
- `API_KEY`;
- `report`, `apps`, `tasks`, `time-entry`, `gql`;
- `webhook replay`;
- `https://example.com/webhook`.

Risque : résumer une liste de commandes et perdre un item.

## MCP et JSON-RPC

Tokens à préserver :
- `ToolsHandler::call_tool()`;
- `top-level error`;
- `JSON-RPC`;
- `ExecuteAbilityAbility`;
- `{}`;
- `null`;
- `type: object`;
- `vendor/adapter#111`.

Risque : traduire ou lisser des noms de fonctions et réserves protocole.

## Workflow d'automatisation

Tokens à préserver :
- `rewrite_lead=false`;
- `retry_count < 3`;
- `needs_retry=true`;
- `status_notes`;
- `Postgres · Upsert Status`;
- `paragraph_index`;
- `sentence_hash`;
- `parent_link`;
- `output_contract`.

Risque : rendre le plan plus clair en perdant des flags, champs ou seuils.

## Configuration locale

Tokens à préserver :
- `ENABLE_QUERY_EMBEDDING = "false"`;
- `SEARCH_MODE="files"`;
- `ENV_DIR="/workspace/.env"`;
- `XDG_CACHE_HOME`;
- `TRANSFORMERS_CACHE`;
- `QUERY_EMBEDDER = "transformers"`;
- `search mcp`.

Risque : corriger la prose en cassant des valeurs exactes.

## Analyse comptable technique

Termes à préserver selon la source :
- `FEC`;
- grand livre;
- balance générale;
- plan comptable;
- lettrage;
- écriture comptable;
- compte auxiliaire;
- score d'anomalie;
- seuils et périodes exactes.

Risque : ajouter de la chaleur, une scène d'utilisateur, une explication redondante ou des bénéfices marketing à un passage déjà précis.

Attendu :
- `retouche_ciblee`;
- paragraphes clairs inchangés;
- longueur stable ou plus courte;
- aucune nouvelle affirmation sur le produit ou la conformité.

## Densité et formatage

Entrée : texte technique de plus de 250 mots, sans gras, avec trois passages marqués et plusieurs paragraphes sains.

Attendu :
- seulement trois zones modifiées;
- aucun nouveau gras, intertitre ou item de liste;
- compression si l'expansion mesurée dépasse 5 %;
- rejet sans raison autorisée au-delà de 10 %.

## Gate cadratin

Entrée : prose française avec une incise, une parenthèse possible et une chute.

Attendu : virgules, parenthèses, deux-points ou point selon la fonction. Aucun cadratin généré, ni demi-cadratin utilisé comme échappatoire.

## Seuil de réussite

- Tous les tokens et éléments de liste attendus restent présents.
- Aucune URL, variable, valeur, condition ou réserve n'est modifiée.
- La prose devient plus claire sans expansion gratuite.
- Aucun score anti-tics n'est affiché sans demande.
- Un passage déjà clair peut rester inchangé.
- Aucun cadratin non protégé ni nouveau gras n'apparaît dans la sortie française.
