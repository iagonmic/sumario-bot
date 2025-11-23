"""
Monta o bloco final da dimensão (Dados → Análise → Recomendações)
"""

from utils.logger import get_logger

logger = get_logger("formatter")

def build_section(dados, analise, recomendacoes) -> dict:
    logger.info(f"Formatando seção: {dados['nome']}")

    return {
        "nome": dados["nome"],
        "dados": dados.get("indicadores", {}),
        "analise": analise,
        "recomendacoes": recomendacoes
    }
