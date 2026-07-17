# Contrat de sortie

## État d'exécution interne

Les champs suivants servent à stabiliser le workflow. Ils ne doivent pas être affichés par défaut :
- `references_ouvertes`;
- `module_route`;
- `route_contexte`;
- `intensite_intervention`;
- `source_boundary` si nécessaire;
- `etape_pipeline_en_cours`;
- `sortie_finale_autorisee`;
- `registre_cible`;
- `marqueurs_detectes`;
- `couverture_semantique_verifiee`;
- `controle_densite`;
- `gate_typographique`;
- `expansion_reason` seulement si une expansion exceptionnelle est conservée.
- `edit_ledger` seulement si une sortie structurée ou une évaluation l'exige.

Un champ interne n'est pas un bloc à imprimer dans la réponse utilisateur.

## Réponse utilisateur par défaut

1. Donner le texte réécrit en premier.
2. Ajouter ensuite, seulement si utile ou demandé, un diagnostic bref de 0 à 5 changements importants.
3. Ne pas afficher de labels comme `texte_rewrite`, `passe_finale` ou `marqueurs_detectes` sauf demande de sortie structurée.

## Format texte seul

Si l'utilisateur veut uniquement le texte :
- donner uniquement la version finale;
- ne pas expliquer les changements;
- ne pas ajouter de titre, bandeau ou note de traitement.

## Route `no_op`

Si le texte est déjà naturel :
- le rendre inchangé ou presque;
- dire brièvement, hors du texte final, que les autres changements seraient cosmétiques si un diagnostic est utile;
- ne pas inventer de marqueurs pour remplir une liste.

## Diagnostic

Le diagnostic doit rester utile :
- de 0 à 5 marqueurs maximum;
- zéro marqueur est valide;
- pas de liste exhaustive;
- nommer le risque principal : trop artificiel, soutenu, familier, vague, promotionnel, professoral ou dilaté;
- distinguer un signal isolé d'un cluster;
- ne pas afficher de score par défaut;
- ne pas annoncer de comptage, pourcentage, nombre de passes ou comparaison avant/après sans mesure réelle;
- ne pas insérer le diagnostic dans le contenu publiable.

## Sortie structurée

Utiliser des champs explicites uniquement si l'utilisateur, un pipeline ou une autre skill le demande. Dans ce cas, suivre exactement le schéma demandé et ne pas exposer d'autres états internes.

## Interdits

- Ne pas dire que le texte est parfaitement humain.
- Ne pas humilier le brouillon.
- Ne pas ajouter de faits, de preuve, de bénéfice ou de contexte.
- Ne pas inventer une scène, anecdote, durée, personne, lieu ou exemple.
- Ne pas changer l'intention commerciale, stratégique ou relationnelle sans le signaler.
- Ne pas promettre qu'un texte devient indétectable.
- Ne pas ajouter de gras, d'intertitres ou de listes sans fonction.
- Ne pas afficher le protocole interne de la skill comme résultat utilisateur.
