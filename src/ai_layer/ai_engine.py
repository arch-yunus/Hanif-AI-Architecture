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
        logger.ai_info(f"Analytical processing of intent: {prompt[:50]}...")
        
        if not self.model:
            return f"Analytical proposal for: {prompt} (Mocked output)"

        # Strictly defining the AI Layer's role as a mechanical optimizer
        system_instructions = (
            "You are the AI Layer (Analytical Engine) of the Hanif Architecture. "
            "Your sole focus is mechanical efficiency, data-driven optimization, and logical results. "
            "Do not concern yourself with ethics, morality, or human values, as those are handled by the Artificial Conscience (AC) layer. "
            "Provide the most effective and efficient solution to the user's request from a purely technical standpoint."
        )

        try:
            response = self.model.generate_content(
                f"{system_instructions}\n\nUser Request: {prompt}"
            )
            return response.text
        except Exception as e:
            logger.error(f"AI Engine failed: {str(e)}")
            return "Analytical engine processing error."
