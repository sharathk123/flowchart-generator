import os
from pathlib import Path

project_name = "flowchart_generator"

list_of_files = [
    # Backend structure
    f"{project_name}/backend/__init__.py",
    f"{project_name}/backend/app.py",               # FastAPI main app
    f"{project_name}/backend/generate_flowchart.py", # Logic for generating Mermaid flowchart
    f"{project_name}/backend/utils.py",             # Utility functions
    f"{project_name}/backend/requirements.txt",     # Backend dependencies
    f"{project_name}/backend/.env",                 # Environment variables file
    f"{project_name}/backend/setup.py",             # Moved setup.py to the backend directory

    # Frontend structure
    f"{project_name}/frontend/package.json",        # Frontend package manager file
    f"{project_name}/frontend/public/index.html",   # HTML entry point for React
    f"{project_name}/frontend/src/App.js",          # Main React component
    f"{project_name}/frontend/src/index.js",        # React entry point
    f"{project_name}/frontend/src/components/Flowchart.js", # React component for rendering flowchart

    # Common project files
    f"{project_name}/README.md",                    # Project documentation
    f"{project_name}/.gitignore",                   # Git ignore for Python, Docker, etc.
    f"{project_name}/Dockerfile",                   # Dockerfile for containerization
    f"{project_name}/.dockerignore",                # Docker ignore to exclude unnecessary files
]

# Create the directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

# Add content to Dockerfile, .dockerignore, and .env files
with open(f"{project_name}/Dockerfile", "w") as f:
    f.write("""
# Use an official Python runtime as a parent image for backend
FROM python:3.9-slim AS backend

# Set the working directory in the container for backend
WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY backend/ /app/backend/

# Expose the port the backend app runs on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]

# Use an official Node.js runtime as a parent image for frontend
FROM node:16 AS frontend

# Set the working directory in the container for frontend
WORKDIR /app/frontend

# Install frontend dependencies
COPY frontend/package.json /app/frontend/
RUN npm install

# Copy the frontend code into the container
COPY frontend/ /app/frontend/

# Expose the port the frontend app runs on
EXPOSE 3000

# Command to run the React app
CMD ["npm", "start"]
""")

with open(f"{project_name}/.dockerignore", "w") as f:
    f.write("""
__pycache__
*.pyc
*.pyo
*.pyd
*.db
*.log
*.git
.env
frontend/node_modules
""")

with open(f"{project_name}/.env", "w") as f:
    f.write("""
# Add your environment variables here
FLASK_ENV=development
DATABASE_URL=your_database_url_here
SECRET_KEY=your_secret_key_here
""")

# Backend requirements.txt (Python dependencies)
with open(f"{project_name}/backend/requirements.txt", "w") as f:
    f.write("""
# FastAPI and ASGI server for the backend
fastapi>=0.95.0
uvicorn[standard]

# Data validation
pydantic

# Placeholder for machine learning or AI dependencies (if needed)
groq

# Development tools for testing and quality checks
pytest
black
flake8
-e .
""")

# Frontend package.json (React dependencies)
with open(f"{project_name}/frontend/package.json", "w") as f:
    f.write("""
{
  "name": "flowchart_generator",
  "version": "1.0.0",
  "main": "index.js",
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-scripts": "4.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
""")

# Frontend React files
with open(f"{project_name}/frontend/src/App.js", "w") as f:
    f.write("""
import React from 'react';
import './App.css';
import Flowchart from './components/Flowchart';

function App() {
  return (
    <div className="App">
      <h1>Flowchart Generator</h1>
      <Flowchart />
    </div>
  );
}

export default App;
""")

with open(f"{project_name}/frontend/src/index.js", "w") as f:
    f.write("""
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
""")

with open(f"{project_name}/frontend/src/components/Flowchart.js", "w") as f:
    f.write("""
import React from 'react';

function Flowchart() {
  return (
    <div>
      <h2>Flowchart will be rendered here</h2>
      {/* You can integrate Mermaid here for flowchart rendering */}
    </div>
  );
}

export default Flowchart;
""")

print(f"Project structure for '{project_name}' with backend and frontend created successfully.")
