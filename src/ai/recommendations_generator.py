"""
Gera recomendações para cada dimensão.
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

data_path = f"{config['paths']['examples_dir']}/exemplo_musica_analise.json"

with open(data_path, 'r', encoding='utf-8') as d:
    data = load(d)

load_dotenv()

logger = get_logger("recommendations")

def generate_recommendations(dimensao_nome, secao) -> list:

    agent = Agent(model=Groq(id='openai/gpt-oss-20b'),
    description="Você é um analista de dados especialista no âmbito acadêmico",
    instructions=[
        "Sempre responda em português",
        "Sua tarefa é fornecer recomendações baseada na análise fornecida e aos dados, para que a reitoria que leia essas recomendações consiga tomar alguma atitude, seja de curto prazo ou longo prazo"
        "Se atenha a análise fornecida, juntamente aos dados e ao que eles querem dizer, não invente informações",
        "Analise especificamente de acordo com a análise, não seja generalista",
        "Considere todo o contexto acadêmico e o modelo de balanced scorecard ao produzir as recomendações"
        ],
    expected_output="Retorne em formato de bullet points, de 3 a 5 bullet points, sendo eles separados por -"
)
    
    response = agent.run(
        f"""Forneça recomendações sobre a dimensão {dimensao_nome}, secao {secao}, seguindo uma estrutura parecida com: 
        - Fortalecer parcerias com empresas, órgãos públicos e organizações sociais para a inserção de egressos.
        - Incentivar projetos de extensão e estágios que aproximem o estudante do mercado de trabalho.
        - Criar mecanismos de acompanhamento de egressos para identificar áreas de baixa empregabilidade e ajustar a formação profissional.""")
    
    # Converte o texto em lista
    recomendacoes_texto = response.content
    recomendacoes_lista = [
        linha.strip().lstrip('- ').strip() 
        for linha in recomendacoes_texto.split('\n') 
        if linha.strip().startswith('-')
    ]
    
    return recomendacoes_lista

def save_recommendations_to_json(data):
    for i, dimensao in enumerate(data['dimensoes']):
        logger.info(f"Gerando recomendações para dimensão {dimensao['nome']}")

        for j, secao in enumerate(data['dimensoes'][i]['secoes']):
            logger.info(f"Gerando recomendações para seção {secao['titulo']}")
            response = generate_recommendations(dimensao['nome'], secao)
            data['dimensoes'][i]['secoes'][j]['recomendacoes'] = response
    
    data_save_path = f"{config['paths']['examples_dir']}/exemplo_musica_recomendacao.json"

    with open(data_save_path, 'w', encoding='utf-8') as file:
        dump(data, file, indent=4, ensure_ascii=False)

save_recommendations_to_json(data)