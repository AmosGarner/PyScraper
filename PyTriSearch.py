import sys, requests, pyperclip, argparse
import webbrowser as browser

googleUrl = 'https://www.google.com/search?q='
connecter = '&'
imgSearchFlag = 'tbm=isch'

def generateURLReadyKeywords(keywords):
    output = ''
    for character in list(keywords):
        if character == ',':
            output += '+'
        else:
            output += character
    return output

def main():
    parser = parser = argparse.ArgumentParser(description="Runs PyTriSearch googling utility.")
    parser.add_argument('--type', dest='search_type', required=False)
    parser.add_argument('--search', dest='keywords', required=True)
    arguments = parser.parse_args()

    if arguments.search_type == 'image' or arguments.search_type == 'i':
        browser.open(googleUrl + generateURLReadyKeywords(arguments.keywords) + connecter + imgSearchFlag)
    else:
        browser.open(googleUrl + generateURLReadyKeywords(arguments.keywords))

if __name__ == '__main__':
    main()
