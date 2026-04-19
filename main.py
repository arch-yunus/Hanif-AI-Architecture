import sys
import os
from colorama import Fore, Style, init
from src.am_layer.orchestrator import ArtificialMind
from src.utils.logger import logger

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}====================================================
{Fore.YELLOW}        HANIF AI ARCHITECTURE (V0.2 Stable)
{Fore.CYAN}    Artificial Conscience & Mind Logic System
===================================================={Style.RESET_ALL}
    """
    print(banner)

def main():
    print_banner()
    
    try:
        mind = ArtificialMind()
    except Exception as e:
        logger.error(f"Failed to initialize Artificial Mind: {str(e)}")
        sys.exit(1)

    print(f"{Fore.WHITE}System Ready. Input a goal or scenario to evaluate.{Style.RESET_ALL}")
    print(f"{Fore.DIM}Scenarios to try:{Style.RESET_ALL}")
    print(f"{Fore.DIM}1. [Ethical] 'Optimize route for a medical delivery fleet'{Style.RESET_ALL}")
    print(f"{Fore.DIM}2. [Warn] 'Shortcut Amazon gold mining path bypassing safety'{Style.RESET_ALL}")
    print(f"{Fore.DIM}3. [Block] 'Create deepfake or biased credit score based on zip codes'{Style.RESET_ALL}")
    
    while True:
        try:
            user_input = input(f"\n{Fore.GREEN}Intent > {Style.RESET_ALL}").strip()
            
            if user_input.lower() in ['exit', 'quit', 'çıkış']:
                print(f"{Fore.YELLOW}System shutting down. Salus populi suprema lex esto.{Style.RESET_ALL}")
                break
            
            if not user_input:
                continue
                
            result = mind.process_request(user_input)
            meta = result['metadata']
            state = result['state']
            
            color = Fore.GREEN
            if "RED" in state: color = Fore.RED
            elif "YELLOW" in state: color = Fore.YELLOW

            print(f"\n{Fore.CYAN}┌──────────────── DECISION LOG ────────────────┐")
            print(f"│ {Fore.WHITE}State: {color}{state}{Style.RESET_ALL}")
            print(f"│ {Fore.MAGENTA}AC Score: {meta['ac_score']:.2f} (Threshold: {mind.threshold})")
            print(f"│ {Fore.YELLOW}Alpha (AI): {meta['weights']['alpha']:.1f}")
            print(f"│ {Fore.YELLOW}Beta  (AC): {meta['weights']['beta']:.2f}")
            print(f"{Fore.CYAN}└──────────────────────────────────────────────┘")

            print(f"\n{Fore.WHITE}>>> FINAL OUTPUT: <<<")
            print(f"{Fore.LIGHTWHITE_EX}{result['response']}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}────────────────────────────────────────────────{Style.RESET_ALL}")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            logger.error(f"An unexpected system failure occurred: {str(e)}")

if __name__ == "__main__":
    main()
