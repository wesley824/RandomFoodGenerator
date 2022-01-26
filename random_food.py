import random
FAST_FOOD = ["Blaze Pizza", "Chipotle", "Mickie Dickie's", "In-n-Out", "Wingstop", "Eggettes", "Chick-Fila", "Nick The Greek", "Domino's"]
WARM_FOOD = ["Marugame", "Kevin's Pho", "Boudin", "Manna"]
SPECIAL_FOOD = ["KBBQ", "Bonchon", "Ramen Nagi", "San Tung", "Daeho", "Dim Sum"]
RANDOM_FOOD = ["Blaze Pizza", "Chipotle", "Mickie Dickie's", "In-n-Out", "Wingstop", "Eggettes",
               "Marugame", "Kevin's Pho", "Boudin", "KBBQ", "Bonchon", "San Tung", "Chick-Fila", "Daeho", "Manna", "Dim Sum", "Nick The Greek", "Domino's"]

Random_Food_Generator = False
Response_Status = False
while Random_Food_Generator != True:
    Answer = str(input("Feeling hungry? What type of food are you feeling today? Fast, warm, special, or don't know?: ").lower())

#Fast Food
    if Answer == "fast":
        print(random.choice(FAST_FOOD))
        Response = str(input("Happy?: ").lower())
        while Response_Status != True:
            if Response == "yes":
                Random_Food_Generator = True
                Response_Status = True
                break
            elif Response == "no":
                print(random.choice(FAST_FOOD))
                Response = str(input("Happy?: ").lower())
            else:
                print("Please say yes or no.")
                Response = str(input("Happy?: ").lower())

#Warm food
    elif Answer == "warm":
        print(random.choice(WARM_FOOD))
        Response = str(input("Happy?: ").lower())
        while Response_Status != True:
            if Response == "yes":
                Random_Food_Generator = True
                Response_Status = True
                break
            elif Response == "no":
                print(random.choice(WARM_FOOD))
                Response = str(input("Happy?: ").lower())
            else:
                print("Please say yes or no.")
                Response = str(input("Happy?: ").lower())

#Special Food
    elif Answer == "special":
        print(random.choice(SPECIAL_FOOD))
        Response = str(input("Happy?: ").lower())
        while Response_Status != True:
            if Response == "yes":
                Random_Food_Generator = True
                Response_Status = True
                break
            elif Response == "no":
                print(random.choice(SPECIAL_FOOD))
                Response = str(input("Happy?: ").lower())
            else:
                print("Please say yes or no.")
                Response = str(input("Happy?: ").lower())

#Fully Random Food
    elif Answer == "idk":
        print(random.choice(RANDOM_FOOD))
        Response = str(input("Happy?: ").lower())
        while Response_Status != True:
            if Response == "yes":
                Random_Food_Generator = True
                Response_Status = True
                break
            elif Response == "no":
                print(random.choice(RANDOM_FOOD))
                Response = str(input("Happy?: ").lower())
            else:
                print("Please say yes or no.")
                Response = str(input("Happy?: ").lower())

#Wrong input 1st question
    else:
        print("Please say fast, warm, special, or idk")


#Drinks
Drink_Places = ["Teaspoon", "TPumps", "Yi Fang", "Eggettes", "Jamba Juice", "Starbucks"]

print("Time for drinks!")
print("")
print(random.choice(Drink_Places))
Drink_Status = False
Response2_Status = False
while Drink_Status != True:
    Response2 = str(input("Happy?: ").lower())

#yes
    if Response2 == "yes":
        print("")
        print("Have a good meal!")
        Response2_Status = True
        Drink_Status = True
        break

#no
    elif Response2 == "no":
        print(random.choice(Drink_Places))

#wrong input 2nd question
    else:
        print("Please say yes or no.")

