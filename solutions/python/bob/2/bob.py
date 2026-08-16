def response(hey_bob):
    
    message = hey_bob.strip()
    question = message.endswith ("?")
    yell = message.isupper()
    if not message:
        return "Fine. Be that way!"
    if question and yell:
        return "Calm down, I know what I'm doing!"
    if question:
        return "Sure."
    if yell:
        return "Whoa, chill out!"
    else:
        return "Whatever."
 
