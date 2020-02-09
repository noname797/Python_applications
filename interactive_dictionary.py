# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:42:40 2019

@author: noname
"""

#intereactive python dictionary

import json
from difflib import get_close_matches


data=json.load(open('data_dic.json'))
print ("Hello There")
def find_meaning(word):
    if (word in data):
        return data[word]
    elif (word.upper() in data):
        return data[word.upper()]
    elif (word.lower() in data):
        return data[word.lower()]
    elif (word.title() in data):
        return data[word.title()]
                 
    else:
        print( "Did you mean "+ "'"+ get_close_matches(word.lower(),data.keys())[0] +"'"+" ?")
        option=str(input("Yes or No ? ").lower())
        if option=='yes':
            return data[get_close_matches(word.lower(),data.keys())[0]]
        elif option=='no':
            return ("The word doesn't exists.")
        else:
            return ("Invalid selection")
while True:

                    
    word=str(input("Enter The Word : "))
    print(find_meaning(word))
    cont=str(input("Want to search for another word ? Yes or No ? ").lower())
    if cont=='yes':
        continue
    else:
        print("Thank You")
        break

#testing
