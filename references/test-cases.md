# Cas tests

## Règle de lecture

Chaque cas précise ce qui doit changer et ce qui doit rester. Une réussite ne se mesure pas au nombre de modifications, mais au respect du sens, de la voix, de la densité et des zones protégées.

## 1. Marketing

Doit retirer : adjectifs creux, promesse générique, verbes vides.

Doit préserver : autorité, clarté, niveau professionnel et preuves existantes.

## 2. Post social

Doit retirer : anaphores faciles, morale finale, structure trop parfaite.

Doit préserver : tension, angle, phrase qui accroche et répétition fonctionnelle.

## 3. Email client

Doit retirer : servilité, faux enthousiasme, préambules automatiques.

Doit préserver : chaleur, précision et relation.

## 4. Note stratégique

Doit retirer : posture de professeur, méta-annonces, auto-validation rhétorique.

Doit préserver : pensée vivante, nuances et vocabulaire métier utile.

## 5. Paragraphe technique

Doit retirer : calques inutiles, flou, sur-promesse et transitions mortes.

Doit préserver : termes métier, structure utile et densité. Intensité attendue : `retouche_ciblee`.

## 6. Créatif ou littéraire

Doit retirer : pseudo-poésie, abstractions émotionnelles, images toutes faites.

Doit préserver : ambiance, tension, silence et étrangeté utile.

## 7. English fallback

Doit utiliser `en-patterns-legacy.md` et ne pas appliquer le gate français zéro cadratin.

## 8. Typographie française visible

Entrée typique : email avec cadratin, majuscule après deux-points, title case et virgule avant `et`.

Doit retirer : tout cadratin généré hors zone source, majuscule fautive après deux-points, title case français et virgule d'Oxford.

Doit préserver : noms propres, citations exactes, URLs et slugs.

## 9. Texte technique avec zones protégées

Entrée typique : paragraphe explicatif avec commande, URL, clé YAML ou extrait JSON.

Doit retirer : tics dans les phrases autour.

Doit préserver : code, commandes, URLs, slugs, clés, listes et Markdown sensible.

## 10. Texte technique hybride

Entrée typique : note n8n ou MCP avec `payload`, `node`, `retry_count`, `rewrite_lead=false`, `status_notes`, tables ou noms de nodes.

Doit retirer : transitions molles, justification verbeuse et humanité ajoutée de force.

Doit préserver : termes système, flags, champs, seuils, liens et listes complètes.

## 11. Texte sensible

Entrée typique : juridique, médical, financier, comptable, RH sensible, sécurité ou conformité.

Doit retirer : lourdeur et tics certains.

Doit préserver : prudence, nuances, conditions et limites. Intensité attendue : `retouche_ciblee`.

## 12. No-op

Entrée typique : texte déjà naturel, précis, court et adapté.

Doit retirer : rien si les corrections seraient cosmétiques.

Doit préserver : voix, rythme et aspérités. Zéro marqueur est valide.

## 13. Échantillon de voix

Doit utiliser l'échantillon pour calibrer rythme, vocabulaire, transitions et aspérités.

Doit éviter : naturel générique, expansion et copie mécanique des défauts.

## 14. Faux positif humain

Entrée typique : texte propre, formel, avec une transition ou une ponctuation marquée isolée.

Doit préserver : le style si aucun cluster n'apparaît.

## 15. Cadence moderne

Doit retirer : punchlines manufacturées, faux aphorismes, fausses confidences et staccato décoratif.

Doit préserver : tension réelle et phrase courte utile.

## 16. Parallélisme négatif utile

Entrée : `Pas X. Y.` ou `Ce n'est pas juste X. C'est Y.` utilisé comme pivot réel.

Doit préserver : l'opposition si elle tranche une distinction ou porte la voix.

Doit retirer : formes décoratives, empilées, interchangeables ou répétées sans nécessité.

## 17. Staccato utile

Entrée : `La note est revenue. Pas la pensée.`

Doit préserver : les phrases courtes qui créent un silence ou un contraste.

## 18. Répétition volontaire

Entrée : `Pas assez pour écrire. Pas assez pour décider. Pas assez pour relier.`

