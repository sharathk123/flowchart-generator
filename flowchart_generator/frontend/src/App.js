import React, { useState, useEffect, useRef } from 'react';
import mermaid from 'mermaid';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [mermaidCode, setMermaidCode] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const mermaidContainerRef = useRef(null);

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

  const handleClear = () => {
    setInput('');
    setMermaidCode('');
  };

  const handleDownload = () => {
    if (mermaidContainerRef.current) {
      const svgElement = mermaidContainerRef.current.querySelector('svg');
      if (svgElement) {
        // Create a canvas to render the SVG and export as PNG
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        const svgData = new XMLSerializer().serializeToString(svgElement);
        const img = new Image();

        img.onload = () => {
          canvas.width = img.width;
          canvas.height = img.height;
          ctx.drawImage(img, 0, 0);
          const dataUrl = canvas.toDataURL('image/png');
          const a = document.createElement('a');
          a.href = dataUrl;
          a.download = 'flowchart.png';
          a.click();
        };

        img.src = 'data:image/svg+xml;base64,' + btoa(svgData); // Convert SVG to base64 string
      }
    }
  };

  useEffect(() => {
    mermaid.initialize({
      startOnLoad: true,
    });
  }, []);

  useEffect(() => {
    if (mermaidCode) {
      mermaid.contentLoaded();  // Trigger re-render for Mermaid diagrams after code update
    }
  }, [mermaidCode]);

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
        <div className="button-container">
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Generating...' : 'Generate Flowchart'}
          </button>
          <button type="button" onClick={handleClear} disabled={isLoading}>
            Clear
          </button>
        </div>
      </form>

      {mermaidCode && (
        <div className="mermaid-code-section">
          <h2>Mermaid Code</h2>
          <pre>{mermaidCode}</pre>
        </div>
      )}

      {mermaidCode && (
        <div className="mermaid-container">
          <h2>Rendered Flowchart</h2>
          <div className="mermaid" ref={mermaidContainerRef}>
            {mermaidCode}
          </div>
          <div className="button-container">
            <button onClick={handleDownload}>Download as PNG</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
