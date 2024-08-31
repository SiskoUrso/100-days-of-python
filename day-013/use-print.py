#Pause 1 The code is supposed to calculate the total number of words given the number pages and the word per page. But it's not currently giving any output. Diagnose the problem using print() statements.

#Orginal Code

# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Using print() to determine the breakdown of the code

# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page == int(input("Number of words per page: "))  # using print we find that this is where the issue is as it is printing out 0 due to the variable not being defined and instead using ==. 
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# Fixed code 

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
