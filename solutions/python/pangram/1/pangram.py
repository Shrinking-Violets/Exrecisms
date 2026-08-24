def is_pangram(sentence):
    alphabet = set()

    for char in sentence.lower():
        if char.isalpha():
            alphabet.add(char)

    return len(alphabet) == 26
            
        
        
           
