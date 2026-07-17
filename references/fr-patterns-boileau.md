# Patterns français inspirés de Boileau

Source d'inspiration : `alxbd/boileau`, skill dédiée au nettoyage des marques IA dans les textes français. Les grilles Babeleur, collectifweb et les sources listées dans `source-map.md` servent de contre-check. Elles ne deviennent jamais un second canon.

## Garde-fou anti-faux-positifs

Ne pas corriger un texte seulement parce qu'il est propre, formel, sec, bien ponctué ou bien structuré.

Un signal isolé ne suffit pas. Chercher des clusters : plusieurs tics qui produisent ensemble une cadence artificielle.

Règle de fonction : un pattern n'est pas un tic tant qu'il remplit une fonction lisible. Avant de corriger staccato, répétition, triade, aphorisme, confidence, familier ou métaphore, vérifier s'il porte un contraste, une progression, un souffle, une mémoire, un hook, une précision ou une voix d'auteur.

Corriger seulement si la forme remplace l'idée, masque le flou, rend la cadence trop régulière, empile plusieurs effets identiques ou donne une fausse profondeur.

À préserver :
- détail précis, rare ou difficile à inventer;
- tension non résolue;
- parenthèses et auto-corrections utiles;
- répétition volontaire;
- mélange de registre cohérent avec l'auteur;
- phrase courte isolée qui sert vraiment le point;
- neutralité et densité d'un passage technique exact.

Un cadratin isolé n'est pas une preuve d'écriture IA. Dans la production finale française, il reste néanmoins interdit par la convention éditoriale de `typography-fr.md`.

## Priorité haute

### Faux registre soutenu

Signaux : `il convient de`, `force est de constater`, `à l'aune de`, `au regard de`, `procéder à`, `s'avérer`, `problématique` comme nom, `thématique`, `finalité`.

Correction : préférer le mot simple si le texte n'a pas besoin d'un registre académique.

### Verbes vides

Signaux : `permettre de`, `favoriser`, `optimiser`, `valoriser`, `accompagner`, `répondre aux enjeux`, `mettre en œuvre`, `s'inscrire dans`.

Correction : chercher l'action concrète. Si elle manque, simplifier sans inventer.

### Lexique gonflé

Signaux : `crucial`, `fondamental`, `incontournable`, `révolutionnaire`, `fascinant`, `significatif`, `profondément`, `véritablement`, `absolument`.

Correction : supprimer l'intensifieur ou le remplacer par une preuve déjà présente. Ne pas ajouter de preuve.

### Calques anglais

Signaux : `adresser un problème`, `faire du sens`, `délivrer de la valeur`, `supporter` pour `prendre en charge`, `basé sur`, `drive`, `matcher`, `sourcer`, virgule avant `et`.

Correction : employer une tournure française naturelle.

### Connecteurs en pluie

Signaux : paragraphes ouverts par `Par ailleurs`, `De plus`, `En outre`, `Néanmoins`, `Toutefois`, `Cependant`, `Ainsi`, `Par conséquent`, `En définitive`.

Correction : supprimer ou remplacer par une articulation simple qui exprime une relation réelle.

### Transitions mortes

Signaux : `il est important de noter que`, `il convient de souligner`, `dans ce contexte`, `à cet égard`, `cela étant dit`, `en résumé`, `en conclusion`.

Correction : supprimer si la phrase ne porte aucune relation logique réelle. Sinon, utiliser un lien simple ou une phrase directe.

### Auto-validation rhétorique

Signaux : `voilà tout l'enjeu`, `c'est précisément le but`, `c'est là que tout se joue`, `voilà l'idée`.

Correction : dire l'idée, puis passer à la suite.

### Posture didactique

Signaux : `ce qu'il faut comprendre`, `il faut savoir`, `retenez ceci`, `gardez à l'esprit`, `notez que`.

Correction : présenter l'information sans parler au lecteur comme à un élève.

### Queues d'analyse creuses

Signaux : `soulignant ainsi l'importance de`, `illustrant la pertinence de`, `reflétant les enjeux de`, `mettant en lumière la nécessité de`.

Correction : couper la queue ou la transformer uniquement si une information vérifiable est déjà présente.

### Humanité ajoutée de force

Signaux : ajout de chaleur, première personne, aparté, anecdote, analogie, question rhétorique, transition conversationnelle ou bénéfice produit autour d'un passage technique qui était déjà clair.

Risque : le texte grossit et devient moins exact tout en paraissant plus expressif.

Correction : revenir à la neutralité utile, supprimer les ajouts sans information et passer en `retouche_ciblee`.

### Dilatation explicative

Signaux : chaque phrase source devient deux phrases, une condition simple reçoit une paraphrase, les mêmes conséquences sont reformulées, des transitions sont ajoutées entre des paragraphes déjà cohérents.

Correction : conserver la couverture sémantique avec moins de mots. Une reformulation locale n'autorise pas à développer le sujet.

### Emphase de formatage

