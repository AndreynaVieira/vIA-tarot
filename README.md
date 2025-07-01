# 🔮 Hub Astrológico com IA

Uma aplicação web full-stack que gera e interpreta mapas astrais personalizados, combinando um backend em Python (FastAPI) com um frontend interativo em React e o poder da Inteligência Artificial Generativa do Google (Gemini).



## 📜 Descrição

Este projeto é uma plataforma astrológica completa que oferece aos usuários uma janela para o autoconhecimento. A aplicação permite a geração de um mapa astral natal detalhado a partir de dados de nascimento (data, hora e local). A partir desses dados, uma análise profunda e única é gerada por uma Inteligência Artificial, interpretando as principais posições planetárias e suas interações.

Além da análise inicial, o projeto conta com um chatbot interativo, permitindo que o usuário "converse" sobre seu mapa e tire dúvidas específicas, recebendo respostas contextuais geradas pela IA.

## 🏛️ Arquitetura da Aplicação

Este projeto é construído sobre uma arquitetura Full-Stack moderna, separando as responsabilidades entre o backend e o frontend para maior organização e escalabilidade.

* **Backend (A "Cozinha" 🍳):**
    * Desenvolvido em **Python** com o framework **FastAPI**.
    * Responsável por toda a lógica de negócio: receber os dados, utilizar a biblioteca `flatlib` para os cálculos astrológicos precisos, conectar-se à API do Google Gemini para gerar as análises e respostas do chat, e expor os resultados através de uma API RESTful.

* **Frontend (O "Salão" 🍽️):**
    * Desenvolvido em **JavaScript** com a biblioteca **React** (utilizando Vite como ferramenta de build).
    * Responsável por toda a experiência do usuário: renderizar a interface gráfica, coletar os dados do usuário através de um formulário interativo, fazer chamadas de API para o backend e exibir os resultados de forma bonita e legível.

As duas partes rodam em servidores independentes e se comunicam através de requisições HTTP.

## ✨ Principais Funcionalidades

- **Cálculo de Mapa Astral:** Utiliza a `flatlib` para calcular com precisão as posições dos 7 planetas clássicos e do Ascendente, incluindo as casas astrológicas.
- **Análise Gerada por IA:** Integra-se com a API do Google Gemini (`gemini-2.5-flash`) para gerar análises de personalidade únicas e coesas.
- **Chatbot Interativo:** Permite que o usuário faça perguntas de acompanhamento sobre seu mapa, com respostas contextuais geradas pela IA.
- **Interface Web Moderna:** Construído com React para uma experiência de usuário rica e interativa.
- **Geocodificação:** Converte automaticamente o nome da cidade de nascimento em coordenadas (latitude e longitude) usando `geopy`.

## 🛠️ Tecnologias Utilizadas

* **Backend:**
    * Python 3.11
    * FastAPI & Uvicorn
    * Flatlib
    * Google Generative AI
    * Python-Dotenv
* **Frontend:**
    * React
    * Vite
    * JavaScript
    * CSS

## 🚀 Como Instalar e Executar

Para rodar este projeto, você precisará iniciar o servidor do backend e o servidor do frontend separadamente.

**1. Pré-requisitos:**
* **Python 3.11** instalado.
* **Node.js e npm** instalados.
* Uma **chave de API** para a IA Generativa do Google, que pode ser obtida no [Google AI Studio](https://aistudio.google.com/).

**2. Clone o Repositório:**
```bash
git clone [https://github.com/AndreynaVieira/vIA-Tarot]
cd nome-da-pasta-do-projeto
```

**3. Configuração do Backend:**
```bash
# Navegue até a pasta do backend
cd backend

# Crie e ative o ambiente virtual
py -3.11 -m venv venv
.\venv\Scripts\activate

# Instale as dependências do Python
pip install -r requirements.txt

# Crie o arquivo .env e adicione sua chave 
GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"

# Inicie o servidor do backend
uvicorn api:app --reload
```
*Deixe este terminal rodando.*

**4. Configuração do Frontend:**
*Abra um **novo terminal**.*
```bash
# Navegue até a pasta do frontend
cd frontend

# Instale as dependências do Node.js
npm install

# Inicie o servidor de desenvolvimento do React
npm run dev
```
*Deixe este segundo terminal rodando.*

**5. Acesse a Aplicação:**
Abra seu navegador e acesse a URL fornecida pelo servidor do frontend (geralmente `http://localhost:8000`).

---

