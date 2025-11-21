"""
Salva o PDF final no local especificado.
"""

from utils.logger import get_logger
import shutil

logger = get_logger("exporter")

def export_pdf(pdf_path: str, destino: str):
    logger.info(f"Exportando PDF final para {destino}")

    # TODO: substituir cópia por escrita real
    shutil.copy(pdf_path, destino)
