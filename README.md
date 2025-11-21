# 📘 Gerador de Sumários Executivos

Este repositório contém um robô capaz de produzir **sumários executivos automatizados** a partir de dados fornecidos pelo usuário.  
O sistema gera **PDFs padronizados**, com a **primeira página fixa** (baseada no modelo institucional) e as páginas seguintes estruturadas por dimensão no formato:

> **Dados → Análise → Recomendações**

O objetivo é tornar mais ágil, consistente e inteligente a produção de relatórios institucionais.

---

## 🚀 Funcionalidades

- 🧩 **Geração automática de sumários executivos**
- 📄 **Template PDF fixo para a primeira página**, seguindo o layout institucional
- 🧠 **Análises textuais produzidas com IA**
- 🔍 Estrutura padronizada para cada dimensão:
  - **Dados**
  - **Análise**
  - **Recomendações**
- 📊 Possibilidade de integrar dados de diferentes fontes (ex: SARA, SAEGO, Metabase, etc.)
- 🛠️ Produção de relatórios profissionais e consistentes

---

## 📂 Estrutura do Relatório

O relatório segue a lógica apresentada no arquivo de referência:

**Primeira página (fixa):**
- Identidade visual
- Objetivo do relatório  
- Explicação das dimensões  
- Contexto geral  
- Modelo de Mapa Estratégico  

**Páginas seguintes (dinâmicas):**  
Para cada dimensão avaliada:
- **Dados:** indicadores numéricos ou qualitativos
- **Análise:** interpretação automática baseada em evidências
- **Recomendações:** sugestões práticas e estratégicas

Exemplo de referência utilizada:  
`[Matemática] Sumário executivo.pdf`

---

## 🧱 Arquitetura do Projeto

- **Python** para processamento de dados e geração do PDF  
- **Template de PDF** com primeira página fixa  
- **Modelo de IA** para texto interpretativo e recomendações  
- **Scripts** de conversão, formatação e validação  

Fluxo do sistema:
1. Recebe dados do usuário (CSV, JSON ou API)
2. Gera interpretações com IA
3. Preenche o modelo fixo da primeira página
4. Monta cada dimensão no formato padronizado
5. Exporta o relatório final em PDF

---

## 🔧 Como Usar

Em desenvolvimento — exemplo de uso esperado:

```bash
python gerar_relatorio.py dados.json --output sumario.pdf
