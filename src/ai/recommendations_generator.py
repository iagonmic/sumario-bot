"""
Gera recomendações para cada dimensão.
"""

from agno.agent import Agent
from agno.models.groq import Groq
from src.utils.logger import get_logger
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd


# teste
from yaml import safe_load
from json import load, dump

with open("src/config.yaml", "r") as f:
    config = safe_load(f)

data_path = f"{config['paths']['analysis_and_recommendation_dir']}/exemplo_musica_analise.json"

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
    expected_output="Retorne em texto corrido, até 300 caracteres"
)
    
    response = agent.run(
        f"""Forneça recomendações sobre a dimensão {dimensao_nome}, secao {secao}, seguindo uma estrutura parecida com: 
        Para fortalecer a inserção dos egressos no mercado de trabalho, é fundamental ampliar as parcerias com empresas, órgãos públicos e organizações sociais, bem como incentivar projetos de extensão e estágios que aproximem os estudantes da prática profissional. Além disso, a criação de mecanismos de acompanhamento dos egressos permite identificar áreas com baixa empregabilidade e ajustar a formação oferecida, garantindo maior alinhamento às demandas atuais do mercado.""")
    
    # Converte o texto em lista
    recomendacoes_texto = response.content
    '''
    recomendacoes_lista = [
        linha.strip().lstrip('- ').strip() 
        for linha in recomendacoes_texto.split('\n') 
        if linha.strip().startswith('-')
    ]
    '''
    
    return recomendacoes_texto

def save_recommendations_to_json(data_path, test=False):
    # ler arquivo
    with open(data_path, 'r', encoding='utf-8') as d:
        data = load(d)

    p = Path(data_path)

    # criar condição para incrementar recomendações do sara a partir dos dados
    if 'sara' in p.name:
        df_recom = get_recommendations(data_path)

    for n, programa in enumerate(data['programas']):
        print(programa)
        print(df_recom.head())
        break # teste ##################
    
        for i, dimensao in enumerate(programa['dimensoes']):
            #logger.info(f"Gerando recomendações para dimensão {dimensao['nome']}")

            for j, secao in enumerate(programa['dimensoes'][i]['secoes']):
                #logger.info(f"Gerando recomendações para seção {secao['titulo']}")
                response = generate_recommendations(dimensao['nome'], secao)
                programa['dimensoes'][i]['secoes'][j]['recomendacoes'] = response
        
        if test == True:
            if n == 0:
                break

    p = Path(data_path)

    data_save_path = p.with_name(f"{p.stem}_analise{p.suffix}")

    with open(data_save_path, 'w', encoding='utf-8') as file:
        dump(data, file, indent=4, ensure_ascii=False)

def get_recommendations(data_path):
    p = Path(data_path)
    df = pd.read_excel(p, sheet_name='Melhoria')
    df_mean = df.groupby(['PERIODO_LETIVO', 'PROGRAMA', 'SIGLA_PROGRAMA', 'SIGLA_CENTRO', 'DIMENSÃO'])['RESPOSTA'].mean().apply(lambda x: round(x*100, 2)).reset_index()
    df_sorted = df_mean.sort_values(by=['PERIODO_LETIVO', 'PROGRAMA', 'SIGLA_PROGRAMA', 'SIGLA_CENTRO', 'RESPOSTA'],
                    ascending=[True, True, True, True, False])
    
    return df_sorted


save_recommendations_to_json(data_path, test=True)