"""Command-line interface for generating Dracma reports."""
from __future__ import annotations

import argparse

from .report import ReportGenerator


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Dracma medical reports")
    parser.add_argument("competence", help="Competence in Mes/Ano format, e.g. Março/2025")
    parser.add_argument("--instructions", nargs="*", default=[], help="Additional instructions")
    parser.add_argument("--excel", default="conferencia.xlsx", help="Path to the spreadsheet")
    parser.add_argument("--output", default="relatorio.txt", help="Output TXT file")

    args = parser.parse_args()

    generator = ReportGenerator(args.excel, args.competence, args.instructions)
    generator.export_txt(args.output)
    print(f"Relatório salvo em {args.output}")


if __name__ == "__main__":
    main()
