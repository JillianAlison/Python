#!/usr/bin/env python
# coding: utf-8

# In[122]:


# Welcome to the Inheritance Game!
# We have good news and bad news. The bad news is your wealthy great Unlce 
# Douglas has passed away. The good news is Uncle Douglas loved games and 
# wants you and your brother to play for $100,000 in inheritance. Unlce 
# Douglas always belived sharing is caring and will reward you for your 
# selfessness. You have the option to either tell the lawyers you want to 
# split the Inheritance 50/50 and walk away with $50,000 each our keep it all 
# for yourself. If you choose to keep everything and your brother choosees to 
# split you keep it all and vice versa. But if you both don't share you will 
# only get $25,000 each and the other $50,000 will be donated to charity. 
# Let the games begin! 

# Import Random Package

import random

# Game Introduction
player_play = input("Do you want to play the Inheritance Game? (yes/no)").lower()

#conditional for incorrect input
while player_play != "yes" and player_play != "no":
    player_play = input("I think you made a mistake. Type 'yes' or 'no'").lower()

#User vs Python
if player_play == "yes":
    user_name = input("Welcome to the Inheritance Game! What is your name?").capitalize()

    print(f"\n{user_name}, we have good news and bad news...")

    print("""
    The bad news is your wealthy great Unlce Douglas has passed away. 
    The good news is Uncle Douglas loved games and wants you and your sibling
    to play for $100,000 in inheritance. Unlce Douglas always belived sharing 
    is caring and will reward you for your selfessness.""")

    # Print Table 
    print(f"""
    The following are potential outcomes of how the Inheritance could be divided:
    {user_name} \ Sibling\t\t   Share \t\t\t\t\t      Keep
    --------------\t ------------------------------\t\t\t -------------------------------
    Share\t\t The money is divided equally \t\t\t{user_name} gets $100k. Your sibling gets $0
    Keep \t\t Your sibling gets $100k. You get $0\t\tYou each get $25,000
    """)

    
# Dictionary of Points
    points = {"keep/share":100000, "share/keep":0, "share/share":50000, "keep/keep":25000}
    
    user_choice = input("Will you share with your sibling or keep it all for yourself?(share/keep)").lower()
    
#Conditional for Incorrect Input
    while user_choice != "keep" and user_choice != "share":
        user_choice = input("I think you made a mistake. Type 'keep' or 'share'").lower()
    
# Sibling Choice 
    sibling_choice = random.choice(["keep", "share"]) 
    
# Conditional structure with the outputs of each scenario
    if user_choice == "keep" and sibling_choice == "keep":
        user_result = points["keep/keep"]
        sibling_result = points["keep/keep"]
        print(f"You and your sibling both decided to keep.\nYou get ${user_result}. Your sibling gets ${sibling_result}")

    elif user_choice == "keep" and sibling_choice == "share":
        user_result = points["keep/share"]
        sibling_result = points["keep/share"]
        print(f"You choose to keep. Your sibling choose to share. \nYou get ${user_result}. Your sibling gets ${sibling_result}")

    elif user_choice == "share" and sibling_choice == "keep":
        user_result = points["share/keep"]
        sibling_result = points["share/keep"]
        print(f"You choose to share. Your sibling choose to keep.\nYou get ${user_result}. Your sibling gets ${sibling_result}")

    elif user_choice == "share" and sibling_choice == "share":
        user_result = points["share/share"]
        sibling_result = points["share/share"]
        print(f"You and your sibling both decided to share.\nYou get ${user_result}. Your sibling gets ${sibling_result}")
 
#Python vs Python
#sib_1 strategy 
    else:
        sib_1 = random.choice(["keep", "share"])
        #sib_2 strategy 
        sib_2 = random.choice(["keep", "share"]) if sib_1 == "keep" else random.choice(["share", "keep"])
        print(f"Sibling 1 choose to {sib_1} and sibling 2 choose to {sib_2}")


    #Loop 5 times
    for x in range(5):
        sib_1 = random.choice(["keep", "share"])
        sib_2 = random.choice(["share", "keep"]) if sib_1 == "keep" else random.choice(["keep", "share"])
        print(f"\nRound {x+1}:")
    print(f"Sibling 1 choose to {sib_1} and sibling 2 choose to {sib_2}")

# Game results 
print(f"\n{user_name}, you will receive ${user_result} and your sibling will receive ${sibling_result}")


# In[ ]:




