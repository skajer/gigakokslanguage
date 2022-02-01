# X - konwertuje tekst jako odwórcony alfabet, Y - "dekodcuje" odwrócony tekst

def x(string):

    siema = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')
    return(string.translate(siema))

def y(string):
        
    siema = str.maketrans('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz')
    return(string.translate(siema))
 
while True:

    global guwno

    print('Wybierz funkcje: x lub y ')
    guwno = input()
    
    if guwno == "x":
        
        def japierdole():

            print("Enter text to convert: ")

            string = input() 
            x(string)
        
               
            #new_input == string
            return string, print(x(string))

        japierdole()


    if guwno == "y":
        
        def japierdole1():

            print("Enter text to convert: ")

            string = input() 
            x(string)
        
               
            #new_input == string
            return string, print(y(string))

        japierdole1()



















############################################################################################