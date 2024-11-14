def pon():
    hand = {1: "グー", 2: "チョキ", 3: "パー"}
    while True:
        try:
            choice = int(input(" 1.グー\n 2.チョキ\n 3.パー\n あなたの手を選択してください。>" ))
            if choice in hand:
                print(f"あなたの手: {hand[choice]}")
                return choice 
            else:
                print("1, 2, 3のいずれかを入力してください。")
        except ValueError:
            print("数字を入力してください。")