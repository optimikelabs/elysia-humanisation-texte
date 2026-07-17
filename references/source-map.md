# Carte des sources et décisions

## But

Tracer les influences de la skill sans importer leurs règles en bloc. Aucune source externe n'est un canon. Chaque pattern est retenu seulement s'il améliore les cas français réels sans invention, surcorrection ni perte de précision.

Audit de référence : 17 juillet 2026.

## Sources

### Boileau

Source : `https://github.com/alxbd/boileau`

Version auditée : `0.1.0`.

Rôle : corpus français principal de marqueurs, notamment registre gonflé, verbes vides, transitions, cadence, cadratins et emphase Markdown.

Repris :
- détection par familles de marqueurs;
- priorité au sens et au registre;
- nettoyage local des passages problématiques.

Adapté ou rejeté :
- ne pas ajouter automatiquement opinion, expérience personnelle ou émotion;
- ne pas rendre concret avec une scène absente;
- ne pas transformer chaque détection en réécriture globale.

### Wikipedia, Signs of AI writing

Source : `https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing`

Rôle : corpus vivant de signaux contextuels.

Repris :
- les marqueurs de formatage et de cadence sont des indices, pas des preuves isolées;
- préserver les formes humaines antérieures aux LLM quand elles remplissent une fonction.

Rejeté :
- utilisation comme détecteur certain ou score de vérité.

### blader/humanizer

Source : `https://github.com/blader/humanizer`

Version auditée : `2.8.2`.

Rôle : contre-check anglophone et discipline de contrôle final.

Repris :
- gate littéral sur les tirets dans la langue cible;
- conservation de la couverture sémantique;
- distinction entre un signal diagnostique et une contrainte de production.

Adapté :
- la règle zéro cadratin s'applique à la prose française générée, avec zones source protégées;
- les règles anglaises ne sont pas transposées mécaniquement au français.

### stop-slop

Source : `https://github.com/hardikpandya/stop-slop`

Rôle : inspiration pour la densité, la directivité et la confiance accordée au lecteur.

Repris :
- soustraction avant ajout;
- suppression des phrases de remplissage;
- deuxième passe de compression.

Rejeté :
- interdiction universelle des adverbes;
- suppression automatique de toute voix passive;
- obligation d'un sujet humain dans chaque phrase;
- règle mécanique qui préfère toujours deux items à trois.

### Humanizer-zh

Source : `https://github.com/op7418/humanizer-zh`

Rôle : comparaison des stratégies d'humanisation fortement expressives.

Rejeté comme doctrine :
- injection systématique de personnalité, d'opinion, de vulnérabilité ou de désordre;
- ajout de scènes et détails émotionnels pour simuler une voix;
- transposition d'une grille anglophone ou chinoise comme canon français.

### collectifweb/claude-skills, humanize

Source : `https://github.com/collectifweb/claude-skills/tree/main/humanize`

Rôle : contre-check de tics français et règle forte sur le cadratin.

Repris :
- interdiction de production du cadratin en français;
- contrôles visibles sur les tics de formatage.

Rejeté :
- quotas de connecteurs, ruptures de registre, ancres concrètes ou longueurs de phrases;
- score unique pris comme objectif;
- injection positive de variété lorsque le texte fonctionne déjà.

### Babeleur

Source : `https://babeleur.be/detecteur-tics-ia.html`

Version auditée : `1.2`, datée du 31 mars 2026.

Rôle : contre-check français de tics fréquents.

Repris :
- signaux sur cadratin, majuscule après deux-points, listes, triades et formulations scolaires.

Rejeté :
- utilisation des ratios comme verdict;
- correction automatique d'un signal isolé.

### avoid-ai-writing

Source : `https://github.com/conorbronsdon/avoid-ai-writing`

Version auditée : `3.16.0`, publiée le 16 juillet 2026.

Rôle : inspiration pour séparer détection, édition ciblée et réécriture.

Repris :
- mode d'édition minimale qui préserve les passages déjà humains;
- choix explicite entre audit, retouche et réécriture.

Adapté :
- ces modes deviennent l'axe `intensite_intervention` de cette skill;
- la retouche ciblée est le défaut, surtout en contexte technique.

## Règle anti-import

Avant d'ajouter une règle externe :
1. nommer le problème terrain qu'elle résout;
2. définir le risque de faux positif;
3. écrire un cas de préservation et un cas de correction;
4. vérifier qu'elle n'ajoute ni invention, ni quota décoratif, ni perte de précision;
5. l'intégrer comme signal ou gate local, jamais comme synchronisation automatique.
