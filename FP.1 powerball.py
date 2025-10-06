import random

varUserName = input("Hello! Welcome to the Lucky Number Generator.\nWhat is your name?\n")

print("\nIt's a pleasure to meet you, " + varUserName + "!\nLet's generate your six lucky numbers...")

firstBall = random.randint(1, 69)
secondBall = random.randint(1,69)
thirdBall = random.randint(1,69)
forthBall = random.randint(1,69)
fifthBall = random.randint(1,69)
powerBall = random.randint(1,26)

print("\nHere are your numbers:\n" + str(firstBall) + "  " + str(secondBall) + "  " + str(thirdBall) + "  " + str(forthBall) + "  " + str(fifthBall) + "    " + str(powerBall))

print("\nGood luck, " + varUserName + "! Have a wonderful day.")


