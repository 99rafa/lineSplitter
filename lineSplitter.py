from pathlib import Path
import sys

running = True

while running:
    print("What is the path of the css file you want to split? (q to exit)")
    file = input()

    if file == 'q':
        sys.exit()


    my_file = Path(file)
    output = ""

    if my_file.is_file():
        f = open(file,"r")
        for line in f:
            for char in line:
                if char == '{' or char == ';':
                    output += ' ' + char + '\n'
                elif char == '}':
                    output += '\n' + char +'\n\n'

                else:
                    output += char
        f.close()
        print("File splitted succesfully!")
        print("What is the path of the output css file?")
        file = input()
        o = open(file,"w")
        o.write(output)
        o.close()
        print("File saved succesfully!")


    else:
        print("Error: File does not exist, try again.")




    
