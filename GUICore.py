import cmd, sys
import subprocess

welcomeMessage = open("WelcomeMessage.txt", "r")
helpMessage = open("HelpMessage.txt", "r")
esa = helpMessage.read()
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
        print(esa)

    def do_run(self, line):
        """run the sim"""
        print("Running sim, close the window, or type ")
        result = subprocess.run(["python", "GravitySimulation.py", "680 320 100 200", "blue red", "20000000000000 1000000000000", "0 0 1 -1"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        print("Closing simulation")

if __name__ == '__main__':
    Gui().cmdloop()