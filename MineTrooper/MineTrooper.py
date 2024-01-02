from Game import Game

def print_menu():
    print("1. Display Board")
    print("2. Open Cell")
    print("3. Check Bank Balance")
    print("4. Quit")

if __name__ == "__main__":
    game = Game(rows=3, columns=3, probability_mine=20, initial_balance=100)

    while True:
        print("\n--- Minesweeper Game ---")
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            game.display_board()
        elif choice == '2':
            row = int(input("Enter the row number: "))
            col = int(input("Enter the column number: "))
            game.open_cell(row, col)
        elif choice == '3':
            print(f"Your current bank balance is: {game.get_bank_balance()}")
        elif choice == '4':
            print(f"\nGame Over. Your final bank is {game.get_bank_balance()}.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
