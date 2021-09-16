#rock paper scissor game
def random():
    import random
    randomcpu = random.randint(1, 3)
    if randomcpu == 1:
       cpu = 'rock'
    elif randomcpu==2:
       cpu = 'paper'
    else:
       cpu = 'scissor'
    userinput = input("choose 'rock' 'paper' or 'scissor'\n")
    game(cpu, userinput)
def game(cpu, userinput):
    #rock
   if cpu == "rock" and userinput == "rock":
        r = ("Draw")
        display(r, cpu, userinput)
   elif cpu == "rock" and userinput == "paper":
       r = ("You Win")
       display(r, cpu, userinput)
   elif cpu == "rock" and userinput == "scissor":
        r = ("Cpu Win")
        display(r, cpu, userinput)
    #paper
   elif cpu == "paper" and userinput == "scissor":
        r = ("You Win")
        display(r, cpu, userinput)
   elif cpu == "paper" and userinput == "paper":
        r = "Draw"
        display(r, cpu, userinput)
   elif cpu == "paper" and userinput == "rock":
        r = "Cpu Win"
        display(r, cpu, userinput)
    #scissor
   elif cpu == "scissor" and userinput == "rock":
        r = "You Win"
        display(r, cpu, userinput)
   elif cpu == "scissor" and userinput == "paper":
        r = "Cpu Win"
        display(r, cpu, userinput)
   elif cpu == "scissor" and userinput == "scissor":
        r = "Draw"
        display(r, cpu, userinput)
   else:
    r = "invalid input"
    display(r, cpu, userinput)
def display(r, cpu, userinput):
    print("cpu choose:", cpu)
    print("you choose:", userinput)
    print("Result:", r)
    random()
random()
