from jinja2 import Template
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"

def load_template(name):
    return Template((TEMPLATE_DIR / name).read_text(encoding="utf8"))

def build_latex_document(dados):
    base = load_template("base.tex")
    first = load_template("first_page.tex")
    dim = load_template("dimension.tex")

    primeira_pagina = first.render(
        fonte=dados["primeira_pagina"]["fonte"],
        coorte=dados["primeira_pagina"]["coorte"],
        curso=dados["primeira_pagina"]["curso"],
        periodo=dados["primeira_pagina"]["periodo_referencia"]
    )

    corpo = []
    for d in dados["dimensoes"]:
        corpo.append(
            dim.render(
                grupo=d["grupo"],
                nome=d["nome"],
                secoes=d["secoes"]
            )
        )

    return base.render(first_page=primeira_pagina, body="\n\n".join(corpo))