Signaux : nouveaux mots en gras, mini-intertitres, labels ou listes ajoutés pour fabriquer une hiérarchie qui n'existait pas.

Correction : préserver le format utile existant, ne pas ajouter de formatage décoratif.

## Priorité moyenne

### Cadence manufacturée

Signaux : suite de fragments courts, phrases qui veulent toutes tomber, morale finale, cadence de punchline.

Garder le staccato s'il crée un silence, un contraste ou un appui réel. Exemple à préserver : `La note est revenue. Pas la pensée.`

Correction : casser seulement les séries trop parfaites et les fins de paragraphe qui cherchent toutes la punchline.

### Aphorismes creux

Signaux : `X est le Y de Z`, `X devient un piège`, `le langage de`, `la monnaie de`, `l'architecture de`.

Garder si la formule condense vraiment l'idée ou sert de hook, puis laisser le texte donner la conséquence concrète.

Correction : remplacer la formule par l'idée si elle sonne juste mais ne dit rien de vérifiable.

### Fausses confidences

Signaux : `Honnêtement ?`, `Le truc, c'est que`, `Soyons clairs`, `La vraie question`, utilisés comme pause théâtrale.

Garder si la confidence est une vraie oralité, un pivot de voix ou un changement d'angle.

Correction : dire directement l'idée si la formule sert seulement à théâtraliser une phrase faible.

### Écriture ancrée dans le diff

Signaux : texte qui raconte ce qui a changé au lieu de décrire l'état actuel, hors changelog, release note ou migration.

Correction : reformuler comme une vérité stable du document.

### Agency abstraite sans acteur

Signaux : `la décision émerge`, `le marché récompense`, `la culture change`, `la conversation se déplace`.

Correction : nommer l'acteur quand il existe, sinon rester sobre sans inventer.

### Faux naturel familier

Signaux : `ça pique`, `ça coince`, `ça gratte`, `ça envoie`, `ça fait le job`, `plutôt cool`, `grosso modo`, `en gros` dans un texte professionnel.

Garder dans un post court ou une voix personnelle si l'expression porte le rythme et reste cohérente avec l'auteur.

Correction : choisir un registre cohérent. Pro sobre par défaut.

### Doublets et triades

Signaux : `simple et intuitif`, `robuste et fiable`, `rapide et efficace`, listes de trois adjectifs abstraits.

Garder une triade si chaque item ajoute une marche réelle : angle, critère, étape, preuve ou conséquence.

Correction : garder le mot utile ou une preuve déjà présente quand la liste recycle des synonymes.

### Structures scolaires

Signaux : `non seulement... mais aussi`, `tant... que...`, `c'est ainsi que`, plans trop visibles `Défis / Perspectives`, introductions qui annoncent le plan sans dire l'idée.

Correction : préférer la coordination simple et le déroulé naturel.

### Parallélisme négatif

Signaux : `ce n'est pas X, c'est Y`, `il ne s'agit pas de... il s'agit de...`, `Pas X. Y.`, `Ce n'est pas juste X. C'est Y.`

Attention : signal faible, pas faute automatique.

Garder si l'opposition tranche une vraie distinction, sert de pivot, appuie le rythme ou porte manifestement la voix de l'auteur.

Corriger seulement si le contraste est décoratif, empilé, interchangeable ou répété sans nécessité.

### Anaphores marketing

Signaux : `Pour celles qui...`, `Parce que...` répété, `Plus de X. Plus de Y.`

Garder la répétition volontaire si elle crée une progression, un martèlement utile ou une mémoire de lecture.

Correction : varier, condenser ou couper si le rythme recycle la même idée.

### Transitions pseudo-journalistiques

Signaux : `derrière les chiffres se cache`, `plus complexe qu'il n'y paraît`, `en apparence... mais en réalité`.

Correction : donner directement la nuance.

### Pseudo-littéraire

Signaux : `promesse murmurée`, `secret brûlant`, `désir vibrant`, `comme si le temps s'était figé`.

Correction : revenir au concret, à l'image juste ou au silence.

### Métaphores trop propres

Signaux : image très lisse, analogie trop symétrique, métaphore qui remplace l'idée au lieu de l'éclairer.

Garder si l'image est l'angle du texte, rend l'idée mémorable ou clarifie une tension réelle.

Correction : couper ou expliciter si l'image masque le propos ou donne une fausse profondeur.

### Sycophance et importance automatique

Signaux : présenter un sujet comme `majeur`, `clé`, `essentiel pour l'avenir` uniquement parce que le texte en parle.

Correction : dire pourquoi avec une conséquence réelle, ou retirer l'importance annoncée.

## Signaux généraux à surveiller

- inflation de l'importance;
- attribution vague;
- conclusion positive générique;
- sections `Défis et perspectives`;
- langage promotionnel touristique ou corporate;
- expansion prise à tort pour de l'humanisation;
- score anti-tics pris comme objectif plutôt que comme outil de diagnostic.
