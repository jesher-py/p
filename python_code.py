# Questions for Quiz
Quiz_questions_and_answers = {'How many Spartans accompany Master Chief in Silver Team?': 3,
             'What is the name of the alien alliance opposing humanity?': 'The covanant',
             'What is the name of the AI that assists Master Chief?'
             'What planet is Master Chief from?': 'Eridanus II',
             'How many clones did Dr. Halsey create of herself for the Cortana project?': 1,
             'What year does the Halo TV show take place?': 2552,
             'How many planets have fallen to the Covenant by the time of the series?': 20,
             'How many years did the Human-Covenant War last?': 28,
             'Where does Soren-066 live in S1': 'Rubble',
             'Which actor portrays Master Chief in the TV series?': "Actor Pablo Schreiber"
}
# Ask for name
name = input('Whats your name? ')
while True:
    length_of_name = len(name)
    if length_of_name > 29:
       print('Please enter a valid name')
       name = input('Whats your name? ')
    if name == " ":
       print('Please enter a valid name')
    else:
       break

# Ask for a number of questions from 5 to 10
print(f'how much do you know about Halo {name}?')
while True:
  try:
      num_questions = int(input('choose between 5 and 10 questions '))
      if num_questions >= 5:
         if num_questions <=10:
            break
         else:
           print('Please choose a valid number')
  except:
    print('Please choose a valid number')



