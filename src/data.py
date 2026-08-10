"""Données sur la Corée du Sud : K-pop, traditions, gastronomie."""

KOREA_DATA = {
    "kpop": {
        "title": "K-pop : le phénomène mondial",
        "description": (
            "La K-pop (Korean Pop) est un genre musical né en Corée du Sud "
            "qui a conquis le monde. Des groupes comme BTS, BLACKPINK, "
            "Stray Kids et TWICE remplissent des stades entiers sur tous "
            "les continents."
        ),
        "key_figures": [
            {"name": "BTS", "debut": 2013, "fans": "ARMY"},
            {"name": "BLACKPINK", "debut": 2016, "fans": "BLINK"},
            {"name": "Stray Kids", "debut": 2018, "fans": "STAY"},
            {"name": "TWICE", "debut": 2015, "fans": "ONCE"},
        ],
        "facts": [
            "Le clip 'Dynamite' de BTS a atteint 1 milliard de vues en record.",
            "BLACKPINK est le premier groupe K-pop à headliner Coachella.",
            "La K-pop génère plus de 10 milliards de dollars par an pour l'économie sud-coréenne.",
        ],
    },
    "tradition": {
        "title": "Traditions : un héritage millénaire",
        "description": (
            "La Corée du Sud préserve un riche patrimoine traditionnel "
            "malgré sa modernisation fulgurante. Du hanbok (vêtement "
            "traditionnel) au hanok (architecture traditionnelle), "
            "la culture coréenne puise ses racines dans plusieurs "
            "millénaires d'histoire."
        ),
        "key_figures": [
            {"name": "Hanbok", "debut": 57, "fans": None},
            {"name": "Hanok", "debut": 14, "fans": None},
            {"name": "Calligraphie", "debut": 0, "fans": None},
            {"name": "Tal (masques traditionnels)", "debut": 0, "fans": None},
        ],
        "facts": [
            "Le hanbok est porté lors des fêtes comme Chuseok (action de grâces).",
            "Les hanoks utilisent le système de chauffage ondol, vieux de plus de 2000 ans.",
            "La Corée compte 21 sites inscrits au patrimoine mondial de l'UNESCO.",
        ],
    },
    "food": {
        "title": "Gastronomie : saveurs et fermentation",
        "description": (
            "La cuisine coréenne est reconnue mondialement pour ses "
            "saveurs audacieuses et ses plats fermentés. Le kimchi, "
            "le bibimbap et le barbecue coréen sont des emblèmes "
            "culinaires qui racontent l'histoire du pays."
        ),
        "key_figures": [
            {"name": "Kimchi", "debut": 0, "fans": None},
            {"name": "Bibimbap", "debut": 0, "fans": None},
            {"name": "Bulgogi", "debut": 0, "fans": None},
            {"name": "Tteokbokki", "debut": 0, "fans": None},
        ],
        "facts": [
            "Il existe plus de 200 variétés de kimchi.",
            "Le bibimbap signifie littéralement 'riz mélangé'.",
            "La fermentation du kimchi peut durer de quelques jours à plusieurs années.",
        ],
    },
}

VALID_SECTIONS = list(KOREA_DATA.keys())