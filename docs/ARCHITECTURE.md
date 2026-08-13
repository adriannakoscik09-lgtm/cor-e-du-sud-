# Architecture

## Vue d'ensemble

Le projet est un générateur de contenu Python sur la Corée du Sud, couvrant trois thèmes : la K-pop, les traditions et la gastronomie.

## Structure

```
cor-e-du-sud-/
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline CI (Python + pytest)
├── src/
│   ├── __init__.py             # Init package, version
│   ├── data.py                 # Données structurées (KOREA_DATA, VALID_SECTIONS)
│   └── content_generator.py    # Générateur de contenu formaté (ContentGenerator)
├── tests/
│   ├── __init__.py
│   └── test_content_generator.py  # 21 tests pytest
├── .gitignore
├── requirements.txt            # pytest>=7.0
└── README.md
```

## Couches

### Données (`src/data.py`)
Source de vérité du contenu. Dictionnaire `KOREA_DATA` avec 3 sections :
- `kpop` : groupes, fans, faits
- `tradition` : hanbok, hanok, calligraphie, faits
- `food` : kimchi, bibimbap, bulgogi, tteokbokki, faits

### Logique (`src/content_generator.py`)
Classe `ContentGenerator` :
- `list_sections()` : retourne les sections disponibles
- `generate_section(name)` : génère le contenu Markdown pour une section
- `generate_all()` : génère tout le contenu concaténé
- `get_fact_count(name)` : retourne le nombre de faits d'une section

### Tests (`tests/test_content_generator.py`)
21 tests pytest couvrant :
- Liste des sections
- Génération de sections (titre, description, figures, faits)
- Gestion des `fans: None` (figures traditionnelles)
- Gestion des `debut=0` avec et sans fans (pas de '(depuis 0)')
- Gestion des erreurs (section inexistante)
- Génération complète
- Comptage de faits

## CI

GitHub Actions (`.github/workflows/ci.yml`) :
1. Checkout du code
2. Setup Python 3.11
3. `pip install -r requirements.txt`
4. `python -m pytest tests/ -v`

## Conventions

- **Commits** : convention Angular (`feat:`, `fix:`, `docs:`, `test:`, `chore:`, `refactor:`)
- **Branches** : `feature/`, `fix/` depuis `main`
- **Code** : Python 3.12+, type hints recommandés
- **Tests** : tout nouveau module doit avoir des tests pytest