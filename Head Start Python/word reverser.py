def wordReverse(word):
    new_word = ''.join(word)
    print (new_word[ : : -1])
    
def main():
    print ("Welcome to Dillon's Word Reverser!!")
    choice1 = 'y'
    while choice1.lower() == 'y':
        word = str (input("\nWhat word or phrase would you like reversed?: "))
        wordReverse(word)
        print()
        choice1 = str(input("Would you like to reverse a new word or phrase? (y/n): "))
        if choice1 != 'y':
            print ("\nBYE!!!!!")
            break

if __name__ == "__main__":
    main()
