"""
Ponto de entrada principal via linha de comando.

Uso esperado:
    python main.py --input data/input/dados.json --output relatorios/relatorio.pdf
"""

from pipeline import run_pipeline
from utils.logger import get_logger

logger = get_logger("main")

def main():
    logger.info("Iniciando execução do gerador de sumários executivos.")
    # Obs.: implementar CLI de verdade usando argparse
    run_pipeline()
    logger.info("Processo concluído.")

if __name__ == "__main__":
    main()
