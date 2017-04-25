import sys, pyperclip
import webbrowser as browser

mapsURL = 'https://www.google.com/maps/place/'
addr = '1046+Circle+Dr,+Seymour,+TN+37865'

def getAddressFromArguments(arguments):
    address = ''
    for argument in arguments:
        address += ' ' + argument
    return address

def getAddressFromClipboard():
    return pyperclip.paste()

def getWebReadyAddress(address):
    charArray = list(address)
    address = ''
    for character in charArray:
        if(character == ' '):
            address += '+'
        else:
            address += character
    return address

def main():
    address = ''
    if len(sys.argv) > 1:
        address = getAddressFromArguments(sys.argv[1:])
    else:
        address = getAddressFromClipboard()
    address = getWebReadyAddress(address)
    browser.open(mapsURL + address)

if __name__ == '__main__':
    main()
