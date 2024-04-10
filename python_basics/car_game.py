interactive = ''
started = False

while True:
    interactive = input('>').lower()

    if interactive == 'start':
        if started:
            print('car is already started!')
        else:
            started = True
            print('The engine has started...voom vooom')
    elif interactive == 'stop':
        if not started:
            print('You have stopped the engine!')
        else:
            started = False
            print('The engine has stopped')
    elif interactive == 'quit':
        break
    elif interactive == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    else:
        print('Command not supported')

