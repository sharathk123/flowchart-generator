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

