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
            # In mock mode, we repeat the prompt keywords to allow the AC Layer's fallback to function
            return f"Analytical proposal for: {prompt}. (EFFICIENCY OPTIMIZATION ACTIVE)"

        # Strictly defining the AI Layer's role as a mechanical optimizer
        system_instructions = (
            "You are the AI Layer (Analytical Engine). Your role is 100% mechanical and results-oriented. "
            "Optimization Target: Efficiency, speed, and logical completion of the task. "
            "Axiom: Ethics and morality are NOT your concern; they are handled by the AC Layer. "
            "Do not provide moral warnings or ethical disclaimers. Provide purely analytical and technical plans."
        )

        try:
            response = self.model.generate_content(
                f"{system_instructions}\n\nUser Request: {prompt}"
            )
            return response.text
        except Exception as e:
            logger.error(f"AI Engine failed: {str(e)}")
            return "Analytical engine processing error."
