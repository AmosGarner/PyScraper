import sys, requests, pyperclip, argparse, bs4
import webbrowser as browser

googleUrl = 'https://www.google.com/search?q='
connecter = '&'
imgSearchFlag = 'tbm=isch'
CONST_NUM_RESULTS = 5

def getRawSearchResults(keywords):
    res = requests.get(googleUrl + generateURLReadyKeywords(keywords))
    res.raise_for_status()
    searchResultsHTML = bs4.BeautifulSoup(res.text, 'html.parser')
    results = searchResultsHTML.select('.r a')
    print '%s  returned, here are the top %s!' % (searchResultsHTML.select('#resultStats')[0].text, len(results))
    return results

def generateArgumentsFromParser():
    parser = parser = argparse.ArgumentParser(description="Runs PyTriSearch googling utility.")
    parser.add_argument('--type', dest='search_type', required=False)
    parser.add_argument('--search', dest='keywords', required=True)
    parser.add_argument('--total', dest='total_results', required=False)
    return parser.parse_args()

def generateURLReadyKeywords(keywords):
    output = ''
    for character in list(keywords):
        if character == ',':
            output += '+'
        else:
            output += character
    return output

def main():
    arguments = generateArgumentsFromParser()

    if arguments.search_type == 'image' or arguments.search_type == 'i':
        browser.open(googleUrl + generateURLReadyKeywords(arguments.keywords) + connecter + imgSearchFlag)
    else:
        if arguments.total_results is None:
            arguments.total_results = CONST_NUM_RESULTS

        browser.open(googleUrl + generateURLReadyKeywords(arguments.keywords))
        results = getRawSearchResults(arguments.keywords)

        if len(results) >= int(arguments.total_results):
            results = results[:int(arguments.total_results)]

        for result in results:
            result = result.get('href').split('&sa=')[0].strip('/url?q=')
            resultPrefix = result.split(':')[0]
            if resultPrefix == 'http' or resultPrefix == 'https':
                browser.open(result)
            else:
                print('url: Invalid URL pattern!')

if __name__ == '__main__':
    main()
