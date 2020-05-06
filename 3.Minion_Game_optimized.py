def minion_game(string):
    # your code goes here

    vowels = "AEIOU"
    vowel_compinations_counter = 0
    constant_compination_counter = 0
    j = 0
    #for i in range(len(vowel_list)):
    for j in range(len(string)):
        if(string[j] in vowels):
            vowel_compinations_counter += (len(string) - j)
        else:
            constant_compination_counter += (len(string) - j)
    
    if (constant_compination_counter > vowel_compinations_counter):
        print('Stuart',constant_compination_counter)
    elif (constant_compination_counter < vowel_compinations_counter):
        print('Kevin', vowel_compinations_counter )
    else:
        print('Draw')


s = 'BANANA'
minion_game(s)