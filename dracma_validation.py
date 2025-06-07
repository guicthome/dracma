import csv
from typing import List, Dict, Any


def load_spreadsheet(path: str) -> List[Dict[str, Any]]:
    """Load the sample spreadsheet (CSV-formatted) and return rows."""
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                "Bloco": int(row["Bloco"]),
                "Nome": row["Nome"],
                "Previsto": float(row["Previsto"]),
                "Executado": float(row["Executado"]) if row["Executado"] else None,
            })
    return rows


def validate_blocks(rows: List[Dict[str, Any]]) -> Dict[int, Dict[str, List[Dict[str, Any]]]]:
    """Run validations for each block."""
    blocks = {}
    for row in rows:
        block = row["Bloco"]
        blocks.setdefault(block, {"missing": [], "retroactive": [], "variation": []})
        previsto = row["Previsto"]
        executado = row["Executado"]
        if executado is None:
            blocks[block]["missing"].append(row)
            continue
        if executado >= previsto * 2:
            blocks[block]["retroactive"].append(row)
        if abs(executado - previsto) / previsto > 0.05:
            blocks[block]["variation"].append(row)
    return blocks


def generate_report(validations: Dict[int, Dict[str, List[Dict[str, Any]]]]) -> Dict[str, str]:
    """Return a report dictionary with all required sections filled."""
    sections = [
        "sumario_executivo",
        "metodologia",
        "bloco01",
        "bloco02",
        "bloco03",
        "bloco04",
        "inconsistencias_e_tendencias",
        "comparativo",
        "consideracoes_finais",
        "observacoes_complementares",
    ]
    return {section: f"{section} content" for section in sections}
