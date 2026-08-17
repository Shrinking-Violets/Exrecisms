import re
def translate_word(text):
    if re.match(r"^(?:[aeiou]|xr|yt)", text):
        return text+"ay"
    
    match = re.match(r"^([^aeiou]*qu)", text)
    if match:
        prefix = match.group(1)
        return text[len(prefix):] + prefix + "ay"
    match = re.match(r"^([^aeiou]+)y", text)
    if match:
        prefix = match.group(1)
        return text[len(prefix):] + prefix + "ay"
    match = re.match(r"^([^aeiou]+)", text)
    if match:
        prefix = match.group(1)
        return text[len(prefix):] + prefix + "ay"   
    return text
def translate(text):
    return " ".join(translate_word(text) for text in text.split())       
        
        
