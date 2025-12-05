from pathlib import Path
import subprocess

def save_tex_file(code, path="output/relatorio.tex"):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(code, encoding="utf8")
    return p

def compile_pdf(tex_path: Path):
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", tex_path.name],
        cwd=tex_path.parent,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return tex_path.with_suffix(".pdf")
