import sys
import webbrowser as browser

def getAddressFromArguments(arguments):
    return ''.join(arguments(1:])

def main():
    if len(sys.argv) > 1:
        getAddressFromArguments(sys.argv[1:])

    return False

if __name__ == '__main__':
    main()
