arr_input = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot']
output = []
used_words = []

# generate all possible combinations from arr_input
for input in arr_input:
    single_array = []
    for i in range(len(input)):
        a = input[i] + input[i+1:] + input[:i]
        a = a.title()
        if a in arr_input and a not in used_words:
            single_array.append(a)
            used_words.append(a)
    output.append(single_array)

output = [i for i in output if len(i) > 0]
print(output)

        

