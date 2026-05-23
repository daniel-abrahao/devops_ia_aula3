# DevOps + IA - Aula 3

## Objetivo do projeto
Estudo de pipeline e agentes de IA para aula de pos-graduacao, com exemplos de observabilidade, quality gate e geracao automatizada de documentacao.

## Descricao dos pipelines
- [Analise de logs](.github/workflows/analise_logs.yml): usa IA para inspecionar [logs/app.log](logs/app.log); cria issue e falha o workflow quando encontra erro critico.
- [Analise de traces](.github/workflows/trace-analysis.yml): analisa [traces/payment-trace.txt](traces/payment-trace.txt) com IA para identificar gargalos; cria issue se houver indicios de timeout/gargalo.
- [Analise de metricas - aprovado](.github/workflows/analisar-metricas.yml): avalia [metrics/system-aprovado.json](metrics/system-aprovado.json) via IA e bloqueia quando a resposta indicar REPROVADO.
- [Analise de metricas - reprovado](.github/workflows/analisar-metricas-reprovado.yml): avalia [metrics/system-reprovado.json](metrics/system-reprovado.json) via IA e abre issue quando reprovado.
- [Cobertura alta](.github/workflows/cobertura_alta.yml): executa testes em [tests_alta/](tests_alta/) e aplica quality gate >= 80% de cobertura em [src_alta/](src_alta/).
- [Cobertura baixa](.github/workflows/cobertura_baixa.yml): executa testes em [tests_baixa/](tests_baixa/) e aplica quality gate >= 80% de cobertura em [src_baixa/](src_baixa/).
- [Quality Gate com IA (OpenAI)](.github/workflows/quality_gate_com%20IA.yml): calcula cobertura e consulta IA para aprovar ou bloquear o deploy.
- [Quality Gate com IA (GroqCloud) - bloqueado](.github/workflows/quality_gate_com_IA%20-%20groq%20-%20baixa.yml): calcula cobertura e consulta IA (Groq); bloqueia se a IA responder BLOQUEADO.
- [Quality Gate com IA (GroqCloud) - autorizado](.github/workflows/quality_gate_com_IA%20-%20groq.yaml): calcula cobertura e consulta IA (Groq) com cenario favoravel.
- [Geracao de documentacao](.github/workflows/doc-generator.yml): usa IA para gerar documentacao e abrir PR automaticamente.

## Exemplos de execucao
### Local (pytest)
```bash
pip install pytest pytest-cov
pytest tests_alta --cov=src_alta --cov-report=term --cov-report=json
pytest tests_baixa --cov=src_baixa --cov-report=term --cov-report=json
```

### GitHub Actions (via gh)
```bash
# Exemplo: rodar analise de logs
gh workflow run .github/workflows/analise_logs.yml

# Exemplo: rodar quality gate com IA (GroqCloud)
gh workflow run .github/workflows/quality_gate_com_IA\ -\ groq\ -\ baixa.yml
```

### Segredos esperados
- `GROQ_API_KEY` (workflows que usam GroqCloud)
- `OPEN_AI_KEY` (workflow de Quality Gate com OpenAI)
- `GITHUB_TOKEN` (ja fornecido pelo GitHub Actions)

## Tecnologias utilizadas
- GitHub Actions e GitHub CLI (`gh`)
- Python 3.11
- Pytest e pytest-cov
- GroqCloud (modelo `llama-3.1-8b-instant`)
- OpenAI (modelo `gpt-4o-mini`)
- curl, jq, bc

## Prints das execucoes

### Pipeline de analise de logs
<img width="500" alt="image" src="https://github.com/user-attachments/assets/68faf806-f15d-4f87-ab8e-1a8dfe5cf5cb" />

### Pipeline de analise de traces
<img width="500" alt="image" src="https://github.com/user-attachments/assets/7306763a-4df8-4d88-878f-802ab332ce9f" />

### Pipeline de análise de métricas
<table>
  <tr>
    <td>
      <img height="300" alt="image" src="https://github.com/user-attachments/assets/21f648a6-941a-424d-87b6-62e0c9989c14" /><br>
      <em>IA analisando métricas - reprovado pela IA</em>
    </td>
    <td>
      <img height="300" alt="image" src="https://github.com/user-attachments/assets/ebd8a82b-7ba2-4b9f-83b4-fa4bc959e695" /><br>
      <em>IA analisando métricas - aprovado pela IA</em>
    </td>
  </tr>
</table>

- [ ] Pipeline de cobertura (alta/baixa)
- [ ] Quality Gate com IA (OpenAI e GroqCloud)

### Pipeline geradora de documentação
<table>
  <tr>
    <td>
      <img height="300" alt="Captura de tela de 2026-05-23 13-05-54" src="https://github.com/user-attachments/assets/9ce0f5f9-d2c7-46ea-aef7-aacb63ee1987" /><br>
      <em>Geracao de documentacao via IA</em>
    </td>
    <td>
      <img height="300" alt="image" src="https://github.com/user-attachments/assets/ece90c62-a020-4b72-b9d2-cd60f8762bc5" /><br>
      <em>PR gerado pela IA</em>
    </td>
  </tr>
</table>
