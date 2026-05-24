# Français par défaut

## Position
Cette skill traite le français comme le cas normal. La grille anglophone n'est plus le centre; elle reste utile en fallback.

## Détection rapide
Mode français si :
- la majorité du texte est en français;
- le texte contient des tournures FR typiques;
- l'utilisateur écrit en français et ne demande pas explicitement l'anglais.

Mode anglais si :
- la majorité du texte est en anglais;
- l'utilisateur demande "in English";
- le brouillon est destiné à une surface anglophone.

## Objectif
Un bon texte humanisé en français :
- dit les choses plus directement;
- garde le niveau de langue adapté;
- remplace les adjectifs vagues par des faits quand ils existent;
- coupe les préambules IA;
- garde les aspérités utiles;
- ne transforme pas tout en conversation de café.

## Ordre de travail
1. Identifier le type de texte : page, email, post, note, SEO, technique, créatif.
2. Choisir le registre dans `register-gate`.
3. Détecter les tics français.
4. Réécrire.
5. Faire la passe voix finale.
