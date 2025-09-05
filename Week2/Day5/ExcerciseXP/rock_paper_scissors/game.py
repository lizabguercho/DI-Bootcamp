import random 

class Game:
    """ Ask the user to select an item """
    def get_user_item(self):
        items = ["rock","paper","scissors"]
        
        while True: 
            user_item = input("Select an item(rock/paper/scissors): ").strip().lower()
            if not user_item: 
                print("Empty input. Please type something.")    
            elif user_item not in items:
                print("Invalid choice.Please choose rock, paper or scissors")
            else:
                return user_item               
    
    def get_computer_item(self):
        items = ["rock","paper","scissors"]
        computer_item = random.choice(items)
        return computer_item
    
    def get_game_result (self, user_item, computer_item):
        
        winning_against = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        if winning_against[user_item] == computer_item:
            return "Win"
        elif user_item == computer_item:
            return "Draw"
        else:
            return "Loss"
        

    def play(self):
        """Asks the player for an input and shows and returns the output of the game"""
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        game_outcome = self.get_game_result(user_choice, computer_choice)
        print(f"User's choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(f"Result : {str(game_outcome)}")
        return game_outcome
    


  
if __name__ == "__main__":
    game = Game()
    # game.play()
    # user_choice = self.get_user_item()



        