from latex.builder import build_latex_document
from latex.writer import save_tex_file, compile_pdf
from latex.treatment import sanitize_json
import json
from pathlib import Path

# 1) Carrega o JSON de teste
dados = json.loads(Path("data/exemplos/exemplo_musica_recomendacao.json").read_text(encoding="utf-8"))
dados = sanitize_json(dados)

# 2) Gera o LaTeX
latex_code = build_latex_document(dados)

# 3) Salva o .tex
tex_path = save_tex_file(latex_code, "prpg/teste.tex")

# 4) Compila para PDF
pdf_path = compile_pdf(tex_path)

print("PDF gerado em:", pdf_path)
