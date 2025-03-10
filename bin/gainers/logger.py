
def write_log(choice, message):
    try:
        with open('gainers.log', 'a') as errorfile:
            errorfile.write(choice.upper() + ' ' + message + '\n')
    except FileNotFoundError:
        with open(f'gainers.log', 'w') as errorfile:
            errorfile.write(choice.upper() + ' ' + message + '\n')

