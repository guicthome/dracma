import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dracma_validation import load_spreadsheet, validate_blocks, generate_report
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "sample_conferencia.xlsx")


def test_load_sample_spreadsheet():
    rows = load_spreadsheet(DATA_PATH)
    assert len(rows) == 7


def test_validation_blocks():
    rows = load_spreadsheet(DATA_PATH)
    result = validate_blocks(rows)
    # Block 1 checks
    assert len(result[1]["missing"]) == 1
    assert len(result[1]["retroactive"]) == 1
    assert len(result[1]["variation"]) == 1
    # Block 2
    assert not result[2]["missing"]
    assert not result[2]["retroactive"]
    assert len(result[2]["variation"]) == 1
    # Block 3
    assert len(result[3]["variation"]) == 1
    # Block 4
    assert len(result[4]["variation"]) == 1


def test_report_generator():
    rows = load_spreadsheet(DATA_PATH)
    validations = validate_blocks(rows)
    report = generate_report(validations)
    expected_sections = [
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
    for section in expected_sections:
        assert section in report and report[section]
    assert len(report) == 10
