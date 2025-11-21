"""
Renderiza a primeira página fixa.
"""

from utils.logger import get_logger

logger = get_logger("first_page")

def render_first_page(dados) -> str:
    logger.info("Renderizando primeira página...")
    
    # TODO: retornar caminho de PDF gerado
    return "templates/primeira_pagina.pdf"
