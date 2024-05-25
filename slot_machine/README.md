# Slot Machine Game
This is a simple slot machine game implemented in Python. The game allows you to deposit money, place bets on multiple lines, and spin the slot machine to potentially win more money based on the symbols that appear.

# Game Explanation

#  Symbol Frequency (symbl_count)
The symbl_count dictionary determines the frequency of each symbol in the slot machine. It controls how often each symbol appears.


- "A": 2 means there are 2 "A" symbols in the slot machine.

- "B": 4 means there are 4 "B" symbols in the slot machine.

- "C": 6 means there are 6 "C" symbols in the slot machine.

- "D": 8 means there are 8 "D" symbols in the slot machine.

The more frequent a symbol, the more likely it is to appear in a spin.

# Symbol Value (symbl_value)
The symbl_value dictionary assigns a value to each symbol. This value is used to calculate winnings when a line of symbols matches.

- "A": 5 means each "A" symbol on a winning line pays 5 units.

- "B": 4 means each "B" symbol on a winning line pays 4 units.

- "C": 3 means each "C" symbol on a winning line pays 3 units.

- "D": 2 means each "D" symbol on a winning line pays 2 units.

Higher value symbols are rarer, while lower value symbols are more common.

# How to Play
1- Deposit Money: The game starts by asking you to deposit money.

2- Choose Number of Lines to Bet On: You can choose to bet on 1 to 3 lines.

3- Place a Bet: You can place a bet amount between the minimum and maximum bet limits.

4- Spin the Slot Machine: The slot machine spins and displays the results.

5- Calculate Winnings: The game calculates any winnings based on the lines and symbols that appeared.

# Running the Game
To start the game, run the main function. It handles the game loop, allowing you to keep playing as long as you have a balance.

# Customization
You can customize the game by changing the rows, cols, symbl_count, and symbl_value variables.

# Still, stay away from gambling!
