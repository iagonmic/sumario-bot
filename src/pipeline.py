"""
pipeline.py — Orquestração completa do processo.
"""

from utils.logger import get_logger
from data_processing.loader import load_input_data
from data_processing.validator import validate_data_structure
from data_processing.preprocess import preprocess_data
from data_processing.dimensions import extract_dimensions

from ai.analysis_generator import save_analysis_to_json
from ai.recommendations_generator import save_recommendations_to_json

from latex.first_page import render_first_page
from pdf.page_builder import render_dimension_pages
from pdf.pdf_merger import merge_pdf
from pdf.exporter import export_pdf

logger = get_logger("pipeline")

def run_pipeline(input_path="data/input/dados.json", output_path="output/relatorios/relatorio.pdf"):
    logger.info("Pipeline iniciado.")

    dados = load_input_data(input_path)
    validate_data_structure(dados)
    dados_tratados = preprocess_data(dados)
    dimensoes = extract_dimensions(dados_tratados)

    save_analysis_to_json(dados_tratados)
    save_recommendations_to_json(dados_tratados)

    primeira_pagina = render_first_page(dados_tratados)
    paginas_dimensoes = render_dimension_pages(secoes)

    pdf_final = merge_pdf([primeira_pagina] + paginas_dimensoes)
    export_pdf(pdf_final, output_path)

    logger.info("Pipeline finalizado.")
