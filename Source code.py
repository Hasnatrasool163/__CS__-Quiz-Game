import time
import random
from colorama import Fore, Style, init
import os
# Initialize colorama
init(autoreset=True)

exitto=f"{Fore.LIGHTRED_EX}"
exitto =r"""

                                                       c=====e
                                                            H
   ____________                                         _,,_H__
  (__((__((___()                                       //|     |
 (__((__((___()()_____________________________________// |ACME |
(__((__((___()()()------------------------------------'  |_____|

"""
exitto+=Style.RESET_ALL

won= f"{Fore.LIGHTGREEN_EX}"


won =r"""
                                                                       
            ,                   
   \  :  /                     
`. __/ \__ .'
_ _\     /_ _       
   /_   _\
 .'  \ /  `.
   /  :  \          
      '
           
       ,....,
      ,::::::<
     ,::/^\"``.
    ,::/, `   e`.
   ,::; |        '.
   ,::|  \___,-.  c)
   ;::|     \   '-'
   ;::|      \
   ;::|   _.=`\
   `;:|.=` _.=`\
     '|_.=`   __\
     `\_..==`` /
      .'.___.-'.
     /          \
    ('--......--')
    /'--......--'\
    `"--......--"

      ,
   \  :  /
`. __/ \__ .'
_ _\     /_ _
   /_   _\
 .'  \ /  `.
   /  :  \    
      '

"""
won+=Style.RESET_ALL

start = f"{Fore.GREEN}"
start=r"""
.__    __    __    __    __    __    __    __    __    __
/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \
\__/   __    __/     /   __   \  /     /   __    __      /
/   __/  \__/   __/  \  /  \  /  \  /   __/   __/  \__/  \
\  /     /   __/   __/  \     \  /  \__/   __/  \__   \  /
/  \  /   __/   __/     /  \__/  \__   \  /   __   \__   \
\  /  \__/  \  /   __/  \  /   __/   __/   __/   __/  \  /
/   __/     /   __/  \  /  \  /   __/  \__/   __/   __   \
\  /   __/  \__/     /  \  /   __/   __/   __/   __/  \__/
/  \  /  \     \  /   __/   __/   __   \  /   __/   __   \
\__/  \  /  \__/  \__/  \__    __/  \  /  \__    __/   __/
/   __/  \__    __/   __   \__/   __/  \     \__/   __/  \
\  /   __   \__/   __/   __/   __/   __/  \  /   __/     /
/  \__   \__   \  /   __/   __/   __/   __/  \__   \  /  \
\  /  \__   \__   \__    __/   __/   __/   __/  \  /  \  /
/  \     \__   \__/  \__/  \__   \  /   __/   __   \__/  \
\  /  \__   \  /     /   __   \  /  \  /  \__   \__/   __/
/   __/  \  /  \  /   __/   __/  \  /   __   \__    __/  \
\__/     /  \  /  \__/   __/  \  /  \__/  \__   \__/     /
/   __/   __/  \  /   __/   __/  \     \     \__/   __/  \
\  /  \  /     /  \  /   __    __/  \__   \  /   __/  \  /
/  \  /  \  /  \  /  \  /  \  /   __/  \__/   __/   __/  \
\  /  \  /  \  /  \__   \     \__/   __   \__/     /  \  /
/   __/  \__/  \  /   __/  \__    __/  \__    __/  \     \
\__/   __   \  /  \__/  \__/  \__/     /  \__/  \__/  \__/
/  \__   \__   \__    __    __    __/   __    __   \__   \
\        /  \__/  \__/  \__/  \__/  \__/  \__/  \__/     /
/  Start \                                         \ end \
\__    __/                                         /   __/
   \__/                                            \__/


"""
start +=Style.RESET_ALL

