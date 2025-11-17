# project2_rock_paper_scissors.py
import random
import time

# Feel free to set this to False if you don't want pauses
USE_PAUSE = True

def pause(seconds=0.6):
    if USE_PAUSE:
        time.sleep(seconds)

def computer_throw():
    """Return a random throw: 'rock', 'paper', or 'scissors'."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_throw():
    """
    Ask the user for their throw and validate the input.
    Accepts:
      r or rock -> rock
      p or paper -> paper
      s or scissors -> scissors
    Keeps asking until a valid input is given.
    """
    mapping = {
        'r': 'rock', 'rock': 'rock',
        'p': 'paper', 'paper': 'paper',
        's': 'scissors', 'scissor': 'scissors', 'scissors': 'scissors'
    }
    while True:
        user_input = input("What is your throw? (r/p/s): ").strip().lower()
        if user_input in mapping:
            return mapping[user_input]
        print(f"'{user_input}' is not a valid throw. Please enter r, p, or s.")
        pause(0.5)

def compare_throws(user_throw, comp_throw):
    """
    Compare the user's and the computer's throws.
    Returns 'win', 'lose', or 'tie' (for the user).
    Rule: rock > scissors, scissors > paper, paper > rock.
    """
    if user_throw == comp_throw:
        return "tie"
    wins = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    return "win" if wins[user_throw] == comp_throw else "lose"

def play_one_round():
    """Play a single round of Rock-Paper-Scissors. Return 'win'/'lose'/'tie'."""
    print("\n---------------------------------")
    print("🎮 Ready to play a new round!")
    pause()

    user = get_user_throw()
    print(f"👉 You threw:       {user.upper()}")
    pause(0.3)

    comp = computer_throw()
    print(f"🖥️  Computer threw: {comp.upper()}")
    pause(0.3)

    result = compare_throws(user, comp)
    if result == "win":
        print("✅ Result: You WIN this round!")
    elif result == "tie":
        print("🟨 Result: It's a TIE.")
    else:
        print("❌ Result: You LOSE this round.")
    pause()

    return result

def play_again():
    """Ask the user if they want to play again."""
    while True:
        ans = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if ans in ('yes', 'y'):
            return True
        if ans in ('no', 'n'):
            return False
        print("Please answer 'yes' or 'no'.")
        pause(0.4)

def start_game():
    print("\n-- Welcome to PY-Rocks ---")
    print("---------------------------------")
    print("This is a Rock-Paper-Scissors championship-level match.")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("Controls: r = rock, p = paper, s = scissors")
    print("---------------------------------")
    pause()

def finish_game(games_played, user_wins, comp_wins):
    print("\n================= MATCH SUMMARY =================")
    print(f"🎯 Rounds played: {games_played}")
    print(f"🙋 You won:       {user_wins}")
    print(f"🤖 Computer won:  {comp_wins}")
    ties = games_played - user_wins - comp_wins
    print(f"🟨 Ties:          {ties}")
    print("=================================================")
    if user_wins > comp_wins:
        print("🏆 Great job! You won the match. See you next time!")
    elif user_wins < comp_wins:
        print("🧠 The computer wins this time. Better luck next round!")
    else:
        print("🤝 It's an overall tie — well played!")
    print("Thanks for playing PY-Rocks!")

def show_running_score(games_played, user_wins, comp_wins):
    ties = games_played - user_wins - comp_wins
    print(f"\n📊 Scoreboard -> You: {user_wins} | Computer: {comp_wins} | Ties: {ties}")
    pause(0.5)

def main():
    start_game()
    games_played = 0
    user_wins = 0
    comp_wins = 0

    while True:
        result = play_one_round()
        games_played += 1

        if result == "win":
            user_wins += 1
        elif result == "lose":
            comp_wins += 1

        show_running_score(games_played, user_wins, comp_wins)

        if not play_again():
            break

    finish_game(games_played, user_wins, comp_wins)

if __name__ == "__main__":
    main()
