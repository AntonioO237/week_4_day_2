#################################Extracting Sub-Strings###################################

# Extracting Sub-Strings Practice #1
# Extract the first word of the following sentence using slicing, and display it on the screen:
sentence = "Controlling complexity is the essence of programming"
substring = sentence.find("Contolling")
print(substring)
substring = (sentence[0:11])
print(substring)
# Hint: "Controlling" is 11 characters long.

# Extracting Sub-Strings Practice #2
# Take every third character starting from the ninth to the end of the sentence, and print the result.
text = "Never trust a computer you can't throw out a window"
print(text[0:-1:3])

# Extracting Sub-Strings Practice #3
# Reverses the position of all the characters in the following sentence and displays the result on the screen.
text = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
print(text[::-1])
##################################### String Methods#################################

# String Methods Practice #1
# Slides 12 -16
# Print the following text in uppercase, using the specific string method:
text = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(text.upper())
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."

# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
word_list = ("Simple","is","better","than","complex.")
joined_list = " ".join(word_list)
print(joined_list)

# String Methods Practice #3
# Replace in the following sentence:
sentence4 = "If the implementation is hard to explain, it might be a bad idea."
new_sentence = sentence4.replace("hard", "easy").replace("bad", "good")
print(new_sentence)
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.

#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.
repetition = "Repetition" * 15
print(repetition)

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
word = "electroencephalographist"