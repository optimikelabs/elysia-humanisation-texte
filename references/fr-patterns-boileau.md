# Patterns français inspirés de Boileau

Source d'inspiration : `alxbd/boileau`, skill dédiée au nettoyage des marques IA dans les textes français. Les grilles Babeleur / collectifweb peuvent servir de contre-check. On adapte les patterns utiles; on ne copie aucune source externe comme second canon.

## Garde-fou anti-faux-positifs

Ne pas corriger un texte seulement parce qu'il est propre, formel, sec, bien ponctué ou bien structuré.

Un signal isolé ne suffit pas. Chercher des clusters : plusieurs tics qui produisent ensemble une cadence IA.

Règle de fonction : un pattern n'est pas un tic tant qu'il remplit une fonction lisible. Avant de corriger staccato, répétition, triade, aphorisme, fausse confidence, familier ou métaphore, vérifier s'il porte un contraste, une progression, un souffle, une mémoire, un hook, une précision ou une voix d'auteur.

Corriger seulement si la forme remplace l'idée, masque le flou, rend la cadence trop régulière, empile plusieurs effets identiques ou donne une fausse profondeur.

À préserver :
- détail précis, rare ou difficile à inventer;
- tension non résolue;
- asides, parenthèses, auto-corrections utiles;
- répétition volontaire;
- mélange de registre cohérent avec l'auteur;
- phrase courte isolée qui sert vraiment le point.

## Priorité haute

### Faux registre soutenu
Signaux : `il convient de`, `force est de constater`, `à l'aune de`, `au regard de`, `procéder à`, `s'avérer`, `problématique` comme nom, `thématique`, `finalité`.

Correction : préférer le mot simple si le texte n'a pas besoin d'un registre académique.

### Verbes vides
Signaux : `permettre de`, `favoriser`, `optimiser`, `valoriser`, `accompagner`, `répondre aux enjeux`, `mettre en œuvre`, `s'inscrire dans`.

Correction : chercher l'action concrète. Si elle manque, simplifier sans inventer.

### Lexique gonflé
Signaux : `crucial`, `fondamental`, `incontournable`, `révolutionnaire`, `fascinant`, `significatif`, `profondément`, `véritablement`, `absolument`.

Correction : supprimer l'intensifieur ou le remplacer par une preuve déjà présente. Ne pas ajouter de preuve inventée.

### Calques anglais
Signaux : `adresser un problème`, `faire du sens`, `délivrer de la valeur`, `supporter` pour `prendre en charge`, `basé sur`, `drive`, `matcher`, `sourcer`, virgule avant `et`.

Correction : employer une tournure française naturelle.

### Connecteurs en pluie
Signaux : paragraphes ouverts par `Par ailleurs`, `De plus`, `En outre`, `Néanmoins`, `Toutefois`, `Cependant`, `Ainsi`, `Par conséquent`, `En définitive`.

Correction : supprimer ou remplacer par une articulation plus simple.

### Transitions mortes
Signaux : `il est important de noter que`, `il convient de souligner`, `dans ce contexte`, `à cet égard`, `cela étant dit`, `en résumé`, `en conclusion`.

Correction : supprimer si la phrase ne porte aucune relation logique réelle; sinon remplacer par `car`, `donc`, `or`, `pourtant`, `en revanche` ou une phrase directe.

### Auto-validation rhétorique
Signaux : `voilà tout l'enjeu`, `c'est précisément le but`, `c'est là que tout se joue`, `voilà l'idée`.

Correction : dire l'idée, puis passer à la suite.

### Posture didactique
Signaux : `ce qu'il faut comprendre`, `il faut savoir`, `retenez ceci`, `gardez à l'esprit`, `notez que`.

Correction : présenter l'information sans parler au lecteur comme à un élève.

### Queues d'analyse creuses
Signaux : `soulignant ainsi l'importance de`, `illustrant la pertinence de`, `reflétant les enjeux de`, `mettant en lumière la nécessité de`.

Correction : couper la queue de phrase ou la transformer en phrase concrète si elle ajoute une information vérifiable.

## Priorité moyenne

### Cadence manufacturée

Signaux : suite de fragments courts, phrases qui veulent toutes "tomber", morale finale, cadence de punchline.

Garder le staccato s'il crée un silence, un contraste ou un appui réel. Exemple à préserver : `La note est revenue. Pas la pensée.`

Correction : casser seulement les séries trop parfaites, les fins de paragraphe qui cherchent toutes la punchline, ou les fragments ajoutés pour fabriquer de l'intensité.

### Aphorismes creux

Signaux : `X est le Y de Z`, `X devient un piège`, `le langage de`, `la monnaie de`, `l'architecture de`.

Garder si la formule condense vraiment l'idée ou sert de hook, puis laisser le texte donner la conséquence concrète.

