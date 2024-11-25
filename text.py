import time
import random
from datetime import datetime, timedelta
from colorama import init, Fore, Style
import itertools
import threading
import sys

# Initialize colorama
init(autoreset=True)

def animate_text(text, delay=0.1):
    """Function to animate a rotating text during loading."""
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    for _ in range(len(text) * 3):
        sys.stdout.write(f"\r{text} {next(spinner)}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\r' + ' ' * (len(text) + 2) + '\r')

def generate_signal(call_put):
    """Generate a random signal based on user input."""
    assets = ["BRLUSD", "USDCAD", "USDCHF", "USDINR", "USDJPY", "USDEGP", "USDINR", "USDNOK", "USDDZD", "USDZAR", "CADCHF", "FB", "USDMXN", "INTC", "USDPKR", "USDPHP"]
    
    # Filter directions based on user choice
    directions = []
    if call_put == "1":
        directions = ["CALL"]
    elif call_put == "2":
        directions = ["PUT"]
    else:
        directions = ["CALL", "PUT"]
    
    return f"{Fore.GREEN if directions[0] == 'CALL' else Fore.RED}{random.choice(assets)}-OTC - {random.choice(directions)}{Style.RESET_ALL}"

def display_banner(email):
    """Display the banner and user information."""
    print(Fore.CYAN + "=" * 60)
    print("                    FULETA BINARY                    ")
    print("=" * 60 + Style.RESET_ALL)
    print(f"{Fore.YELLOW}Telegram Official : https://t.me/Fuleta_Binary")
    print(f"Users Email acc   : {Fore.GREEN}{email}")
    print(f"{Fore.YELLOW}OTC Version       : 2.0")
    print(f"Timezone          : Your current timezone")
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    print()
    time.sleep(1)  # 1-second sleep after displaying banner

def display_loading():
    """Display loading and filtering phase with animations."""
    animate_text("Loading assets...")
    animate_text("Filtering Your Signals...")
    animate_text("Making Complete Now:")
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    print()
    time.sleep(1)  # Additional delay for a polished look

def main():
    # Display banner first
    email = input(Fore.CYAN + "Enter Your Email: " + Style.RESET_ALL)
    password = input(Fore.CYAN + "Enter Your Password: " + Style.RESET_ALL)
    time.sleep(1)  # Delay to make it look smooth after input

    display_banner(email)

    # User input for settings
    timeframe = input(Fore.YELLOW + "Enter Timeframe in Minutes: " + Style.RESET_ALL)
    accuracy = input(Fore.YELLOW + "Enter Accuracy (e.g., 84): " + Style.RESET_ALL)
    call_put = input(Fore.YELLOW + "Choose Option - 1 for CALL, 2 for PUT, 3 for BOTH: " + Style.RESET_ALL)
    time.sleep(1)  # Delay after taking inputs

    # Display loading after user inputs
    display_loading()
    
    # Current time for signal generation
    current_time = datetime.now()
    end_time = current_time + timedelta(hours=1)  # Generate signals for the next 1 hour

    # Randomly decide the number of signals between 8 and 10
    num_signals = random.randint(8, 10)
    signal_times = sorted([
        current_time + timedelta(minutes=random.randint(1, 60)) for _ in range(num_signals)
    ])

    # Generate and display signals
    print(Fore.MAGENTA + "Generated Signals List:" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    
    for signal_time in signal_times:
        signal = generate_signal(call_put)
        formatted_time = signal_time.strftime("%H:%M")
        print(f"{Fore.YELLOW}{formatted_time}{Style.RESET_ALL} - {signal}")
        time.sleep(1)  # Delay for effect

    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    
    # Exit option after signal generation
    exit_choice = input(Fore.GREEN + "\nPress 'E' to Exit or any other key to Restart: " + Style.RESET_ALL).lower()
    if exit_choice == 'e':
        print(Fore.RED + "\nExiting... Goodbye!" + Style.RESET_ALL)
        time.sleep(1)
        sys.exit()
    else:
        print(Fore.YELLOW + "\nRestarting the program...\n" + Style.RESET_ALL)
        time.sleep(1)
        main()  # Restart the program

if __name__ == "__main__":
    main()
