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
#this function is copied from SimulationCore.py mostly because InterfaceCore shouldn't use that module, this function should have it's own module
def SplitStringIntoList(string):
    li = list(string.split(" "))
    return li


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
        
        #handle interactive mode
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

            print("Running sim, close the window, or type ")
            result = subprocess.run(["python", "ElectricFieldSimulation.py", posarg, "", "", "", qarg, str(amount)], capture_output=True, text=True)
            #print(result.stdout)
            #print(result.stderr)
        
        #non interactive mode
        elif line[:11] == "--arguments": 
            passedargs = line[13:]
            tempstring = ""
            listofargs = []
            # check if starting and ending chars were passed correctly, it couldn't be done before, because the code that handles
            # making user input correct for the program, needs to have those
            if passedargs[:2] != "[[" and passedargs[-2:] != "]]":
                print("print help EfSim here")
                return
            
            # making input correct for program
            for i in passedargs:
                if i == "[":
                    continue
                elif i != "]":
                    if i == ',':
                        i = ""
                        #continue
                    tempstring += i
                    
                elif i == "]":
                    listofargs.append(tempstring)
                    tempstring = ''
            
            #this is really stupid, but I couldn't bother to rewire this code, what it does is that while passing the args like so [[args],[args]] a third string with nothing
            #inside is created, so we just pop it so that there's no bugs. This is inefficient, the function should have been written so that this doesn't need to be done
            if len(listofargs) >= 3:
                listofargs.pop()
            print(listofargs)
            
            
            #this code is REALLY unreadble and probably very inefficient, this should be rewritten sometime, probably.
            #also, this should be made into an inner function, as it can be used to check for kind of mode used, at least in EFSim
            #checking if passedargs are correct
            
            for i in listofargs:
                pausecounter = 0
                index = -1
                for n in i:
                    index += 1
                    if n != ',':
                        if n != ' ':
                            if n == '-':
                                continue
                            # if its not a special char, check if it is a number
                            try:
                                x = int(n)
                            except:
                                print("print help EfSim here")
                                return
                        else:
                            #if first char is pause, return
                            if index == 0:
                                print("print help EfSim here")
                                return
                            pausecounter += 1
                if pausecounter != 2:
                    print("print help EfSim here pauses")
                    return
            

            print("Running sim, close the window, or type ")   
            
            #this is some messy code, should be fixed
            ghb = ""
            amounts = len(listofargs)
            possarg = ""
            for i in listofargs:
                ghb += SplitStringIntoList(i)[0] + " "
                possarg += SplitStringIntoList(i)[1] + " " + SplitStringIntoList(i)[2] + " "

            #temp code to implement the input of x and y of the test charge, this code should be used in interactive mode, not "argument" mode
            xtest = input("Input x pos of test charge ")
            ytest = input("Input y pos of test charge ")
            
            result = subprocess.run(["python", "ElectricFieldSimulation.py", possarg, "", "", "", ghb, str(amounts),(xtest + " " + ytest) ], capture_output=True, text=True)
            return
        elif line[:2] == "-a":
            passedargs = line[2:]
            print("no other args yet quitting")
            return
        else:
            print("print help EfSim here")
            return
        
        #change the order of the inputs, right now they are NOT inputted the same way as when creating a new class
        #result = subprocess.run(["python", "ElectricFieldSimulation.py", "680 320 100 200", "blue red", "20000000000000 1000000000000", "0 0 1 -1", "1 -2"], capture_output=True, text=True)
        #no need to pass colors here, those will be chosen inside electricfieldsim or the simcore depending on the implementation
        #no need to pass mass here, it's unneded in this sim
        #result = subprocess.run(["python", "ElectricFieldSimulation.py", posarg, "", "", "", qarg, str(amount)], capture_output=True, text=True)
        print("Closing simulation")

if __name__ == '__main__':
    Gui().cmdloop()