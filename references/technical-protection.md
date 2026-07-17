# Protection technique

## But

Humaniser les phrases autour du système sans casser le contrat technique ni créer d'embonpoint rédactionnel. Dans un texte technique, certains mots anglais sont des objets du système, pas des tics IA.

La neutralité, la précision et la concision constituent une voix humaine valide. Ne pas ajouter artificiellement de chaleur, d'oralité, d'analogie ou de contexte.

## Intensité par défaut

Choisir `retouche_ciblee`.

- Modifier uniquement les phrases réellement marquées.
- Laisser inchangés les paragraphes déjà clairs.
- Remplacer ou soustraire avant d'ajouter.
- Ne pas développer une explication technique sous prétexte de la rendre plus humaine.
- Utiliser `reecriture_structurelle` seulement si l'organisation globale empêche la compréhension.

## Zones protégées

Ne pas modifier :
- code, commandes, URLs, slugs, chemins, variables d'environnement;
- clés JSON/YAML/TOML, noms de champs, tables et colonnes;
- noms de fonctions, classes, composants, nodes, workflows et endpoints;
- listes de commandes, options, capacités, endpoints, checks ou statuts quand l'exhaustivité sert le diagnostic;
- extraits Markdown où le format fait partie de la preuve;
- valeurs exactes utiles au debug : statuts, flags, ids, versions, seuils et hashes;
- termes comptables, financiers, juridiques ou réglementaires dont le sens est normé.
- formulations métier qui portent un critère de décision et qu'un synonyme plus large affaiblirait.

## Termes hybrides à préserver

Préserver si le mot nomme un objet réel du système :
- `payload`, `node`, `workflow`, `retry`, `lead`, `backstop`, `seed`, `hint`, `fixture`, `runner`;
- `status_notes`, `needs_retry`, `retry_count`, `rewrite_lead`, `final_markdown`;
- `page_id`, `paragraph_index`, `sentence_hash`, `parent_link`, `output_contract`;
- `GraphQL`, `MCP`, `CLI`, `API`, `JSON-RPC`, `NDJSON`, `StyleSpec`.

## Ce qui peut être humanisé

Modifier seulement :
- les phrases d'explication autour des tokens;
- les transitions molles;
- les formulations inutilement abstraites;
- les répétitions sans information;
- les phrases qui annoncent au lieu de dire;
- les tics de cadence réellement présents en cluster.

## Interdits spécifiques

Ne pas :
- ajouter une anecdote d'usage, un utilisateur fictif ou une scène produit;
- ajouter une phrase de bénéfice ou une transition conversationnelle absente de la source;
- remplacer un terme exact par un synonyme plus accessible mais ambigu;
- résumer une liste exhaustive;
- ajouter du gras Markdown ou des intertitres pour donner une apparence plus éditoriale;
- allonger chaque paragraphe technique pour le rendre plus chaleureux.

## Contrôle de densité

Pour un texte de plus de 250 mots, si le comptage est fiable :
- viser une longueur stable ou plus courte;
- au-delà de 5 % d'expansion, lancer une passe de compression;
- au-delà de 10 %, refuser la version sauf demande explicite de développement ou raison sémantique précise.

Pour un texte court, supprimer toute proposition ajoutée qui n'est pas nécessaire à la compréhension d'une information déjà présente.

## Contrôle avant sortie

Comparer l'avant et l'après :
- tous les tokens techniques exacts sont-ils présents ?
- une liste a-t-elle perdu ou gagné un item ?
- les chemins, URLs, flags et noms de champs sont-ils inchangés ?
- les conditions, limites et degrés de certitude sont-ils conservés ?
- les modalités et conditions cumulatives ont-elles gardé la même force ?
- une formulation métier décisionnelle a-t-elle été remplacée par un terme plus vague ?
- les paragraphes déjà clairs sont-ils restés stables ?
- la phrase est-elle plus claire sans être moins exacte ni plus longue sans raison ?
- la prose française générée respecte-t-elle le gate zéro cadratin ?
- du gras ou une nouvelle structure ont-ils été ajoutés sans fonction ?

Si un doute subsiste, garder le terme original et améliorer seulement la phrase autour.
