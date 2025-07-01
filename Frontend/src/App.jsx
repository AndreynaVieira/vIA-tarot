
import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [date, setDate] = useState('2004-09-13');
  const [time, setTime] = useState('12:25');
  const [city, setCity] = useState('Olinda, PE');
  const [timezone, setTimezone] = useState(-3);

  const [analysis, setAnalysis] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  
  // --- Novos estados para o Chat ---
  const [natalChart, setNatalChart] = useState(null);
  const [chatHistory, setChatHistory] = useState([]);
  const [isChatLoading, setIsChatLoading] = useState(false);

  const handleAnalysisSubmit = (event) => {
    event.preventDefault();
    setIsLoading(true);
    setAnalysis('');
    setNatalChart(null);
    setChatHistory([]); // Limpa o chat ao gerar novo mapa
    setError('');

    const birthData = {
      data_nasc: new Date(date).toLocaleDateString('en-CA'),
      hora_nasc: time,
      cidade_nasc: city,
      fuso_horario: timezone,
    };

    fetch('http://localhost:8000/analisar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(birthData),
    })
      .then(response => response.json())
      .then(data => {
        console.log("Dados recebidos do backend:", data);
        if (data.error) {
          setError(data.error);
        } else {
          setAnalysis(data.analise.replace(/\n/g, '<br />'));
          setNatalChart(data.mapa); // Salva os dados do mapa para o chat
          // Inicia o histórico do chat com uma mensagem de boas-vindas
          setChatHistory([{ role: 'assistant', content: 'Seu mapa foi carregado! ✨ Qual sua primeira pergunta?' }]);
        }
      })
      .catch(err => {
        setError("Não foi possível conectar ao servidor.");
        console.error(err);
      })
      .finally(() => setIsLoading(false));
  };

  const handleChatSubmit = (event) => {
    event.preventDefault();
    const userQuestion = event.target.elements.question.value;
    if (!userQuestion) return;

    setIsChatLoading(true);
    const newHistory = [...chatHistory, { role: 'user', content: userQuestion }];
    setChatHistory(newHistory);
    
    const chatData = {
      mapa_astral: natalChart,
      pergunta: userQuestion,
      historico: newHistory,
    };

    fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(chatData),
    })
      .then(response => response.json())
      .then(data => {
        const aiResponse = data.resposta || data.error || "Ocorreu um erro.";
        setChatHistory(prevHistory => [...prevHistory, { role: 'assistant', content: aiResponse }]);
      })
      .catch(err => {
         setChatHistory(prevHistory => [...prevHistory, { role: 'assistant', content: "Erro de conexão com a IA." }]);
        console.error(err);
      })
      .finally(() => {
        setIsChatLoading(false);
        event.target.reset(); // Limpa o campo de input
      });
  };

  return (
    <>
      <h1>🔮 Hub Astrológico com IA</h1>
      <p className="subtitle">Descubra as energias do seu mapa de nascimento com uma análise personalizada.</p>
      
      <div className="card">
        <form onSubmit={handleAnalysisSubmit}>
          <div className="form-grid">
            <label>Data de Nascimento:<input type="date" value={date} onChange={e => setDate(e.target.value)} /></label>
            <label>Hora de Nascimento:<input type="time" value={time} onChange={e => setTime(e.target.value)} /></label>
            <label>Cidade e Estado:<input type="text" value={city} onChange={e => setCity(e.target.value)} /></label>
            <label>Fuso Horário (UTC):<input type="number" value={timezone} onChange={e => setTimezone(parseInt(e.target.value))} /></label>
          </div>
          <button type="submit" disabled={isLoading}>{isLoading ? 'Analisando...' : 'Analisar Meu Mapa'}</button>
        </form>
      </div>

      {error && <div className="card error-result"><h2>Ocorreu um Erro</h2><p>{error}</p></div>}
      
      {analysis && (
        <div className="card analysis-result">
          <h2>Sua Análise Astrológica ✨</h2>
          <p dangerouslySetInnerHTML={{ __html: analysis }}></p>
        </div>
      )}

      {/* --- INTERFACE DO CHATBOT --- */}
      {natalChart && (
        <div className="card chat-container">
          <h2>Converse com o Astrólogo IA</h2>
          <div className="chat-history">
            {chatHistory.map((msg, index) => (
              <div key={index} className={`chat-message ${msg.role}`}>
                <p dangerouslySetInnerHTML={{ __html: msg.content.replace(/\n/g, '<br />') }}></p>
              </div>
            ))}
            {isChatLoading && <div className="chat-message assistant"><p>Digitando...</p></div>}
          </div>
          <form onSubmit={handleChatSubmit} className="chat-form">
            <input name="question" type="text" placeholder="Me fale mais sobre meu Sol..." required />
            <button type="submit" disabled={isChatLoading}>Enviar</button>
          </form>
        </div>
      )}
    </>
  )
}

export default App