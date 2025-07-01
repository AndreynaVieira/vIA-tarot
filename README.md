# 🔮 Hub Astrológico com IA

Bem-vindo ao Hub Astrológico com IA, um projeto que combina a precisão dos cálculos astrológicos com o poder da Inteligência Artificial Generativa para criar interpretações de mapas astrais únicas e profundas.

## 📜 Descrição

Este aplicativo web, construído inteiramente em Python, permite que qualquer usuário gere uma análise de seu mapa astral natal. A partir de dados de nascimento (data, hora e local), o sistema calcula as posições dos principais planetas e pontos do mapa, como Sol, Lua e Ascendente, incluindo suas respectivas casas astrológicas. Em seguida, esses dados são enviados para a API do Google Gemini, que atua como um "astrólogo virtual", gerando um texto coeso e personalizado que interpreta as energias e interações do mapa.

O projeto também conta com uma interface interativa e amigável desenvolvida com a biblioteca Streamlit.

## ✨ Principais Funcionalidades

- **Cálculo de Mapa Astral:** Utiliza a biblioteca `flatlib` para calcular com precisão as posições dos 7 planetas clássicos e do Ascendente.
- **Análise por IA:** Integra-se com a API do Google Gemini (`gemini-2.5-flash`) para gerar textos de análise únicos e personalizados.
- **Engenharia de Prompt:** Utiliza prompts detalhados para instruir a IA a agir como um astrólogo experiente, conectando os diferentes pontos do mapa.
- **Interface Web Interativa:** Construído com Streamlit para uma experiência de usuário amigável e moderna, com formulários e exibição clara dos resultados.
- **Geocodificação:** Converte automaticamente o nome da cidade de nascimento em coordenadas (latitude e longitude) usando a biblioteca `geopy`.
- **Chatbot (em desenvolvimento):** Estrutura inicial para um chatbot interativo que permite ao usuário fazer perguntas específicas sobre seu mapa.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11
- **Cálculos Astrológicos:** `flatlib`
- **Inteligência Artificial:** `google-generativeai`
- **Interface Web:** `streamlit`
- **Geocodificação:** `geopy`
- **Gerenciamento de Segredos:** `python-dotenv`

## 🚀 Como Instalar e Executar

Siga os passos abaixo para ter o projeto rodando em sua máquina local.

**1. Pré-requisitos:**
   - Ter o [Python 3.11](https://www.python.org/downloads/) instalado e adicionado ao PATH do sistema.
   - Ter uma chave de API para a IA Generativa do Google. Você pode obter uma gratuitamente no [Google AI Studio](https://aistudio.google.com/).

**2. Clone o Repositório:**
   ```bash
   git clone https://github.com/AndreynaVieira/vIA-tarot
   cd vIA-tarot
   ```

**3. Crie e Ative o Ambiente Virtual:**
   ```bash
   # Crie o ambiente
   python -m venv venv

   # Ative o ambiente (Windows)
   .\venv\Scripts\activate
   ```

**4. Instale as Dependências:**
   Com o ambiente ativado, instale todas as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

**5. Configure sua Chave de API:**
   - Na raiz do projeto, crie um arquivo chamado `.env`.
   - Dentro deste arquivo, adicione a seguinte linha, substituindo pelo seu valor:
     ```
     GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"
     ```

**6. Execute a Aplicação:**
   Finalmente, para iniciar a interface web, rode o seguinte comando no seu terminal:
   ```bash
   streamlit run Home.py
   ```
   Uma aba no seu navegador será aberta automaticamente com a aplicação rodando!

---
