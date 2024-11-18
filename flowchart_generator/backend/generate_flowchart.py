import os
import re
import logging
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
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

# Create the one-shot Mermaid code generation prompt
def create_one_shot_mermaid_prompt() -> BasePromptTemplate:
    try:
        one_shot_context = """
        You are a flowchart generation assistant. Your task is to generate flowcharts in Mermaid syntax based on the provided instructions.
        Follow these rules when generating Mermaid 11.4.0 compatible code. Don't include any instructions or styles except the Mermaid code.

        QUESTION: {input}

        YOUR ANSWER (Mermaid Code):
        """
        
        # Create the prompt template for one-shot usage
        one_shot_mermaid_code_prompt = ChatPromptTemplate.from_messages(
            [("system", one_shot_context), ("human", "{input}")]
        )
        logger.info("One-shot Mermaid code prompt created successfully.")
        return one_shot_mermaid_code_prompt
    except Exception as e:
        logger.error(f"Error creating one-shot Mermaid code prompt: {e}")
        raise

# Clean the Mermaid code to remove extra markers
def clean_mermaid_code(llm_response):
    # Remove the mermaid code block markers and any unwanted text
    mermaid_code = re.sub(r'```mermaid\s*|\s*```', '', llm_response)
    return mermaid_code.strip()

# Create the flowchart generation chain
def create_flowchart_generation_chain():
    load_environment()
    model = initialize_model()

    try:
        # Create the LLMChain with the one-shot prompt template
        one_shot_prompt = create_one_shot_mermaid_prompt()

        question_answer_chain = LLMChain(
            llm=model,
            prompt=one_shot_prompt
        )

        logger.info("Flowchart generation chain created successfully.")

        def run_chain(input_text: str) -> str:
            # Pass 'input' as key in the dictionary to match the prompt template
            output = question_answer_chain.run({"input": input_text})
            return clean_mermaid_code(output)

        return run_chain

    except Exception as e:
        logger.error(f"Error creating flowchart generation chain: {e}")
        raise

# Main method to test the flowchart generation
def main():
    try:
        # Initialize the flowchart generation chain
        flowchart_chain = create_flowchart_generation_chain()

        # Example input for generating a flowchart
        input_text = "employee onboarding process"

        # Generate the flowchart using the chain
        mermaid_code = flowchart_chain(input_text)

        # Print the Mermaid code output
        print(f"Generated Mermaid Code:\n{mermaid_code}")

    except Exception as e:
        logger.error(f"Error in main method: {e}")

if __name__ == "__main__":
    main()
