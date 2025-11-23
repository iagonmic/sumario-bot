"""
Constrói páginas dinâmicas a partir de HTML + CSS usando Jinja + Pyppeteer.
"""

import json
import asyncio
import os
from jinja2 import Environment, FileSystemLoader
from pyppeteer import launch
from utils.logger import get_logger

logger = get_logger("pages_builder")


async def _gerar_pdf_assincrono(html_str: str, saida_pdf: str):
    """
    Função interna assíncrona.
    Recebe HTML renderizado e converte para PDF via Chrome headless.
    """
    temp_html_path = "saida_temp.html"

    # Salva HTML temporário
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_str)

    # Abre navegador headless
    browser = await launch(headless=True, args=["--no-sandbox"])
    page = await browser.newPage()

    # Carrega HTML
    await page.goto("file://" + os.path.abspath(temp_html_path))

    # Gera PDF
    await page.pdf({
        "path": saida_pdf,
        "format": "A4",
        "printBackground": True
    })

    await browser.close()


def _gerar_pdf(html_str: str, saida_pdf: str):
    """
    Wrapper síncrono: executa o processo assíncrono internamente.
    """
    asyncio.run(_gerar_pdf_assincrono(html_str, saida_pdf))


def render_dimension_pages(secoes: list) -> list:
    """
    Renderiza as páginas de dimensões e gera PDFs individuais ou um PDF único.
    """
    logger.info("Renderizando páginas das dimensões...")

    # --------------------------
    # 1. Carregar Template Jinja
    # --------------------------
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("templates/template_dimensao.html")

    # --------------------------
    # 2. Renderizar HTML
    # --------------------------
    html_renderizado = template.render(dimensoes=secoes)

    # --------------------------
    # 3. Gerar PDF
    # --------------------------
    saida_pdf = "relatorio_dimensoes.pdf"
    _gerar_pdf(html_renderizado, saida_pdf)

    logger.info(f"PDF gerado com sucesso: {saida_pdf}")

    return [saida_pdf]
