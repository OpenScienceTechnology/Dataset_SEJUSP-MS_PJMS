# 🟣 Monitor da Violência Contra a Mulher em Mato Grosso do Sul (SEJUSP-MS/PJMS)

[![Dados Públicos](https://img.shields.io/badge/Dados-Públicos-blue)](#-fonte-dos-dados)
[![Fonte SEJUSP-MS](https://img.shields.io/badge/Fonte-SEJUSP--MS-purple)](https://monitorviolenciacontramulher.sejusp.ms.gov.br/)
[![PJMS/TJMS](https://img.shields.io/badge/Parceria-PJMS%2FTJMS-indigo)](https://www.tjms.jus.br/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)](#-como-usar-com-python)
[![LGPD](https://img.shields.io/badge/Ética-LGPD-important)](#-ética-privacidade-e-lgpd)

> 📊 Repositório destinado à documentação, organização e análise exploratória dos dados extraídos do **Monitor da Violência Contra a Mulher**, com foco em registros relacionados à violência doméstica, feminicídios, estupros, homicídios de mulheres, medidas protetivas de urgência e atendimentos de emergência no Estado de Mato Grosso do Sul.

---

## 📌 Visão geral

O **Monitor da Violência Contra a Mulher** é uma iniciativa institucional voltada à integração e visualização de informações sobre violência de gênero em Mato Grosso do Sul. A plataforma reúne dados de segurança pública e do sistema de justiça, permitindo análises por período, município, tipo de ocorrência, características das vítimas/autores e indicadores territoriais.

Este repositório organiza bases exportadas em formato `.xls` do Monitor, permitindo sua utilização em projetos de:

- 📈 análise exploratória de dados;
- 🗺️ visualização territorial por município;
- 📊 construção de dashboards;
- 🤖 mineração de dados e aprendizado de máquina;
- 🧠 estudos acadêmicos sobre violência contra a mulher;
- 🏛️ suporte à formulação de políticas públicas baseadas em evidências.

---

## 🏛️ Fonte dos dados

**Fonte principal:** Monitor da Violência Contra a Mulher — SEJUSP-MS e PJMS/TJMS  
🔗 https://monitorviolenciacontramulher.sejusp.ms.gov.br/

**Órgãos relacionados:**

- **SEJUSP-MS** — Secretaria de Estado de Justiça e Segurança Pública de Mato Grosso do Sul;
- **PJMS/TJMS** — Poder Judiciário de Mato Grosso do Sul / Tribunal de Justiça de Mato Grosso do Sul;
- Sistemas de registros policiais, judiciais e medidas protetivas associados ao monitoramento da violência de gênero.

> ⚠️ Observação: os arquivos deste repositório foram extraídos/exportados do painel público e devem ser tratados como dados administrativos. Sua interpretação exige cautela metodológica, pois registros oficiais podem refletir notificações, boletins, atendimentos ou procedimentos, não necessariamente a totalidade real dos eventos ocorridos.

---

## 📁 Arquivos documentados

Os arquivos analisados possuem extensão `.xls`, mas seu conteúdo está estruturado como **tabelas HTML** exportadas pelo sistema. Isso significa que podem ser abertos no Excel, LibreOffice ou lidos em Python com `pandas.read_html()`.

| Nº | Arquivo | Tema | Registros | Colunas | Período observado no arquivo | Municípios identificados |
|---:|---|---|---:|---:|---|---:|
| 1 | `ATENDIMENTOS_EMERGENCIA_MS_2026-05-18.xls` | 🚨 Atendimentos de emergência | 41.548 | 8 | 27/12/2016 a 14/05/2026 | 91 |
| 2 | `MEDIDAS_PROTETIVAS_URGENCIA_MPU_MS_2026-05-18.xls` | 🛡️ Medidas protetivas de urgência / MPU | 800 | 16 | 02/02/2026 a 11/02/2026 | 52 |
| 3 | `MULHERES_VITIMAS_HOMICIDIOS_MS_2026-05-18.xls` | ⚰️ Mulheres vítimas de homicídios | 1.715 | 16 | 07/01/2016 a 09/02/2026 | 61 |
| 4 | `VITIMAS_ESTUPRO_MS_2026-05-18.xls` | 🚫 Vítimas de estupro | 43.509 | 16 | 01/01/2016 a 11/02/2026 | 79 |
| 5 | `VITIMAS_FEMINICIDIOS_MS_2026-05-18.xls` | 🕯️ Vítimas de feminicídios | 997 | 16 | 05/01/2016 a 24/01/2026 | 67 |
| 6 | `VITIMAS_VIOLENCIA_DOMESTICA_MS_2026-05-18.xls` | 🏠 Vítimas de violência doméstica | 2.900 | 16 | 24/01/2026 a 11/02/2026 | 75 |

**Total bruto de registros analisados:** `91.469` linhas.

> ⚠️ Atenção metodológica: em alguns arquivos com nome associado a “vítimas”, a coluna `ENVOLVIMENTO` também contém registros classificados como `AUTOR`. Para análises estritamente voltadas às vítimas, recomenda-se filtrar `ENVOLVIMENTO == "VÍTIMA"` antes de calcular indicadores.

---

## 🗂️ Estrutura recomendada do repositório

```text
monitor-violencia-contra-mulher-ms/
├── README.md
├── LICENSE
├── requirements.txt
├── data/
│   ├── raw/
│   │   ├── ATENDIMENTOS_EMERGENCIA_MS_2026-05-18.xls
│   │   ├── MEDIDAS_PROTETIVAS_URGENCIA_MPU_MS_2026-05-18.xls
│   │   ├── MULHERES_VITIMAS_HOMICIDIOS_MS_2026-05-18.xls
│   │   ├── VITIMAS_ESTUPRO_MS_2026-05-18.xls
│   │   ├── VITIMAS_FEMINICIDIOS_MS_2026-05-18.xls
│   │   └── VITIMAS_VIOLENCIA_DOMESTICA_MS_2026-05-18.xls
│   ├── processed/
│   │   ├── atendimentos_emergencia.csv
│   │   ├── medidas_protetivas_urgencia.csv
│   │   ├── mulheres_vitimas_homicidios.csv
│   │   ├── vitimas_estupro.csv
│   │   ├── vitimas_feminicidios.csv
│   │   └── vitimas_violencia_domestica.csv
│   └── external/
│       └── municipios_ms_ibge.geojson
├── notebooks/
│   ├── 01_leitura_e_padronizacao.ipynb
│   ├── 02_analise_exploratoria.ipynb
│   ├── 03_visualizacao_geografica.ipynb
│   └── 04_modelagem_preditiva.ipynb
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── features.py
│   ├── visualization.py
│   └── models.py
├── reports/
│   ├── figures/
│   └── dashboard/
└── docs/
    └── dicionario_dados.md
```

---

## 🧾 Dicionário de dados

### 🚨 Arquivo: `ATENDIMENTOS_EMERGENCIA_MS_2026-05-18.xls`

| Campo | Descrição |
|---|---|
| `DATA` | Data e hora do atendimento registrado. |
| `MÊS` | Mês textual da ocorrência/atendimento. |
| `ANO` | Ano do registro. |
| `DIA DA SEMANA` | Dia da semana do atendimento. |
| `FATO` | Tipo de fato registrado, como ameaça, lesão corporal ou descumprimento de medida protetiva. |
| `MUNICÍPIO` | Município do atendimento. |
| `BAIRRO` | Bairro informado no registro. |
| `TIPO DE LOCAL` | Tipo de local associado ao atendimento, como residência, via urbana ou condomínio. |

### 🛡️ Arquivos com 16 colunas

Os demais arquivos possuem estrutura semelhante:

| Campo | Descrição |
|---|---|
| `Nº BO` | Número do boletim de ocorrência ou identificador administrativo do registro. |
| `FATO` | Tipo penal ou descrição do fato registrado. |
| `FATO AGRUPADO` | Categoria agregada do fato, útil para classificação analítica. |
| `BAIRRO DO FATO` | Bairro onde o fato foi registrado. |
| `UF DO FATO` | Unidade da Federação. |
| `MUNICÍPIO DO FATO` | Município do fato. |
| `CÓDIGO IBGE` | Código municipal utilizado pelo IBGE. |
| `ANO DO FATO` | Ano de ocorrência do fato. |
| `DATA DO FATO` | Data do fato registrado. |
| `HORA DO FATO` | Horário do fato, quando disponível. |
| `ENVOLVIMENTO` | Papel da pessoa no registro, como `VÍTIMA` ou `AUTOR`. |
| `SEXO` | Sexo informado no registro. |
| `NACIONALIDADE` | Nacionalidade informada. |
| `ESCOLARIDADE` | Escolaridade registrada. |
| `COR/RAÇA` | Informação de cor/raça, quando disponível. |
| `IDADE NO FATO` | Idade da pessoa no momento do fato. |

---

## 🔎 Principais categorias observadas

### 🚨 Atendimentos de emergência

Principais fatos registrados:

1. `AMEAÇA (VIOLENCIA DOMESTICA)` — 12.018 registros;
2. `DESCUMPRIMENTO DE MEDIDA PROTETIVA DE URGENCIA` — 9.581 registros;
3. `VIAS DE FATO (VIOLENCIA DOMESTICA)` — 9.109 registros;
4. `LESAO CORPORAL DOLOSA (VIOLENCIA DOMESTICA)` — 3.620 registros;
5. `LESAO CORPORAL (VIOLENCIA DOMESTICA)` — 3.243 registros.

Municípios com maior número de registros neste arquivo:

| Município | Registros |
|---|---:|
| Campo Grande | 13.410 |
| Dourados | 6.720 |
| Três Lagoas | 5.253 |
| Corumbá | 3.325 |
| Ponta Porã | 2.759 |

Locais mais recorrentes:

| Tipo de local | Registros |
|---|---:|
| Residência | 29.179 |
| Via urbana | 8.179 |
| Condomínio residencial | 902 |
| Via local | 568 |
| Aldeia indígena | 509 |

### 🚫 Vítimas de estupro

O arquivo `VITIMAS_ESTUPRO_MS_2026-05-18.xls` é o maior conjunto individual, com `43.509` registros. As categorias mais frequentes em `FATO` incluem:

- `ESTUPRO DE VULNERAVEL`;
- `ESTUPRO`;
- `ESTUPRO (VIOLENCIA DOMESTICA)`;
- registros agregados envolvendo ameaça e violência doméstica.

### 🕯️ Feminicídios

O arquivo de feminicídios possui `997` registros brutos. Como existem linhas com `ENVOLVIMENTO = AUTOR`, recomenda-se aplicar filtros antes de gerar indicadores específicos de vítimas.

### 🏠 Violência doméstica

O arquivo de violência doméstica apresenta `2.900` registros, todos referentes ao ano de 2026 no recorte fornecido. Os fatos mais frequentes são ameaça, injúria, vias de fato e lesões corporais associadas à violência doméstica.

---

## 🧪 Como usar com Python

### 1️⃣ Criar ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

### 2️⃣ Instalar dependências

```bash
pip install pandas numpy matplotlib seaborn plotly openpyxl lxml beautifulsoup4 scikit-learn geopandas folium streamlit
```

Ou crie um arquivo `requirements.txt`:

```txt
pandas>=2.2
numpy>=1.26
matplotlib>=3.8
seaborn>=0.13
plotly>=5.20
openpyxl>=3.1
lxml>=5.0
beautifulsoup4>=4.12
scikit-learn>=1.4
geopandas>=0.14
folium>=0.16
streamlit>=1.35
```

### 3️⃣ Ler os arquivos `.xls` exportados como HTML

```python
from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

arquivo = RAW_DIR / "VITIMAS_VIOLENCIA_DOMESTICA_MS_2026-05-18.xls"

df = pd.read_html(arquivo, encoding="latin-1")[0]

print(df.head())
print(df.info())
```

### 4️⃣ Ler todos os arquivos automaticamente

```python
from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

arquivos = {
    "atendimentos_emergencia": "ATENDIMENTOS_EMERGENCIA_MS_2026-05-18.xls",
    "medidas_protetivas_urgencia": "MEDIDAS_PROTETIVAS_URGENCIA_MPU_MS_2026-05-18.xls",
    "mulheres_vitimas_homicidios": "MULHERES_VITIMAS_HOMICIDIOS_MS_2026-05-18.xls",
    "vitimas_estupro": "VITIMAS_ESTUPRO_MS_2026-05-18.xls",
    "vitimas_feminicidios": "VITIMAS_FEMINICIDIOS_MS_2026-05-18.xls",
    "vitimas_violencia_domestica": "VITIMAS_VIOLENCIA_DOMESTICA_MS_2026-05-18.xls",
}

dados = {}

for nome, arquivo in arquivos.items():
    caminho = RAW_DIR / arquivo
    dados[nome] = pd.read_html(caminho, encoding="latin-1")[0]
    print(f"✅ {nome}: {dados[nome].shape[0]:,} linhas x {dados[nome].shape[1]} colunas")
```

---

## 🧹 Pipeline de tratamento recomendado

```python
import pandas as pd
import unicodedata


def normalizar_colunas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
        .str.replace(" ", "_", regex=False)
        .str.replace("/", "_", regex=False)
    )
    return df


def remover_acentos(texto):
    if pd.isna(texto):
        return texto
    return "".join(
        c for c in unicodedata.normalize("NFKD", str(texto))
        if not unicodedata.combining(c)
    )


def padronizar_texto(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for coluna in df.select_dtypes(include="object").columns:
        df[coluna] = df[coluna].astype(str).str.strip()
    return df


def tratar_datas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for coluna in ["DATA", "DATA_DO_FATO"]:
        if coluna in df.columns:
            df[coluna] = pd.to_datetime(df[coluna], dayfirst=True, errors="coerce")
    return df


def filtrar_vitimas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "ENVOLVIMENTO" in df.columns:
        df = df[df["ENVOLVIMENTO"].astype(str).str.upper().eq("VÍTIMA")]
    return df
```

---

## 📊 Exemplos de análises

### 📍 Ocorrências por município

```python
import matplotlib.pyplot as plt

df = dados["atendimentos_emergencia"].copy()

top_municipios = (
    df["MUNICÍPIO"]
    .value_counts()
    .head(10)
    .sort_values()
)

top_municipios.plot(kind="barh", figsize=(10, 6))
plt.title("Top 10 municípios por atendimentos de emergência")
plt.xlabel("Registros")
plt.ylabel("Município")
plt.tight_layout()
plt.show()
```

### 📅 Série histórica anual

```python
serie_anual = (
    dados["atendimentos_emergencia"]
    .groupby("ANO")
    .size()
    .reset_index(name="registros")
)

print(serie_anual)
```

### 🏠 Locais mais recorrentes

```python
locais = (
    dados["atendimentos_emergencia"]["TIPO DE LOCAL"]
    .value_counts()
    .head(10)
)

print(locais)
```

### 👥 Separar vítimas e autores

```python
df_estupro = dados["vitimas_estupro"].copy()

vitimas_estupro = df_estupro[df_estupro["ENVOLVIMENTO"].astype(str).str.upper() == "VÍTIMA"]
autores_estupro = df_estupro[df_estupro["ENVOLVIMENTO"].astype(str).str.upper() == "AUTOR"]

print("Vítimas:", vitimas_estupro.shape)
print("Autores:", autores_estupro.shape)
```

---

## 🗺️ Ideias de visualização geográfica

Para análises espaciais, recomenda-se cruzar os dados com malhas municipais do IBGE.

Exemplos de mapas possíveis:

- 🟣 mapa coroplético de registros por município;
- 🔥 mapa de concentração de atendimentos de emergência;
- 🕯️ mapa de feminicídios por ano;
- 🚫 distribuição territorial de estupros;
- 🛡️ medidas protetivas por município;
- 📌 comparação entre interior, fronteira e região metropolitana de Campo Grande.

Exemplo conceitual:

```python
import geopandas as gpd

malha_ms = gpd.read_file("data/external/municipios_ms_ibge.geojson")

indicador = (
    dados["atendimentos_emergencia"]
    .groupby("MUNICÍPIO")
    .size()
    .reset_index(name="registros")
)

mapa = malha_ms.merge(
    indicador,
    left_on="NM_MUN",
    right_on="MUNICÍPIO",
    how="left"
)

mapa["registros"] = mapa["registros"].fillna(0)
mapa.plot(column="registros", legend=True, figsize=(10, 10))
```

---

## 🤖 Possibilidades de aprendizado de máquina

Este conjunto de dados pode apoiar estudos de **mineração de dados**, **classificação**, **clusterização** e **modelagem preditiva**, desde que respeitados os limites éticos e estatísticos.

### 🔮 Exemplos de perguntas analíticas

- Quais municípios concentram maior volume de registros por tipo de violência?
- Há sazonalidade mensal, semanal ou horária nos atendimentos?
- Quais categorias de fato estão mais associadas a registros de violência doméstica?
- Existem agrupamentos territoriais com perfis semelhantes de violência?
- É possível identificar padrões de risco recorrentes em determinadas regiões?

### 🧠 Modelos possíveis

| Técnica | Aplicação sugerida |
|---|---|
| `K-Means` | Agrupar municípios por perfil de ocorrências. |
| `DBSCAN` | Identificar concentrações espaciais ou comportamentos atípicos. |
| `Random Forest` | Classificar tipos de fato ou estimar importância de variáveis. |
| `Árvore de Decisão` | Criar regras interpretáveis para apoio analítico. |
| `Regressão` | Estimar tendência temporal de registros. |
| `Séries temporais` | Avaliar sazonalidade e projeções por ano/mês. |
| `NLP` | Padronizar descrições textuais de fatos e categorias agregadas. |

> ⚠️ Modelos preditivos neste tema devem ser usados como apoio analítico, nunca como ferramenta automática de decisão individual, policiamento discriminatório ou exposição de vítimas.

---

## 📈 Indicadores sugeridos

| Indicador | Descrição |
|---|---|
| `total_registros` | Número bruto de registros por base. |
| `registros_por_ano` | Evolução anual dos registros. |
| `registros_por_mes` | Distribuição mensal. |
| `registros_por_municipio` | Concentração territorial. |
| `registros_por_fato` | Frequência dos tipos de fato. |
| `vitimas_por_cor_raca` | Perfil racial informado, quando disponível. |
| `vitimas_por_escolaridade` | Escolaridade das vítimas, quando disponível. |
| `vitimas_por_faixa_etaria` | Faixas de idade no momento do fato. |
| `autores_por_sexo` | Perfil de autores nos registros em que essa informação aparece. |
| `locais_mais_frequentes` | Locais com maior ocorrência em atendimentos de emergência. |

---

## 🧮 Exemplo de criação de faixas etárias

```python
import pandas as pd

def criar_faixa_etaria(df):
    df = df.copy()
    df["IDADE NO FATO"] = pd.to_numeric(df["IDADE NO FATO"], errors="coerce")

    bins = [0, 12, 17, 29, 39, 49, 59, 120]
    labels = [
        "0-12",
        "13-17",
        "18-29",
        "30-39",
        "40-49",
        "50-59",
        "60+"
    ]

    df["FAIXA_ETARIA"] = pd.cut(
        df["IDADE NO FATO"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    return df
```

---

## 📊 Sugestão de dashboard

Um dashboard público ou acadêmico pode conter:

- 🧭 filtros por ano, município, fato e envolvimento;
- 📍 mapa de calor por município;
- 📆 série temporal anual e mensal;
- 🏠 ranking por tipo de local;
- 👥 distribuição por sexo, cor/raça, escolaridade e idade;
- 🚨 painel específico de feminicídios;
- 🛡️ painel de medidas protetivas;
- 📄 exportação de tabelas agregadas em CSV/Excel.

Ferramentas recomendadas:

- `Streamlit` para painel interativo simples;
- `Plotly Dash` para aplicação analítica avançada;
- `Power BI` ou `Looker Studio` para visualização institucional;
- `Folium` e `GeoPandas` para mapas.

---

## ⚠️ Limitações dos dados

1. **Subnotificação:** violência contra a mulher é fenômeno sensível e parte dos casos pode não ser registrada oficialmente.
2. **Registro administrativo:** os dados representam registros, atendimentos, boletins ou procedimentos, não necessariamente eventos únicos.
3. **Duplicidade possível:** um mesmo caso pode gerar múltiplos registros, pessoas envolvidas ou atualizações administrativas.
4. **Arquivos heterogêneos:** nem todas as bases possuem o mesmo período, o mesmo volume ou a mesma granularidade.
5. **Campos ausentes ou incompletos:** variáveis como idade, escolaridade, cor/raça e horário podem conter valores nulos, não informados ou inconsistentes.
6. **Mudanças legais e classificatórias:** categorias como feminicídio podem sofrer alterações de registro ao longo dos anos, afetando comparações históricas.
7. **Interpretação contextual:** números absolutos devem ser analisados junto a população municipal, rede de atendimento, política pública local e variações de notificação.

---

## 🔐 Ética, privacidade e LGPD

Embora os dados sejam oriundos de fonte pública, o tema envolve violência de gênero, vítimas, autores e registros sensíveis. Recomenda-se:

- ✅ divulgar apenas resultados agregados;
- ✅ evitar exposição de número de boletim de ocorrência em materiais públicos;
- ✅ remover ou anonimizar campos identificadores antes de publicar bases derivadas;
- ✅ não tentar reidentificar vítimas, autores ou famílias;
- ✅ não combinar dados com fontes externas para inferir identidade individual;
- ✅ evitar análises que reforcem estigmas territoriais, raciais, sociais ou de gênero;
- ✅ documentar hipóteses, filtros e limitações metodológicas;
- ✅ utilizar os dados para pesquisa, transparência, prevenção e formulação responsável de políticas públicas.

> 🛑 Este projeto não substitui canais oficiais de denúncia, atendimento emergencial, assistência social, saúde, segurança pública ou justiça.

---

## 🧾 Padronização recomendada para bases processadas

Para facilitar análises futuras, recomenda-se converter as bases brutas para CSV padronizado:

```python
from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

for nome, arquivo in arquivos.items():
    df = pd.read_html(RAW_DIR / arquivo, encoding="latin-1")[0]
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
        .str.replace(" ", "_", regex=False)
        .str.replace("/", "_", regex=False)
    )
    df.to_csv(OUT_DIR / f"{nome}.csv", index=False, encoding="utf-8-sig")
```

---

## ✅ Boas práticas para commits

Sugestão de mensagens de commit:

```bash
git add README.md data/raw/*.xls

git commit -m "docs: adiciona documentação do Monitor da Violência Contra a Mulher"
git commit -m "data: adiciona bases brutas exportadas da SEJUSP-MS"
git commit -m "feat: cria pipeline inicial de leitura e padronização"
git commit -m "analysis: adiciona análise exploratória dos registros por município"
```

Se os arquivos ultrapassarem o limite recomendado pelo GitHub, utilize Git LFS:

```bash
git lfs install
git lfs track "*.xls"
git add .gitattributes
git add data/raw/*.xls
git commit -m "data: versiona arquivos xls com Git LFS"
```

---

## 🧑‍💻 Exemplo de notebook inicial

```python
# 01_leitura_e_padronizacao.ipynb

from pathlib import Path
import pandas as pd

RAW_DIR = Path("../data/raw")

arquivo = RAW_DIR / "ATENDIMENTOS_EMERGENCIA_MS_2026-05-18.xls"
df = pd.read_html(arquivo, encoding="latin-1")[0]

print("Dimensões:", df.shape)
display(df.head())

df["DATA"] = pd.to_datetime(df["DATA"], dayfirst=True, errors="coerce")

df.groupby("ANO").size().plot(kind="bar", title="Atendimentos de emergência por ano")
```

---

## 📚 Referências institucionais

- SEJUSP-MS. **Monitor da Violência Contra a Mulher**. Disponível em: https://monitorviolenciacontramulher.sejusp.ms.gov.br/
- Tribunal de Justiça de Mato Grosso do Sul. **Monitor da Violência Contra a Mulher é lançado como ferramenta inovadora**. Disponível em: https://www.tjms.jus.br/noticia/64929
- Governo de Mato Grosso do Sul / SEJUSP-MS. **Mato Grosso do Sul conta com ferramenta importante para o enfrentamento à violência de gênero**. Disponível em: https://www.sejusp.ms.gov.br/mato-grosso-do-sul-conta-com-ferramenta-importante-para-o-enfrentamento-a-violencia-de-genero/
- Brasil. **Lei nº 13.709/2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)**.

---

## 📌 Status do projeto

- ✅ Bases brutas identificadas;
- ✅ Estrutura de colunas mapeada;
- ✅ Dicionário de dados inicial criado;
- ✅ Recomendações de uso em Python documentadas;
- 🔄 Próximas etapas sugeridas: limpeza, normalização, análise exploratória, mapas e dashboard.

---

## 🤝 Contribuição

Contribuições são bem-vindas para:

- corrigir inconsistências de nomenclatura;
- criar scripts de limpeza;
- adicionar notebooks de análise exploratória;
- construir visualizações geográficas;
- desenvolver dashboards;
- melhorar a documentação metodológica;
- propor indicadores responsáveis para políticas públicas.

---

## 📄 Licença

Este repositório utiliza dados públicos de órgãos oficiais. Verifique sempre os termos de uso da fonte original antes de redistribuir bases derivadas.

Sugestão para o código-fonte do projeto: licença `MIT`.  
Sugestão para documentação: `CC BY 4.0`, com citação da fonte original dos dados.

---

## ✍️ Como citar este repositório

```text
VIANA. Monitor da Violência Contra a Mulher em Mato Grosso do Sul: documentação e análise de dados públicos da SEJUSP-MS e PJMS/TJMS. GitHub, 2026. Fonte dos dados: Monitor da Violência Contra a Mulher — SEJUSP-MS. Disponível em: https://monitorviolenciacontramulher.sejusp.ms.gov.br/
```

---

## 💜 Finalidade social

A organização destes dados busca apoiar a produção de conhecimento, o fortalecimento da transparência pública e o desenvolvimento de soluções analíticas voltadas à prevenção da violência contra mulheres em Mato Grosso do Sul.

> 📢 Dados bem documentados podem fortalecer pesquisas, orientar políticas públicas e ampliar a capacidade institucional de prevenção, proteção e resposta à violência de gênero.
