# 🚺 Monitor da Violência Contra a Mulher — Conversor XLS para CSV

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green?style=for-the-badge&logo=pandas)
![CSV](https://img.shields.io/badge/Output-CSV-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-success?style=for-the-badge)

## 📌 Descrição do Projeto

Este repositório contém um script em Python desenvolvido para converter automaticamente arquivos `.xls` disponibilizados pelo **Monitor da Violência Contra a Mulher**, mantido com dados da **SEJUSP-MS** e do **PJMS**, em arquivos `.csv` estruturados, padronizados e compatíveis com ferramentas de análise de dados.

🔗 **Fonte oficial dos dados:**  
https://monitorviolenciacontramulher.sejusp.ms.gov.br/

O objetivo principal do script é facilitar o tratamento inicial dos dados públicos sobre violência contra a mulher no estado de **Mato Grosso do Sul**, permitindo que os arquivos sejam utilizados posteriormente em análises exploratórias, dashboards, estudos estatísticos, mineração de dados e modelos de aprendizado de máquina.

---

## 🎯 Objetivo

O script `xls_to_csv_Monitor_of_Violence_Against_Women.py` tem como finalidade:

- 📥 Ler arquivos `.xls` baixados do portal oficial;
- 🔎 Identificar tabelas HTML embutidas nesses arquivos;
- 🔄 Converter os dados para arquivos `.csv`;
- 🧹 Realizar limpeza inicial de nomes de colunas e valores textuais;
- 🧾 Gerar relatório completo da conversão;
- 📊 Preparar os dados para uso em Python, Excel, Power BI, Tableau, bancos de dados e pipelines de Ciência de Dados.

---

## 🗂️ Contexto dos Dados

O **Monitor da Violência Contra a Mulher** disponibiliza informações relacionadas a diferentes tipos de violência e medidas de proteção no estado de Mato Grosso do Sul.

Entre os arquivos esperados pelo script estão:

| Arquivo de entrada `.xls` | Arquivo de saída `.csv` |
|---|---|
| `ATENDIMENTOS_EMERGENCIA*.xls` | `atendimentos_emergencia.csv` |
| `MEDIDAS_PROTETIVAS_URGENCIA*.xls` | `medidas_protetivas_urgencia.csv` |
| `MPU*.xls` | `medidas_protetivas_urgencia.csv` |
| `MULHERES_VITIMAS_HOMICIDIOS*.xls` | `mulheres_vitimas_homicidios.csv` |
| `VITIMAS_ESTUPRO*.xls` | `vitimas_estupro.csv` |
| `VITIMAS_FEMINICIDIOS*.xls` | `vitimas_feminicidios.csv` |
| `VITIMAS_VIOLENCIA_DOMESTICA*.xls` | `vitimas_violencia_domestica.csv` |

---

## 🔍 Descoberta Técnica Importante

Embora os arquivos sejam disponibilizados com extensão `.xls`, eles **não são planilhas Excel tradicionais**.

Na prática, os arquivos são:

- 📄 tabelas HTML;
- 💾 salvas com extensão `.xls`;
- 🔤 geralmente codificadas em `latin-1`, `cp1252` ou `ISO-8859-1`;
- 📊 compatíveis com leitura via `pandas.read_html()`.

Por isso, o script utiliza uma estratégia robusta de leitura, tentando múltiplos encodings em cascata.

---

## ⚙️ Funcionalidades

O script possui as seguintes funcionalidades:

- ✅ Detecção automática de arquivos `.xls` no diretório;
- ✅ Conversão de tabelas HTML para `DataFrame`;
- ✅ Exportação para `.csv` com separador `;`;
- ✅ Codificação de saída em `utf-8-sig`, compatível com Excel em português;
- ✅ Padronização dos nomes dos arquivos de saída;
- ✅ Limpeza básica dos nomes das colunas;
- ✅ Remoção de espaços extras em valores textuais;
- ✅ Substituição de valores textuais inválidos como `nan`, `None` e `NaN`;
- ✅ Geração de relatório `.txt`;
- ✅ Estatísticas por dataset;
- ✅ Contagem de linhas, colunas e duplicidades;
- ✅ Registro de erros detalhados;
- ✅ Exibição de logs no console.

---

## 🧰 Tecnologias Utilizadas

O projeto utiliza as seguintes bibliotecas e recursos:

| Tecnologia | Finalidade |
|---|---|
| `Python` | Linguagem principal do script |
| `pandas` | Leitura, tratamento e exportação dos dados |
| `texttable` | Geração de tabelas no relatório `.txt` |
| `lxml` | Parser HTML utilizado pelo `pandas.read_html()` |
| `html5lib` | Parser alternativo para HTML |
| `BeautifulSoup` | Fallback opcional para leitura HTML |
| `pathlib` | Manipulação moderna de caminhos |
| `datetime` | Registro de data e hora |
| `platform` | Identificação do sistema operacional |
| `traceback` | Registro detalhado de erros |

---

## 📦 Instalação

### 1. Clone este repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
2. Crie um ambiente virtual
Windows
python -m venv .venv
.venv\Scripts\activate
Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
3. Instale as dependências
pip install pandas texttable lxml html5lib beautifulsoup4
📁 Estrutura Recomendada do Projeto
monitor-violencia-contra-mulher-ms/
│
├── xls_to_csv_Monitor_of_Violence_Against_Women.py
│
├── ATENDIMENTOS_EMERGENCIA_MS_2026-05-18.xls
├── MEDIDAS_PROTETIVAS_URGENCIA_MPU_MS_2026-05-18.xls
├── MULHERES_VITIMAS_HOMICIDIOS_MS_2026-05-18.xls
├── VITIMAS_ESTUPRO_MS_2026-05-18.xls
├── VITIMAS_FEMINICIDIOS_MS_2026-05-18.xls
├── VITIMAS_VIOLENCIA_DOMESTICA_MS_2026-05-18.xls
│
├── atendimentos_emergencia.csv
├── medidas_protetivas_urgencia.csv
├── mulheres_vitimas_homicidios.csv
├── vitimas_estupro.csv
├── vitimas_feminicidios.csv
├── vitimas_violencia_domestica.csv
│
└── relatorio_conversao_xls_csv.txt
▶️ Como Usar

Coloque o script Python na mesma pasta dos arquivos .xls baixados do Monitor da Violência Contra a Mulher.

Depois, execute:

python xls_to_csv_Monitor_of_Violence_Against_Women.py

O script irá:

🔎 localizar todos os arquivos .xls no diretório;
📥 ler as tabelas HTML contidas nos arquivos;
🔄 converter cada tabela para .csv;
🧾 gerar um relatório completo de execução;
📊 apresentar um sumário final no terminal.
📤 Arquivos Gerados

Após a execução, o script gera arquivos .csv padronizados.

Exemplo:

atendimentos_emergencia.csv
medidas_protetivas_urgencia.csv
mulheres_vitimas_homicidios.csv
vitimas_estupro.csv
vitimas_feminicidios.csv
vitimas_violencia_domestica.csv

Também é gerado o relatório:

relatorio_conversao_xls_csv.txt
🧾 Relatório de Conversão

O relatório .txt contém informações como:

📌 nome dos arquivos processados;
✅ quantidade de conversões concluídas;
❌ quantidade de erros;
📊 número de linhas e colunas por dataset;
💾 tamanho dos arquivos de entrada e saída;
🔤 encoding utilizado na leitura;
🧹 estatísticas básicas de qualidade dos dados;
🔁 quantidade de registros duplicados;
📋 lista de colunas encontradas;
⚠️ erros detalhados, caso existam.
📊 Exemplo de Uso dos CSVs no Python

Após a conversão, os arquivos .csv podem ser carregados com pandas:

import pandas as pd

df = pd.read_csv(
    "vitimas_feminicidios.csv",
    sep=";",
    encoding="utf-8-sig"
)

print(df.head())
print(df.info())

Também é possível carregar todos os arquivos .csv automaticamente:

import pandas as pd
import glob
import os

csvs = glob.glob("*.csv")

dfs = {
    os.path.basename(arquivo): pd.read_csv(
        arquivo,
        sep=";",
        encoding="utf-8-sig"
    )
    for arquivo in csvs
}

for nome, df in dfs.items():
    print(f"{nome}: {df.shape[0]} linhas e {df.shape[1]} colunas")
🧠 Possibilidades de Análise de Dados

Os arquivos convertidos podem ser utilizados em diferentes etapas de Ciência de Dados.

📌 Análise Exploratória
distribuição de ocorrências por município;
evolução temporal dos casos;
comparação entre tipos de violência;
identificação de municípios com maior incidência;
análise de recorrência por período.
📊 Visualização de Dados

Os dados podem ser utilizados em:

Power BI;
Tableau;
Looker Studio;
Streamlit;
Dash;
Matplotlib;
Seaborn;
Plotly.
🤖 Aprendizado de Máquina

Os dados também podem apoiar modelos preditivos, como:

classificação de risco;
agrupamento de municípios;
previsão de tendência temporal;
análise de padrões territoriais;
identificação de fatores associados à violência.

Exemplos de técnicas:

🌳 Árvores de Decisão;
🌲 Random Forest;
📈 Regressão;
🧩 K-Means;
🔎 DBSCAN;
🧠 Redes neurais;
📊 Séries temporais.
🗺️ Exemplos de Perguntas Analíticas

Este conjunto de dados pode auxiliar investigações como:

Quais municípios apresentam maior número de registros?
Há crescimento ou redução dos casos ao longo dos anos?
Quais tipos de violência são mais recorrentes?
Existem padrões regionais de feminicídio?
Há relação entre medidas protetivas e registros de violência doméstica?
Quais períodos apresentam maior concentração de atendimentos?
Quais municípios exigem maior atenção em políticas públicas?
🧪 Validação dos Dados

Após a conversão, recomenda-se verificar:

df.info()
df.describe(include="all")
df.isna().sum()
df.duplicated().sum()

Também é recomendável conferir:

nomes das colunas;
valores ausentes;
valores duplicados;
tipos de dados;
datas em formato textual;
inconsistências nos nomes dos municípios;
campos numéricos importados como texto.
⚠️ Tratamento de Erros

O script registra erros no console e no relatório final.

Erros comuns:

❌ Nenhum arquivo .xls encontrado

Verifique se os arquivos estão na mesma pasta do script.

Nenhum arquivo .xls encontrado no diretório!
❌ Dependência ausente

Instale as bibliotecas necessárias:

pip install pandas texttable lxml html5lib beautifulsoup4
❌ Arquivo não parece tabela HTML

O arquivo pode estar corrompido, vazio ou não corresponder ao formato esperado.

❌ Problema de encoding

O script tenta automaticamente:

latin-1
cp1252
iso-8859-1
utf-8
utf-8-sig

Caso nenhum funcione, o script tenta fallback com BeautifulSoup.

🧼 Boas Práticas Recomendadas

Antes de realizar análises avançadas, recomenda-se:

padronizar nomes de municípios;
converter colunas de datas para datetime;
revisar campos categóricos;
verificar duplicidades;
criar dicionário de dados;
registrar a data de download dos arquivos;
manter os arquivos originais em uma pasta separada;
versionar os dados processados;
documentar todas as transformações realizadas.
📁 Sugestão de Organização para Ciência de Dados
Dataset/
│
├── raw/
│   ├── arquivos_xls_originais/
│
├── processed/
│   ├── arquivos_csv_convertidos/
│
├── reports/
│   ├── relatorio_conversao_xls_csv.txt
│
├── notebooks/
│   ├── 01_analise_exploratoria.ipynb
│   ├── 02_visualizacao_dados.ipynb
│   ├── 03_modelagem_preditiva.ipynb
│
├── src/
│   ├── xls_to_csv_Monitor_of_Violence_Against_Women.py
│
└── README.md
🔐 Ética, Privacidade e Responsabilidade

Embora os dados sejam públicos, o tema envolve violência contra a mulher, feminicídio, estupro, violência doméstica e medidas protetivas.

Por isso, recomenda-se:

tratar os dados com responsabilidade;
evitar exposição indevida de informações sensíveis;
não realizar inferências discriminatórias;
não individualizar vítimas;
não usar os dados para perseguição, estigmatização ou exposição;
contextualizar os resultados estatísticos;
apoiar o uso dos dados em políticas públicas, prevenção e proteção social.
🚀 Próximos Passos do Projeto

Possíveis melhorias futuras:

criar pipeline automatizado de download dos arquivos;
criar dashboard interativo em Streamlit;
integrar dados por município com indicadores do IBGE;
gerar mapas geográficos com geopandas;
criar modelo de previsão de tendência;
gerar relatório automático em PDF;
criar banco de dados SQLite ou PostgreSQL;
criar API para consulta dos dados tratados;
desenvolver painel de monitoramento por município.
📚 Fonte dos Dados

Os dados utilizados devem ser obtidos diretamente no portal oficial:

Monitor da Violência Contra a Mulher — SEJUSP-MS e PJMS
https://monitorviolenciacontramulher.sejusp.ms.gov.br/

👨‍💻 Autor

VIANA
Projeto voltado à organização, conversão e preparação de dados públicos sobre violência contra a mulher no estado de Mato Grosso do Sul para fins de análise de dados, pesquisa aplicada e desenvolvimento de soluções em Ciência de Dados.

📄 Licença

Este projeto pode ser utilizado para fins educacionais, acadêmicos, científicos e de interesse público.

Sugestão de licença:

MIT License
🤝 Contribuições

Contribuições são bem-vindas.

Você pode colaborar com:

melhorias no script;
tratamento de dados;
padronização de colunas;
documentação;
notebooks de análise;
dashboards;
modelos preditivos;
validação dos dados;
integração com outras fontes públicas.
⭐ Apoie o Projeto

Se este repositório foi útil para sua pesquisa, estudo ou desenvolvimento, considere deixar uma estrela no GitHub.

⭐ Dados públicos bem documentados fortalecem a transparência, a pesquisa e a formulação de políticas públicas.
