## Documentação do Sistema

### Arquitetura

O sistema é composto por cinco componentes principais:

1. **GitHub Actions**: Responsável por executar workflows automação de tarefas.
2. **API de Documentação**: Utilizada para gerar documentação do sistema.
3. **Repositorio**: Armazena todos os códigos-fonte e metadados do sistema.
4. **Modelos**: Utilizados para gerar documentação e análise de dados.
5. **Testes**: Executados para garantir a qualidade e funcionamento correto do sistema.

### Componentes Principais

#### .github/workflows/doc-generator.yml

Workflow responsável por gerar documentação do sistema.

* Inclui um job chamado `analisar-traces` que executa uma série de etapas:
 * `uses: actions/checkout@v4`: Faz o checkout do repositório atual.
 * `name: Login GitHub CLI`: Realiza o login no GitHub CLI.
 * `env: GROQCLOUD_API_KEY`: Configura a chave do API da Groq.
 * `run: IA gera documentacao do sistema`: Chama o model de IA para gerar a documentação.
 * `Criar PR com documentacao`: Cria um pull request com a documentação gerada.

#### src_alta/app.py e src_baixa/app.py

Arquivos que contém as funções principais do sistema, incluindo a soma, divisão e outros cálculos.

#### tests_alta/test_app.py e tests_baixa/test_app.py

Arquivos que contém os testes unitários para as funções principais do sistema.

### Fluxos de Dados

O fluxo de dados do sistema é como segue:

1. Ação do usuário: Inicia o workflow de documentação.
2. GitHub Actions: Executa o workflow de documentação.
3. API de Documentação: Utiliza os modelos para gerar a documentação.
4. Documentação Gerada: É salva no repositório e incluída no pull request.

### Arquivos no Repositorio

#### .github/workflows/analisar-metricas-reprovado.yml e .github/workflows/analisar-metricas.yml

Workflows que analisam as métricas do sistema.

#### .github/workflows/cobertura_alta.yml e .github/workflows/cobertura_baixa.yml

Workflows que executam os testes de cobertura do sistema.

#### .github/workflows/traces-payment-trace.txt

Arquivo que armazena o registro de trazas do sistema.

### Conteudo dos Arquivos Principais

#### metrics/system-aprovado.json e metrics/system-reprovado.json

Arquivos que contêm as métricas do sistema aprovado e reprovado.

#### src_alta/app.py e src_baixa/app.py

Arquivos que contêm as funções principais do sistema.

#### tests_alta/test_app.py e tests_baixa/test_app.py

Arquivos que contêm os testes unitários para as funções principais do sistema.

### README.md

Arquivo que armazena a documentação gerada pelo sistema.

Espero que essa documentação tenha sido útil! Se tiver alguma dúvida ou precisar de esclarecimentos, por favor não hesite em perguntar.
