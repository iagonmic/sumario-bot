"""
Geração de análises para cada dimensão.
"""

from agno.agent import Agent
from agno.models.groq import Groq
from src.utils.logger import get_logger
from dotenv import load_dotenv

# teste
from yaml import safe_load
from json import load, dump

with open("src/config.yaml", "r") as f:
    config = safe_load(f)

data_path = f"{config['paths']['examples_dir']}/exemplo_musica.json"

with open(data_path, 'r', encoding='utf-8') as d:
    data = load(d)

load_dotenv()

logger = get_logger("analysis")

def generate_analysis(dimensao_nome, secao) -> str:

    agent = Agent(model=Groq(id='openai/gpt-oss-20b'),
    description="Você é um analista de dados especialista no âmbito acadêmico",
    instructions=[
        "Sempre responda em português",
        "Se atenha exclusivamente aos dados e ao que eles querem dizer",
        "Analise especificamente de acordo com o dado, não seja generalista",
        "Considere todo o contexto acadêmico e o modelo de balanced scorecard ao produzir a análise",
        "Não forneça recomendações"
        ],
    expected_output="Retorne uma resposta enxuta, de 2 a 4 linhas"
)
    
    response = agent.run(
        f"""Faça uma análise para a dimensao {dimensao_nome}, seção {secao}, seguindo uma estrutura parecida com: O índice de ocupação dos egressos é moderado,
        indicando que pouco mais da metade dos formados está inserida no mercado de trabalho. O resultado aponta a necessidade de ampliar
        o vínculo entre a formação acadêmica e as oportunidades profissionais, especialmente no contexto local e regional.""")

    return response.content

def save_analysis_to_json(data):
    for i, dimensao in enumerate(data['dimensoes']):
        logger.info(f"Gerando análise para dimensão {dimensao['nome']}")

        for j, secao in enumerate(data['dimensoes'][i]['secoes']):
            logger.info(f"Gerando análise para seção {secao['titulo']}")
            response = generate_analysis(dimensao['nome'], secao)
            data['dimensoes'][i]['secoes'][j]['analise'] = response

    
    data_save_path = f"{config['paths']['examples_dir']}/exemplo_musica_analise.json"


    with open(data_save_path, 'w', encoding='utf-8') as file:
        dump(data, file, indent=4, ensure_ascii=False)


save_analysis_to_json(data)