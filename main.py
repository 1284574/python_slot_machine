import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
# global constant for number of lines in slot machine

ROWS = 3
COLS = 3

# dictionary to count the number of times each symbol appears in columns
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# value of each symbol 
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# function to check if user won

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines




def get_slot_machine_spin(rows, cols, symbols):
    # randomly select a symbol from the list of symbols
    all_symbols = []
    #  symbol = key, symbol_count = value
    for symbol, symbol_count in symbols.items():
        # _ = anonymous variable
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        # splice : = copy of list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" | ")
            else:
                print(column[row], end =" | ")
        
        print()


# function to record user input and create deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        # check if amount is a number
        # isDigits returns true if amount is a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount



def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        # check if amount is a number
        # isDigits returns true if amount is a number
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
   # print(balance, lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        anwser = input("Press enter to play (q to quit).")
        if anwser == "q":
            break
        balance += spin(balance)
    
    print(f"You are left with ${balance}")

main()