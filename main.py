import pandas

# {new_item:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_alphabet.csv")

# TODO 1. Create a dictionary from the .csv into this format {key: code}, i.e. {"A":"Alfa", "B":"Bravo"}
nato_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}


# TODO.2 Create a list of the phonetic code words from a word that the user inputs

user_word = input("Please choose a word to convert: ").upper()
output_list = [nato_dictionary[letter] for letter in user_word]








