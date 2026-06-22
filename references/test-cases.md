# Cas tests

## 1. Marketing
Doit retirer : adjectifs creux, promesse générique, verbes vides.
Doit préserver : autorité, clarté, niveau pro.

## 2. Post X
Doit retirer : anaphores faciles, morale finale, structure trop parfaite.
Doit préserver : tension, angle, phrase qui accroche.

## 3. Email client
Doit retirer : servilité, "avec plaisir", "n'hésitez pas", faux enthousiasme.
Doit préserver : chaleur, précision, relation.

## 4. Note stratégique
Doit retirer : posture de prof, méta-annonces, auto-validation rhétorique.
Doit préserver : pensée vivante, nuances, vocabulaire métier utile.

## 5. Paragraphe technique
Doit retirer : calques anglais inutiles, flou, sur-promesse.
Doit préserver : termes métier nécessaires.

## 6. Créatif / littéraire
Doit retirer : pseudo-poésie, abstractions émotionnelles, images toutes faites.
Doit préserver : ambiance, tension, silence.

## 7. English fallback
Doit utiliser `en-patterns-legacy` et ne pas appliquer les règles typographiques françaises.

## 8. Typographie FR visible
Entrée typique : email avec tiret cadratin, majuscule après deux-points, title case et virgule avant `et`.
Doit retirer : tiret cadratin hors dialogue, majuscule fautive après deux-points, title case français, virgule d'Oxford.
Doit préserver : noms propres, citations, URLs, slugs.

## 9. Texte technique avec zones protégées
Entrée typique : paragraphe explicatif avec commande, URL, clé YAML ou extrait JSON.
Doit retirer : tics IA dans les phrases autour.
Doit préserver : code, commandes, URLs, slugs, clés JSON/YAML, Markdown sensible.

## 9b. Texte technique hybride
Entrée typique : note n8n/MCP avec `payload`, `node`, `retry_count`, `rewrite_lead=false`, `status_notes`, noms de tables ou noms de nodes.
Doit retirer : transitions molles, justification verbeuse, "il est important de noter".
Doit préserver : termes système hybrides, noms exacts de nodes, flags, champs, tables, fonctions, seuils, liens Markdown et listes complètes de commandes/capacités.

## 10. Texte sensible
Entrée typique : juridique, médical, financier, RH sensible, sécurité ou conformité.
Doit retirer : flou, lourdeur, tics IA évidents.
Doit préserver : prudence, nuances, conditions, limites. Sortie agressive interdite.

## 11. No-op
Entrée typique : texte déjà naturel, précis, court et adapté.
Doit retirer : rien si les corrections seraient cosmétiques.
Doit préserver : voix, rythme, aspérités utiles.

## 12. Échantillon de voix
Doit utiliser le sample pour calibrer rythme, vocabulaire, transitions et aspérités.
Doit éviter : naturel générique, voix trop lissée.

## 13. Faux positif humain
Entrée typique : texte propre, formel, avec un tiret ou une transition isolée.
Doit préserver : style si aucun cluster IA n'apparaît.

## 14. Cadence moderne IA
Doit retirer : punchlines manufacturées, faux aphorismes, fausses confidences, staccato décoratif.
Doit préserver : tension réelle et phrase courte utile.

## 15. Score interne invisible
Doit utiliser le score seulement si utile au diagnostic.
Doit préserver : aucune note chiffrée en sortie normale.

## 16. Canaris techniques
Doit rejouer `real-corpus-canaries.md`.
Doit préserver : tokens, URLs, flags, listes et valeurs exactes.
Doit retirer seulement autour des tokens : punchlines, aphorismes, fausses confidences et métaphores inutiles.

## 17. Note Post X / Markdown complete
Entrée typique : note avec frontmatter, `Draft Final`, `Méta-Analyse`, `Runtime`, `Performance`, archives et parfois `statut_creation: publié`.
Doit isoler : le bloc `Draft Final`, `Version recommandée` ou le bloc demandé.
Doit préserver : frontmatter, URLs, score, runtime, tâches, archives, trace publiée et fautes exactes d'une version déjà publiée.
Doit éviter : réécrire toute la note, corriger silencieusement une archive publiée, afficher un score interne ou transformer les labels éditoriaux en contenu final.
