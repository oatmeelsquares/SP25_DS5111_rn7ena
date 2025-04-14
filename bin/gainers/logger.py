'''
    A simple function to write to logs in the correct place for my
    project.

    Will consider shifting to python logging package, but this small
    function is all I need for the moment.
'''

def write_log(choice, message):
    try:
        with open('gainers.log', 'a') as errorfile:
            errorfile.write(choice.upper() + ' ' + message + '\n')
    except FileNotFoundError:
        with open(f'gainers.log', 'w') as errorfile:
            errorfile.write(choice.upper() + ' ' + message + '\n')

