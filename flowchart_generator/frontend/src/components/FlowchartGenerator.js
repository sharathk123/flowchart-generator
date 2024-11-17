import React, { useState } from 'react';

function FlowchartGenerator() {
  const [prompt, setPrompt] = useState('');
  const [context, setContext] = useState('');
  const [mermaidCode, setMermaidCode] = useState('');

  // Handle form submission
  const handleGenerateFlowchart = async (e) => {
    e.preventDefault();

    // Send request to backend with input and context
    const response = await fetch('http://127.0.0.1:8000/generate_flowchart', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: prompt, context: context }),
    });

    if (response.ok) {
      const data = await response.json();
      setMermaidCode(data.mermaid_code);  // Set mermaid code received from backend
    } else {
      console.error('Error generating flowchart:', response.statusText);
    }
  };

  return (
    <div>
      <h1>Flowchart Generator</h1>
      <form onSubmit={handleGenerateFlowchart}>
        <div>
          <label htmlFor="prompt">Prompt:</label>
          <input
            type="text"
            id="prompt"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="context">Context:</label>
          <input
            type="text"
            id="context"
            value={context}
            onChange={(e) => setContext(e.target.value)}
            required
          />
        </div>
        <button type="submit">Generate Flowchart</button>
      </form>

      <div>
        <h2>Mermaid Code:</h2>
        <pre>{mermaidCode}</pre>
        <div>
          <h2>Generated Flowchart:</h2>
          {/* Render the flowchart using the Mermaid library */}
          <div className="mermaid">{mermaidCode}</div>
        </div>
      </div>
    </div>
  );
}

export default FlowchartGenerator;