wrong = f"{Fore.RED}"
wrong=r"""                                    .
                                          `.

                                     ...
                                        `.
                                  ..
                                    `.
                            `.        `.
                         ___`.\.//
                            `---.---
                           /     \.--
                          /       \-
                         |   /\    \
                         |\==/\==/  |
                         | `@'`@'  .--.
                  .--------.           )
                .'             .   `._/
               /               |     \
              .               /       |
              |              /        |
              |            .'         |   .--.
             .'`.        .'_          |  /    \
           .'    `.__.--'.--`.       / .'      |
         .'            .|    \\     |_/        |
       .'            .' |     \\               |
     .-`.           /   |      .      __       |
   .'    `.     \   |   `           .'  )      \
  /        \   / \  |            .-'   /       |
 (  /       \ /   \ |                 |        |
  \/         (     \/                 |        |
  (  /        )    /                 /   _.----|
   \/   //   /   .'                  |.-'       `
   (   /(   /   /                    /      `.   |
    `.(  `-')  .---.                |    `.   `._/
       `._.'  /     `.   .---.      |  .   `._.'
              |       \ /     `.     \  `.___.'
              |        Y        `.    `.___.'
              |      . |          \         \
              |       `|           \         |
              |        |       .    \        |
              |        |        \    \       |
            .--.       |         \           |
           /    `.  .----.        \          /
          /       \/      \        \        /
          |       |        \       |       /
           \      |    @    \   `-. \     /
            \      \         \     \|.__.'
             \      \         \     |
              \      \         \    |
               \      \         \   |
                \    .'`.        \  |
                 `.-'    `.    _.'\ |
                   |       `.-'    ||
              .     \     . `.     ||      .'
               `.    `-.-'    `.__.'     .'
                 `.                    .'
             .                       .'
              `.
                                           .-'
                                        .-'

      \                 \
       \         ..      \
        \       /  `-.--.___ __.-.___
`-.      \     /  #   `-._.-'    \   `--.__
   `-.        /  ####    /   ###  \        `.
________     /  #### ############  |       _|           .'
            |\ #### ##############  \__.--' |    /    .'
            | ####################  |       |   /   .'
            | #### ###############  |       |  /
            | #### ###############  |      /|      ----
          . | #### ###############  |    .'<    ____
        .'  | ####################  | _.'-'\|
      .'    |   ##################  |       |
             `.   ################  |       |
               `.    ############   |       | ----
              ___`.     #####     _..____.-'     .
             |`-._ `-._       _.-'    \\\         `.
          .'`-._  `-._ `-._.-'`--.___.-' \          `.
        .' .. . `-._  `-._        ___.---'|   \   \
      .' .. . .. .  `-._  `-.__.-'        |    \   \
     |`-. . ..  . .. .  `-._|             |     \   \
     |   `-._ . ..  . ..   .'            _|
      `-._   `-._ . ..   .' |      __.--'
          `-._   `-._  .' .'|__.--'
              `-._   `' .'
                  `-._.'
                  
"""
wrong +=Style.RESET_ALL

# ASCII art for correct and incorrect answers
CORRECT_ASCII_ART = f"{Fore.GREEN}"
CORRECT_ASCII_ART += r"""
      /`.                      
           /   :.                        _
          /     \\                      | |
       ,;/,      ::              >>>>---: |>
   ___:c/.(      ||                     | |
 ,'  _|:)>>>--,-'B)>                    | |
(  '---'\--'` _,'||                     | |
 `--.    \ ,-'   ;;                     | |
     |    \|    //                  ,>-.| |
     |     \   ;'                  ^    |_|
     |_____|\,'                          |
     :     :                             |
     |  ,  |                             |
     | : \ :                             |
     | | : :                             |
     | | | |                            /|\
     | | |_`.                          / | \
     '--`                             /  |  \
                                         '
"""
CORRECT_ASCII_ART += Style.RESET_ALL

End_ART = f"{Fore.GREEN}"
End_ART += r"""
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\
"""
End_ART += Style.RESET_ALL

INCORRECT_ASCII_ART = f"{Fore.RED}"
INCORRECT_ASCII_ART += r"""
 .-. .-.       .-. .-.
    (   Y   )     (   Y   )
     `|   |`       `|   |`
      | 00|_       _|00 |
      |  ,__)     (__,  |
      |,_|           L_,|
      ||               ||
      | \_,         ,_/ |
      |   |         |   |
      |   |         |   |
    (`  A  `)     (`  A  `)
     '-' '-'       '-' '-'
"""
INCORRECT_ASCII_ART += Style.RESET_ALL

