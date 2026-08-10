# Corée du Sud — Générateur de contenu

Projet de génération de contenu sur la Corée du Sud, couvrant la K-pop, les traditions et la gastronomie.

## Structure

- `src/` — code source
- `src/data.py` — données sur la Corée du Sud (K-pop, traditions, cuisine)
- `src/content_generator.py` — générateur de contenu
- `tests/` — suite de tests (pytest)
- `.github/workflows/` — intégration continue

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```python
from src.content_generator import ContentGenerator

generator = ContentGenerator()
print(generator.generate_section("kpop"))
print(generator.generate_section("tradition"))
print(generator.generate_section("food"))
```

## Tests

```bash
python -m pytest tests/ -v
```

## Licence

Propriétaire — Company #820199