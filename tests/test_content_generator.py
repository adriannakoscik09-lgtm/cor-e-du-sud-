"""Tests pour le générateur de contenu sur la Corée du Sud."""

import pytest

from src.content_generator import ContentGenerator
from src.data import KOREA_DATA, VALID_SECTIONS


@pytest.fixture
def generator():
    return ContentGenerator()


class TestListSections:
    def test_returns_all_valid_sections(self, generator):
        sections = generator.list_sections()
        assert sections == VALID_SECTIONS

    def test_contains_kpop(self, generator):
        assert "kpop" in generator.list_sections()

    def test_contains_tradition(self, generator):
        assert "tradition" in generator.list_sections()

    def test_contains_food(self, generator):
        assert "food" in generator.list_sections()


class TestGenerateSection:
    def test_kpop_section_has_title(self, generator):
        content = generator.generate_section("kpop")
        assert "K-pop" in content

    def test_tradition_section_has_title(self, generator):
        content = generator.generate_section("tradition")
        assert "Traditions" in content

    def test_food_section_has_title(self, generator):
        content = generator.generate_section("food")
        assert "Gastronomie" in content

    def test_section_contains_description(self, generator):
        content = generator.generate_section("kpop")
        assert "Korean Pop" in content

    def test_section_contains_key_figures(self, generator):
        content = generator.generate_section("kpop")
        assert "BTS" in content
        assert "BLACKPINK" in content

    def test_section_contains_facts(self, generator):
        content = generator.generate_section("food")
        assert "kimchi" in content.lower()

    def test_tradition_section_handles_none_fans(self, generator):
        """Les figures traditionnelles n'ont pas de fans (None).
        Le générateur doit gérer ce cas sans erreur."""
        content = generator.generate_section("tradition")
        assert "Hanbok" in content
        assert "fans:" not in content

    def test_food_section_does_not_show_debut_zero(self, generator):
        """Les figures avec debut=0 ne doivent pas afficher '(depuis 0)'.
        Afficher 'depuis 0' n'a pas de sens pour des éléments
        dont l'origine est ancienne ou inconnue."""
        content = generator.generate_section("food")
        assert "Kimchi" in content
        assert "(depuis 0)" not in content

    def test_tradition_section_does_not_show_debut_zero(self, generator):
        """Les figures traditionnelles avec debut=0 ne doivent
        pas afficher '(depuis 0)'."""
        content = generator.generate_section("tradition")
        assert "Calligraphie" in content
        assert "(depuis 0)" not in content

    def test_invalid_section_raises_error(self, generator):
        with pytest.raises(ValueError, match="introuvable"):
            generator.generate_section("invalid_section")


class TestGenerateAll:
    def test_generates_all_sections(self, generator):
        content = generator.generate_all()
        assert "K-pop" in content
        assert "Traditions" in content
        assert "Gastronomie" in content

    def test_sections_separated_by_divider(self, generator):
        content = generator.generate_all()
        assert "---" in content


class TestGetFactCount:
    def test_kpop_fact_count(self, generator):
        """La section kpop a 3 faits dans les données."""
        count = generator.get_fact_count("kpop")
        assert count == 3

    def test_tradition_fact_count(self, generator):
        """La section tradition a 3 faits dans les données."""
        count = generator.get_fact_count("tradition")
        assert count == 3

    def test_food_fact_count(self, generator):
        """La section food a 3 faits dans les données."""
        count = generator.get_fact_count("food")
        assert count == 3

    def test_invalid_section_raises_error(self, generator):
        with pytest.raises(ValueError, match="introuvable"):
            generator.get_fact_count("invalid")