# Análise de Dados: Doença Cardíaca


## Visão geral

Este repositório contém uma análise exploratória e experimentos de modelagem sobre um conjunto de dados relacionado a doenças cardíacas. O objetivo é investigar fatores associados ao diagnóstico e construir modelos preditivos simples, com documentação clara das etapas e resultados.

Sumário
- [Objetivo](#objetivo)
- [Resumo dos dados](#resumo-dos-dados)
- [Metodologia](#metodologia)
- [Como executar](#como-executar)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Resultados e observações](#resultados-e-observações)
- [Dependências](#dependências)

--------------------------------------------------
Objetivo
--------------------------------------------------
- Explorar e entender a estrutura do conjunto de dados.
- Realizar limpeza e pré-processamento básicos.
- Investigar relações entre variáveis clínicas e a presença de doença cardíaca.
- Treinar e comparar modelos de classificação simples (ex.: regressão logística, árvore de decisão) e discutir limitações.

--------------------------------------------------
Resumo dos dados
--------------------------------------------------
O dataset inclui variáveis demográficas e clínicos-exames relacionados ao diagnóstico de doença cardíaca (por exemplo: idade, sexo, pressão arterial, colesterol, resultados de teste de esforço). A descrição detalhada de cada coluna está disponível no notebook principal.

--------------------------------------------------
Metodologia
--------------------------------------------------
1. Inspeção inicial e limpeza (tratamento de valores faltantes, tipos de variáveis).
2. Análise exploratória: estatísticas descritivas e visualizações para entender distribuições e correlações.
3. Engenharia de features e codificação de categóricas.
4. Treinamento e validação de modelos de classificação com avaliação por métricas (acurácia, precisão, recall, AUC).
5. Interpretação dos resultados e recomendações para trabalhos futuros.

--------------------------------------------------
Como executar
--------------------------------------------------
1. Criar um ambiente (virtualenv/conda) e instalar dependências:
```bash
# Exemplo com pip
pip install -r requirements.txt
```
2. Colocar os dados em data/ (ou ajustar caminhos no notebook).
3. Abrir e executar o notebook principal em notebooks/ na ordem das células.
4. Consultar a seção "Resultados" no notebook para interpretações e gráficos.

--------------------------------------------------
Estrutura do repositório
--------------------------------------------------
- notebooks/        -> notebooks com análise, visualizações e modelagem  
- data/             -> dados brutos e processados (não versionar dados sensíveis)  
- scripts/          -> scripts auxiliares para pré-processamento  
- README.md         -> este arquivo

--------------------------------------------------
Resultados e observações
--------------------------------------------------
- Os notebooks trazem experimentos iniciais e comparações entre modelos.  
- As conclusões são condicionais à qualidade e representatividade dos dados; sugerem-se mais testes e validação externa antes de uso em produção.

--------------------------------------------------
Dependências
--------------------------------------------------
Principais pacotes esperados:
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
Versões específicas podem ser indicadas em requirements.txt.

--------------------------------------------------
Notas finais
--------------------------------------------------
O trabalho é uma prática de análise de dados e aprendizado de máquina aplicada ao dataset disponível. Há espaço para aprimoramentos em pré-processamento, seleção de features e experimentos de modelagem.