SKIP_ASCII_ART = f"{Fore.YELLOW}"
SKIP_ASCII_ART += r"""
                          .-.
                          {{#}}
          {}               8@8
        .::::.             888
    @\\/W\/\/W\//@         8@8
     \\/^\/\/^\//     _    )8(    _
      \_O_{}_O_/     (@)__/8@8\__(@)
 ____________________ `~"-=):(=-"~`
|<><><>  |  |  <><><>|     |.|
|<>      |  |      <>|     |S|
|<>      |  |      <>|     |'|
|<>   .--------.   <>|     |.|
|     |   ()   |     |     |P|
|_____| (O\/O) |_____|     |'|
|     \   /\   /     |     |.|
|------\  \/  /------|     |U|
|       '.__.'       |     |'|
|        |  |        |     |.|
:        |  |        :     |N|
 \       |  |       /      |'|
  \<>    |  |    <>/       |.|
   \<>   |  |   <>/        |K|
    `\<> |  | <>/'         |'|
      `-.|__|.-`           \ /
                            ^
"""
SKIP_ASCII_ART += Style.RESET_ALL

# Achievement Levels
ACHIEVEMENT_LEVELS = {
    5: "Novice",
    30: "Intermediate",
    55: "Advanced",
    70: "Master",
    90: "Insane",
    99: "Verteran(Old_Master!!)"
}

# Leaderboard to store final scores
leaderboard = []


class Level:
    def __init__(self, question, answer, check_answer_fn=None):
        self.question = question
        self.answer = answer
        self.check_answer_fn = check_answer_fn if check_answer_fn else self.default_check
        self.color = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])
        # self.max_attempts = 5  # Maximum attempts allowed for each level
    
    def play(self, lifelines, score):
        os.system("cls")
        print("\nGame Start: Solve to progress. You have 5 skips total!!!.")
        print(f"{self.color}{self.question}{Style.RESET_ALL}")
        start_time = time.time()
        while time.time() - start_time < 300:  # Maximum time limit of 5 minutes (300 seconds)
            remaining_time = int(300 - (time.time() - start_time))
            print(f"{Fore.YELLOW}Time Left: {remaining_time} seconds{Style.RESET_ALL}", end='\r')
            user_answer = input(f"{Fore.CYAN}Answer (type 'skip' to skip, 'quit' to exit): {Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}")
            if user_answer.lower() == 'quit':
                print(exitto)
                print("You quit the game.")
                return False, score
            elif user_answer.lower() == 'skip':
                if 'skip' in lifelines and lifelines['skip'] > 0:
                    lifelines['skip'] -= 1
                    print("Level skipped.\n")
                    print(SKIP_ASCII_ART)
                    return True, score
                else:
                    print("No skips left.")
                    continue

            if self.check_answer_fn(user_answer):
                print("Correct!\n")
                score += 1
                return True, score
            else:
                print(INCORRECT_ASCII_ART)
                print("Incorrect. Try again.")
        print("Time's up! Game Over.")
        return False, score

    def default_check(self, user_answer):
        return user_answer.lower() == self.answer.lower()


def display_achievement(score):
    for level, title in ACHIEVEMENT_LEVELS.items():
        if score >= level:
            print(f"Achievement Unlocked: {title}!:{Fore.LIGHTCYAN_EX}")


def display_leaderboard():
    print("\nLeaderboard:")
    for i, (name, score) in enumerate(leaderboard, 1):
        print("0. Muhammad Hasnat Rasool : 101")
        print(f"{i}. {name}: {score} points")


def level_1_check(user_answer):
    return user_answer.isdigit() and int(user_answer) == 4


def level_2_check(user_answer):
    return user_answer == '9'

def level_3_check(user_answer):
    return user_answer.lower() == 'def'

def level_4_check(user_answer):
    return user_answer.lower() == 'loop'

def level_5_check(user_answer):
    try:
        return eval(user_answer) == 120
    except:
        return False

def level_6_check(user_answer):
    return user_answer.lower() == 'false'

def level_7_check(user_answer):
    return user_answer == '1024'

def level_8_check(user_answer):
    return user_answer.lower() == 'recursion'

def level_9_check(user_answer):
    return user_answer == '8'

def level_10_check(user_answer):
    return user_answer.lower() == 'binary search'

