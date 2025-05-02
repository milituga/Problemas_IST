# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 20:12:07 2025

@author: Miguel Pascoal, Rita Fernandes
"""

import webbrowser 

def count_words():
    # Get the sentence from the user
    sentence = input("Enter a sentence: ")
    
    # Split the sentence into words (splitting by spaces) with .split()
    words = sentence.split()
    
    # Count the number of words with len(words)
    num_words = len(words)
    
    # Return the number of words
    print(f"The number of words in the sentence is: {num_words}")
    
    if num_words < 20:
        print("Try typing more than 20 words for a surprise")
    else:
        url = "https://media1.tenor.com/m/yham-EkbRJ4AAAAd/cat-post-this-cat-when-they-least-expect-it.gif"
        webbrowser.open(url)

count_words()
