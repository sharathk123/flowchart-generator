import os
import logging
from dotenv import load_dotenv
from typing import Dict, Any

# Setup logger for utils
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env
def load_environment():
    try:
        load_dotenv()  # Loads the .env file
        logger.info("Environment loaded successfully.")
    except Exception as e:
        logger.error(f"Error loading environment: {e}")
        raise

# Function to get the GROQ_API_KEY from environment
def get_groq_api_key() -> str:
    try:
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            logger.error("GROQ_API_KEY is not set in environment variables!")
            raise ValueError("GROQ_API_KEY is missing.")
        return groq_api_key
    except Exception as e:
        logger.error(f"Error retrieving GROQ_API_KEY: {e}")
        raise

# Initialize session history storage
class MessageHistoryHandler:
    def __init__(self, store: Dict[str, Any]):
        self.store = store

    def get_history(self, session_id: str):
        if session_id not in self.store:
            self.store[session_id] = []
        return self.store[session_id]

    def add_to_history(self, session_id: str, user_input: str, model_output: str):
        history = self.get_history(session_id)
        history.append({"user_input": user_input, "model_output": model_output})
