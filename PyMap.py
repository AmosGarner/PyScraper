import sys, pyperclip
import webbrowser as browser

def getAddressFromArguments(arguments):
    address = ''
    for argument in arguments:
        address += ' ' + argument
    return address

def getAddressFromClipboard():
    return pyperclip.paste()

def main():
    address = ''
    if len(sys.argv) > 1:
        address = getAddressFromArguments(sys.argv[1:])
    else:
        address = getAddressFromClipboard()

    print(address)

if __name__ == '__main__':
    main()
