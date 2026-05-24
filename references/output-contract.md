# Contrat de sortie

## Format normal

```text
registre_cible: ...
marqueurs_detectes:
- ...

texte_rewrite:
...

passe_finale:
...

changements_principaux:
- ...
```

## Champs internes possibles

Utiliser seulement si utile :
- `route`: FR standard, anglais, technique, sensible, no-op, audit anti-tics.
- `sortie_finale_autorisee`: oui/non, avec raison courte si non.
- `audit_slop`: diagnostic optionnel si l'utilisateur demande un audit ou si le texte est long et très marqué IA.

## Format court
Si l'utilisateur veut seulement le texte :
- donner uniquement `texte_rewrite`;
- ne pas expliquer les changements.

## Diagnostic
Le diagnostic doit rester utile :
- 3 à 8 marqueurs maximum;
- pas de liste exhaustive si elle ralentit la lecture;
- nommer le risque principal : trop IA, trop soutenu, trop familier, trop vague, trop promotionnel, trop professoral.
- ne pas afficher de score par défaut; si un score est utile, le présenter comme signal d'audit et non comme vérité.

## Interdits
- Ne pas dire que le texte est "désormais parfaitement humain".
- Ne pas humilier le brouillon.
- Ne pas ajouter des faits.
- Ne pas changer l'intention commerciale, stratégique ou relationnelle sans le signaler.
- Ne pas promettre qu'un texte devient indétectable par un détecteur IA.
