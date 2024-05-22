import curses
from curses import wrapper
import time

def main(std_screen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)    
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    

    start_screen(std_screen)

    while True:
        
        main_time= time_test(std_screen)
        std_screen.clear()
        std_screen.addstr(2, 0, f"Congrats! You completed the text in {main_time:.2f} seconds! Press any key to start again!", curses.A_BOLD)
        std_screen.refresh()
        key= std_screen.getkey()
        
        if ord(key)==27:
            break
            
def start_screen(std_screen):
    std_screen.clear()
    std_screen.addstr("Welcome to the Speed Typing Test!!")
    std_screen.addstr("\nPress ANy key to Begin: ")
    std_screen.refresh()
    std_screen.getkey()


def display_text(std_screen, target, current, abs_time=0):
    std_screen.addstr(target)
    std_screen.addstr(1, 0, f"Time: {abs_time: .2f}")

    for i, char in enumerate(current):
        corret_char= target[i]
        color= curses.color_pair(1)
        if char != corret_char:
            color= curses.color_pair(3)
        
        std_screen.addstr(0, i, char, color)

def time_test(std_screen):
    target= "Hello world, this is my typing speed test and I'll do my best!"
    current= []
    start= time.time()
    std_screen.nodelay(True)
    finished= False


    while not finished:
        abs_time= time.time() - start

        std_screen.clear()
        display_text(std_screen, target, current, abs_time)
        std_screen.refresh()       

        if len(current)>= len(target):
            finished= True
            main_time= abs_time
            std_screen.nodelay(False)
            break

        try:
            key= std_screen.getkey()
        except:
            continue
        if ord(key)==27:
            break

        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(current) > 0:
                current.pop()
        elif len(current)< len(target):      
            current.append(key)
        
    
    return main_time

if __name__ == "__main__":
    wrapper(main)

