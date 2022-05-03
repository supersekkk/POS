color_to_code = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
              "Asparagus": "#87a96b", "Barn Red": "#7c0a02", "Black Olive": "#3b3c36", "BlanchedAlmond": "#ffebcd",
              "Boysenberry": "#873260", "Bright Turquoise": "#08e8de", "Brink Pink": "#fb607f"}
for key in color_to_code:
    print(key)
user_choice = input("What colorcode do you need?")
while user_choice != "":
    if user_choice in color_to_code:
        print(f"{user_choice} has colorcode  {color_to_code[user_choice]}")
    else:
        print("Invalid choice")
    user_choice = input("What colorcode do you need?")