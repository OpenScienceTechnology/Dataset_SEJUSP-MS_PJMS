#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================
  MONITOR DA VIOLÊNCIA CONTRA A MULHER - SEJUSP/MS e PJMS
  Conversor XLS (HTML) → CSV
  🔗 Fonte: https://monitorviolenciacontramulher.sejusp.ms.gov.br/
=========================================================================================
  Descrição:
      Converte arquivos XLS do Monitor da Violência contra a Mulher
      (que são tabelas HTML com extensão .xls) para CSV (UTF-8, separador ";").
      Gera relatório TXT completo de execução usando Texttable.

  Uso:
      Copie este script para a mesma pasta onde estão os arquivos .xls e execute:
          python xls_to_csv_Monitor_of_Violence_Against_Women.py

  Dependências:
      pip install pandas texttable lxml html5lib
=========================================================================================
🔍 Descoberta Técnica Importante:
Os arquivos .xls do "MONITOR DA VIOLÊNCIA CONTRA A MULHER - SEJUSP/MS e PJMS" 
são na verdade tabelas HTML com extensão .xls (prática comum em portais gov. 
brasileiros), encoding latin-1. O script lida com isso automaticamente, tentando 
múltiplos encodings em cascata, com fallback para BeautifulSoup se necessário.
📌 Os arquivos são tabelas HTML com extensão .xls, codificadas em latin-1 (ISO-8859-1).
=========================================================================================
  Script  : Monitor Violência MS - Script de Conversão
  Autor   : VIANA
  Data    : 2026-05-23
  Versão  : 1.0.0
  Nota    : 🧾 Script de conversão de arquivos XLS para CSV
=========================================================================================
"""

# ──────────────────────────────────────────────────────────────────────────────
# IMPORTAÇÕES
# ──────────────────────────────────────────────────────────────────────────────
import sys
import os
import re
import time
import traceback
import platform
from io import StringIO
from datetime import datetime
from pathlib import Path

# Verificação de dependências antes de importar
_DEPS_REQUIRED = {
    "pandas": "pandas",
    "texttable": "texttable",
}

_MISSING = []
for mod, pkg in _DEPS_REQUIRED.items():
    try:
        __import__(mod)
    except ImportError:
        _MISSING.append(pkg)

if _MISSING:
    print(f"\n[ERRO] Dependências ausentes: {', '.join(_MISSING)}")
    print(f"       Execute: pip install {' '.join(_MISSING)}")
    sys.exit(1)

import pandas as pd
import texttable as tt


# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES GLOBAIS
# ──────────────────────────────────────────────────────────────────────────────

# Mapeamento: nome do arquivo XLS → nome do CSV de saída
FILE_MAP = {
    "ATENDIMENTOS_EMERGENCIA":       "atendimentos_emergencia.csv",
    "MEDIDAS_PROTETIVAS_URGENCIA":   "medidas_protetivas_urgencia.csv",
    "MPU":                           "medidas_protetivas_urgencia.csv",   # alias
    "MULHERES_VITIMAS_HOMICIDIOS":   "mulheres_vitimas_homicidios.csv",
    "VITIMAS_ESTUPRO":               "vitimas_estupro.csv",
    "VITIMAS_FEMINICIDIOS":          "vitimas_feminicidios.csv",
    "VITIMAS_VIOLENCIA_DOMESTICA":   "vitimas_violencia_domestica.csv",
}

# Encodings a tentar (ordem de prioridade)
ENCODINGS_TO_TRY = ["latin-1", "cp1252", "iso-8859-1", "utf-8", "utf-8-sig"]

# Separador CSV de saída
CSV_SEPARATOR = ";"

# Encoding de saída CSV
CSV_ENCODING = "utf-8-sig"   # UTF-8 com BOM — compatível com Excel BR

# Nome do relatório de execução
REPORT_FILENAME = "relatorio_conversao_xls_csv.txt"

# Largura da tabela no relatório TXT
TABLE_WIDTH = 120

# Banner do sistema
BANNER = r"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║       MONITOR DA VIOLÊNCIA CONTRA A MULHER — SEJUSP/MS e PJMS                    ║
║       Conversor XLS (HTML) → CSV                                                 ║
║       Fonte: https://monitorviolenciacontramulher.sejusp.ms.gov.br/              ║
╚══════════════════════════════════════════════════════════════════════════════════╝
"""


