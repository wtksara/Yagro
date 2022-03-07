
# User input
user_input = input ( "Enter word : ")

# Open file
file = open('linux.words', "r")
# Loop through the file line by line
for line in file:
    # If the word consist the string
    if user_input.casefold() in line.casefold():
        print(line)
# Close file
file.close()