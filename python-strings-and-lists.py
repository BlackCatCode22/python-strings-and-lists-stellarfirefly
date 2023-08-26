# Jay C. Parangalan, CIT-95 Fall 2023
# Python Strings and Lists

# text string for testing
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."

#---- functions

# find text length, basically just a wrapper around len()
def calculate_length(text):
    return len(text)

# return both uppercase and lowercase versions of text
def upper_and_lower(text):
    return text.upper(), text.lower()

# reverse individual words in the string
# note that punctuation is included as part of the words
def reverse_words(text):
    first_word = True
    words = text.split()
    new_string = ""
    for word in words:
        if first_word == True:      # add a space separator only after the first word
            new_string = word[::-1]
            first_word = False
        else:
            new_string += " " + word[::-1]
    return new_string

# count occurrances of a character
def char_count(text, char):
    return text.count(char)

def remove_from_list(list, to_remove):
    return [item for item in list if item != to_remove]

#---- start of program

print("The test text is:")
print(text)
print()

#---- string tasks

def perform_string_tasks():
    # length
    print("The length of the text is", calculate_length(text),"characters.")

    # upper and lower
    text_upper, text_lower = upper_and_lower(text)
    print("Uppercase version:", text_upper)
    print("Lowercase version:", text_lower)

    # split into words
    word_list = text.split()
    num_words = len(word_list)
    print("Number of words:", num_words)

    # get substring
    substring_start = int(input("Starting index of substring: "))
    substring_end = int(input("Ending index of substring: "))
    print("Substring: \"" + text[substring_start:substring_end] + "\"")

    # replace substring
    old_string = input("Old text to replace: ")
    new_string = input("New text: ")
    print("Replaced string:", text.replace(old_string, new_string))

    # whitespace removal
    print("Leading and trailing whitespace removed:", text.strip())

    # split into sentences
    # TODO: not sure yet if we can assume all sentences are
    # separated by periods, or if we have to account for all
    # common punctuation (question marks, exclamation points)

    # reverse individual words
    print("Words reversed:", reverse_words(text))

    # character count
    char_to_count = input("Enter character to count: ")
    print("That character occurs", char_count(text, char_to_count), "times.")

    # substring count
    # the char_count() function also correctly counts substrings
    substr_to_count = input("Enter substring to count: ")
    print("That substring occurs", char_count(text, substr_to_count), "times.")

print("---- string tasks")
perform_string_tasks()    # comment out to test only the list tasks
print()

#---- list tasks

def perform_list_tasks():
    word_list = text.split()

    # append to word list
    word_list.append("Pythonic")

    # insert at beginning of word list
    word_list.insert(0, "awesome")

    # print third word in the list
    print("The third word in the list is: ", word_list[2])

    # print 6th through 9th words in the list
    print("The 6th through 9th words in the list are:", word_list[6:10])

    # remove "amazing" from the list
    word_list = remove_from_list(word_list, "amazing")

    # sort the word list in alphabetical order
    word_list.sort()

    # count occurrences of "is"
    print("The word \"is\" occurs", word_list.count("is"), "times.")

    # join current state of word list with spaces
    print("The word list so far is: "," ".join(word_list))

    # reverse the order of the list
    word_list.reverse()

    # make a copy of the list
    copied_list = word_list
    word_list = []  # empty out the original list, should not affect copy
    print("The final state of the list is:", copied_list)

print("---- list tasks")
perform_list_tasks()    # comment out to test only the string tasks
print()
