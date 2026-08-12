"""Générateur de contenu sur la Corée du Sud.

Ce module génère des sections de contenu formaté à partir des données
définies dans src/data.py.
"""

from src.data import KOREA_DATA, VALID_SECTIONS


class ContentGenerator:
    """Génère du contenu formaté sur la Corée du Sud."""

    def __init__(self):
        self.data = KOREA_DATA

    def list_sections(self):
        """Retourne la liste des sections disponibles."""
        return VALID_SECTIONS

    def generate_section(self, section_name):
        """Génère le contenu formaté pour une section donnée.

        Args:
            section_name: nom de la section ('kpop', 'tradition', 'food').

        Returns:
            Une chaîne formatée avec le titre, la description, les figures
            clés et les faits intéressants.

        Raises:
            ValueError: si la section n'existe pas.
        """
        if section_name not in self.data:
            raise ValueError(
                f"Section '{section_name}' introuvable. "
                f"Sections disponibles: {', '.join(self.list_sections())}"
            )

        section = self.data[section_name]
        lines = []

        # Titre
        lines.append(f"# {section['title']}")
        lines.append("")

        # Description
        lines.append(section["description"])
        lines.append("")

        # Figures clés
        lines.append("## Points clés")
        for figure in section["key_figures"]:
            debut = figure.get("debut", 0)
            has_fans = "fans" in figure and figure["fans"] is not None
            if debut and has_fans:
                lines.append(
                    f"- **{figure['name']}** (depuis {debut}) — fans: {figure['fans']}"
                )
            elif debut:
                lines.append(f"- **{figure['name']}** (depuis {debut})")
            elif has_fans:
                lines.append(f"- **{figure['name']}** — fans: {figure['fans']}")
            else:
                lines.append(f"- **{figure['name']}")
        lines.append("")

        # Faits intéressants
        lines.append("## Le saviez-vous ?")
        for i, fact in enumerate(section["facts"], start=1):
            lines.append(f"{i}. {fact}")

        return "\n".join(lines)

    def generate_all(self):
        """Génère le contenu complet pour toutes les sections."""
        sections = []
        for section_name in self.list_sections():
            sections.append(self.generate_section(section_name))
        return "\n\n---\n\n".join(sections)

    def get_fact_count(self, section_name):
        """Retourne le nombre de faits pour une section donnée.

        Args:
            section_name: nom de la section.

        Returns:
            Le nombre de faits (int).

        Raises:
            ValueError: si la section n'existe pas.
        """
        if section_name not in self.data:
            raise ValueError(
                f"Section '{section_name}' introuvable. "
                f"Sections disponibles: {', '.join(self.list_sections())}"
            )
        return len(self.data[section_name]["facts"])