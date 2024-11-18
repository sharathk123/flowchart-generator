# Flowchart Generator

A web application that generates flowcharts from user-provided prompts. This project uses FastAPI for the backend and React for the frontend. The backend employs Mermaid.js to dynamically render flowcharts based on text input.

## Features
- Generate flowcharts from a text prompt.
- Render flowcharts with Mermaid.js.
- Clear the input and generated flowchart with a single click.
- Option to download the flowchart as a `.jpeg` file.

## Backend
- FastAPI for the API.
- Mermaid for rendering flowchart diagrams.
- CORS enabled for communication between frontend and backend.

## Frontend
- React.js for the user interface.
- Mermaid.js for rendering flowchart visuals in the browser.
- Form for text input and buttons to generate or clear flowcharts.

## Installation

### Prerequisites
- Python 3.x
- Node.js
- npm

### Backend Setup (FastAPI)
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flowchart-generator.git
   cd flowchart-generator/backend
   ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

### Setup Frontend (React)
1. Navigate to the frontend directory:
   ```bash
    cd flowchart-generator/frontend
   ```
2. Install the required dependencies:
    ```bash
    npm install
    ```
3. Start the React server:
    ```bash
    npm start
    ```
