# Documentação do Sistema
====================================

## Arquitetura do Sistema
-------------------------

O sistema atual é composto por vários componentes, incluindo:

*   `src_alta` e `src_baixa`: são as pastas principais do código do sistema, contendo as implementações das funções `somar` e `dividir`.
*   `tests_alta` e `tests_baixa`: são as pastas que contêm os testes unitários para as funções implementadas em `src_alta` e `src_baixa`, respectivamente.
*   `metrics`: é a pasta que contém os arquivos JSON que armazenam as métricas do sistema.
*   `traces`: é a pasta que contém os arquivos de logs do sistema.
*   `.github/workflows`: é a pasta que contém os arquivos de configuração do GitHub Actions, incluindo os workflows para análise de métricas, gerar documentação e criar PRs.

## Componentes Principais
------------------------

Os componentes principais do sistema são as funções `somar` e `dividir`, implementadas em `src_alta` e `src_baixa`. Essas funções são responsáveis por realizar as operações básicas de cálculo e verificar se o argumento `b` é zero. Além disso, há a função `verificar_numero` em `src_baixa`, que verifica se um número é positivo, negativo ou zero, e a função `eh_par` em `src_baixa`, que verifica se um número é par.

## Fluxos de Dados
-----------------

Os fluxos de dados principais do sistema são:

*   A coleta de métricas do sistema, armazenadas em `metrics/system-aprovado.json` e `metrics/system-reprovado.json`.
*   A geração de documentação do sistema via GitHub Actions, utilizando o workflow `doc-generator.yml`.
*   A criação de PRs com documentação atualizada, utilizando o workflow `doc-generator.yml`.

## Fluxos de Execução
------------------

Os fluxos de execução principais do sistema são:

*   O fluxo de execução do GitHub Actions, que roda os workflows `analisar-metricas-reprovado`, `analisar-metricas`, `analise_logs`, `cobertura_alta`, `cobertura_baixa`, `doc-generator`, `quality_gate_com_IA`, `quality_gate_com_IA - groq - baixa`, `quality_gate_com_IA - groq`, `trace-analysis`.
*   O fluxo de execução dos testes unitários, utilizados para verificar a implementação das funções `somar` e `dividir`.

## Glossário de Termos
----------------------

*   **métricas**: são dados coletados para monitorar o desempenho do sistema.
*   **documentação**: é a descrição escrita dos componentes do sistema, incluindo o código, fluxos de dados e fluxos de execução.
*   **GitHub Actions**: é o serviço de automação de tarefas do GitHub, que permite criar fluxos de execução para realizar tarefas como analisar métricas, gerar documentação e criar PRs.
*   **workflow**: é o script de configuração do GitHub Actions, que define o fluxo de execução para realizar uma tarefa específica.

## Referências
--------------

*   [GitHub Actions](https://github.com/features/actions)
*   [GitHub](https://github.com)
*   [Python](https://www.python.org)

## Alterações Futuras
---------------------

*   Implementar a integração com outros bancos de dados para coletar métricas de desempenho.
*   Implementar a geração de relatórios de desempenho para os administradores do sistema.
*   Implementar a criação de PRs com documentação atualizada para os colaboradores do projeto.

# README.md em Markdown
====================================

```markdown
# Documentação do Sistema
====================================

## Arquitetura do Sistema
-------------------------

O sistema atual é composto por vários componentes, incluindo:

*   `src_alta` e `src_baixa`: são as pastas principais do código do sistema, contendo as implementações das funções `somar` e `dividir`.
*   `tests_alta` e `tests_baixa`: são as pastas que contêm os testes unitários para as funções implementadas em `src_alta` e `src_baixa`, respectivamente.
*   `metrics`: é a pasta que contém os arquivos JSON que armazenam as métricas do sistema.
*   `traces`: é a pasta que contém os arquivos de logs do sistema.
*   `.github/workflows`: é a pasta que contém os arquivos de configuração do GitHub Actions, incluindo os workflows para análise de métricas, gerar documentação e criar PRs.

## Componentes Principais
------------------------

Os componentes principais do sistema são as funções `somar` e `dividir`, implementadas em `src_alta` e `src_baixa`. Essas funções são responsáveis por realizar as operações básicas de cálculo e verificar se o argumento `b` é zero. Além disso, há a função `verificar_numero` em `src_baixa`, que verifica se um número é positivo, negativo ou zero, e a função `eh_par` em `src_baixa`, que verifica se um número é par.

## Fluxos de Dados
-----------------

Os fluxos de dados principais do sistema são:

*   A coleta de métricas do sistema, armazenadas em `metrics/system-aprovado.json` e `metrics/system-reprovado.json`.
*   A geração de documentação do sistema via GitHub Actions, utilizando o workflow `doc-generator.yml`.
*   A criação de PRs com documentação atualizada, utilizando o workflow `doc-generator.yml`.

## Fluxos de Execução
------------------

Os fluxos de execução principais do sistema são:

*   O fluxo de execução do GitHub Actions, que roda os workflows `analisar-metricas-reprovado`, `analisar-metricas`, `analise_logs`, `cobertura_alta`, `cobertura_baixa`, `doc-generator`, `quality_gate_com_IA`, `quality_gate_com_IA - groq - baixa`, `quality_gate_com_IA - groq`, `trace-analysis`.
*   O fluxo de execução dos testes unitários, utilizados para verificar a implementação das funções `somar` e `dividir`.

## Glossário de Termos
----------------------

*   **métricas**: são dados coletados para monitorar o desempenho do sistema.
*   **documentação**: é a descrição escrita dos componentes do sistema, incluindo o código, fluxos de dados e fluxos de execução.
*   **GitHub Actions**: é o serviço de automação de tarefas do GitHub, que permite criar fluxos de execução para realizar tarefas como analisar métricas, gerar documentação e criar PRs.
*   **workflow**: é o script de configuração do GitHub Actions, que define o fluxo de execução para realizar uma tarefa específica.

## Referências
--------------

*   [GitHub Actions](https://github.com/features/actions)
*   [GitHub](https://github.com)
*   [Python](https://www.python.org)

## Alterações Futuras
---------------------

*   Implementar a integração com outros bancos de dados para coletar métricas de desempenho.
*   Implementar a geração de relatórios de desempenho para os administradores do sistema.
*   Implementar a criação de PRs com documentação atualizada para os colaboradores do projeto.
```
