# Variantes privée et publique

## Noyau commun

Une variante privée et cette variante publique peuvent partager la même doctrine comportementale :
- routage contexte puis intensité;
- retouche ciblée par défaut;
- couverture sémantique;
- protection technique;
- budget de densité;
- gate zéro cadratin;
- contrat de sortie;
- carte des sources et tests génériques.

## Variante privée

Classe recommandée : `personal/local`.

Elle peut contenir des identifiants personnels, conventions métier, chemins, URLs et canaris terrain. Ces éléments ne doivent pas être copiés vers une distribution publique.

## Variante publique

Classe : `portable`.

Elle doit rester :
- générique;
- autonome;
- sans identifiant privé, chemin local réel ou URL interne;
- accompagnée de canaris anonymisés et d'un guide de personnalisation.

## Protocole de synchronisation

1. Modifier d'abord le noyau comportemental dans une branche de travail.
2. Appliquer le même changement aux deux variantes.
3. Réinjecter seulement les différences intentionnelles de chaque enveloppe.
4. Valider les liens, le YAML et les tests sur les deux packages.
5. Scanner la variante publique pour les identifiants privés.
6. Comparer les fichiers communs et documenter toute divergence restante.
7. Ne jamais copier automatiquement les canaris privés dans le dépôt public.

## Fichiers autorisés à diverger

- `SKILL.md` : description, tags et classe de portabilité;
- `README.md`;
- fichier d'intégration runtime locale, privé uniquement;
- `references/register-gate.md`;
- `references/source-boundaries.md`;
- `references/real-corpus-canaries.md`;
- `VARIANTS.md`.

Les autres fichiers doivent rester identiques sauf justification documentée.
