from game import Game

def get_user_menu_choice():
    """Asks for the menu choice up until the user gives a correct one."""
    while True:
        print("\n----Menu----")
        print("1. Play a new game")
        print("2. Show scores ")
        print("3. Quit ")
        
        valid_options = ["1","2","3"]
        choice = input("Choose (1-3): ").strip()
        if choice in valid_options:
            return choice
        else:
            print("Invalid choice. Please enter 1,2 or 3")

def print_results(results:dict):
    wins = results.get("win", 0)
    losses = results.get("loss", 0)
    draws = results.get("draw", 0)

    print("\nGame Results:")
    print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "1":
            print("Starting a new game...")
            game = Game()
            outcome = game.play().lower()
            results[outcome] = results.get(outcome, 0) + 1
        elif choice == "2":
            print_results(results)
        else:
            print_results(results)
            print("Thank you for playing!")
            break
            

if __name__ == "__main__":
    main()       

