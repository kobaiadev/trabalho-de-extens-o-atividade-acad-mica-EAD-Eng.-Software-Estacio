# Trabalho de Extensão - Atividade Acadêmica EAD Eng.Software de Software Estacio
APLICAÇÃO DE BUSINESS INTELLIGENCE NA ANÁLISE DE PERDAS E RISCOS NO VAREJO UTILIZANDO POWER BI
<div align="center">

# 🛠️ LPS Workshops Volta Redonda 2026

[![Status](https://img.shields.io/badge/Conclu%C3%ADdo-100%25-brightgreen)](https://github.com/danieldslima/lps-extensao-vr-2026)
[![Est%C3%A1cio](https://img.shields.io/badge/Est%C3%A1cio%20de%20S%C3%A1-2026.1%20EAD-blue)](https://estacio.br)
[![Participantes](https://img.shields.io/badge/15%20devs%20capacitados-success)](https://github.com/danieldslima/lps-extensao-vr-2026/issues)
[![PlantUML](https://img.shields.io/badge/Tech-PlantUML%20%7C%20Zoom%20%7C%20GitHub-orange)](https://plantuml.com)

**Trabalho de Extensão Universitária: Capacitação em Linhas de Produtos de Software (LPS) para desenvolvedores locais de Volta Redonda, RJ.**

**Daniel da Silva Lima | Matrícula: 202401159018 | Linhas de Produtos de Software (597)**

</div>

## 📋 Sobre o Projeto

Desenvolvi **3 workshops online** (EAD Estácio de Sá) para **15 profissionais de TI locais**, ensinando **gerenciamento de variabilidade**, **feature models** e **engenharia de domínio/aplicação**. 

**Impacto real:**
- 12/15 certificados (80% aprovação quizzes)
- 3 protótipos feature models criados
- 5 oportunidades LPS identificadas em PMEs (ex.: apps de estoque reutilizáveis)

**Case prático:** Adaptação para lanchonetes locais (controle vendas/estoque com variabilidade por cliente).

## ✨ Funcionalidades Aprendidas

- Modelagem de **feature models** com PlantUML
- Identificação de **domínios comuns** em projetos locais
- Reuso de **famílias de software** (reduz tempo 40%)
- Práticas **ágil para LPS**

## 🖼️ Demo: Feature Model Exemplo (Gestão Estoque)

```plantuml
@startuml feature-model-lanchonete
skinparam monochrome true
title Feature Model: Sistema Gestão Lanchonete

[*] --> LPS_Gestao
LPS_Gestao <|-- Estoque
LPS_Gestao <|-- Vendas
LPS_Gestao <|-- Relatorios

Estoque <|-- ControleManual : obrigatório
Estoque <|-- ControleDigital : opcional
Estoque <|-- AlertasBaixoEstoque : opcional

Vendas <|-- PDV : obrigatório
Vendas <|-- Delivery : opcional

Relatorios <|-- Diario : obrigatório
Relatorios <|-- Mensal : opcional

note right of ControleDigital
  Case: Lanchonete Sabor da Roça
end note
@enduml
```

*(Renderize: [PlantUML Online](http://www.plantuml.com/plantuml/uml/))*

## 📚 Conteúdo dos Workshops

| Workshop | Data | Duração | Material |
|----------|------|---------|----------|
| 1. Intro LPS & Domínio | 08/03 | 2h | [Slides PDF](docs/slides-w1-intro.pdf) |
| 2. Feature Models | 22/03 | 3h | [PlantUML Proto](examples/feature-model.iuml) |
| 3. Eng. Aplicação | 12/04 | 3h | [Vídeo Demo](https://youtube.com/unlisted) |

## 🚀 Como Usar

1. **Clone:**
   ```bash
   git clone https://github.com/danieldslima/lps-extensao-vr-2026.git
   ```

2. **Materiais:** `docs/slides-*.pdf` + `/examples/`

## 📈 Resultados

- **Quizzes:** 85% média
- **NPS:** 8.7/10
- **Relatório:** [PDF Completo](docs/Trabalho.pdf)

## 🤝 Contribua

Fork → Issue → PR para `develop`.

## 📄 Licença
[MIT](LICENSE)

**Daniel da Silva Lima** | [LinkedIn](https://linkedin.com/in/danieldslima) | Volta Redonda, RJ
