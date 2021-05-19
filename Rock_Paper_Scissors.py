import random


def display_results(response, choice):
    replies = ["Sorry, but the computer chose {0}",
               "There is a draw ({0})",
               "Well done. The computer chose {0} and failed"]
    print(replies[response].format(choice))


def user_input(plays_list):
    valid_words = ["!exit", "!rating"]
    valid_words.extend(plays_list)
    word = input()
    while valid_words.count(word) == 0:
        print("Invalid input")
        word = input()
    return word


def comp_selection(plays_list):
    high_limit = len(plays_list)
    rand_choice = random.randint(0, (high_limit - 1))
    return plays_list[rand_choice]

# find the user's choice in the list, then find the list length - 1 / 2 items before that, 
# if the comp choice is in that, the user wins, if not, the comp wins
def the_winner(plays_list, user, comp):
    options = len(plays_list)
    win_len = int((options - 1) / 2)
    position = plays_list.index(user)
    user_win = []
    # the indexes for the win list will start with position - 1 
    # this will be done with a for loop with a range of 0, win_len + 1
    # The win list can be appended with the words at those indexes each loop
    for num in range(1, (win_len + 1)):
        user_win_pos = position - num
        if user_win_pos < 0:
            user_win_pos += options
        user_win.append(plays_list[user_win_pos])

    if user_win.count(comp) > 0:
        return 100
    else:
        return 0




#*******MAIN*******
# get the user's name and the possible plays
print("Enter your name: ", end="")
name = input()
print("Hello, {0}".format(name))
plays = input().split(',')
if len(plays) < 2:
    plays = ["rock", "paper", "scissors"]
print("Okay, let's start")

# create the rating file (there may not be one)
rating_file = open("rating.txt", "a")
rating_file.close()

# loading the file into a dictionary with
# names as keys and scores as values
rating_file = open("rating.txt", "r")
rating_dict = {}
for line in rating_file:
    temp = line.split()
    rating_dict[temp[0]] = temp[1]
rating_file.close()

# looking for the user and adding them if they are not in the list
if name not in rating_dict:
    rating_dict[name] = "0"

selection = user_input(plays)

while selection != "!exit":
    # getting the user's points
    points = int(rating_dict[name])

    # the computer plays:
    comp_choice = comp_selection(plays)

    # finding the winner and adding the points
    if selection == "!rating":
        print("Your rating: {0}".format(points))
    elif selection == comp_choice:
        display_results(1, comp_choice)
        points += 50
    else:
        earned = the_winner(plays, selection, comp_choice)
        points += earned
        if earned == 0:
            display_results(0, comp_choice)
        else:
            display_results(2, comp_choice)


    # updating the points
    rating_dict[name] = str(points)
    # getting the next selection
    selection = user_input(plays)

print("Bye!")

# updating the rating file
rating_file = open("rating.txt", "w")
for key in rating_dict:
    print("{0} {1}".format(key, rating_dict[key]), 
          file=rating_file, flush=True)

rating_file.close()
