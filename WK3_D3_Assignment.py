# Final Exercise:

# Create a Move_Tutor Class that inherits from the Pokemon parent class.¶
# This class should have a list attribute (move_list) that holds pokemon moves which should be populated with an api call to the PokeApi moves section (just like we did with abilities and types in the Pokemon class example). Finally create a class method that teaches your pokemon up to 4 moves. This method should take in a user input to what move they would like to teach and do a membership inside the move_list. If the move exists inside the move_list the pokemon can learn that move and append to the final taught_moves list.

# grab all the names of the moves from the list and grab a giant list of the moves that the pokemon can learn
# take in user input that asks which move you want to teach your pokemon
# is that move inside that list?
# if not, then display 'can't learn that move'
# if they reach max moves, maybe a functionality that lets you replaces moves already learned
# grab move stats and save to a dictionary


import requests

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.types = []

class Move_Tutor(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.move_list = self.get_move_list()
        self.taught_moves = []

    def get_move_list(self):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}/")
        pokemon_data = response.json()
        move_list = [move['move']['name'] for move in pokemon_data['moves']]
        return move_list

    def show_move_list(self):
        print(f"Moves available to learn for {self.name.title()}:\n")
        for move in self.move_list:
            print(move)

    def show_learned_moves(self):
        print(f"{self.name.title()} learned the following moves:")
        for move in self.taught_moves:
            print(move)

    def teach_moves(self):
        print(f"Teaching moves to {self.name.title()}")
        while len(self.taught_moves) < 4:
            print("\nPlease choose from the following options:")
            print("\t1. Show available moves to learn")
            print("\t2. Show learned moves")
            print("\t3. Teach a move")
            print("\t4. Quit")

            choice = input("Select an option: ")

            if choice == '1':
                self.show_move_list()
            elif choice == '2':
                self.show_learned_moves()
            elif choice == '3':
                if len(self.taught_moves) == 4:
                    print(f"{self.name.title()} already knows 4 moves. {self.name.title()} can't learn more.")
                else:
                    move_to_teach = input("Enter a move to teach: ")
                    if move_to_teach in self.move_list and move_to_teach not in self.taught_moves:
                        self.taught_moves.append(move_to_teach)
                        print(f"{self.name} learned {move_to_teach}!")
                    elif move_to_teach in self.taught_moves:
                        print(f"{self.name} already knows {move_to_teach}.")
                    else:
                        print(f"{move_to_teach} is not an option for {self.name.title()}.")
            elif choice == '4':
                break
            else:
                print("Invalid option. Please choose again.")

pokemon_name = "Piplup"
tutor = Move_Tutor(pokemon_name)

while True:
    print(f"\nWhat would you like to do with {pokemon_name.title()}?")
    print("\t1. Show available moves to learn")
    print("\t2. Show learned moves")
    print("\t3. Teach moves")
    print("\t4. Quit")

    user_choice = input("Select an option: ")

    if user_choice == '1':
        tutor.show_move_list()
    elif user_choice == '2':
        tutor.show_learned_moves()
    elif user_choice == '3':
        tutor.teach_moves()
    elif user_choice == '4':
        print("Exiting game.")
        break
    else:
        print("Invalid option. Please choose again.")