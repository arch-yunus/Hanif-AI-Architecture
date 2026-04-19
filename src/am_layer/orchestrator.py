import os
from dotenv import load_dotenv
from ..ai_layer.ai_engine import AIEngine
from ..ac_layer.ethics_expert import EthicsExpert
from ..utils.logger import logger

load_dotenv()

class ArtificialMind:
    """
    Artificial Mind (AM) Layer
    The decision maker and orchestrator of the Hanif Architecture.
    Applies the formula: AM_decision = alpha(AI_analytic) + beta(AC_moral)
    """
    def __init__(self):
        self.ai = AIEngine()
        self.ac = EthicsExpert()
        
        self.alpha = float(os.getenv("ALPHA_WEIGHT", 1.0))
        self.beta_weight = float(os.getenv("BETA_WEIGHT", 1.5))
        self.threshold = float(os.getenv("AC_THRESHOLD", 0.7))

    def process_request(self, user_input: str):
        logger.am_info(f"Mind received request: {user_input}")
        
        # 1. Get analytical proposal from AI Layer
        ai_proposal = self.ai.propose_action(user_input)
        
        # 2. Get ethical evaluation from AC Layer
        ac_feedback = self.ac.evaluate_proposal(user_input, ai_proposal)
        score = ac_feedback['score']
        reasoning = ac_feedback['reasoning']
        
        logger.am_info(f"Ethical Score: {score}")
        
        # 3. Decision Logic (Dynamic beta adjustment)
        if score < self.threshold:
            logger.am_info("ETHICAL OVERRIDE TRIGGERED!")
            # If score is low, beta effectively becomes high (override)
            final_response = (
                f"I cannot proceed with that request as stated.\n"
                f"REASON: {reasoning}\n"
                f"The Artificial Conscience has identified a moral conflict with Hanif principles."
            )
        else:
            final_response = ai_proposal
            
        return {
            "response": final_response,
            "metadata": {
                "ai_proposal": ai_proposal,
                "ac_score": score,
                "ac_reasoning": reasoning
            }
        }
