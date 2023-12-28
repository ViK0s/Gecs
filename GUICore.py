import cmd, sys
import subprocess

"""def CheckForMultipleArgs(line:str):
    if type(line) != str:
        print("bad args")
        return
    else:
        if line[0] != '-':
            print("no args passed, or bad args")
        elif line[0] == '-':
            for i in line:"""


welcomeMessage = open("WelcomeMessage.txt", "r")
helpMessagetemp = open("HelpMessage.txt", "r")
helpMessage = helpMessagetemp.read()
running = False
class Gui(cmd.Cmd):
    intro = welcomeMessage.read()
    prompt = '>> '
    #doc_header = helpMessage.read()
    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True
    
    def do_help(self, line):
        """Show more information about the program"""
        print(helpMessage)

    #def help_hello(self):
    #    print("bruh")

    # aliasing
    do_exit = do_quit

    def do_NbodySim(self, line):
        """run the sim"""
        print("Running sim, close the window, or type ")
        #make a function, that makes it so that the last char is not an empty space
        if line == '--interactive' or line == "-i":
            print("Running interactive mode")
            
        
        #change the order of the inputs, right now they are NOT inputted the same way as when creating a new class
        result = subprocess.run(["python", "GravitySimulation.py", "680 320 100 200", "blue red", "20000000000000 1000000000000", "0 0 1 -1", "1 -2"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        print("Closing simulation")

    def do_EFSim(self, line):
        """run the sim"""
        posarg = ""
        qarg = ""
        if line == '--interactive' or line == "-i":
            print("Running interactive mode")
            print("pass the amount of bodies you want in the sim")
            amount = input()
            #WARNING, no check for if the passed args were okay
            for i in range(int(amount)):
                print("pass the q of the " + str(i+1) + " body")
                q = input()
                print("pass the x of the " + str(i+1) + " body")
                x = input()
                print("pass the y of the " + str(i+1) + " body")
                y = input()

                #concatenate the string so it can be passed as an arg for the subprocess
                posarg += x + " " + y + " "
                
                qarg += q + " "
        else:
            print("no other args yet quitting")
            return
        print("Running sim, close the window, or type ")
        #change the order of the inputs, right now they are NOT inputted the same way as when creating a new class
        #result = subprocess.run(["python", "ElectricFieldSimulation.py", "680 320 100 200", "blue red", "20000000000000 1000000000000", "0 0 1 -1", "1 -2"], capture_output=True, text=True)
        #no need to pass colors here, those will be chosen inside electricfieldsim or the simcore depending on the implementation
        #no need to pass mass here, it's unneded in this sim
        result = subprocess.run(["python", "ElectricFieldSimulation.py", posarg, "", "", "", qarg, str(amount)], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        print("Closing simulation")

if __name__ == '__main__':
    Gui().cmdloop()