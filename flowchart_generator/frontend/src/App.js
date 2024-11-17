import React, { useState, useEffect } from 'react';
import mermaid from 'mermaid';
import './App.css';  // Assuming you will add CSS here

function App() {
  const [input, setInput] = useState('');
  const [mermaidCode, setMermaidCode] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);

    try {
      const response = await fetch("http://localhost:8000/generate_flowchart", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          input: input,
        }),
      });

      const data = await response.json();
      setMermaidCode(data.mermaid_code);
      mermaid.contentLoaded();  // Re-render Mermaid after receiving new code
    } catch (error) {
      console.error('Error generating flowchart:', error);
    }

    setIsLoading(false);
  };

  useEffect(() => {
    // Initialize Mermaid when the component is mounted
    mermaid.initialize({
      startOnLoad: true, // Automatically render diagrams on page load
    });
  }, []);

  return (
    <div className="App">
      <h1>Flowchart Generator</h1>
      <form onSubmit={handleSubmit}>
        <textarea 
          value={input} 
          onChange={handleChange} 
          placeholder="Enter your prompt" 
          rows="5"
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Generating...' : 'Generate Flowchart'}
        </button>
      </form>
      
      {/* Section to display Mermaid Code */}
      {mermaidCode && (
        <div className="mermaid-code-section">
          <h2>Mermaid Code</h2>
          <pre>{mermaidCode.content}</pre> {/* Access content key */}
        </div>
      )}

      {/* Section to display the Mermaid Chart */}
      {mermaidCode && (
        <div className="mermaid-container">
          <h2>Rendered Flowchart</h2>
          <div className="mermaid">
            {mermaidCode.content} {/* Access content key */}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
