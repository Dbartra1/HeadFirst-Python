# creating the list for vowels 
vowels = ['a', 'e', 'i', 'o', 'u']
# creating an object for user input
word = str (input ("Please enter a word: "))
# creating a empty set for vowels to be placed in when found
found = []
# for loop for finding vowels in user input based on list of vowels 
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            
for vowel in found:
    print (vowel)