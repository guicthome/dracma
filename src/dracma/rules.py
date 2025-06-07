"""Business rules extracted from dracma.txt."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .spreadsheet import SheetData


@dataclass
class BlockResult:
    title: str
    details: List[str]


def _find_column_index(headers: List[str], name: str) -> int:
    for idx, header in enumerate(headers):
        if header and header.strip().lower() == name.strip().lower():
            return idx
    raise ValueError(f"Header '{name}' not found")


def analyze_bloco01(sheet: SheetData, competence: str) -> BlockResult:
    previsto_idx = _find_column_index(sheet.headers, "PREVISTO")
    executado_idx = _find_column_index(sheet.headers, competence)

    details: List[str] = []
    for row in sheet.rows[:-1]:  # ignore last row (total)
        nome = row.get(sheet.headers[1], "")
        previsto = row.get(sheet.headers[previsto_idx], 0) or 0
        executado = row.get(sheet.headers[executado_idx], 0) or 0
        if executado == 0:
            details.append(f"{nome}: valor executado zerado")
        if previsto and executado >= 2 * previsto:
            details.append(f"{nome}: possível retroativo (executado {executado})")
    return BlockResult(title="Bloco 01 – Governança", details=details)


def analyze_bloco02(sheet: SheetData, competence: str) -> BlockResult:
    previsto_idx = _find_column_index(sheet.headers, "PREVISTO")
    previsto_metas_idx = _find_column_index(sheet.headers, "PREVISTO METAS")
    executado_idx = _find_column_index(sheet.headers, competence)

    details: List[str] = []
    for row in sheet.rows[:-1]:
        nome = row.get(sheet.headers[1], "")
        previsto = (row.get(sheet.headers[previsto_idx], 0) or 0) + (
            row.get(sheet.headers[previsto_metas_idx], 0) or 0
        )
        executado = row.get(sheet.headers[executado_idx], 0) or 0
        if executado == 0:
            details.append(f"{nome}: valor executado zerado")
    return BlockResult(title="Bloco 02 – Salário Fixo", details=details)


def analyze_bloco03(sheet: SheetData, competence: str) -> BlockResult:
    previsto_idx = _find_column_index(sheet.headers, "PREVISTO SOMA")
    executado_idx = _find_column_index(sheet.headers, competence)

    details: List[str] = []
    for row in sheet.rows[:-1]:
        tipo = row.get(sheet.headers[1], "")
        previsto = row.get(sheet.headers[previsto_idx], 0) or 0
        executado = row.get(sheet.headers[executado_idx], 0) or 0
        if previsto:
            diff = abs(executado - previsto) / previsto
            if diff > 0.05:
                details.append(f"{tipo}: variação {diff:.2%}")
    return BlockResult(title="Bloco 03 – Plantões", details=details)


def analyze_bloco04(sheet: SheetData, competence: str) -> BlockResult:
    previsto_idx = _find_column_index(sheet.headers, "PREVISTO")
    executado_idx = _find_column_index(sheet.headers, competence)

    details: List[str] = []
    for row in sheet.rows[:-1]:
        item = row.get(sheet.headers[0], "")
        previsto = row.get(sheet.headers[previsto_idx], 0) or 0
        executado = row.get(sheet.headers[executado_idx], 0) or 0
        if previsto:
            diff = abs(executado - previsto) / previsto
            if diff > 0.05:
                details.append(f"{item}: variação {diff:.2%}")
    return BlockResult(title="Bloco 04 – Variável", details=details)
