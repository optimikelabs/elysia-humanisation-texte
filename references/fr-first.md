# Français par défaut

## Position

Cette skill traite le français comme le cas normal. La grille anglophone n'est plus le centre, elle reste utile en fallback.

## Détection rapide

Mode français si :
- la majorité du texte est en français;
- le texte contient des tournures françaises typiques;
- l'utilisateur écrit en français et ne demande pas explicitement l'anglais.

Mode anglais si :
- la majorité du texte est en anglais;
- l'utilisateur demande `in English`;
- le brouillon est destiné à une surface anglophone.

## Objectif

Un bon texte humanisé en français :
- dit les choses plus directement;
- garde le niveau de langue adapté;
- remplace les adjectifs vagues par des faits seulement quand ils existent;
- rend concret uniquement avec un élément présent ou fourni;
- coupe les préambules IA;
- garde les aspérités utiles;
- peut rester neutre et compact, surtout en contexte technique;
- ne transforme pas tout en conversation de café;
- ne s'allonge pas pour prouver qu'il est plus humain.

## Ordre de travail

1. Identifier le type de texte.
2. Isoler la zone éditable si nécessaire.
3. Choisir le registre.
4. Choisir l'intensité dans `intensite-intervention.md`.
5. Détecter de 0 à 5 marqueurs pertinents, zéro est valide.
6. Modifier la plus petite surface utile.
7. Faire la passe voix finale, puis une vérification soustractive.
8. Appliquer les gates de sens, densité, formatage et typographie.
