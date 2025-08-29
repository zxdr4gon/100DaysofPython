
print("Welcome to the secret auction!")

bidding = {

}

while True:
    name = input("Name: ")
    bid = int(input("Your bid: "))

    bidding.update({name:bid})
    ask = input("Is there any other bidder? y/n \n").lower()
    if ask == 'n':
        break
    else:
        continue


winner = max(bidding.values())

for key,val in bidding.items():
  if val == winner:
    win = key

print(f"{win} wins with a bid of ${winner}")
