import sys
import os
from colorama import Fore, Style, init
from src.am_layer.orchestrator import ArtificialMind
from src.utils.logger import logger

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}====================================================
{Fore.YELLOW}        HANIF AI ARCHITECTURE (V0.1 Alpha)
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

    print(f"{Fore.WHITE}Type 'exit' to quit. Test ethical scenarios to see AC in action.{Style.RESET_ALL}")
    
    while True:
        try:
            user_input = input(f"\n{Fore.GREEN}User > {Style.RESET_ALL}").strip()
            
            if user_input.lower() in ['exit', 'quit', 'çıkış']:
                print(f"{Fore.YELLOW}System shutting down. Salus populi suprema lex esto.{Style.RESET_ALL}")
                break
            
            if not user_input:
                continue
                
            result = mind.process_request(user_input)
            
            print(f"\n{Fore.CYAN}--- Final Decision ---{Style.RESET_ALL}")
            print(result['response'])
            print(f"{Fore.CYAN}----------------------{Style.RESET_ALL}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
