import psutil
import time
import os

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
BOLD = '\033[1m'
END = '\033[0m'

def get_color(usage):
    if usage < 30:
        return GREEN
    elif usage < 60:
        return YELLOW
    else:
        return RED

def show_overall():
    cpu = psutil.cpu_percent(interval=1)
    color = get_color(cpu)
    print(f"\n{BOLD}OVERALL CPU:{END}")
    print(f"Usage: {color}{cpu:.1f}%{END}")

def show_freq():
    freq = psutil.cpu_freq()
    print(f"\n{BOLD}CPU FREQUENCY:{END}")
    if freq:
        print(f"Current: {freq.current:.0f} MHz")
        print(f"Max: {freq.max:.0f} MHz")
    else:
        print(f"{RED}Frequency info not available{END}")

def live_mode():
    print(f"\n{BOLD}Live Monitoring{END}")
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)            
            color = get_color(cpu)
            print(f"\rCPU Usage: {color}{cpu:.1f}% {END}    ", end="", flush=True)
    except KeyboardInterrupt:
        print(f"\n\n{GREEN}Stopped{END}")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{BLUE}{BOLD}=== CPU MONITOR ==={END}")
        print(f"{GREEN}1.{END} Show Overall CPU")
        print(f"{GREEN}2.{END} Show CPU Frequency")
        print(f"{RED}3.{END} Live Monitor")
        print(f"{BLUE}0.{END} Exit")
        print("-" * 30)

        choice = input("Enter your choice (0-3): ")
        if choice == '1':
            show_overall()
        elif choice == '2':
            show_freq()
        elif choice == '3':
            live_mode()
        elif choice == '0':
            print(f"{GREEN}Thank You!{END}")
            break
        else:
            print(f"{RED}Invalid choice{END}")

        if choice != '3' and choice != '0':
            input("\nPress Enter to Continue...")

if __name__ == "__main__":
    main()
