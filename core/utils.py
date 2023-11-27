'''
Messages Related Functions
'''

import re

LoggedMessages = {}

def printAcknowledgeMessage():
    printInputMessage('Acknowledge: (Enter)')
    print()

def printErrorMessage(message, acknowledge=True, separator='\n'):
    printBoxedMessage('ERROR', message, separator=separator)
    if acknowledge is True:
        printAcknowledgeMessage(True)

def printStatusMessage(message, inline=False, force=False, label='STATUS'):
    if label is not None:
        label += ': '
    else:
        label = ''

    print(f'{label}{message}', end=("" if inline is True else None), flush=True)

def printFatalMessage(message):
    printBoxedMessage('FATAL', message)
    printAcknowledgeMessage()
    exit('FATAL ERROR OCCURRED')

def printBoxedMessage(base, Messages, separator='\n', break_line=True):
    char_split = 140

    if not isinstance(Messages, list):
        Messages = [Messages]

    FinalMessages = []
    for index, message in enumerate(Messages):
        _message = (base + ': ' if index == 0 else f'{index}: ') + message
        if len(_message) < char_split:
            spacing = "".join([' ' * int(((char_split - len(_message)) / 2))])
            _message = (spacing + _message + spacing)[:char_split - 1]

        if break_line is True:
            FinalMessages.append(re.sub("(.{" + str(char_split) + "})", "\\1\n", _message, 0, re.DOTALL))
        else:
            FinalMessages.append(_message)

    spacer = "".join(['!' * char_split])
    print(f'\n{spacer}\n' + f"{separator}".join(FinalMessages) + f'\n{spacer}\n')

def printInputMessage(message):
    print('INPUT: ' + message)
    input_prepend = " >>  "
    return input(input_prepend)

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


''''###############################################################################################'''
