import random

stages = [ 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/
'''
word_list = ["abruptly",  "absurd",  "abyss",  "affix",  "askew",  "avenue",  "awkward",  "axiom",  "azure",  "bagpipes",  "bandwagon",  "banjo",  "bayou",  "beekeeper",
  "bikini",  "blitz",  "blizzard",  "boggle",  "bookworm",  "boxcar",  "boxful",  "buckaroo",  "buffalo",  "buffoon",  "buxom",  "buzzard",  "buzzing",  "buzzwords",  "caliph",
  "cobweb",  "cockiness",  "croquet",  "crypt",  "curacao",  "cycle",  "daiquiri",  "dirndl",  "disavow",  "dizzying",  "duplex",  "dwarves",  "embezzle",  "equip",  "espionage",
  "euouae",  "exodus",  "faking",  "fishhook",  "fixable",  "fjord",  "flapjack",  "flopping",  "fluffiness",  "flyby",  "foxglove",  "frazzled",  "frizzled",  "fuchsia",  "funny",
  "gabby",  "galaxy",  "galvanize",  "gazebo",  "giaour",  "gizmo",  "glowworm",  "glyph",  "gnarly",  "gnostic",  "gossip",  "grogginess",  "haiku",  "haphazard",  "hyphen",  "iatrogenic",
  "icebox",  "injury",  "ivory",  "ivy",  "jackpot",  "jaundice",  "jawbreaker",  "jaywalk",  "jazziest",  "jazzy",  "jelly",  "jigsaw",  "jinx",  "jiujitsu",  "jockey",  "jogging",
  "joking",  "jovial",  "joyful",  "juicy",  "jukebox",  "jumbo",  "kayak",  "kazoo",  "keyhole",  "khaki",  "kilobyte",  "kiosk",  "kitsch",  "kiwifruit",  "klutz",  "knapsack",
  "larynx",  "lengths",  "lucky",  "luxury",  "lymph",  "marquis",  "matrix",  "megahertz",  "microwave",  "mnemonic",  "mystify",  "naphtha",  "nightclub",  "nowadays",  "numbskull",
  "nymph",  "onyx",  "ovary",  "oxidize",  "oxygen",  "pajama",  "peekaboo",  "phlegm",  "pixel",  "pizazz",  "pneumonia",  "polka",  "pshaw",  "psyche",  "puppy",  "puzzling",
  "quartz",  "queue",  "quips",  "quixotic",  "quiz",  "quizzes",  "quorum",  "razzmatazz",  "rhubarb",  "rhythm",  "rickshaw",  "schnapps",  "scratch",  "shiv",  "snazzy",  "sphinx",
  "spritz",  "squawk",  "staff",  "strength",  "strengths",  "stretch",  "stronghold",  "stymied",  "subway",  "swivel",  "syndrome",  "thriftless",  "thumbscrew",  "topaz",  "transcript",
  "transgress",  "transplant",  "triphthong",  "twelfth",  "twelfths",  "unknown",  "unworthy",  "unzip",  "uptown",  "vaporize",  "vixen",  "vodka",  "voodoo",  "vortex",  "voyeurism",
  "walkway",  "waltz",  "wave",  "wavy",  "waxy",  "wellspring",  "wheezy",  "whiskey",  "whizzing",  "whomever",  "wimpy",  "witchcraft",  "wizard",  "woozy",  "wristwatch",
  "wyvern",  "xylophone",  "yachtsman",  "yippee",  "yoked",  "youthful",  "yummy",  "zephyr",  "zigzag",  "zigzagging",  "zilch",  "zipper",  "zodiac",  "zombie"]

print(logo)
chosen_word = random.choice(word_list)


placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)    

game_over = False
correct_letters = []

lives = 6

while not game_over:
    guess_a_letter = input("Guess a letter: ").lower()
    
    if guess_a_letter in correct_letters:
        print(f"You've already guessed {guess_a_letter} ")
        
    display = ""
    for letter in chosen_word:
        if letter == guess_a_letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter        
        else:
            display += "_"
    print(display)
            
    if guess_a_letter not in chosen_word:
        lives -= 1
        print(f"You guessed {guess_a_letter}, that's not in the word. You lose a life. ")
        print(f"**********************{lives}/6 LIVES LEFT********************")
        if lives == 0:
            game_over = True
            print("********************YOU LOSE*********************")
            print(f"The correct word was {chosen_word}")
    
    if "_" not in display:
        game_over = True
        print("********************YOU WIN********************")
    
    print(stages[lives])
   



