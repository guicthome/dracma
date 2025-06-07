import argparse
from datetime import datetime
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from jinja2 import Template
import textwrap

RULE_FILE = 'dracma.txt'
HTML_TEMPLATE = 'modelo_email_web.html'

# Basic mapping of sheets and columns based on dracma.txt
BLOCK_CONFIG = {
    'Bloco01': {
        'previsto_cols': ['PREVISTO'],
    },
    'Bloco02': {
        'previsto_cols': ['PREVISTO', 'PREVISTO METAS'],
    },
    'Bloco03': {
        'previsto_cols': ['PREVISTO SOMA'],
    },
    'Bloco04': {
        'previsto_cols': ['PREVISTO'],
    },
}

def read_rules(path: str) -> dict:
    """Extract thresholds from dracma.txt"""
    rules = {}
    block = None
    with open(path, 'r', encoding='utf-8') as fh:
        for line in fh:
            if line.startswith('### BLOCO'):
                block = line.strip().split('–')[0].split()[-1]
            if '5%' in line and block:
                rules[block] = 5
    return rules

def load_data(xls: str, competencia: str) -> dict:
    xls_file = pd.ExcelFile(xls)
    data = {}
    for sheet in BLOCK_CONFIG:
        if sheet not in xls_file.sheet_names:
            continue
        df = pd.read_excel(xls_file, sheet_name=sheet)
        previsto = df[BLOCK_CONFIG[sheet]['previsto_cols']].sum(axis=1)
        if competencia not in df.columns:
            raise ValueError(f'Competência {competencia} não encontrada na aba {sheet}')
        executado = df[competencia]
        total_previsto = previsto.sum()
        total_executado = executado.sum()
        diff = total_executado - total_previsto
        pct = (diff / total_previsto) * 100 if total_previsto else 0
        data[sheet] = {
            'previsto': total_previsto,
            'executado': total_executado,
            'diff': diff,
            'pct': pct,
        }
    return data

def generate_text(data: dict, competencia: str) -> str:
    lines = []
    lines.append(f'RELATÓRIO DE CONFERÊNCIA – {competencia}')
    lines.append('-'*50)
    for block, values in data.items():
        pct = values['pct']
        flag = '⚠️' if abs(pct) > 5 else 'OK'
        lines.append(f'{block}: Previsto R$ {values["previsto"]:.2f} | Executado R$ {values["executado"]:.2f} | Diferença {pct:.2f}% {flag}')
    return '\n'.join(lines)

def generate_pdf(data: dict, competencia: str, output: Path):
    with PdfPages(output) as pdf:
        for block in ['Bloco03', 'Bloco04']:
            if block not in data:
                continue
            values = data[block]
            fig, ax = plt.subplots()
            ax.bar(['Previsto', 'Executado'], [values['previsto'], values['executado']], color=['#004080', '#00a2e8'])
            ax.set_title(f'{block} - {competencia}')
            pdf.savefig(fig)
            plt.close(fig)

def generate_html(data: dict, competencia: str, output: Path):
    with open(HTML_TEMPLATE, 'r', encoding='utf-8') as fh:
        template = Template(fh.read())
    blocks = []
    for name in ['Bloco01', 'Bloco02', 'Bloco03', 'Bloco04']:
        if name not in data:
            continue
        d = data[name]
        pct = d['pct']
        msg = f"Previsto R$ {d['previsto']:.2f}, Executado R$ {d['executado']:.2f} ({pct:.2f}%)"
        blocks.append({'name': name, 'message': msg})
    html = template.render(competencia=competencia, data=datetime.now().strftime('%d/%m/%Y %H:%M'), blocks=blocks)
    output.write_text(html, encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description='Gerar relatórios de conferência médica')
    parser.add_argument('-c', '--competencia', required=True, help='Nome da coluna da competência (ex: Março/2025)')
    parser.add_argument('-e', '--excel', default='conferencia.xlsx', help='Arquivo .xlsx com os dados')
    parser.add_argument('-o', '--output', default='relatorio', help='Prefixo dos arquivos de saída')
    args = parser.parse_args()

    rules = read_rules(RULE_FILE)
    data = load_data(args.excel, args.competencia)

    text_report = generate_text(data, args.competencia)
    Path(f'{args.output}.txt').write_text(text_report, encoding='utf-8')
    generate_pdf(data, args.competencia, Path(f'{args.output}.pdf'))
    generate_html(data, args.competencia, Path(f'{args.output}.html'))
    print('Relatórios gerados com prefixo', args.output)

if __name__ == '__main__':
    main()
