
#import wordscore function
import sys
import wordscore as ws

if (len(sys.argv) !=2):
    print("Need an argument. Example: python3 scrabble.py \"ZAEFIEE\"")
    exit(1)

#if our rack is less than 2 letters or greater than 7 letters
#print an error.
if(len(sys.argv[1]) < 2) or (len(sys.argv[1]) > 7):
    print("Please enter between 2-7 letters.")
    exit(1)

#if anything other than ? or * is used for wild cards, print an error. 
for w in sys.argv[1]:
    if not w.isalpha():
        if w == "?" or w == "*":
            pass
        else:
            print(letter,"character used. You can only use ? or * for wild cards")
            

#check if there are more than one ? in input             
wildcard1_count = sys.argv[1].count("?")
if wildcard1_count > 1:
    print("You can only use one ? as wildcard")
    exit(1)

#check if there are more than one * in input            
wildcard2_count = sys.argv[1].count("*")
if wildcard2_count > 1:
    print("You can only use one * as wildcard")
    exit(1)

#rename sys.argv[1] and capitalizing all letters 
rack = sys.argv[1].upper()

#designate wildcard_flag as False if empty
#and True if it has ? or *
wildcard_total = 0 
wildcard_flag = False

if "?" in rack:
    wildcard_total += 1
    wildcard_flag = True 
    
if "*" in rack:
    wildcard_total += 1
    wildcard_flag = True 
    

#open sowpods.txt words    
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]
    
#letter scores
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

#create a list and go through sowpod.txt and only taking the words that 
#are 2-7 letter and add them to the list.  
filtered_data = []
for dat in data:
    if (len(dat) >= 2) and (len(dat) <= 7):
        filtered_data.append(dat)
        

#create a new list         
word_tuples = []

#go through each word from the filtered list 
#set initial word validity as true 
#initialize wildcard_counter 
#initialize total_wildcard_score as 0.
for word in filtered_data:
    word_valid = True
    wildcard_counter = wildcard_total
    total_wildcard_score = 0 
    
    #create a new list and go through each letter in our rack. 
    #if all the characters are letters
    #then append them in the list. 
    list_rack = []
    for r in rack:
        if r.isalpha():
            list_rack.append(r)
    
    #if there is a wildcard
    #for character w in word
    #if it is in the rack list
    #remove the character 
    if wildcard_flag:
        for w in word:
            if w in list_rack:
                list_rack.remove(w)
                
            #otherwise if wildcared_counter equals 0 
            #word is not valid, then go to another word in filtered_data
            #else recall the function score_word from ws. 
            #then decrease the wildcard by 1
            else:
                if wildcard_counter == 0:
                    word_valid = False
                    break
                else: 
                    total_wildcard_score += ws.score_word(w,scores)
                    wildcard_counter -= 1
                    
    #if there is no wildcard
    #for character w in word, if it also exist in rack list
    #then the word is valid
    #remove the character
    else:
        for w in word:
            if w in list_rack:
                word_valid = True 
                list_rack.remove(w)
            
            #otherwise break because the word is not valid 
            #go to another word in filtered data
            else:
                word_valid = False
                break
                
    #if word_valid 
    #then recall the function score_word from ws and assign them as word_score
    #subtract total_wildcard_score
    #then append word_score and the word in our list. 
    if word_valid:
        word_score = ws.score_word(word,scores) - total_wildcard_score
        word_tuples.append((word_score, word.lower()))
        
        
#sort the word_tuple according to the score.         
word_tuples = sorted(word_tuples, key = lambda x: x[0], reverse = True)


 
#Display them shown
for tup in word_tuples:
    print("("+str(tup[0])+", "+tup[1]+")")  
    
print("Total number of words: "+str(len(word_tuples)))
