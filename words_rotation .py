"""
This library will find the possible combinations of words rotation in a given input. 
"""

# List of input words
arr_input = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot']

# Generate all possible combinations from a list of words
def words_rotation(list_input=arr_input):
    """
    This function will find the possible combinations of words rotation in a given input.
    """
    output = []  # initiate empty list for the output
    used_words = []  # initiate empty list to store the used words
    for input in list_input:
        single_array = []  # initiate empty list to store the possible combinations for each word
        for i in range(len(input)):
            a = input[i] + input[i+1:] + input[:i]  # Create a word by shifting its position
            a = a.title()
            if a in list_input and a not in used_words: # Check if there is any matching word
                single_array.append(a)
                used_words.append(a)
        output.append(single_array)

    output = [i for i in output if len(i) > 0]
    print(output)


if __name__ == '__main__':
    words_rotation()
