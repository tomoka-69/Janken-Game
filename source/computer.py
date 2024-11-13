import random

def pon():
    hand = {1: "グー", 2: "チョキ", 3: "パー"}
    choice = random.randint(1, 3)
    print(f"コンピュータの手: {hand[choice]}")
    return choice