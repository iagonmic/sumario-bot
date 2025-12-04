def latex_escape(text: str) -> str:
    """
    Escapa caracteres especiais do LaTeX.
    """
    if not isinstance(text, str):
        return text

    replacements = {
        "\\": r"\\",
        "%": r"\%",
        "$": r"\$",
        "&": r"\&",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "#": r"\#",
        "^": r"\^{}",
        "~": r"\~{}",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text

def sanitize_json(obj):
    if isinstance(obj, dict):
        return {k: sanitize_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize_json(v) for v in obj]
    elif isinstance(obj, str):
        return latex_escape(obj)
    else:
        return obj
