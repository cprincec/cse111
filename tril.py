model = "GMC Acadia"
length = 193
width = 75
height = 67

# Open a text file named dimensions.txt in append mode.
with open("dimensions.txt", "at") as dimens_file:

    # Print a car's model and dimensions to the file.
    print(model, file=dimens_file)
    print(f"{length}, {width}, {height}", file=dimens_file)