"""Generation of text reports for medical financial auditing."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List

from .spreadsheet import load_sheet
from .rules import (
    analyze_bloco01,
    analyze_bloco02,
    analyze_bloco03,
    analyze_bloco04,
)


@dataclass
class Report:
    competence: str
    generated_at: datetime
    instructions: List[str]
    blocks: List[str]


class ReportGenerator:
    def __init__(self, workbook_path: str, competence: str, instructions: List[str] | None = None):
        self.workbook_path = workbook_path
        self.competence = competence
        self.instructions = instructions or []
        self.generated_at = datetime.now()

    def _analyze(self) -> List[str]:
        blocks: List[str] = []
        bloco01 = analyze_bloco01(load_sheet(self.workbook_path, "Bloco01"), self.competence)
        bloco02 = analyze_bloco02(load_sheet(self.workbook_path, "Bloco02"), self.competence)
        bloco03 = analyze_bloco03(load_sheet(self.workbook_path, "Bloco03"), self.competence)
        bloco04 = analyze_bloco04(load_sheet(self.workbook_path, "Bloco04"), self.competence)

        blocks.append("01. Sumário Executivo\n" + "\n".join(self.instructions))
        blocks.append("02. Metodologia\nAplicadas regras do dracma.txt")
        blocks.append("03. " + bloco01.title + "\n" + "\n".join(bloco01.details))
        blocks.append("04. " + bloco02.title + "\n" + "\n".join(bloco02.details))
        blocks.append("05. " + bloco03.title + "\n" + "\n".join(bloco03.details))
        blocks.append("06. " + bloco04.title + "\n" + "\n".join(bloco04.details))
        blocks.append("07. Inconsistências e Tendências")
        blocks.append("08. Comparativo com Mês Anterior")
        blocks.append("09. Considerações Finais")
        blocks.append("10. Observações Complementares")
        return blocks

    def generate_report(self) -> Report:
        blocks = self._analyze()
        return Report(
            competence=self.competence,
            generated_at=self.generated_at,
            instructions=self.instructions,
            blocks=blocks,
        )

    def export_txt(self, path: str) -> None:
        report = self.generate_report()
        lines = [
            "RELATÓRIO DE CONFERÊNCIA MENSAL – REPASSE MÉDICO",
            f"Competência: {report.competence}",
            f"Data/Hora da Geração: {report.generated_at:%d/%m/%Y %H:%M}",
            "Solicitante: Dr. Guilherme Camargo Thomé",
            "Agente: Dracma – GPT Especializado em Controle de Repasse Médico",
            "",
        ]
        lines.extend(report.blocks)
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(lines))
