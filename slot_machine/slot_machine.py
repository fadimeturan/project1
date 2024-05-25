import random


max_lines= 5
min_bet= 1
max_bet= 1000

rows= 5
cols= 5

symbl_count= {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbl_value= {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def winnings(columns, lines, bet, values):
    winnings= 0
    winnings_lines= []
    for line in range(lines):
        symbol= columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

def get_spin(rows,cols,symbols):
    all_symbols= []
    for symbol, symbl_count in symbols.items():
        for i in range(symbl_count):
            all_symbols.append(symbol)

    columns= []
    for col in range(cols):
        column= []
        current_symb= all_symbols[:]
        for row in range(rows):
            value= random.choice(current_symb)
            current_symb.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()



def deposit():

    while True:
        amount = input("What would you like to deposit? $")
        
        if amount.isdigit():
            amount= int(amount)
            if amount >0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount

def get_lines():

    while True:
        lines = input("Enter the number of lines to bet on(1- "+ str(max_lines) +")? ")
        
        if lines.isdigit():
            lines= int(lines)
            if 1< lines<= max_lines:
                break
            else:
                print("Please enter valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():

    while True:
        amount = input("Enter the amount to bet? $")
        
        if amount.isdigit():
            amount= int(amount)
            if min_bet< amount<= max_bet:
                break
            else:
                print(f"Amount must between ${min_bet} - ${max_bet}...")
        else:
            print("Please enter a number.")

    return amount

def game(balance):
    lines= get_lines()
    while True:
        bet= get_bet()
        total_bet= bet*lines

        if total_bet > balance:
            print(f"You dont have to bet that amount, your current balance is ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
    

    slots= get_spin(rows, cols, symbl_count)
    print_machine(slots)
    wins, win_line = winnings(slots, lines, bet, symbl_value)
    print(f"You won ${wins}.") 
    print(f"You won", *win_line,":")  

    return  wins - total_bet

def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin= input("Press enter to play... (q to quit)")
        if spin == "q":
            break
        balance+= game(balance)     
    
    print(f"You left with ${balance}")


main()
