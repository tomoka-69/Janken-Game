import player, computer, janken_judge

def janken_main():
    player_wins, computer_wins = 0, 0
    round_num = 1

    while round_num <= 3:
        print(f"\n----- ラウンド {round_num} -----")
        player_choice = player.pon()         
        computer_choice = computer.pon()   
        
        result = janken_judge.judge(player_choice, computer_choice)
        
        if result == "勝ち":
            print("\n<><><><><><><><><><><>\nあなたの勝ちです！\n<><><><><><><><><><><>")
            player_wins += 1
            round_num += 1
        elif result == "負け":
            print("\n<><><><><><><><><><><>\nコンピュータの勝ちです！\n<><><><><><><><><><><>")
            computer_wins += 1
            round_num += 1
        else:
            print("\n<><><><><><><><><><><>\n引き分けです！再戦します！\n<><><><><><><><><><><>")

    print("\n【最終結果】")
    print(f"あなた: {player_wins}勝")
    print(f"コンピュータ: {computer_wins}勝")

    if player_wins > computer_wins:
        print("あなたの総合勝利です！")    
    else:
        print("コンピュータの総合勝利です！")
        

if __name__ == '__main__':
    janken_main()
