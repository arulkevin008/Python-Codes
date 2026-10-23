def al_to_mc(string):
    morse_dict = {
        # Letters
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
        "e": ".", "f": "..-.", "g": "--.", "h": "....",
        "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.",
        "q": "--.-", "r": ".-.", "s": "...", "t": "-",
        "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
        "y": "-.--", "z": "--..",
        # Numbers
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----."
    }

    converted_string = ""
    for i in string:
        if i in morse_dict:
            converted_string += morse_dict[i] + " "  
        elif i == " ":
            converted_string += "/ "  
        else:
            converted_string += "? "  
    return converted_string

string = input("Enter the string : ").lower()
print("The Given Input: ", string)
result = al_to_mc(string)
print("The Morse code: ", result)



