# 🩺 Dracma – Agente GPT para Conferência de Repasse Médico

Este repositório contém os arquivos oficiais do agente **Dracma**, utilizado para realizar a conferência mensal dos repasses médicos do Hospital **ICDS Unihealth – Governador Valadares**.

---

## 📌 Objetivo

Automatizar a validação técnica e narrativa dos repasses médicos mensais, gerando relatórios padronizados por competência, conforme regras institucionais e estrutura fixa de análise.

---

## 🧠 Funcionamento do Agente

O Dracma é um GPT personalizado executado dentro do **ChatGPT Plus (Custom GPT)**, com comportamento ajustado às diretrizes da instituição.

### Fluxo Operacional:

1. O agente acessa a planilha `conferencia.xlsx`, hospedada neste repositório
2. O usuário informa a competência a ser conferida (ex: Março/2025)
3. A conferência é executada automaticamente conforme as regras do `dracma.txt`
4. O agente gera um relatório completo com exportação para os formatos:
   - `.TXT` colável
   - `.PDF` com gráficos
   - `.HTML` (modelo institucional)

---

## 📂 Estrutura dos Arquivos

| Arquivo                  | Descrição                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| `dracma.txt`             | Script com todas as regras de conferência, estrutura dos blocos e narrativa |
| `conferencia.xlsx`       | Planilha oficial com dados financeiros por competência                   |
| `modelo_email_web.html`  | Modelo institucional em HTML para versão final do relatório por e-mail   |

---

## 🧾 Estrutura do Relatório

O relatório é sempre composto pelos seguintes blocos fixos:

1. Sumário Executivo  
2. Metodologia  
3. Bloco 01 – Governança  
4. Bloco 02 – Salário Fixo  
5. Bloco 03 – Plantões  
6. Bloco 04 – Variável  
7. Inconsistências e Tendências  
8. Comparativo com Mês Anterior  
9. Considerações Finais  
10. Observações Complementares

---

## ✅ Versão Atual

- `v3.0 – Junho/2025`  
- Nova estrutura: planilha hospedada no GitHub  
- Modelo HTML institucional com gráficos interativos  
- Exportações automáticas em `.TXT`, `.PDF` e `.HTML`

---

## 🔄 Atualizações Esperadas

Sempre que houver alteração nas regras, rubricas, layout ou narrativas, os seguintes arquivos devem ser atualizados:

- `dracma.txt` (regras e estrutura narrativa)
- `conferencia.xlsx` (dados de competência)
- `modelo_email_web.html` (modelo visual)

---

## 🔐 Licença

Uso exclusivo do Hospital **ICDS Unihealth – Governador Valadares**.  
Proibida a reprodução, redistribuição ou modificação externa sem autorização formal.
