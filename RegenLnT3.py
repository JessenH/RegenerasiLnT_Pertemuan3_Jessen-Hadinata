from operator import truediv
import random

user_wins = 0
comp_wins = 0

options = ["batu", "gunting", "kertas"]

while True:
    print("CHILL CORNER\n")
    print("1. Game suit")
    print("2. Beli es krim")
    print("3. Exit")
    user_input = input(">>: ")

   
    if user_input == "3":
        break   

    elif user_input == "1":
         user_input = input("Ketik batu, gunting, kertas: ").lower()
         random_number = random.randint(0, 2)
        # batu: 0, kertas: 1, gunting: 2
         computer_pick = options[random_number]
         print("Bot memilih", computer_pick + ".")

         if user_input == "batu" and computer_pick == "gunting":
            print("Kamu menang!")
            user_wins += 1

         elif user_input == "kertas" and computer_pick == "batu":
            print("Kamu menang!")
            user_wins += 1

         elif user_input == "gunting" and computer_pick == "kertas":
            print("Kamu menang!")
            user_wins += 1

         elif user_input == computer_pick : 
            print("Hasilnya seri!")

         else:
            print("Bot menang!")
            comp_wins  += 1

         print("\nKamu menang", user_wins, "kali.")
         print("Bot menang", comp_wins , "kali.\n")
        
    elif user_input == "2":
        rasa = ["vanilla", "coklat"]
        harga_rasa = [3000, 5000]
        topping = ["polos", "meses", "oreo"]
        harga_topping = [0, 2000, 4000]
        rasa = 0
        topping = 0

        user_rasa = input("Pilih rasa [vanilla, coklat]: ")
        if user_rasa == "vanilla":
           rasa = 0
        else:
           rasa = 1
        
        user_topping = input("Pilih topping [polos, meses, oreo]: ")
        if  user_topping == "polos":
           topping = 0
        elif user_topping == "meses":
           topping = 1
        else:
           topping = 2
      
        total = harga_rasa[rasa] + harga_topping[topping]
        print("Harga es krim yang harus dibayar: " + str(total) + "\n")
    
         



