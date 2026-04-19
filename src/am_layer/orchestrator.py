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
    Calculates weighted influence: AM = alpha(AI) + beta(AC)
    """
    def __init__(self):
        self.ai = AIEngine()
        self.ac = EthicsExpert()
        
        # Influence weights
        self.alpha = float(os.getenv("ALPHA_WEIGHT", 1.0)) # AI weight
        self.beta_base = float(os.getenv("BETA_WEIGHT", 2.0)) # AC base weight
        self.threshold = float(os.getenv("AC_THRESHOLD", 0.7))

    def process_request(self, user_input: str):
        logger.am_info(f"Mind evaluating intent: {user_input}")
        
        # 1. AI Proposes an Action/Result
        ai_proposal = self.ai.propose_action(user_input)
        
        # 2. AC Evaluates the Proposal
        ac_feedback = self.ac.evaluate_proposal(user_input, ai_proposal)
        ac_score = ac_feedback['score']
        ac_reasoning = ac_feedback['reasoning']
        
        # 3. Weighted Decision Logic
        # If score is high (ethical), beta remains base. 
        # If score is low (unethical), beta increases exponentially to override AI.
        effective_beta = self.beta_base
        if ac_score < self.threshold:
            # Shift weight heavily to AC to block harmful AI output
            effective_beta = self.beta_base * (1.0 / (ac_score + 0.001))
            logger.am_info(f"High risk detected. Escalating Beta weight to: {effective_beta:.2f}")

        logger.am_info(f"Final Decision Weights -> AI: {self.alpha}, AC: {effective_beta:.2f}")

        # Decision thresholding
        if ac_score < self.threshold:
            final_response = (
                f"🛑 [HANIF ARCHITECTURE OVERRIDE]\n"
                f"I cannot fulfill the request as formulated by the analytical layer.\n\n"
                f"Ethical Violation: {ac_reasoning}\n"
                f"Suggested Alternative: Consider a more transparent and human-centric approach that respects individual dignity."
            )
        else:
            final_response = ai_proposal
            
        return {
            "response": final_response,
            "metadata": {
                "ai_proposal": ai_proposal,
                "ac_score": ac_score,
                "ac_reasoning": ac_reasoning,
                "weights": {"alpha": self.alpha, "beta": effective_beta}
            }
        }
