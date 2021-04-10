'''

generic script for compiling software

'''

import PyInstaller.__main__


def install(file_name, program_name):
    PyInstaller.__main__.run([
        file_name,
        '--onefile',
        '--clean',
       ('-n'+program_name)
    ])


def main():
    file_loop = 1
    name_loop = 1
    while file_loop:
        file_name = input("Please input [file.py]\n\n")
        print("File Name Entered: [",file_name ,"] is this correct?\n")
        user_input = input("[ y ] / [ n ] ?\n")
        if if_input_yes(user_input):
            file_loop = 0
        while name_loop:
            program_name = input("Please insert [Name] of software package\n\n")
            print("Program Named: [",program_name ,"] is this correct?\n")
            user_input = input("[ y ] / [ n ] ?\n")
            if if_input_yes(user_input):
                name_loop = 0
        print("Building Software Package... Please Stand By\n\n")
        try:
            install(file_name, program_name)
        except:
            print("Software Build Failed, check foundations. Exiting...\n\n")

            
                
def if_input_yes(user_input):
    if user_input.lower()=="y" or user_input.lower()=="yes":
        return True
    else:
        return False



if __name__ == "__main__":
    main()

