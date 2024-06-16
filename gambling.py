#Gambling game mines from stake
import random
import time

def gamble(mine):
    #Intially the box contains 5 diamonds
    magic_box = ["💎","💎","💎","💎","💎",]

    #Now we will add the number of bombs as mentioned by the user
    for m in range(mine):
        magic_box.append("💣")


    #Chooses one element at random from the magic_box
    choose = random.choice(magic_box)
    return choose

def amount(mine , bet):
    if mine == 1:
        bet *= 1
    elif mine == 3:
        bet *= 3
    elif mine == 5:
        bet *= 5
    elif mine == 10:
        bet *= 10

    return bet


def main():
    print("Are you ready to become the next millionair????")
    print("_________________________________________________________________________________________________________________________________________")
    time.sleep(2)

    #First user must fill the wallet with some amount so that he can bet
    balance = int(input("Enter the amount you want to store in the wallet : Rs "))
    print()
    time.sleep(1)
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Balance = {balance}")
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    time.sleep(1)
    print("Lets Start ..............")
    time.sleep(1)

    # User will enter the bet amount and the number of mines he want to add int the magic box
    while True:
        bet = int(input("Enter the bet amount : Rs "))

        # the bet amount will be deducted from the user balance
        if bet > balance:
            print("Insufficient funds. You dont have that much money in wallet")

        balance -= bet
        if balance < 0:
            add_money = input("Do you want to credit more money to keep playing(y/n) ? ").lower()
            if add_money == "y":
                added_money = int(input("Enter the amount you want to credit : Rs "))
                balance += added_money
            else:
                print("Thankyou so much for playing . Hope you enjoyed playing..")
                break

        print(f"Remaining balance = Rs {balance}")
        print()
        time.sleep(1)

        mine = int(input("Enter the Number of Mines you want in box(1/3/5/10)? "))
        time.sleep(1)
        print()

        #gamble! result whether its a mine or a diamond
        result = gamble(mine)
        print("GAMBLINGGG..................")
        time.sleep(4)
        print(result)
        print()

        #Displays amount if user wins
        if result == "💎":
            profit = amount(mine , bet)
            balance += profit
            print(f"Profit : Rs {profit}")
        else :
            profit = 0
            print("Oops! its a bomb.You lose your bet amount...")

            print(f"Your Balance : Rs.{balance}")
            print()

        if balance == 0:
                    print()

        answer = input("Do you want to play again(y/n) ? ").lower()
        if answer == "n":
            print("Thankyou for playing")
            print(f"Your total amount = {balance}")
            break



if __name__ == "__main__":
    main()


