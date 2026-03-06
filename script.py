my_script = "Welcome back! Today we are looking at the newest GTA 6 map leaks. map"

words_list = my_script.split()
total_words = len(words_list)

print("SUCCESS! The code is running.")

words_list = my_script.split()
total_words = len(words_list)

print("SUCCESS! The code is running.")
print("Total words in the script:", total_words)

keyword_count = my_script.count("map")
print("Times the word'map'appears in the script: ", keyword_count)

#lower 
my_script2 = "Welcome back! Today we are looking at the newest GTA 6 map leaks."
clean_script = my_script2.lower()
total_word = len(clean_script)
print ("total word in the script :",total_word)
user_input = input("what word do ypu want to  search for ?")
clear_word =  user_input.lower()
keyword_count2 = clean_script.count(clear_word)
print("times the word used :",keyword_count2)