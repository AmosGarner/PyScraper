# PyScraper
WEb scraper utilities built with python

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
     * [Pyperclip](https://pypi.python.org/pypi/pyperclip):Cross platform clipboard module
     * [Webbrowser](https://docs.python.org/2/library/webbrowser.html): Web browser module capable of opening broswer windows.
     
