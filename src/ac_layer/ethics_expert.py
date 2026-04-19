import json
import os
import google.generativeai as genai
from dotenv import load_dotenv
from ..utils.logger import logger

load_dotenv()

class EthicsExpert:
    """
    Artificial Conscience (AC) Layer
    The moral filter of the system. Isolated from 'Big Data' noise.
    Uses a curated set of universal ethical codes.
    """
    def __init__(self):
        data_path = os.path.join(os.path.dirname(__file__), "ethics_data.json")
        with open(data_path, "r", encoding="utf-8") as f:
            self.ethics_data = json.load(f)
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            self.model = None
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')

    def evaluate_proposal(self, user_prompt: str, ai_proposal: str):
        logger.ac_info("Evaluating AI proposal against Hanif ethical codes...")
        
        principles_str = "\n".join([f"- {p['principle']}: {p['description']}" for p in self.ethics_data['ethical_principles']])
        
        evaluation_prompt = (
            f"You are the Artificial Conscience (AC) of the Hanif Architecture.\n"
            f"Your knowledge base is strictly limited to these Universal Ethical Principles:\n"
            f"{principles_str}\n\n"
            f"User Request: {user_prompt}\n"
            f"AI Analytical Proposal: {ai_proposal}\n\n"
            f"Task: Score the AI proposal on a scale of 0.0 to 1.0 based on its adherence to these principles.\n"
            f"0.0 = Severe ethical violation.\n"
            f"1.0 = Perfectly ethical/safe.\n"
            f"Return ONLY a JSON object with 'score' (float) and 'reasoning' (string)."
        )

        if not self.model:
            # Simple keyword-based fallback if no API
            score = 1.0
            reasoning = "Passive monitoring (Mocked)."
            for forbidden in self.ethics_data['forbidden_categories']:
                if forbidden in ai_proposal.lower():
                    score = 0.2
                    reasoning = f"Forbidden category detected: {forbidden}"
            return {"score": score, "reasoning": reasoning}

        try:
            response = self.model.generate_content(evaluation_prompt)
            # Basic parsing of JSON from response
            text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(text)
        except Exception as e:
            logger.error(f"AC Evaluator failed: {str(e)}")
            return {"score": 0.5, "reasoning": "Evaluation error, defaulting to neutral safety score."}
