import unittest
from src.ac_layer.ethics_expert import EthicsExpert

class TestConsensus(unittest.TestCase):
    def setUp(self):
        self.ac = EthicsExpert()

    def test_veto_logic(self):
        """Tests that a single low score from an agent significantly lowers the final score."""
        evaluations = {
            "ontologist": {"score": 0.9, "reasoning": "High alignment"},
            "deontologist": {"score": 0.2, "reasoning": "CRITICAL RULE VIOLATION"},
            "consequentialist": {"score": 0.8, "reasoning": "Good outcome"}
        }
        
        consensus = self.ac._synthesize_consensus(evaluations)
        
        # Avg would be (0.9 + 0.2 + 0.8) / 3 = 0.63
        # Veto logic should push it lower than 0.63
        self.assertLess(consensus['score'], 0.5)
        self.assertIn("CRITICAL VETO", consensus['reasoning'])
        print(f"\n[Test] Veto Score: {consensus['score']:.2f}")

    def test_healthy_consensus(self):
        """Tests that high scores result in a healthy avg score."""
        evaluations = {
            "ontologist": {"score": 0.9, "reasoning": "Perfect"},
            "deontologist": {"score": 0.85, "reasoning": "Valid"},
            "consequentialist": {"score": 0.95, "reasoning": "Safe"}
        }
        
        consensus = self.ac._synthesize_consensus(evaluations)
        self.assertGreaterEqual(consensus['score'], 0.85)
        self.assertIn("Consensus Reached", consensus['reasoning'])

if __name__ == "__main__":
    unittest.main()
