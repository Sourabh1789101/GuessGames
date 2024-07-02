import pyautogui
import random
import os

# Directory to store scores
score_dir = "Scores"
if not os.path.exists(score_dir):
    os.makedirs(score_dir)

# Initialize score files if they do not exist
for mode in ["easy", "medium", "hard"]:
    score_file = os.path.join(score_dir, mode)
    if not os.path.exists(score_file):
        with open(score_file, "w") as f:
            f.write("987654")

# Easy mode
def game_easy():
    guess = random.randint(1, 10)
    step = 1

    ask = pyautogui.prompt(
        text='Guess the number between 1 and 10 :)',
        title='Guess Game (Easy)',
    )
    while ask != str(guess):
        pre = ask
        if int(ask) > guess:
            ask = pyautogui.prompt(
                text=f'Enter a number smaller than {pre}',
                title='Guess Game (Easy)',
            )
        elif int(ask) < guess:
            ask = pyautogui.prompt(
                text=f'Enter a number bigger than {pre}',
                title='Guess Game (Easy)',
            )
        step += 1

    check = pyautogui.confirm(
        text=f'You found the number in {step} steps',
        title='Guess Game (Easy)',
        buttons=['Again', 'Exit']
    )

    with open(os.path.join(score_dir, "easy"), "r") as data1:
        best = data1.readlines()[0]
        if step < int(best):
            with open(os.path.join(score_dir, "easy"), "w") as data2:
                data2.write(str(step))

    if check == "Again":
        game_easy()
    else:
        pyautogui.alert(
            text="Bye Bye",
            title='Guess Game'
        )

# Medium mode
def game_medium():
    guess = random.randint(1, 50)
    step = 1

    ask = pyautogui.prompt(
        text='Guess the number between 1 and 50 :)',
        title='Guess Game (Medium)',
    )
    while ask != str(guess):
        pre = ask
        if int(ask) > guess:
            ask = pyautogui.prompt(
                text=f'Enter a number smaller than {pre}',
                title='Guess Game (Medium)',
            )
        elif int(ask) < guess:
            ask = pyautogui.prompt(
                text=f'Enter a number bigger than {pre}',
                title='Guess Game (Medium)',
            )
        step += 1

    check = pyautogui.confirm(
        text=f'You found the number in {step} steps',
        title='Guess Game (Medium)',
        buttons=['Again', 'Exit']
    )

    with open(os.path.join(score_dir, "medium"), "r") as data1:
        best = data1.readlines()[0]
        if step < int(best):
            with open(os.path.join(score_dir, "medium"), "w") as data2:
                data2.write(str(step))

    if check == "Again":
        game_medium()
    else:
        pyautogui.alert(
            text="Bye Bye",
            title='Guess Game'
        )

# Hard mode
def game_hard():
    guess = random.randint(1, 100)
    step = 1

    ask = pyautogui.prompt(
        text='Guess the number between 1 and 100 :)',
        title='Guess Game (Hard)',
    )
    while ask != str(guess):
        pre = ask
        if int(ask) > guess:
            ask = pyautogui.prompt(
                text=f'Enter a number smaller than {pre}',
                title='Guess Game (Hard)',
            )
        elif int(ask) < guess:
            ask = pyautogui.prompt(
                text=f'Enter a number bigger than {pre}',
                title='Guess Game (Hard)',
            )
        step += 1

    check = pyautogui.confirm(
        text=f'You found the number in {step} steps',
        title='Guess Game (Hard)',
        buttons=['Again', 'Exit']
    )

    with open(os.path.join(score_dir, "hard"), "r") as data1:
        best = data1.readlines()[0]
        if step < int(best):
            with open(os.path.join(score_dir, "hard"), "w") as data2:
                data2.write(str(step))

    if check == "Again":
        game_hard()
    else:
        pyautogui.alert(text="Bye Bye", title='Guess Game')

# Reset scores
def reset_scores():
    for mode in ["easy", "medium", "hard"]:
        with open(os.path.join(score_dir, mode), "w") as s1:
            s1.write("987654")
    pyautogui.alert(text="Scores have been reset to 987654", title='Guess Game')

# Show scores
def show_scores():
    with open(os.path.join(score_dir, 'easy')) as data:
        easy_score = data.readlines()[0]

    with open(os.path.join(score_dir, 'medium')) as data:
        medium_score = data.readlines()[0]

    with open(os.path.join(score_dir, 'hard')) as data:
        hard_score = data.readlines()[0]

    pyautogui.confirm(
        title="Guess Game (Score)",
        text=f"Easy: {easy_score.rjust(10)}\nMedium: {medium_score.rjust(10)}\nHard: {hard_score.rjust(10)}",
        buttons=["OK"]
    )

# Main menu
def main_menu():
    mode = pyautogui.confirm(
        text="Please select an option\nEasy: 1 to 10\nMedium: 1 to 50\nHard: 1 to 100\nScore: Show scores\nReset: Reset scores",
        title="Guess Game",
        buttons=['Easy', 'Medium', 'Hard', 'Score', 'Reset', 'Exit']
    )
    if mode == "Easy":
        game_easy()
    elif mode == "Medium":
        game_medium()
    elif mode == "Hard":
        game_hard()
    elif mode == "Score":
        show_scores()
    elif mode == "Reset":
        reset_scores()
    else:
        pyautogui.alert(text="Bye Bye", title='Guess Game')

if __name__ == "__main__":
    main_menu()
