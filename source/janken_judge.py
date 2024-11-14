def judge(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "引き分け"
    elif (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 3) or \
         (player_choice == 3 and computer_choice == 1):
        return "勝ち"
    else:
        return "負け"
