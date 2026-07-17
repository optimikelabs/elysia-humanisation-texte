# Tests reproductibles

`fixtures.json` décrit des assertions déterministes sur les sorties d'un modèle : tokens, modalités, formulations métier, blocs stables, densité, gras et cadratins.

Le modèle doit produire un JSON de forme :

```json
{"results":[{"id":"modalites_comptables","output":"..."}]}
```

Validation locale :

```powershell
python tests/validate_package.py
python tests/validate_outputs.py tests/fixtures.json tests/sample-output.json
```

Le script ne juge pas la qualité littéraire. Il bloque les régressions objectivables avant la revue humaine.
