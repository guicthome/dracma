# 🩺 Dracma – Agente GPT para Conferência de Repasse Médico

Este repositório contém os arquivos oficiais do agente **Dracma**, utilizado para realizar a conferência mensal dos repasses médicos do Hospital **ICDS Unihealth – Governador Valadares**.

---

## 📌 Objetivo

Automatizar a validação técnica e narrativa dos repasses médicos mensais, com geração de relatórios institucionais por competência. O agente segue uma estrutura padronizada de análise baseada em regras, blocos e validações.

---

## 🧠 Como Funciona

O Dracma é um agente **Custom GPT** executado no ambiente **ChatGPT Plus**, com comportamento especializado.

### 🔄 Fluxo de execução:

1. O usuário informa a competência (ex: Março/2025)
2. O GPT acessa a planilha oficial `conferencia.xlsx`, hospedada neste repositório
3. Caso existam instruções específicas da competência (ex: trechos de e-mail), o usuário pode **colar diretamente no GPT** antes da análise
4. O Dracma executa a validação técnica com base no script `dracma.txt` e nas instruções coladas
5. O relatório é gerado em três formatos: `.txt`, `.pdf` (com gráficos), e `.html` institucional

---

## 📂 Estrutura dos Arquivos

| Arquivo                  | Descrição                                                                  |
|--------------------------|---------------------------------------------------------------------------|
| `dracma.txt`             | Script com todas as regras de validação e lógica narrativa                |
| `conferencia.xlsx`       | Planilha oficial com dados financeiros por competência                    |
| `modelo_email_web.html`  | Modelo institucional em HTML para envio do relatório final por e-mail     |
| `relatorios/`            | (Opcional) Diretório para armazenar exemplos de relatórios já gerados     |

---

## 📋 Instruções Complementares (Novo)

A partir da versão **v3.0**, o agente Dracma permite o uso de **instruções adicionais coladas diretamente no chat** do GPT antes da conferência, tais como:

- "Foi pago um retroativo para o Dr. João"
- "Neste mês, o médico Fulano foi substituído pelo Sicrano"
- "Não considerar o valor X, pois trata-se de glosa do mês anterior"

Essas instruções são tratadas como **regras adicionais vinculadas à competência atual**, e influenciam diretamente a análise e o relatório gerado.

---

## 🧾 Estrutura do Relatório

O relatório institucional é composto por 10 blocos fixos:

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
- Integração com instruções manuais coladas no GPT  
- Planilha hospedada no GitHub  
- Exportações automáticas `.TXT`, `.PDF`, `.HTML`  
- Modelo de e-mail institucional atualizado

---

## 🔐 Licença

Uso exclusivo do Hospital **ICDS Unihealth – Governador Valadares**.  
É proibida a redistribuição externa sem autorização formal.
