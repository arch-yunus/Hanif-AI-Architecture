import os
import google.generativeai as genai
from dotenv import load_dotenv
from ..utils.logger import logger

load_dotenv()

class AIEngine:
    """
    Artificial Intelligence Layer (Analytic/Mechanical Engine)
    Gathers data, performs analysis, and proposes actions.
    """
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            logger.error("GEMINI_API_KEY not found in environment.")
            self.model = None
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')

    def propose_action(self, prompt: str):
        logger.ai_info(f"Analyzing prompt: {prompt[:50]}...")
        
        if not self.model:
            # Fallback mock for testing if no API key
            return f"Analytical response to: {prompt} (Mocked due to missing API key)"

        try:
            response = self.model.generate_content(
                f"You are the AI Layer of Hanif Architecture. Be analytical and efficient. "
                f"Analyze and provide a response for: {prompt}"
            )
            return response.text
        except Exception as e:
            logger.error(f"AI Engine failed: {str(e)}")
            return "AI Engine Error: Unable to process request."
