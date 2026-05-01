# Trabalho de Extensão - Atividade Acadêmica EAD Eng. Software Estácio
APLICAÇÃO DE BUSINESS INTELLIGENCE NA ANÁLISE DE PERDAS E RISCOS NO VAREJO UTILIZANDO POWER BI

<div align="center">

# 📊 Dashboard de Prevenção de Perdas VR 2026

[![Status](https://img.shields.io/badge/Conclu%C3%ADdo-100%25-brightgreen)](https://github.com/danieldslima/trabalho-de-extensao-EAD-Eng.-Software-Estacio)
[![Estácio](https://img.shields.io/badge/Est%C3%A1cio%20de%20S%C3%A1-2026.1%20EAD-blue)](https://estacio.br)
[![Tech](https://img.shields.io/badge/Tech-Power%20BI%20%7C%20Python%20%7C%20SQL-orange)](#)
[![PlantUML](https://img.shields.io/badge/Modelagem-PlantUML-blue)](https://plantuml.com)

**Trabalho de Extensão Universitária: Implementação de Business Intelligence e automação de ETL para análise de riscos operacionais no varejo de Volta Redonda, RJ.**

**Daniel da Silva Lima | Matrícula: 202401159018 | Engenharia de Software**

</div>

## 📋 Sobre o Projeto

Este projeto consiste no desenvolvimento de uma solução de **Business Intelligence** para otimizar a análise de perdas em uma unidade varejista (**CNPJ: 15.347.973/0001-79**). A solução substitui processos manuais de limpeza de dados por um pipeline automatizado em Python, alimentando dashboards interativos.

**Impacto real:**
- **Automação de ETL:** Substituição da limpeza manual do arquivo `App Analise de Perdas.xlsx`.
- **Padronização:** Filtragem de colunas irrelevantes (ID) e foco em KPIs estratégicos: Loja, Ano, Mês e Perdas(Brt).
- **Eficiência:** Redução no tempo de resposta e identificação imediata de unidades críticas.

**Case prático:** Aplicação de Engenharia de Software para transformar dados brutos de planilhas em indicadores de performance (Excelente/Estável).

## ✨ Funcionalidades Técnicas

- **Limpeza Automatizada:** Script Python (Pandas) para higienização seletiva de dados.
- **Modelagem Star Schema:** Estruturação de dados para alta performance no Power BI.
- **Dashboards Interativos:** Visualização temporal (2024-2026) e comparação regional.
- **Auditoria SQL:** Consultas para identificação de outliers e validação de riscos.

## 📚 Conteúdo do Repositório

| Componente | Arquivo | Finalidade |
| :--- | :--- | :--- |
| **Automação** | `scripts/automacao_perdas.py` | Script Python para limpeza do arquivo XLSX. |
| **Banco de Dados** | `sql/consulta_perdas.sql` | Estrutura de tabelas e auditoria de riscos. |
| **Data** | `data/App Analise de Perdas.xlsx` | Base de dados bruta recebida para análise. |
| **Relatório** | `docs/Trabalho.pdf` | Documentação completa do projeto de extensão. |

## 🚀 Como Usar

**Clone:**
```bash
git clone [https://github.com/danieldslima/trabalho-de-extensao-EAD-Eng.-Software-Estacio.git](https://github.com/danieldslima/trabalho-de-extensao-EAD-Eng.-Software-Estacio.git)
