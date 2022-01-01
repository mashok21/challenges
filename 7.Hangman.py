import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []

for i in chosen_word:
    display.append("_")

print(display)

# print(chosen_word)

attempt = 0

score = 0

while True:

    attempt_score = 0

    guess = input('Guess a letter\n').lower()

    attempt += 1

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]
            attempt_score = 1

    score += attempt_score

    if (attempt - score) == len(stages):
        print('Game Over, You\'r hanged!')
        print(stages[-len(stages)])
        break

    if attempt_score == 0:
        print(stages[score - attempt])

    print(display)

    if '_' not in display:
        print("Game Over, You Win!")
        break

# print(pos)

print(display)
