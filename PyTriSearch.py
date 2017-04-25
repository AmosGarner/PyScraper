import sys, requests, pyperclip
import webbrowser as browser

googleUrl = 'https://www.google.com/search?q='
connecter = '&'
imgSearchType = 'tbm=isch'

def main():
    if len(sys.argv) > 1:
        return False
    else:
        browser.open(googleUrl + 'cat' + connecter + imgSearchType)

if __name__ == '__main__':
    main()
