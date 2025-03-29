# 🩺 Dracma – Agente GPT para Conferência de Repasse Médico

Este repositório contém o script oficial (`dracma.txt`) e os arquivos complementares do agente GPT **Dracma**, utilizado para realizar conferências mensais dos repasses médicos no Hospital **ICDS Unihealth – Governador Valadares**.

---

## 📌 Objetivo

Automatizar a validação técnica e narrativa dos repasses médicos, com geração de relatórios padronizados por competência. O agente Dracma atua em conformidade com regras institucionais e estrutura por blocos de validação.

---

## 🧠 Como Funciona o Agente Dracma (via ChatGPT Pro)

O agente Dracma é executado dentro do **Custom GPT** do ChatGPT Plus, com comportamento especializado configurado previamente. Ele:

1. Solicita os arquivos de planilhas (.xlsx)
2. Identifica a competência e o ciclo selecionado
3. Executa a conferência automática
4. Gera relatórios em `.TXT`, `.PDF` e versão Gmail

> ⚠️ **Os arquivos `.xlsx` devem ser enviados manualmente a cada execução no GPT.**

---

## 📂 Estrutura dos Arquivos no Repositório

| Arquivo                      | Descrição                                                                 |
|-----------------------------|---------------------------------------------------------------------------|
| `dracma.txt`                | Script unificado com regras de conferência, blocos, validações e narrativa |
| `exemplo_fevereiro.txt`     | Modelo oficial de relatório estruturado usado como base                   |
| `botao_gmail.html`          | Botão automático de envio do relatório via Gmail                          |
| `relatorio_fevereiro2025.txt` | Exemplo real de relatório gerado (colável no sistema)                      |
| `relatorio_fevereiro2025.pdf` | Versão final em PDF com gráfico embutido                                 |
| `grafico_blocos_plantao_fev2025.png` | Gráfico gerado automaticamente pelo agente (Bloco 03)                 |

---

## 📊 Blocos de Validação

O relatório é dividido em 10 blocos obrigatórios:

1. Sumário Executivo  
2. Metodologia  
3. Governança  
4. Salário Fixo  
5. Plantões  
6. Produção  
7. Inconsistências e Tendências  
8. Comparativo com Mês Anterior  
9. Considerações Finais  
10. Observações Complementares

---

## ✅ Versão Atual

- `v2.4.1 – Março/2025`  
- Compatível com Competências a partir de Janeiro/2025  
- Validações ajustadas para margens relativas, agrupamentos por especialidade e retroativos

---

## 📦 Uso Interno

Este repositório é utilizado como fonte oficial pelo agente Dracma, e deve ser atualizado sempre que houver mudanças em:

- Lógica de conferência
- Estrutura de rubrica
- Blocos narrativos
- Exportações e formatos

---

## 🔐 Licença

Uso exclusivo interno do ICDS Unihealth – Governador Valadares.  
Proibida a reprodução ou distribuição externa sem autorização.
