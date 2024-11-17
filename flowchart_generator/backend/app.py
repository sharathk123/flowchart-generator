from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from generate_flowchart import create_flowchart_generation_chain
import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Initialize FastAPI app
app = FastAPI()

# Allow CORS from your frontend (adjust the origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow the frontend to communicate with the backend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Request model for input
class FlowchartRequest(BaseModel):
    input: str  # The prompt text input from the user

# Response model for Mermaid code output
class MermaidResponse(BaseModel):
    mermaid_code: str  # The generated Mermaid code to display as a flowchart

# Initialize the flowchart generation chain once
generate_flowchart_chain = create_flowchart_generation_chain()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Flowchart Generator API!"}

# Dummy function to simulate flowchart generation
def generate_flowchart(input_text):
    try:
        # Simulating a model output structure with 'role' and 'content' keys
        mermaid_code = f"""
        graph TD;
            A[Start] --> B{{{input_text}}}
            B --> C[Action]
            C --> D[End]
        """
        return {"role": "assistant", "content": mermaid_code}
    except Exception as e:
        logger.error(f"Error generating flowchart: {e}")
        raise
    
@app.post("/generate_flowchart")
async def generate_flowchart_endpoint(request: FlowchartRequest):
    try:
        # Extract the input text from the request
        input_text = request.input
        
        # Call the flowchart generation function with session_id and input_text
        mermaid_code = generate_flowchart(input_text)  # No await here

        # Return the response as a JSON object
        return JSONResponse(content={"mermaid_code": mermaid_code})
        
    except Exception as e:
        logger.error(f"Error generating flowchart: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")