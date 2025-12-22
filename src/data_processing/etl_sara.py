import pandas as pd
#from utils.logger import get_logger
import json
from pathlib import Path

#logger = get_logger("etl")

# dados do sara -> dados_prpg.xlsx
# dados do sidtec ->

data_output = "data/ready"


mapa_dimensoes_sara = {
    "Recomendação curso": {
        "grupo": "ESTUDANTES E ORGANIZAÇÕES",
        "nome": "Estudantes e Organizações",
        "titulo": "NPS",
        "subtitulo": "Recomendação do Programa",
        "indicador": "nps"
    },
    "Desempenho dos docentes": {
        "grupo": "PROCESSOS INTERNOS",
        "nome": "Processos Internos",
        "titulo": "Formação",
        "subtitulo": "Desempenho dos Docentes",
        "indicador": "docentes_media"
    },
    "Coordenação": {
        "grupo": "PROCESSOS INTERNOS",
        "nome": "Processos Internos",
        "titulo": "Suporte à Formação",
        "subtitulo": "Coordenação",
        "indicador": "coordenacao_media"
    },
    "Secretaria": {
        "grupo": "PROCESSOS INTERNOS",
        "nome": "Processos Internos",
        "titulo": "Suporte à Formação",
        "subtitulo": "Secretaria",
        "indicador": "secretaria_media"
    },
    "Infraestrutura": {
        "grupo": "PROCESSOS INTERNOS",
        "nome": "Processos Internos",
        "titulo": "Gestão",
        "subtitulo": "Infraestrutura",
        "indicador": "infraestrutura_media"
    }
}


def transform_sara(data_path):
    """
    Aceita um arquivo xlsx e transforma em json com o nome do arquivo no diretório data/ready com o mesmo nome
    
    :param data_path: XLSX
    """


    indicadores = [
        'Recomendação curso', # nps
        'Desempenho dos docentes', # docentes_media
        'Coordenação', # coordenação_media
        'Secretaria', # secretaria_media
        'Infraestrutura' # infraestrutura_media
    ]

    # parte de notas
    df_notas = pd.read_excel(data_path, sheet_name='Notas')

    medias = df_notas.groupby(['PERIODO_LETIVO', 'PROGRAMA', 'SIGLA_PROGRAMA', 'SIGLA_CENTRO', 'DIMENSÃO'])['RESPOSTA'].mean().reset_index() # calcular medias
    medias = medias.query('DIMENSÃO in @indicadores') # filtrar por indicadores selecionados

    saida = Path("../ready")
    saida.mkdir(exist_ok=True)

    for periodo, df_p in medias.groupby("PERIODO_LETIVO"):
        json_periodo = gerar_json_periodo(df_p, periodo)

        with open(saida / f"sara_{periodo}.json", "w", encoding="utf-8") as f:
            json.dump(json_periodo, f, ensure_ascii=False, indent=2)

    df_melhoria = pd.read_excel(data_path, sheet_name='Melhoria')


def gerar_json_periodo(df_periodo, periodo):
    resultado = {
        "primeira_pagina": {
            "fonte": "SARA",
            "coorte": periodo,
            "periodo_referencia": periodo
        },
        "dimensoes": []
    }

    grupos = {}

    for _, row in df_periodo.iterrows():
        dim_sara = row["DIMENSÃO"]
        valor = round(row["RESPOSTA"], 2)

        if dim_sara not in mapa_dimensoes_sara:
            continue

        m = mapa_dimensoes_sara[dim_sara]

        grupo_nome = m["grupo"]
        nome_dimensao = m["nome"]
        titulo = m["titulo"]
        subtitulo = m["subtitulo"]
        indicador = m["indicador"]

        # cria grupo se não existir
        if grupo_nome not in grupos:
            grupos[grupo_nome] = {
                "grupo": grupo_nome,
                "nome": nome_dimensao,
                "secoes": {}
            }

        grupo = grupos[grupo_nome]

        # cria seção se não existir
        if subtitulo not in grupo["secoes"]:
            grupo["secoes"][subtitulo] = {
                "titulo": titulo,
                "subtitulo": subtitulo,
                "fonte": "SARA",
                "indicadores": {}
            }

        # adiciona indicador
        grupo["secoes"][subtitulo]["indicadores"][indicador] = valor

    # transforma secoes em lista
    for grupo in grupos.values():
        grupo["secoes"] = list(grupo["secoes"].values())
        resultado["dimensoes"].append(grupo)

    return resultado
