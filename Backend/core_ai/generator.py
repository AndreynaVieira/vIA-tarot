import google.generativeai as genai # type: ignore
from dotenv import load_dotenv # type: ignore
import os 

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
# Config da IA
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

def gerar_analise_ia(mapa_astral: dict) -> str:
    """
    Usa um LLM (Gemini) para gerar uma análise de personalidade integrada
    a partir dos dados do mapa astral.
    """
    print("Conectando com a IA para gerar sua análise personalizada...")
    
    dados_formatados = []
    for nome, dados in mapa_astral.items():
        if nome == 'ascendente':
            dados_formatados.append(f"- {dados.get('planeta', 'N/A')}: {dados.get('signo', 'N/A')}")
        else:
            dados_formatados.append(f"- {dados.get('planeta', 'N/A')}: {dados.get('signo', 'N/A')} na Casa {dados.get('casa', 'N/A')}")
    
    string_dados = "\n".join(dados_formatados)
    
    prompt = f"""
    Aja como um astrólogo experiente, didático e acolhedor. Use uma linguagem fácil de entender e calorosa, pode utilizar emojis, mas não exagere. Traga os pontos positivos e pontos fortes de cada elemento.
    Aja como um astrólogo mestre, com um tom de voz sábio e encorajador.
    Sua tarefa é escrever uma análise de mapa astral profunda e integrada com base nos dados abaixo.

    DADOS DO MAPA:
    {string_dados}

    INSTRUÇÕES PARA A ANÁLISE:
    1.  **Parágrafo de Abertura:** Comece com uma saudação calorosa. Apresente o "Big 3" (Sol, Lua e Ascendente) como os pilares da personalidade.
    2.  **Análise do Eu (Sol e Ascendente):** Analise a identidade do Sol. Em seguida, explique como o signo do Ascendente colore a forma como a energia do Sol é expressa no mundo. Use a Casa do Sol para indicar em que área da vida essa identidade mais brilha.
    3.  **Análise Emocional (Lua):** Analise a natureza emocional da Lua e como ela se manifesta na área da vida indicada pela Casa da Lua.
    4.  **Análise da Mente e Ação (Mercúrio e Marte):** Analise Mercúrio e Marte em conjunto. Explique como a pessoa pensa e se comunica (Mercúrio na sua Casa) e como ela age e direciona sua energia (Marte na sua Casa).
    5.  **Análise do Amor e Expansão (Vênus e Júpiter):** Descreva o que a pessoa valoriza no amor (Vênus na sua Casa) e onde ela encontra sorte e crescimento (Júpiter na sua Casa).
    6.  **O Grande Mestre (Saturno):** Explique qual é a grande lição ou área de amadurecimento indicada por Saturno e sua casa.
    7.  **Parágrafo de Fechamento:** Termine com uma mensagem inspiradora sobre como usar esses conhecimentos para o autodesenvolvimento.

    IMPORTANTE: Escreva em português do Brasil. Crie um texto fluido e conectado, não apenas uma lista de descrições. Mostre como as energias interagem.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Ocorreu um erro ao contatar a IA: {e}"
    
def responder_pergunta_ia(mapa_astral: dict, pergunta: str, historico: list) -> str:
    """
    Usa o mapa astral e o histórico da conversa como contexto para responder 
    a uma pergunta específica do usuário.
    """
    print(f"Enviando pergunta para a IA com histórico: {pergunta}")

    dados_formatados = []
    for nome, dados in mapa_astral.items():
        if nome == 'ascendente':
            dados_formatados.append(f"- {dados.get('planeta', 'N/A')}: {dados.get('signo', 'N/A')}")
        else:
            dados_formatados.append(f"- {dados.get('planeta', 'N/A')}: {dados.get('signo', 'N/A')} na Casa {dados.get('casa', 'N/A')}")
    
    string_dados = "\n".join(dados_formatados)
    
    # Formata o histórico para incluir no prompt
    string_historico = "\n".join([f"- {msg['role']}: {msg['content']}" for msg in historico])

    prompt = f"""
    Você é um astrólogo-assistente. Um usuário já tem o mapa astral dele e agora está conversando com você para tirar dúvidas.
    
    **CONTEXTO (O MAPA DO USUÁRIO):**
    {string_dados}

    **HISTÓRICO RECENTE DA CONVERSA:**
    {string_historico}

    **NOVA PERGUNTA DO USUÁRIO:**
    "{pergunta}"

    **SUA TAREFA:**
    Com base no mapa do usuário e no histórico da conversa, responda à NOVA PERGUNTA de forma direta, clara e acolhedora. Se a pergunta for um acompanhamento de uma resposta anterior, use o histórico para entender o contexto. Seja breve e foque na pergunta feita. Use português do Brasil.
    """

    try:
        response = model.generate_content(prompt)
        if response.parts:
            return response.text
        else:
            return "A IA não conseguiu processar sua pergunta. Tente reformulá-la."
    except Exception as e:
        return f"Ocorreu um erro ao contatar a IA: {e}"