def level_11_check(user_answer):
    # Is 7 prime?
    return user_answer.lower() == 'yes'

def level_12_check(user_answer):
    # Fibonacci sequence 5th number?
    return user_answer == '5'

def level_13_check(user_answer):
    # Reverse of 'game'?
    return user_answer == 'emag'

def level_14_check(user_answer):
    # 3 * 3 - 2?
    return user_answer == '7'

def level_15_check(user_answer):
    # Binary of 10?
    return user_answer == '1010'

def level_16_check(user_answer):
    # Light year unit? (Answer abbreviation)
    return user_answer.lower() == 'bytes'

def level_17_check(user_answer):
    # Square root of 121?
    return user_answer == '11'

def level_18_check(user_answer):
    # Is Python case-sensitive? (Yes or No)
    return user_answer.lower() == 'yes'

def level_19_check(user_answer):
    # Capital of France?
    return user_answer.lower() == 'paris'

def level_20_check(user_answer):
    # E = mc^2, solve for m=2, c=3 (E=?)
    return user_answer == '18'
def level_21_check(user_answer):
    # Decimal to Hexadecimal of 255?
    return user_answer.lower() == 'ff'

def level_22_check(user_answer):
    # What logical operator represents logical AND in Python?
    return user_answer == 'and'

def level_23_check(user_answer):
    # If x = 8, then what is the value of 2(x^2) / 4 - 2?
    return user_answer == '30'

def level_24_check(user_answer):
    # ASCII value of 'A'?
    return user_answer == '65'

def level_25_check(user_answer):
    # How many continents are there?
    return user_answer == '7'

def level_26_check(user_answer):
    # What is the derivative of x^2?
    return user_answer == '2x'

def level_27_check(user_answer):
    # What is the largest planet in our solar system?
    return user_answer.lower() == 'jupiter'

def level_28_check(user_answer):
    # What HTTP status code stands for Not Found?
    return user_answer == '404'

def level_29_check(user_answer):
    # Calculate the sum of the first 100 natural numbers.
    sum_100 = sum(range(1, 101))
    return user_answer == str(sum_100)

def level_30_check(user_answer):
    # What is the time complexity of Binary Search in Big O notation?
    return user_answer.lower() == 'o(log n)'
def level_31_check(user_answer):
    # 7 * (8 + 9) - 50?
    return user_answer == '69'

def level_32_check(user_answer):
    # Find the next number in the sequence: 2, 4, 8, 16, ?
    return user_answer == '32'

def level_33_check(user_answer):
    # What data type is 'True' in Python?
    return user_answer.lower() == 'boolean'

def level_34_check(user_answer):
    # Solve for x: 2x + 3 = 9
    return user_answer == '3'

# def level_35_check(user_answer):
#     # How many continents are there?
#     return user_answer == '7'
def level_35_check(user_answer):
    return user_answer =='5'
    print("Level 37: If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?")
def level_36_check(user_answer):
    # Convert "101101" from binary to decimal.
    return user_answer == '45'

def level_37_check(user_answer):
    # What HTTP status code stands for "Not Found"?
    return user_answer == '127.0.0.1'

def level_38_check(user_answer):
    # Name the sorting algorithm with O(n log n) average time complexity.
    # Accepting multiple correct answers for educational purposes.
    return user_answer.lower() in ['merge sort', 'heapsort', 'quicksort']

def level_39_check(user_answer):
    # Calculate the area of a circle with radius 7 (use 22/7 for π).
    return user_answer == '154'  # A = πr^2

def level_40_check(user_answer):
    return user_answer =="[5, 4, 3, 2, 1]"

def level_41_check(user_answer):
    return user_answer.lower() == "array"

def level_42_check(user_answer):
    return user_answer.lower() == "algorithm"
def level_43_check(user_answer):
    return user_answer.lower() == "linked list"

def level_44_check(user_answer):
    return user_answer.lower() == "stack"

def level_45_check(user_answer):
    return user_answer.lower() == "queue"

def level_46_check(user_answer):
    return user_answer.lower() == "hash table"

def level_47_check(user_answer):
    return user_answer.lower() == "graph"

def level_48_check(user_answer):
    return user_answer.lower() == "dynamic programming"

