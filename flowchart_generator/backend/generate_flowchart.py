import os
import logging
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from typing import Dict, Any
from dotenv import load_dotenv
from langchain.prompts.base import BasePromptTemplate

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env
def load_environment():
    try:
        load_dotenv()  # Loads the .env file
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            logger.error("GROQ_API_KEY is not set in environment variables!")
            raise ValueError("GROQ_API_KEY is missing.")
        logger.info("Environment loaded successfully.")
    except Exception as e:
        logger.error(f"Error loading environment: {e}")
        raise

# Initialize the ChatGroq model
def initialize_model() -> ChatGroq:
    try:
        model = ChatGroq(model="llama-3.1-70b-versatile", temperature=0.5)
        logger.info("Model initialized successfully.")
        return model
    except Exception as e:
        logger.error(f"Error initializing model: {e}")
        raise

# Create the generic Mermaid code generation prompt
def create_generic_mermaid_prompt() -> BasePromptTemplate:
    try:
        # Generic context for flowchart generation
        generic_context = """
        You are a flowchart generation assistant. Your task is to generate flowcharts in Mermaid syntax based on the provided instructions.
        The flowchart should outline the steps involved in a process, making sure that each step is clearly represented with arrows showing the flow.

        CONTEXT:
        The context will describe a process, and your task is to visualize it as a flowchart in Mermaid syntax.
        You will receive an input question asking for a flowchart, and your goal is to generate the corresponding Mermaid code.

        QUESTION: {input}

        YOUR ANSWER (Mermaid Code):
        """
        
        # Create the prompt template with the generic context
        mermaid_code_prompt = ChatPromptTemplate.from_messages(
            [("system", generic_context), MessagesPlaceholder(variable_name="chat_history"), ("human", "{input}")]
        )
        logger.info("Generic Mermaid code prompt created successfully.")
        return mermaid_code_prompt
    except Exception as e:
        logger.error(f"Error creating Mermaid code prompt: {e}")
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

# Create the flowchart generation chain
def create_flowchart_generation_chain():
    load_environment()
    model = initialize_model()
    store = {}
    history_handler = MessageHistoryHandler(store)

    try:
        mermaid_code_prompt = create_generic_mermaid_prompt()

        # Create the LLMChain with the model and the Mermaid code prompt
        question_answer_chain = LLMChain(
            llm=model,
            prompt=mermaid_code_prompt
        )

        logger.info("Flowchart generation chain created successfully.")

        def run_chain_with_history(session_id: str, input_text: str) -> str:
            chat_history = history_handler.get_history(session_id)
            output = question_answer_chain.run({"input": input_text, "chat_history": chat_history})
            
            # Return the response with proper structure
            response = {
                "role": "assistant",  # This is an example; adjust depending on the context
                "content": output     # The generated Mermaid code or response
            }
            
            history_handler.add_to_history(session_id, input_text, output)
            return clean_mermaid_code(response)

        return run_chain_with_history
    except Exception as e:
        logger.error(f"Error creating flowchart generation chain: {e}")
        raise

import re

def clean_mermaid_code(llm_response):
    # Remove the mermaid code block markers and any unwanted text
    mermaid_code = re.sub(r'```mermaid|```', '', llm_response)
    return mermaid_code.strip()

# Main method to test the flowchart generation
def main():
    try:
        # Initialize the flowchart generation chain
        flowchart_chain = create_flowchart_generation_chain()
        
        # Example input for generating a flowchart (could be anything like "employee onboarding", "order processing", etc.)
        input_text = "employee onboarding process"
        session_id = "session_1"  # A unique session ID
        
        # Prepare inputs as a dictionary
        inputs = {"session_id": session_id, "input_text": input_text}

        # Generate the flowchart using the chain
        mermaid_code = flowchart_chain(inputs)
        
        # Print the Mermaid code output
        print(f"Generated Mermaid Code:\n{mermaid_code}")

    except Exception as e:
        logger.error(f"Error in main method: {e}")

if __name__ == "__main__":
    main()
