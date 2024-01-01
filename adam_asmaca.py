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

import random

end_of_game = False
world_list = ["python","javascript","react","django"]
secilen_kelime = random.choice(world_list)
kelime_uzunlugu = len(secilen_kelime)
lives = 6

display = []

for _ in range(kelime_uzunlugu):
  display += "_"

while not end_of_game:
  tahmin = input("bir harf tahmin et").lower()
  for position in range(kelime_uzunlugu):
    harf = secilen_kelime[position]
    if harf == tahmin:
      display[position] = harf 


  if tahmin not in secilen_kelime:
    lives -= 1
    if lives == 0 :
      end_of_game = True
      print("Kaybettin")

  print(f"{''.join(display)}")


  if "_" not in display:
    end_of_game = True
    print("Kazandın")

  print(stages[lives])