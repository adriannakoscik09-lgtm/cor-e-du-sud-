# Guide de contribution

Merci de contribuer au projet Corée du Sud !

## Workflow Git

1. Créer une branche depuis `main` : `feature/ma-feature` ou `fix/mon-fix`
2. Coder avec des commits clairs (convention Angular)
3. Pousser et ouvrir une Pull Request vers `main`
4. La CI doit passer (pytest)
5. Merge après revue

## Convention de commits

```
<type>: <description courte>
```

Types : `feat`, `fix`, `docs`, `test`, `chore`, `refactor`, `style`, `perf`

Exemples :
- `feat: ajouter la section K-beauty`
- `fix: corriger get_fact_count`
- `test: ajouter des tests pour generate_all`

## Style de code

- Python 3.12+
- Docstrings sur toutes les classes et méthodes publiques
- Noms de fichiers : `snake_case.py`
- Noms de classes : `PascalCase`

## Tests

- Tout nouveau module doit avoir des tests pytest
- Lancer `python -m pytest tests/ -v` avant de pousser
- La CI GitHub Actions valide automatiquement les PR