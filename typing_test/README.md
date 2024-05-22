# Speed Typing Test

  The Speed Typing Test is a Python program designed to measure the user's typing speed and accuracy by typing a specific text.

# Usage
Upon launching the program, you will be greeted with a start screen message prompting you to press any key to begin the typing speed test. Once you initiate the test, the target text will appear on the screen, and you can start typing. As you type, the program will display the target text along with your input, highlighting correct characters in green and incorrect characters in red. Once you complete typing the target text, the program will show you how many seconds it took for you to finish typing.
# Functions

# 1. start_screen
This function displays a welcome message before the typing speed test begins.
Parameters: std_screen (Standard screen object representing the screen)
Functionality:
Clears the screen.
Displays the welcome message.


# 2. display_text
This function displays the target text and the user's input text, highlighting correct characters in green and incorrect characters in red.

Parameters: std_screen (Standard screen object representing the screen), target (The target text), current (The user's input text), abs_time (Elapsed time)

Functionality:
Prints the target text and the user's input text on the screen.
Highlights correct and incorrect characters with colors.


# 3. time_test
This function performs the typing speed test, measuring how long it takes for the user to complete the target text.

Parameters: std_screen (Standard screen object representing the screen)

Functionality:
Displays the target text and the user's input text on the screen.
Monitors the user's input and prints an updated version of correct characters and elapsed time on the screen.
Stops the test when the user completes the target text and calculates the elapsed time.

Return Value: main_time (The time elapsed for the user to complete the target text)

# 4. main
This function initiates the typing speed test and displays the result after the user completes the test.

Parameters: std_screen (Standard screen object representing the screen)

Functionality:
Displays the welcome message by calling the start_screen function.
Performs the typing speed test by calling the time_test function.
Displays the result after the user completes the test and provides the option to restart or exit.
