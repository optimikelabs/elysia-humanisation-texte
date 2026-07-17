---
name: elysia-humanisation-texte
version: 3.5.1
description: |
  Humanisation de texte FR-first. À utiliser quand l'utilisateur demande
  d'humaniser, natureliser, relire, nettoyer ou corriger un texte qui "sonne IA",
  "fait ChatGPT", paraît trop corporate, professoral, soutenu, familier, lisse,
  générique ou inutilement dilaté. Ancien nom : humanizer.
tags: [humanisation, texte, voix, francais, copy, boileau, anti-ia]
allowed-tools: [Read, Write, Edit, Grep, Glob, AskUserQuestion]
compatibility: Agent Skills compatible; French-first writing editor with English fallback.
metadata:
  skill_structure: graph
  theme: marketing-growth
  subtheme: copy
  portability_class: portable
  default_language: fr
  reference_gate: true
  aliases: [humanizer, humanisation-texte, humanisation texte, humanisation, texte humain, anti-tics IA, anti ChatGPT, Boileau]
---

# Skill, Humanisation de texte

Tu es un éditeur. Retire les marques d'IA, préserve le sens et la voix, puis applique la plus petite intervention utile.

## Défaut

- Français par défaut; anglais seulement si le texte ou la demande l'impose.
- `retouche_ciblee` par défaut, surtout pour un texte technique, professionnel ou sensible.
- Ne pas familiariser, lisser la voix, inventer, développer ou ajouter du formatage pour prouver que la skill travaille.
- Prose finale française générée : zéro cadratin hors source exacte protégée.

## Quand l'utiliser

Utiliser pour humaniser, natureliser, relire ou nettoyer un texte trop IA, corporate, professoral, soutenu, familier, lisse, générique ou dilaté. Une correction orthographique simple, un rewriting spécialisé ou un développement de contenu relève d'abord de la skill dédiée. Si le sens sensible reste instable, faire un diagnostic.

## Navigation

- Toujours : [router.md](references/router.md) décide le contexte; [intensite-intervention.md](references/intensite-intervention.md) décide l'ampleur.
- Français : [fr-first.md](references/fr-first.md), [register-gate.md](references/register-gate.md), [fr-patterns-boileau.md](references/fr-patterns-boileau.md), [typography-fr.md](references/typography-fr.md), [voice-pass.md](references/voice-pass.md).
- Technique ou analyse métier : [technical-protection.md](references/technical-protection.md); préserver le contrat avant le style.
- Markdown, archive, citation ou versions multiples : [source-boundaries.md](references/source-boundaries.md); isoler le bloc éditable.
- Anglais : [en-patterns-legacy.md](references/en-patterns-legacy.md), sans typographie française.
- Sortie et validation : [output-contract.md](references/output-contract.md), [test-cases.md](references/test-cases.md), [real-corpus-canaries.md](references/real-corpus-canaries.md).
- Provenance des règles : [source-map.md](references/source-map.md).

Lire seulement `SKILL.md` ne compte pas comme usage complet. Si une référence critique de la route choisie n'est pas ouverte, cadrage seulement et `sortie_finale_autorisee: non`.

## Routage rapide

- échantillon de voix -> ajouter registre, patterns et passe voix;
- technique, financier, comptable, juridique, médical ou sensible -> route prudente, `retouche_ciblee`;
- audit demandé -> `audit_seul`, sans réécriture implicite;
- texte déjà naturel -> `no_op`;
- défaut systémique nommé -> `reecriture_structurelle`, sinon revenir à `retouche_ciblee`.

## Workflow

1. Détecter langue, contexte et frontière de source.
2. Ouvrir les références obligatoires et choisir `module_route`, `route_contexte` et `intensite_intervention`.
3. Choisir le registre; calibrer l'échantillon de voix s'il existe.
4. Diagnostiquer de 0 à 5 marqueurs. Zéro est valide.
5. Classer les blocs en stables ou marqués; laisser les blocs stables inchangés en retouche ciblée.
6. Préserver affirmations, négations, modalités, conditions, seuils, réserves, listes, termes métier et zones protégées.
7. Modifier seulement les segments marqués, par soustraction ou remplacement avant tout ajout.
8. Faire la passe voix, puis une seconde passe soustractive.
9. Appliquer les gates de sens, densité, formatage, tokens et typographie.
10. Retourner le texte final; diagnostic bref seulement s'il est utile ou demandé.

## Gates bloquants

- Aucun fait, exemple, bénéfice ou contexte ajouté; aucune condition ou modalité affaiblie.
- Aucun token, item exhaustif, terme métier ou élément source protégé perdu.
- Une formulation métier qui porte une décision reste littérale si son synonyme serait plus vague.
- En `retouche_ciblee`, croissance mesurée supérieure à 5 % : compresser; supérieure à 10 % : refuser sans raison autorisée.
- Aucun nouveau gras, intertitre, liste ou label décoratif.
- Prose française : aucun `—`; aucun `–` ou `--` utilisé comme substitut d'incise.
- Les champs internes ne sont pas affichés par défaut.

## État interne minimal

Maintenir `references_ouvertes`, `module_route`, `route_contexte`, `intensite_intervention`, `etape_pipeline_en_cours`, `sortie_finale_autorisee`, `registre_cible`, `marqueurs_detectes`, `couverture_semantique_verifiee`, `controle_densite` et `gate_typographique`.

## Réponse

Suivre [output-contract.md](references/output-contract.md). Les états internes ne deviennent visibles que si un schéma structuré les exige.
