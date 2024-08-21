import random   
import secrets 

def generatingText(length) -> str:
        
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    
    lower_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
     
    upper_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
     
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', 
                   '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', 
                   '?', '@', '[', '\\', ']', '^', '_', '`','{', '|', 
                   '}', '~']
    
    text = ''.join((secrets.choice(digits + lower_characters + upper_characters + punctuation)) for i in range(length))
    
    return text
    
