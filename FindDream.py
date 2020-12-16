import random
def checkNum(val, rand):
    if val==rand:
        print('Congrats! You guessed correctly. Somehow.')
        print('If this prints before the day I die, someone fucking tell me')
    if val!= rand:
        print('lol scrub git gud. you will never be as good as dream')
    print('the random number was:', rand)
    print('your number was:', val)
    print('-------------------------------')

    
def game():
    val = input("What is your number? ")
    
    try:
        float(val)
    except ValueError:
        print('please for the love of god i can only do numbers')
        print('im a mathematician for crying out loud. stop giving me')
        print('fucking arrays or strings or some dumb shit. jfc')
        print('like i legit have no idea what u entered means')
        return True
    
    val = float(val)
    
    rand = random.randint(1, 7500000000000)
    
    if type(val) is float:
        val = int(round(val, 1))

    if type(val) is int:
        if val==0:
            print('giving up??? knew ur not as good as drema lol. byeeee')
            return False
        
        elif val<1 or val>7500000000000:
            print("\n bruh you had one fucking job, ur number has to be between 1 and 7.5 trillion holy shit. Start over.")
            return True

        elif val==69:
            print('haha nice')
            checkNum(val, rand)
            return True

        elif val==420:
            print('lol ty')
            checkNum(val, rand)
            return True

        else:
            checkNum(val, rand)
            return True


print('Welcome to Can You Be As Lucky As Dream!')
print('I am your host, Terrence, but you can call me terry ;)')
print('It is a simple game, type a number between 1 and 7.5 trillion')
print('and I tell you if you were correct!')
print('if you put in a float, I will round your number')
print('Type 0 to exit the game! ty and pogchamp')

x = True
while x:
    x = game()
