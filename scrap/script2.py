# web scrapping code made by Rishabh Bhardwaj
# follow me at http://www.knoobypie.com/about-me/
# folow me on linkedin @https://www.linkedin.com/in/rishabh-bhardwaj-791903171/
# github https://github.com/rishabh3354

# <<<<<<<<-pre-requestie->>>>>>>>>>>>>>>>
# install the following python module:
# pip install requests
# pip install bs4
# output will be in html format, Recommended to save file in html format


import requests
from bs4 import BeautifulSoup
import sys


def getlyrics(url_str):

    url = url_str
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    try:
        response = requests.get(url, timeout=10, headers=headers)
        # print(response)


    except requests.ConnectionError as err:
        print("<<<<<<<<<<<< PLEASE CHECK YOUR INTERNET CONNECTION >>>>>>>>>>>>>>>>>>")
        # print(str(err))
    except requests.Timeout as err:
        print("OOPS!! Timeout Error")
        # print(str(err))
    except requests.RequestException as err:
        print("OOPS!! UNEXPECTED Error")
        # print(str(err))

    else:

        req = requests.get(url)

        soup = BeautifulSoup(req.content, "lxml")
        mm = str(soup)

        c = mm.count("<div>")
        pos = 0

        mydata = ""

        while c > 0:
            startpos = mm.find('<div>', pos, len(mm))
            endpos = mm.find('</div>', startpos, len(mm))
            startpos = startpos + 5
            mydata = mm[startpos:endpos]
            pos = endpos
            c -= 1
        print(mydata)
        # cleantext = BeautifulSoup(mydata, "lxml")
        # cleantext=cleantext.get_text()
        # sys.stdout.flush()
        return mydata


if __name__ == '__main__':
    url = ""
    # sys.stdout.flush()
    getdata = getlyrics(url)
    # sys.stdout.flush()