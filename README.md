# PyScraper
Web scraper utilities built with python.

## Project Info:
* Name: PyScraper
* Version: 0.2
* Author: Amos Garner
* License: MIT

## Install Commands:
Clone project repository into project directory:
```git clone git@github.com:AmosGarner/PyScraper.git```

## Utilities:
* PyMap: Search for an address in Google Maps.
   * Arguments:
     * None: will use last value copied to clipboard as the address
     * Address: Enter in a value and the script will use that value to search google maps.
   * Example: ```python PyMap.py 60 Rue Caulaincourt Paris France```
   * Dependencies:
     * [pyperclip](https://pypi.python.org/pypi/pyperclip):Cross platform clipboard module
     * [webbrowser](https://docs.python.org/2/library/webbrowser.html): Web browser module capable of opening broswer windows.

* PySearch: Preforms a standard or image search on google agains user provided keywords and opens the top N results in your default browser.
  * Arguments:
    * search: Searches google with the comma separated keywords provided by the user.
    * total: Augments the number of results returned to the user. (Optional)
    * type: Sets the search type that google does. (Optional)
  * Example: ```python PySearch.py --search agamerstudios,amos,garner --total 3```
  * Example: ```python PySearch.py --type i --search agamerstudios,amos,garner ```
  * Dependencies:
    * [pyperclip](https://pypi.python.org/pypi/pyperclip):Cross platform clipboard module
    * [webbrowser](https://docs.python.org/2/library/webbrowser.html): Web browser module capable of opening browser windows.
    * [argparser](https://docs.python.org/3/library/argparse.html): Parses arguments provided by the user into objects
    * [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Python module used for parsing and selecting html elements
    * [requests](http://docs.python-requests.org/en/master/): Gets data from a request to a server and the response from that server.