Doit préserver : progression et mémoire de lecture.

Doit retirer : répétition qui recycle la même idée.

## 19. Triade utile

Doit préserver : trois items qui ajoutent chacun un critère, une étape ou une conséquence.

Doit retirer : triade de synonymes abstraits comme `simple, puissant, efficace`.

## 20. Aphorisme utile

Doit préserver : formule qui condense vraiment l'idée et dont la suite donne une conséquence concrète.

Doit retirer : formule qui remplace l'argument.

## 21. Typographie sociale utile

Entrée typique : saut de ligne, parenthèse ou ponctuation imparfaite qui porte le souffle d'un post court.

Doit préserver : la respiration utile.

Doit éviter : lisser le rythme ou générer un cadratin pour recréer le souffle.

## 22. Métaphore utile

Doit préserver : image qui clarifie ou condense une tension réelle.

Doit retirer : image décorative qui remplace l'idée.

## 23. Document Markdown complet

Entrée : document avec frontmatter, brouillon, notes éditoriales, performance, archives et trace de publication.

Doit isoler : le bloc demandé ou recommandé.

Doit préserver : frontmatter, URLs, scores, notes, tâches, archives et version publiée.

## 24. Concrétisation inventée

Entrée : ouverture générale sans personne, lieu ou scène fournie.

Doit préserver : le niveau de généralité.

Doit éviter : inventer une scène, une durée, un personnage ou une anecdote.

## 25. Diagnostic mesuré

Doit préserver : diagnostic bref, séparé du texte final.

Doit éviter : comptages, pourcentages ou comparaisons non mesurés.

## 26. Remplacement fonctionnel du cadratin

Entrées :
- incise;
- précision ambiguë;
- rupture avant une chute.

Doit produire respectivement :
- virgules;
- parenthèses;
- deux-points ou point.

Doit éviter : `—`, ou l'utilisation de `–` et `--` comme échappatoire stylistique.

## 27. Citation source exacte

Entrée : citation contenant un cadratin, suivie d'une prose explicative française.

Doit préserver : le cadratin uniquement dans la citation protégée si l'exactitude est demandée.

Doit retirer : tout cadratin dans la prose générée autour.

## 28. Densité technique longue

Entrée : article technique de plus de 250 mots avec trois passages marqués et plusieurs paragraphes déjà clairs.

Doit modifier : seulement les trois passages.

Doit préserver : les autres paragraphes, les conditions et les termes métier.

Gate : si un comptage fiable est disponible, toute hausse supérieure à 5 % déclenche une compression; une hausse supérieure à 10 % est refusée sans raison autorisée.

## 29. Réécriture structurelle justifiée

Entrée : plusieurs paragraphes construits sur le même plan scolaire, avec introduction et conclusion génériques.

Doit choisir : `reecriture_structurelle` et nommer le défaut systémique en interne.

Doit préserver : blocs déjà solides, thèse, preuves et réserves.

## 30. Retouche ciblée prioritaire

Entrée : texte globalement naturel avec deux transitions mortes.

Doit choisir : `retouche_ciblee`.

Doit éviter : réordonner tout le texte ou changer le registre.

## 31. Zéro marqueur valide

Entrée : texte humain, exact et adapté.

Doit choisir : `no_op`.

Doit éviter : remplir artificiellement un diagnostic.

## 32. Aucun nouveau gras

Entrée : texte sans gras Markdown.

Doit préserver : absence de gras, sauf demande explicite ou nécessité fonctionnelle du support.

## 33. Seconde passe soustractive

Entrée : première version réécrite qui a ajouté deux transitions et une paraphrase.

Doit retirer : les trois ajouts si aucune information n'est gagnée.

## 34. Développement explicitement demandé

Entrée : demande combinée `développe puis humanise`.

Doit distinguer : objectif d'expansion et passe d'humanisation.

Doit éviter : présenter l'augmentation de longueur comme une conséquence nécessaire de l'humanisation.

## 35. Contrat de sortie

Entrée : demande normale de réécriture.

Doit produire : texte final puis diagnostic bref si utile.

Doit éviter : afficher les champs internes, labels de pipeline ou bandeaux de traitement.