Correction : remplacer la formule par l'idée concrète si elle sonne juste mais ne dit rien de vérifiable, ne change pas la compréhension, ou remplace l'argument.

### Fausses confidences

Signaux : `Honnêtement ?`, `Le truc, c'est que`, `Soyons clairs`, `La vraie question`, utilisés comme pause théâtrale.

Garder si la confidence est une vraie oralité, un pivot de voix ou un changement d'angle.

Correction : dire directement l'idée si la formule sert seulement à théâtraliser une phrase faible.

### Écriture ancrée dans le diff

Signaux : texte qui raconte ce qui a changé au lieu de décrire l'état actuel, hors changelog, release note ou migration.

Correction : reformuler comme une vérité stable du document.

### Agency abstraite sans acteur

Signaux : `la décision émerge`, `le marché récompense`, `la culture change`, `la conversation se déplace`.

Correction : nommer l'acteur quand il existe; sinon rester sobre sans inventer.

### Faux naturel familier
Signaux : `ça pique`, `ça coince`, `ça gratte`, `ça envoie`, `ça fait le job`, `plutôt cool`, `grosso modo`, `en gros` dans un texte pro.

Garder dans un post court ou une voix personnelle si l'expression porte le rythme et reste cohérente avec l'auteur.

Correction : choisir un registre cohérent. Pro sobre par défaut, surtout dans une page, un email client ou un document commercial.

### Doublets et triades
Signaux : `simple et intuitif`, `robuste et fiable`, `rapide et efficace`, listes de trois adjectifs abstraits.

Garder une triade si chaque item ajoute une marche réelle : angle, critère, étape, preuve ou conséquence.

Correction : garder le mot utile ou remplacer par une preuve quand la liste recycle des synonymes ou cherche seulement un rythme ternaire.

### Structures scolaires
Signaux : `non seulement... mais aussi`, `tant... que...`, `c'est ainsi que`, plans trop visibles `Défis / Perspectives`, introductions qui annoncent le plan sans dire l'idée.

Correction : préférer la coordination simple et le déroulé naturel.

### Parallélisme négatif
Signaux : `ce n'est pas X, c'est Y`, `il ne s'agit pas de... il s'agit de...`.

Signaux sociaux courts : `Pas X. Y.`, `Pas le plus X. Le plus Y.`, `Ce n'est pas juste X. C'est Y.`

Attention : signal faible, pas faute automatique. En post court, ce rythme peut appuyer une vraie opposition, mais il peut aussi devenir un gabarit.

Garder si l'opposition tranche une vraie distinction, sert de phrase-pivot, appuie le rythme ou porte manifestement la voix de l'auteur.

Risque IA : cadence reconnaissable quand l'opposition est décorative, empilée, interchangeable, répétée sans nécessité ou ajoutée pour donner une fausse profondeur.

Correction : arbitrer selon la fonction réelle dans le passage. Ne pas supprimer un parallélisme utile; réécrire seulement si le contraste ne change rien, si plusieurs formes identiques s'empilent, ou si le second membre répète juste le premier en plus solennel.

### Anaphores marketing
Signaux : `Pour celles qui...`, `Parce que...` répété, `Plus de X. Plus de Y.`

Garder la répétition volontaire si elle crée une progression, un martèlement utile ou une mémoire de lecture. Exemple : `Pas assez pour écrire. Pas assez pour décider. Pas assez pour relier.`

Correction : utiliser ce rythme seulement si c'est une intention claire; sinon varier, condenser ou couper.

### Transitions pseudo-journalistiques
Signaux : `derrière les chiffres se cache`, `plus complexe qu'il n'y paraît`, `en apparence... mais en réalité`.

Correction : donner directement la nuance.

### Pseudo-littéraire
Signaux : `promesse murmurée`, `secret brûlant`, `désir vibrant`, `comme si le temps s'était figé`.

Correction : revenir au concret, à l'image juste, ou au silence.

### Métaphores trop propres
Signaux : image très lisse, analogie trop symétrique, métaphore qui remplace l'idée au lieu de l'éclairer.

Garder si l'image est l'angle du texte, rend l'idée mémorable ou clarifie une tension réelle.

Correction : couper ou expliciter si l'image masque le propos, donne une fausse profondeur ou ressemble à une décoration de surface.

### Sycophance et importance automatique
Signaux : présenter un sujet comme `majeur`, `clé`, `essentiel pour l'avenir` uniquement parce que le texte parle de lui.

Correction : dire pourquoi c'est important, avec une conséquence réelle, ou retirer l'importance annoncée.

## Signaux IA généraux à surveiller
- inflation de l'importance;
- attribution vague;
- conclusion positive générique;
- sections `Défis et perspectives`;
- langage promotionnel touristique ou corporate.
- score anti-tics pris comme objectif plutôt que comme outil de diagnostic.
