import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():

    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Only letters allowed, Please enter again.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

# letters = [letter for letter in word]
# answer = [value for (key, value) in nato_dict.items() for letter in letters if letter.upper() == key]

# for letter in letter:
#     for key in nato_dict:
#         if letter.upper() == key:
#             answer.append(nato_dict[key])

#output_list = [nato_dict[letter] for letter in word]

# print(answer)




