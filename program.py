# My first game

# Welcome message
print("Welcome to the game!")
print("Let's play!")
print()

# def dictionary
dictionary = {}

# Ask user's info
print("Please submit your age")
prompt_age = input("> ")
prompt_age = int(prompt_age)


print("Please submit your name")
prompt_name = input("> ")
prompt_name = prompt_name.title()
dictionary['employee'] = (prompt_name, prompt_age)

print("What language would you like to start with?")
prompt_lang = input("> ")
prompt_lang = prompt_lang.title()
dictionary["lang"] = prompt_lang

if prompt_lang == 'Python':
  print(r'☆。★。☆。★')
  print(r' 。☆ 。☆。☆')
  print(r'★。＼｜／。★')
  print(r'- Yay Python! -')
  print(r'★。／｜＼。★')
  print(r'   。☆。。☆   ')
  print(r'☆。★。 ☆  ★')

else:
  print("Yay!")

# Questionnaire about user's future life choices

while True:
  print("Are you ready to become an engineer?")
  ready = input("> ")
  ready = ready.upper()
  
  if (ready == "EXIT"):
    print("Goodbye!")
    break

  elif (ready.startswith("Y")):
    print("I knew you'd say that! Being engineer is so cool!")

  elif (ready.startswith("N")):
    print("Well, maybe you need some more time to think about it.")

  elif (ready == "I DONT KNOW"):
    print("Let me explain why being engineer is so cool!")
    print("You get to work with the most talented people and unique programs!")

  else:
    print("Sorry, wrong answer")

# Red vs blue buttons
print()
print("You have a two choices: pressing a red button or a blue. Press r or b to see your future.")
button = input("> ")
button = button.lower()

if (button.startswith("r")):
  print("Congratulations! You just became an engineer!")

else:
  print("Unfortunately right now you are not eligible to become an engineer. Try to pick up on some more coding.")

# Choosing a path
print()
print("Please make a selection: Would you like to go right or left? Enter r or l.")

way = input("> ")
way = way.lower()

if (way == "r"):
  print("Fantastic! You just got an offer from Brightitech!")

elif (way == "l"):
  print("Keep looking for your dream job!")

# Joining a team
print()

team_info = []

print("Enter five teams you are looking to join:")
team_name = input("> ")
team_info.append(team_name)

team_name = input("> ")
team_info.append(team_name)

team_name = input("> ")
team_info.append(team_name)


team_name = input("> ")
team_info.append(team_name)

team_name = input("> ")
team_info.append(team_name)

print("There is so many great teams at Brightitech:")

for team in team_info:
  print(team)

# The five functions
def first_team(team_name):
  print('''
  The {} team would like to you to solve a simple math problem. If your solution will pass, you may join this team.
  x = 100
  y = 5
  modulo = x % y'''.format(team_name))
 
  print("Enter the value for modulo:")
  modulo = input("> ")
  modulo = int(modulo)
  if modulo == 0:
    return True
  else:
    print("Wrong answer")
    return False

is_right_answer = first_team(team_info[0])

if is_right_answer:
  print("Congratulations on making it to {} team at Brightitech!".format(team_info[0]))


# def second_team():

# second_team()

def third_team(team_name):
  
  print('''
  The {} team would like you to answer this technical question:
  How do you could the length of characters in a string in Python?
  A: len(str)
  B: count(str)
  C: sizeof(str)
  Enter choice A, B or C:
  '''.format(team_name))

  choice = input("> ")
  
  if choice == "A":
    print("Welcome to our team.")
    return True

  else:
    print("Try joining another team.")
    return False
is_correct_answer = third_team(team_info[2])

if is_correct_answer:
  print("Congratulations on making it to {} team at Brightitech".format(team_info[2]))

# Printing information on new engineer
print()
print("For all new employees we will be storing their information in our file system.")
for key, val in dictionary.items():
  print('{}: {}'.format(key, val))

print("Please select Y or N if your information is correct:")
selection = input("> ")
selection = selection.upper()
print("Thank you for playing this game! Goodbye!")

# def fourth_team():

# forth_team()

# def fifth_team():

# fifth_team()