# ──────────────────────────────────────────────────────────────────────────────
# UTILITÁRIOS
# ──────────────────────────────────────────────────────────────────────────────

def log(msg: str, level: str = "INFO") -> None:
    """Imprime mensagem formatada no console."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = {"INFO": "●", "OK": "✔", "WARN": "⚠", "ERR": "✘", "HDR": "═"}.get(level, "●")
    print(f"  [{timestamp}] {prefix} {msg}")


def separator(char: str = "─", width: int = 80) -> str:
    return char * width


def fmt_size(num_bytes: int) -> str:
    """Formata tamanho de arquivo de forma legível."""
    for unit in ["B", "KB", "MB", "GB"]:
        if abs(num_bytes) < 1024.0:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} TB"


def fmt_duration(seconds: float) -> str:
    """Formata duração em formato legível."""
    if seconds < 60:
        return f"{seconds:.2f}s"
    m, s = divmod(int(seconds), 60)
    return f"{m}m {s:02d}s"


def clean_column_name(col: str) -> str:
    """Normaliza nome de coluna (strip de espaços extras)."""
    if isinstance(col, str):
        return col.strip()
    return str(col)


def detect_csv_name(xls_path: Path) -> str:
    """
    Detecta o nome do CSV de saída com base no nome do arquivo XLS.
    Verifica correspondência com FILE_MAP por substring (case-insensitive).
    Retorna nome padronizado ou cria um nome genérico.
    """
    stem = xls_path.stem.upper()
    for key, csv_name in FILE_MAP.items():
        if key in stem:
            return csv_name
    # Fallback: usa o próprio nome do XLS, apenas em minúsculas
    return xls_path.stem.lower() + ".csv"


def read_html_xls(xls_path: Path) -> tuple[pd.DataFrame, str, float]:
    """
    Lê um arquivo XLS que é na verdade uma tabela HTML.
    Tenta múltiplos encodings e retorna (DataFrame, encoding_usado, tempo_leitura).
    Lança ValueError se nenhum encoding funcionar.
    """
    last_error = None
    t0 = time.time()

    for enc in ENCODINGS_TO_TRY:
        try:
            with open(xls_path, "r", encoding=enc, errors="replace") as fh:
                content = fh.read()

            # Verifica se parece HTML com tabela
            if "<table" not in content.lower():
                raise ValueError(f"Conteúdo não parece ser uma tabela HTML (encoding={enc})")

            tables = pd.read_html(StringIO(content), flavor="lxml")

            if not tables:
                raise ValueError("Nenhuma tabela HTML encontrada no arquivo.")

            # Usa a primeira tabela (maior, caso haja mais de uma)
            df = max(tables, key=lambda t: t.shape[0])

            # Limpeza dos nomes de coluna
            df.columns = [clean_column_name(c) for c in df.columns]

            # Limpeza geral dos valores string (compatível pandas 2 e 3)
            str_cols = df.select_dtypes(include=["object", "string"]).columns
            for col in str_cols:
                df[col] = df[col].astype(str).str.strip()
                df[col] = df[col].replace({"nan": "", "None": "", "NaN": ""})

            elapsed = time.time() - t0
            return df, enc, elapsed

        except Exception as e:
            last_error = e
            continue

    # Se chegou aqui, todos os encodings falharam
    # Tenta fallback com BeautifulSoup se disponível
    try:
        from bs4 import BeautifulSoup
        log(f"  Tentando fallback com BeautifulSoup...", "WARN")
        with open(xls_path, "rb") as fh:
            raw = fh.read()
        for enc in ENCODINGS_TO_TRY:
            try:
                soup = BeautifulSoup(raw.decode(enc, errors="replace"), "html.parser")
                table = soup.find("table")
                if table:
                    headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]
                    rows = []
                    for tr in table.find("tbody").find_all("tr"):
                        rows.append([td.get_text(strip=True) for td in tr.find_all("td")])
                    df = pd.DataFrame(rows, columns=headers)
                    elapsed = time.time() - t0
                    return df, enc + " (BeautifulSoup)", elapsed
            except Exception:
                continue
    except ImportError:
        pass

    raise ValueError(f"Falha na leitura do arquivo. Último erro: {last_error}")


def analyze_dataframe(df: pd.DataFrame) -> dict:
    """Gera estatísticas descritivas do DataFrame."""
    stats = {
        "n_rows": len(df),
        "n_cols": len(df.columns),
        "n_cells": len(df) * len(df.columns),
        "columns": list(df.columns),
        "dtypes": {c: str(df[c].dtype) for c in df.columns},
        "nulls": {c: int(df[c].isna().sum() + (df[c] == "").sum())
                  for c in df.select_dtypes(include=["object", "string"]).columns},
        "duplicates": int(df.duplicated().sum()),
        "col_summaries": {},
    }

    # Resumo por coluna categórica relevante
    for col in df.columns:
        try:
            n_unique = df[col].nunique()
            top_values = df[col].value_counts().head(3).to_dict()
            stats["col_summaries"][col] = {
                "unique": n_unique,
                "top3": top_values,
            }
        except Exception:
            pass

    return stats


# ──────────────────────────────────────────────────────────────────────────────
# GERADOR DE RELATÓRIO TXT
# ──────────────────────────────────────────────────────────────────────────────

def build_report(
    dir_path: Path,
    results: list[dict],
    global_start: float,
    global_end: float,
) -> str:
    """
    Constrói o conteúdo completo do relatório TXT de execução.
    Usa texttable para as tabelas.
    """
    lines = []
    W = TABLE_WIDTH

    def line(txt=""):
        lines.append(txt)

    def hline(char="═"):
        lines.append(char * W)

    def title(txt, char="═"):
        lines.append(char * W)
        lines.append(f"  {txt}")
        lines.append(char * W)

    # ── Cabeçalho ──────────────────────────────────────────────────────────
    hline("═")
    line("  MONITOR DA VIOLÊNCIA CONTRA A MULHER — SEJUSP/MS e PJMS")
    line("  RELATÓRIO DE CONVERSÃO XLS → CSV")
    hline("═")
    line(f"  Fonte     : https://monitorviolenciacontramulher.sejusp.ms.gov.br/")
    line(f"  Gerado em : {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}")
    line(f"  Diretório : {dir_path}")
    line(f"  Sistema   : {platform.system()} {platform.release()} | Python {platform.python_version()}")
    line(f"  Duração   : {fmt_duration(global_end - global_start)}")
    hline("─")
    line()

    # ── Resumo Executivo ───────────────────────────────────────────────────
    title("1. RESUMO EXECUTIVO", "═")
    line()

    ok_results  = [r for r in results if r["status"] == "OK"]
    err_results = [r for r in results if r["status"] != "OK"]
    total_rows  = sum(r.get("n_rows", 0) for r in ok_results)
    total_cols  = sum(r.get("n_cols", 0) for r in ok_results)
    total_bytes = sum(r.get("csv_bytes", 0) for r in ok_results)

    tab = tt.Texttable(max_width=W)
    tab.set_deco(tt.Texttable.BORDER | tt.Texttable.HEADER | tt.Texttable.VLINES)
    tab.set_cols_align(["l", "r"])
    tab.set_cols_dtype(["t", "t"])
    tab.add_rows([
        ["MÉTRICA", "VALOR"],
        ["Arquivos XLS encontrados",  str(len(results))],
        ["Conversões com sucesso",     str(len(ok_results))],
        ["Conversões com erro",        str(len(err_results))],
        ["Total de registros (linhas)",f"{total_rows:,.0f}".replace(",", ".")],
        ["Total de colunas (soma)",    str(total_cols)],
        ["Volume total dos CSVs",      fmt_size(total_bytes)],
        ["Tempo total de execução",    fmt_duration(global_end - global_start)],
    ])
    line(tab.draw())
    line()

    # ── Tabela de Resultados por Arquivo ──────────────────────────────────
    title("2. RESULTADOS POR ARQUIVO", "═")
    line()

    tab2 = tt.Texttable(max_width=W)
    tab2.set_deco(tt.Texttable.BORDER | tt.Texttable.HEADER | tt.Texttable.VLINES)
    tab2.set_cols_align(["l", "l", "r", "r", "r", "r", "l", "l"])
    tab2.set_cols_dtype(["t", "t", "t", "t", "t", "t", "t", "t"])
    tab2.set_cols_width([30, 32, 8, 8, 12, 9, 10, 9])
    tab2.header([
        "ARQUIVO XLS", "CSV GERADO", "LINHAS", "COLUNAS",
        "TAMANHO XLS", "TAM CSV", "ENCODING", "STATUS"
    ])

    for r in results:
        tab2.add_row([
            r["xls_name"][:30],
            r.get("csv_name", "—")[:32],
            f"{r.get('n_rows', 0):,.0f}".replace(",", ".") if r["status"] == "OK" else "—",
            str(r.get("n_cols", "—")),
            fmt_size(r.get("xls_bytes", 0)),
            fmt_size(r.get("csv_bytes", 0)) if r["status"] == "OK" else "—",
            r.get("encoding", "—"),
            r["status"],
        ])

    line(tab2.draw())
    line()

    # ── Detalhamento por Dataset ───────────────────────────────────────────
    title("3. DETALHAMENTO POR DATASET", "═")

    for idx, r in enumerate(results, 1):
        line()
        hline("─")
        line(f"  [{idx}/{len(results)}] {r['xls_name']}")
        hline("─")

        if r["status"] != "OK":
            line(f"  STATUS  : ERRO")
            line(f"  Arquivo : {r['xls_path']}")
            line(f"  Detalhe : {r.get('error', 'Erro desconhecido')}")
            line()
            continue

        line(f"  Status       : CONVERSÃO CONCLUÍDA COM SUCESSO")
        line(f"  XLS (entrada): {r['xls_path']}")
        line(f"  CSV (saída)  : {r['csv_path']}")
        line(f"  Encoding XLS : {r['encoding']}")
        line(f"  Encoding CSV : {CSV_ENCODING} (separador: '{CSV_SEPARATOR}')")
        line(f"  Tempo leitura: {fmt_duration(r.get('read_time', 0))}")
        line(f"  Tamanho XLS  : {fmt_size(r.get('xls_bytes', 0))}")
        line(f"  Tamanho CSV  : {fmt_size(r.get('csv_bytes', 0))}")
        line()

        # Colunas do dataset
        line("  COLUNAS DO DATASET:")
        stats = r.get("stats", {})
        cols = stats.get("columns", [])
        dtypes = stats.get("dtypes", {})
        nulls = stats.get("nulls", {})
        col_sum = stats.get("col_summaries", {})

        tab_col = tt.Texttable(max_width=W)
        tab_col.set_deco(tt.Texttable.BORDER | tt.Texttable.HEADER | tt.Texttable.VLINES)
        tab_col.set_cols_align(["r", "l", "l", "r", "r", "l"])
        tab_col.set_cols_dtype(["t", "t", "t", "t", "t", "t"])
        tab_col.set_cols_width([4, 32, 10, 8, 10, 38])
        tab_col.header(["#", "COLUNA", "TIPO", "NULOS/\nVAZIOS", "ÚNICOS", "TOP-3 VALORES"])

        for i, col in enumerate(cols, 1):
            summ = col_sum.get(col, {})
            top3 = summ.get("top3", {})
            top3_str = " | ".join(
                f"{str(k)[:18]!r}({v})" for k, v in list(top3.items())[:3]
            )
            tab_col.add_row([
                str(i),
                col[:32],
                dtypes.get(col, "—"),
                str(nulls.get(col, "—")),
                str(summ.get("unique", "—")),
                top3_str[:38],
            ])

        line(tab_col.draw())
        line()

        # Resumo de qualidade
        dup = stats.get("duplicates", 0)
        n_rows = stats.get("n_rows", 0)
        line(f"  QUALIDADE DOS DADOS:")
        line(f"    Registros totais  : {n_rows:,.0f}".replace(",", "."))
        line(f"    Registros duplicad: {dup:,.0f}".replace(",", "."))
        pct_dup = (dup / n_rows * 100) if n_rows > 0 else 0
        line(f"    Taxa duplicação   : {pct_dup:.2f}%")
        line()

    # ── Estrutura de Arquivos Gerados ─────────────────────────────────────
    title("4. ESTRUTURA DE ARQUIVOS GERADOS", "═")
    line()
    line(f"  {dir_path}/")
    line(f"  ├── [XLS originais]")
    for r in results:
        status_icon = "✔" if r["status"] == "OK" else "✘"
        line(f"  │   ├── {r['xls_name']} ({fmt_size(r.get('xls_bytes', 0))})")
    line(f"  │")
    line(f"  ├── [CSVs gerados]")
    for r in ok_results:
        line(f"  │   ├── {r.get('csv_name', '—')} ({fmt_size(r.get('csv_bytes', 0))})")
    line(f"  │")
    line(f"  └── {REPORT_FILENAME}  ← este relatório")
    line()

    # ── Erros Detalhados ──────────────────────────────────────────────────
    if err_results:
        title("5. ERROS DETALHADOS", "═")
        line()
        for r in err_results:
            line(f"  Arquivo : {r['xls_name']}")
            line(f"  Caminho : {r.get('xls_path', '—')}")
            line(f"  Erro    : {r.get('error', 'Desconhecido')}")
            if r.get("traceback"):
                line(f"  Stack   :")
                for tb_line in r["traceback"].splitlines():
                    line(f"    {tb_line}")
            line()
    else:
        title("5. ERROS", "═")
        line()
        line("  Nenhum erro registrado. Todas as conversões foram bem-sucedidas.")
        line()

    # ── Próximos Passos (análise de dados) ────────────────────────────────
    title("6. PRÓXIMOS PASSOS — ANÁLISE DE DADOS EM PYTHON", "═")
    line()
    line("  Os arquivos CSV gerados estão prontos para análise. Exemplo de carga:")
    line()
    line("  ┌─────────────────────────────────────────────────────────────────────┐")
    line("  │  import pandas as pd                                                │")
    line("  │  import glob, os                                                    │")
    line("  │                                                                     │")
    line("  │  # Carregar todos os CSVs gerados                                  │")
    line("  │  pasta = os.path.dirname(os.path.abspath(__file__))                │")
    line("  │  csvs = glob.glob(os.path.join(pasta, '*.csv'))                    │")
    line("  │  dfs  = {os.path.basename(f): pd.read_csv(f, sep=';',             │")
    line("  │          encoding='utf-8-sig') for f in csvs}                      │")
    line("  │                                                                     │")
    line("  │  # Exemplo: ocorrências por município (atendimentos emergência)     │")
    line("  │  df = dfs['atendimentos_emergencia.csv']                            │")
    line("  │  print(df.groupby('MUNICÍPIO')['FATO'].count().sort_values())      │")
    line("  └─────────────────────────────────────────────────────────────────────┘")
    line()

    # ── Rodapé ────────────────────────────────────────────────────────────
    hline("═")
    line(f"  Fim do relatório — {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    line(f"  SEJUSP-MS / PJMS — Monitor da Violência contra a Mulher — MS/Brasil")
    hline("═")

    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# FUNÇÃO PRINCIPAL
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    global_start = time.time()

    print(BANNER)

    # ── 1. Detecta diretório de trabalho ──────────────────────────────────
    # Estratégia: usa o diretório atual (CWD) como primário.
    # Se não encontrar arquivos .xls, tenta o diretório do próprio script.
    # Isso cobre ambos os casos:
    #   1) Executar via terminal na mesma pasta: python xls_to_csv_monitor_violencia.py
    #   2) Executar passando o caminho completo:  python /caminho/para/script.py
    cwd = Path(os.getcwd())
    script_dir_fallback = Path(os.path.abspath(
        sys.argv[0] if len(sys.argv) > 0 and os.path.isfile(sys.argv[0])
        else __file__
    )).parent

    if list(cwd.glob("*.xls")):
        script_dir = cwd
        log(f"Diretório detectado (CWD): {script_dir}", "INFO")
    elif list(script_dir_fallback.glob("*.xls")):
        script_dir = script_dir_fallback
        log(f"Diretório detectado (script): {script_dir}", "INFO")
    else:
        script_dir = cwd
        log(f"Diretório de trabalho: {script_dir}", "INFO")

    log(f"Diretório de trabalho: {script_dir}", "INFO")
    log(separator(), "HDR")

    # ── 2. Localiza arquivos XLS ──────────────────────────────────────────
    xls_files = sorted(script_dir.glob("*.xls"))

    if not xls_files:
        log("Nenhum arquivo .xls encontrado no diretório!", "ERR")
        log(f"Certifique-se de que os arquivos .xls estão em: {script_dir}", "ERR")
        sys.exit(1)

    log(f"Arquivos .xls encontrados: {len(xls_files)}", "OK")
    for f in xls_files:
        log(f"  → {f.name}  ({fmt_size(f.stat().st_size)})", "INFO")

    log(separator(), "HDR")

    # ── 3. Processa cada arquivo ──────────────────────────────────────────
    results: list[dict] = []

    for xls_path in xls_files:
        log(f"Processando: {xls_path.name}", "INFO")

        result = {
            "xls_name": xls_path.name,
            "xls_path": str(xls_path),
            "xls_bytes": xls_path.stat().st_size,
            "status": "ERRO",
            "error": None,
            "traceback": None,
        }

        try:
            # 3a. Lê o arquivo XLS (tabela HTML)
            log(f"  ↳ Lendo tabela HTML...", "INFO")
            df, encoding_used, read_time = read_html_xls(xls_path)

            result["encoding"] = encoding_used
            result["read_time"] = read_time
            result["n_rows"] = len(df)
            result["n_cols"] = len(df.columns)

            log(f"  ↳ Lido com sucesso: {len(df):,} linhas × {len(df.columns)} colunas"
                f"  (encoding={encoding_used}, {fmt_duration(read_time)})", "OK")

            # 3b. Determina nome do CSV de saída
            csv_name = detect_csv_name(xls_path)
            csv_path = script_dir / csv_name
            result["csv_name"] = csv_name
            result["csv_path"] = str(csv_path)

            # 3c. Salva CSV
            log(f"  ↳ Salvando CSV: {csv_name}", "INFO")
            df.to_csv(
                csv_path,
                sep=CSV_SEPARATOR,
                index=False,
                encoding=CSV_ENCODING,
                lineterminator="\n",
            )

            result["csv_bytes"] = csv_path.stat().st_size
            log(f"  ↳ Salvo: {fmt_size(result['csv_bytes'])}", "OK")

            # 3d. Análise do DataFrame
            log(f"  ↳ Analisando estatísticas...", "INFO")
            result["stats"] = analyze_dataframe(df)

            result["status"] = "OK"
            log(f"  ↳ Conversão concluída!", "OK")

        except Exception as e:
            result["error"] = str(e)
            result["traceback"] = traceback.format_exc()
            log(f"  ↳ ERRO: {e}", "ERR")

        results.append(result)
        log(separator("─"), "HDR")

    # ── 4. Gera relatório TXT ─────────────────────────────────────────────
    global_end = time.time()
    log("Gerando relatório de execução...", "INFO")

    try:
        report_content = build_report(script_dir, results, global_start, global_end)
        report_path = script_dir / REPORT_FILENAME

        with open(report_path, "w", encoding="utf-8") as fh:
            fh.write(report_content)

        log(f"Relatório salvo: {report_path.name}  ({fmt_size(report_path.stat().st_size)})", "OK")

    except Exception as e:
        log(f"Erro ao gerar relatório: {e}", "ERR")

    # ── 5. Sumário Final no Console ───────────────────────────────────────
    log(separator("═"), "HDR")
    ok_count  = sum(1 for r in results if r["status"] == "OK")
    err_count = sum(1 for r in results if r["status"] != "OK")
    total_rows = sum(r.get("n_rows", 0) for r in results if r["status"] == "OK")

    log(f"SUMÁRIO FINAL", "HDR")
    log(f"  Arquivos processados : {len(results)}", "INFO")
    log(f"  Conversões OK        : {ok_count}", "OK")
    log(f"  Erros                : {err_count}", "ERR" if err_count else "INFO")
    log(f"  Total de registros   : {total_rows:,.0f}".replace(",", "."), "INFO")
    log(f"  Tempo total          : {fmt_duration(global_end - global_start)}", "INFO")
    log(separator("═"), "HDR")

    if ok_count == len(results):
        log("Todas as conversões concluídas com sucesso!", "OK")
    else:
        log(f"Atenção: {err_count} arquivo(s) com erro. Verifique o relatório.", "WARN")

    log(f"Relatório completo: {REPORT_FILENAME}", "INFO")
    log(separator("═"), "HDR")


# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