def level_49_check(user_answer):
    return user_answer.lower() == "linked list"

def level_50_check(user_answer):
    return user_answer == "404"

def level_51_check(user_answer):
    return user_answer.lower() in ["merge sort", "quick sort", "heapsort"]

def level_52_check(user_answer):
    return user_answer.lower() == "ls"

def level_53_check(user_answer):
    return user_answer.lower() == "where"

def level_54_check(user_answer):
    return user_answer == "git log"

def level_55_check(user_answer):
    return user_answer == "255"

def level_56_check(user_answer):
    return user_answer.lower() == "parity bit"

def level_57_check(user_answer):
    return user_answer.lower() == "shebang"

def level_58_check(user_answer):
    return user_answer == "128"

def level_59_check(user_answer):
    return user_answer.lower() == "tuple"

def level_60_check(user_answer):
    return user_answer == "cat"

def level_61_check(user_answer):
    return user_answer.lower() == "omega"

def level_62_check(user_answer):
    return user_answer.lower() == "equals"

def level_63_check(user_answer):
    return user_answer.lower() == "background-color"

def level_64_check(user_answer):
    return user_answer.lower() == "insert"

def level_65_check(user_answer):
    return user_answer.lower() == "a"

def level_66_check(user_answer):
    return user_answer.lower() == "element, class, id"

def level_67_check(user_answer):
    return user_answer.lower() == "declarative"

def level_68_check(user_answer):
    return user_answer.lower() == "memcached"

def level_69_check(user_answer):
    return user_answer.lower() == "fetch"

def level_70_check(user_answer):
    return user_answer.lower() in ["private", "methods", "encapsulation"]

def level_71_check(user_answer):
    return user_answer.lower() == "triple quotes"

def level_72_check(user_answer):
    return user_answer.lower() == "bubble sort"

def level_73_check(user_answer):
    return user_answer.lower() == "o(infinity)"

def level_74_check(user_answer):
    return user_answer.lower() == "media queries"

def level_75_check(user_answer):
    return user_answer.lower() == "stack"

def level_76_check(user_answer):
    return user_answer.lower() == "firewall"

def level_77_check(user_answer):
    return user_answer.lower() == "gzip"

def level_78_check(user_answer):
    return user_answer == "largest"

def level_79_check(user_answer):
    return user_answer.lower() == "json"

def level_80_check(user_answer):
    return user_answer.lower() == "o(1)"

def level_81_check(user_answer):
    return user_answer.lower() == "agile"

def level_82_check(user_answer):
    return user_answer.lower() == "s3"

def level_83_check(user_answer):
    return user_answer.lower() == "malware"

def level_84_check(user_answer):
    return user_answer.lower() == "nan"

def level_85_check(user_answer):
    return user_answer.lower() == "html"

def level_86_check(user_answer):
    return user_answer.lower() == "aes"

def level_87_check(user_answer):
    return user_answer.lower() == "tcp"

def level_88_check(user_answer):
    return user_answer.lower() == "abstract"

def level_89_check(user_answer):
    return user_answer.lower() == "o(n)"

def level_90_check(user_answer):
    return user_answer.lower() == "vim"

def level_91_check(user_answer):
    return user_answer.lower() == "leaf"

def level_92_check(user_answer):
    return user_answer.lower() == "pandas"

def level_93_check(user_answer):
    return user_answer.lower() == "ip"

def level_94_check(user_answer):
    return user_answer.lower() == "creational"

def level_95_check(user_answer):
    return user_answer.lower() == "private"

def level_96_check(user_answer):
    return user_answer.lower() == "regression"

def level_97_check(user_answer):
    return user_answer.lower() == "javascript"

def level_98_check(user_answer):
    return user_answer.lower() == "join"

def level_99_check(user_answer):
    return user_answer.lower() == "sprint"
def level_100_check(user_answer):
    return True

def complex_logic_check(input_func, correct_answer):
    """
    A generic function to handle complex logic checks, where input_func is used
    to get the user's answer, and correct_answer is what the answer should be.
    """
    user_answer = input_func()
    return user_answer.lower() == correct_answer.lower()


def execute_level(level_func):
    """
    Executes a given level function and returns True if the player succeeds,
    False otherwise.
    """
    return level_func()

