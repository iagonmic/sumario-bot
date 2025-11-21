"""
Junta vários PDFs em um só.
"""

from utils.logger import get_logger

logger = get_logger("pdf_merger")

def merge_pdf(lista_de_pdfs: list) -> str:
    logger.info("Unificando PDFs em um único documento final...")
    
    # TODO: implementar merge real
    return "relatorio_final_temp.pdf"
