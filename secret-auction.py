from replit import clear
from art import logo
print(logo)
print("Welcome to The Secret Auction Program.")

def add_user(name,bid):
    new_user = {
      "name" : user_name,
      "bid"  : user_bid,
      }   
    users.append(new_user)

users = []
auction = True
while auction:
  user_name = input("What is your name? ")
  user_bid = int(input("Make your bid. £"))
  user_continue = input("Are their any other bidders? Type 'yes' or 'no'. ").lower()
  add_user(user_name, user_bid)
  if user_continue == "yes":
    clear()
    add_user(user_name, user_bid)
  elif user_continue == "no":
    auction = False
    max_value = max(users, key=lambda x: x['bid'])
    print(f"The Highest bid is {max_value['name']} with £{max_value['bid']}!")
  