levels = [
    Level("Level 1: \n 2+2?", "4", level_1_check),
    Level("Level 2: \n4+5?", "9", level_2_check),
    Level("Level 3: \nPython function keyword?", "def", level_3_check),
    Level("Level 4: \nStructure repeats code?", "loop", level_4_check),
    Level("Level 5: \n5 factorial?", "120", level_5_check),
    Level("Level 6: \nIs Python statically typed?", "false", level_6_check),
    Level("Level 7: \n2^10?", "1024", level_7_check),
    Level("Level 8: \nCalling itself?", "recursion", level_8_check),
    Level("Level 9: \nCube root of 512?", "8", level_9_check),
    Level("Level 10: \nEfficient search method?", "binary search", level_10_check),
    Level("Level 11: \nIs 7 a prime number?", "yes", level_11_check),
    Level("Level 12: \nWhat is the 5th number in the Fibonacci sequence?", "5", level_12_check),
    Level("Level 13: \nWhat is 'game' spelled backwards?", "emag", level_13_check),
    Level("Level 14: \nCalculate: 3 * 3 - 2", "7", level_14_check),
    Level("Level 15: \nWhat is the binary representation of 10?", "1010", level_15_check),
    Level("Level 16: \nWhat is the unit used for size of files?", "bytes", level_16_check),
    Level("Level 17: \nWhat is the square root of 121?", "11", level_17_check),
    Level("Level 18: \nIs Python case-sensitive?", "yes", level_18_check),
    Level("Level 19: \nWhat is the capital of France?", "paris", level_19_check),
    Level("Level 20: \nIf E = mc^2 and m=2, c=3, what is E?", "18", level_20_check),
    Level("Level 21: \nDecimal to Hexadecimal of 255?", "ff", level_21_check),
    Level("Level 22: \nPython logical AND operator?", "and", level_22_check),
    Level("Level 23: \nIf x = 8, then 2(x^2) / 4 - 2 = ?", "30", level_23_check),
    Level("Level 24: \nASCII value of 'A'?", "65", level_24_check),
    Level("Level 25: \nHow many continents are there?", "7", level_25_check),
    Level("Level 26: \nDerivative of x^2?", "2x", level_26_check),
    Level("Level 27: \nLargest planet in our solar system?", "jupiter", level_27_check),
    Level("Level 28: \nHTTP status code for Not Found?", "404", level_28_check),
    Level("Level 29: \nSum of the first 100 natural numbers?", str(sum(range(1, 101))), level_29_check),
    Level("Level 30: \nTime complexity of Binary Search (Big O notation)?", "o(log n)", level_30_check),
    Level("Level ??: \n7 * (8 + 9) - 50?", "69", level_31_check),
    Level("Level ??: \nFind the next number in the sequence: 2, 4, 8, 16, ?", "32", level_32_check),
    Level("Level ??: \nWhat data type is 'True' in Python?", "boolean", level_33_check),
    Level("Level ??: \nSolve for x: 2x + 3 = 9", "3", level_34_check),
    Level("Level ??: \nIf it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?","5",level_35_check),
    # Level("How many continents are there?", "7", level_35_check),
    Level("Level ??: \nConvert '101101' from binary to decimal.", "45", level_36_check),
    Level("Level ??: \nTell which server used for testing apps on local machine?(hint-> 0.0.0.0 pattern)", "127.0.0.1", level_37_check),
    Level("Level ??: \nName the sorting algorithm with O(n log n) average time complexity.", "merge sort", level_38_check),
    Level("Level ??: \nCalculate the area of a circle with radius 7 (use 22/7 for π).", "154", level_39_check),
    Level("Level ??: \nIf list = [1, 2, 3, 4, 5], what is list[::-1]?(hint->[1,1,1,1,1] pattern)", "[5, 4, 3, 2, 1]", level_40_check),
    # Level("If list = [1, 2, 3, 4, 5], what is list[::-1]?", "[5, 4, 3, 2, 1]", level_40_check),
Level("Level ??: \nWhat data structure stores elements at contiguous memory locations?", "array", level_41_check),
    Level("Level ??: \nWhat is a step-by-step procedure for solving a problem?", "algorithm", level_42_check),
Level("Level 43: \nWhich protocol is used for securely transferring files over the internet?", "sftp", level_43_check),
Level("Level ??: \nWhat is the principle of DRY in software development?", "don't repeat yourself", level_44_check),
Level("Level ??: \nWhich programming paradigm does Python support that involves inheriting from classes?", "object-oriented programming", level_45_check),
Level("Level ??: \nIn machine learning, what is 'Overfitting'?", "model too closely fits the training data", level_46_check),
Level("Level ??: \nWhich cloud computing service model provides virtualized computing resources over the internet?", "iaas", level_47_check),
Level("Level ??: \n0b101 + 0b110 = ? (base 10)", "11", level_48_check),
Level("Level ??: \nPrimary data structure for Blockchain:", "linked list", level_49_check),
Level("Level ??: \nHTTP status code for 'Not Found':", "404", level_50_check),
Level("Level 51: \nO(n log n) typical for:", "merge sort", level_51_check),
Level("Level 52: \nLinux command to list directories and files:", "ls", level_52_check),
Level("Level 53: \nSELECT name FROM users WHERE age > 30 AND city = 'New York'; (SQL part missing):", "where", level_53_check),
Level("Level 54: \nGit command to view commit history:", "git log", level_54_check),
Level("Level 55: \n(2^8)-1 = ?", "255", level_55_check),
Level("Level 56: \nError checking method with odd 1's count:", "parity bit", level_56_check),
Level("Level 57: \n#! in scripts:", "shebang", level_57_check),
Level("Level 58: \nIPv6 Address Length (bits):", "128", level_58_check),
Level("Level 59: \nPython's Immutable Sequence Type:", "tuple", level_59_check),
Level("Level ??: \nLinux Command for File Content Display:", "cat", level_60_check),
Level("Level ??: \nAlgorithm Complexity: Best Case (Symbol):", "omega", level_61_check),
Level("Level ??: \nJava: Checking Object Equality (Method):", "equals", level_62_check),
Level("Level ??: \nCSS: Specifies the Background Color (Property):", "background-color", level_63_check),
Level("Level ??: \nSQL: Command to Add a New Row to a Table:", "insert", level_64_check),
Level("Level ??: \nHTML: Defines a Hyperlink (Element):", "a", level_65_check),
Level("Level ??: \nCorrect Order of CSS Specificity (Lowest to Highest):", "element, class, id", level_66_check),
Level("Level ??: \nProgramming Paradigm Focusing on 'What to Solve':", "declarative", level_67_check),
Level("Level ??: \nCaching Mechanism Reducing Database Load:", "memcached", level_68_check),
Level("Level 69: \nNOT an HTTP Method:", "fetch", level_69_check),
Level("Level 70: \nEncapsulation in OOP: Achieved Using (Concept):", "private", level_70_check),
Level("Level 71: \nPython: String Multi-Line Definition:", "triple quotes", level_71_check),
Level("Level 72: \nSorting Algorithm with O(n^2) Worst Case:", "bubble sort", level_72_check),
Level("Level 73: \nBig O Notation: Infinite Loops (Symbol):", "o(infinity)", level_73_check),
Level("Level 74: \nWeb Development: Ensures Responsive Design (Concept):", "media queries", level_74_check),
Level("Level 75: \nProgramming: LIFO Principle (Data Structure):", "stack", level_75_check),
Level("Level 76: \nNetwork Security: Unauthorized Access Prevention (Device):", "firewall", level_76_check),
Level("Level 77: \nLossless Data Compression (Example):", "gzip", level_77_check),
Level("Level 78: \nMax Heap: Root Element Property:", "largest", level_78_check),
Level("Level 79: \nREST API: Data Format (Common):", "json", level_79_check),
Level("Level 80: \nAsymptotic Analysis: Constant Time (Symbol):", "o(1)", level_80_check),
Level("Level 81: \nSoftware Development: Iterative Model (Example):", "agile", level_81_check),
Level("Level 82: \nCloud Storage: Amazon Service:", "s3", level_82_check),
Level("Level 83: \nCybersecurity: Malicious Software (Short):", "malware", level_83_check),
Level("Level 84: \nData Science: Missing Values (Common Term):", "nan", level_84_check),
Level("Level 85: \nWeb: Language for Webpage Structure:", "html", level_85_check),
Level("Level 86: \nEncryption: Symmetric Key (Example):", "aes", level_86_check),
Level("Level 87: \nInternet Protocol: Reliable, Ordered Delivery (Acronym):", "tcp", level_87_check),
Level("Level 88: \nOOP: Abstract Class Keyword (Java):", "abstract", level_88_check),
Level("Level 89: \nComplexity: Searching Unsorted List (Worst Case):", "o(n)", level_89_check),
Level("Level 90: \nLinux: Command Line Text Editor:", "vim", level_90_check),
Level("Level 91: \nBinary Trees: No Children Nodes (Term):", "leaf", level_91_check),
Level("Level 92: \nPython Data Analysis Library:", "pandas", level_92_check),
Level("Level 93: \nNetwork: Address Identifying a Device (Acronym):", "ip", level_93_check),
Level("Level 94: \nDesign Pattern: Object Creation (Category):", "creational", level_94_check),
Level("Level 95: \nProgramming: Preventing External Access (Modifier):", "private", level_95_check),
Level("Level 96: \nMachine Learning: Supervised Learning (Example):", "regression", level_96_check),
Level("Level 97: \nWeb Development: Client-Side Scripting Language:", "javascript", level_97_check),
Level("Level 98: \nDatabase: Relation Between Tables (Term):", "join", level_98_check),
Level("Level 99: \nAgile Methodology: Work Cycle (Term):", "sprint", level_99_check),
Level("Level 100: \n Achievement: Completed All Levels (Badge): ", "i did it", level_100_check)
    # Level("Solve the multi-part maze.",  level_13_check),
    # {"question": "Level 32: Multi-step logic question.", "func": level_32},
    
]

def check_lvl_101(random_number):
    """
    Checks if the user can recall the randomly generated number.
    Displays trophy animation and Champion art on success.
    """

    user_answer = input(f"{Fore.BLUE}What was the number you were asked to remember? {Fore.RESET}")

    if user_answer.isdigit() and int(user_answer) == random_number:
        print(f"\n{Fore.GREEN}Correct! You have a good memory!{Fore.RESET}")
        
        print(f"\nCongratulations! You are the {Fore.YELLOW}Champion!{Fore.RESET}")
        return True
    else:
        print(wrong)
        print(f"\n{Fore.RED}Incorrect! Your memory failed you.{Fore.RESET}")
        return False

def start_game():
    global random_number
    print(start)
    print(f"{Fore.LIGHTBLUE_EX}Welcome to the __CS__ Quiz Game!:{Style.RESET_ALL}\n")
    random_number = random.randint(0, 100)  # Generate random number
    print(f"Don't forget to remember the number: {Fore.LIGHTMAGENTA_EX}{random_number}{Fore.RESET}")
    player_name = input(f"Enter your name: {Fore.LIGHTGREEN_EX}")
    os.system("cls")
    
    lifelines = {'skip': 5}  # Allow 3 skips
    score = 0
    
    print("\nGame Start: Solve to progress. You have 5 skips.")
    for i, lvl in enumerate(levels, 1):
        print(f"\nLevel {i}")
        correct, score = lvl.play(lifelines, score)
        if not correct:
            print(INCORRECT_ASCII_ART)
            print(f"Incorrect. Game Over.:{Fore.BLUE}")
            break
        else:
            print(f"Correct!:{Fore.GREEN}\n")
            print(CORRECT_ASCII_ART)
            display_achievement(score)
            time.sleep(2)  # Pause for 2 seconds for visual effect
    else:
        print("\nCongratulations! You completed all levels.")
        print(f"Now, for the final challenge: Level 101!")
        if check_lvl_101(random_number):
            print(f"\nCongratulations, {player_name}! You are the {Fore.YELLOW}Champion{Fore.RESET}!")
            print(won)
        else:
            print(wrong)
            print("Sorry, you failed the final challenge. Better luck next time!")
            

        leaderboard.append((player_name, score))
        display_leaderboard()
        print(f"Your final score: {score}")



if __name__ == "__main__":
    start_game()
