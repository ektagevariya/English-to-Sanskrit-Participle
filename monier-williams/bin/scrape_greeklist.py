"""

The Greek words used by the MW dictionary are defined on a web page. This
script scrapes the web page then prints the data in CSV format to stdout.
"""

import os
import sys

from bs4 import BeautifulSoup


def main():
    assert len(sys.argv) > 1
    filename = sys.argv[1]
    soup = BeautifulSoup(open(filename).read())
    print 'L,betacode,index'
    for row in soup('table', {'class': 'maintable'})[0].tbody('tr'):
        L_element = row('td', {'class': 'Ltd'})
        if not L_element:
            continue

        L = L_element[0].string
        # `L` fully specifies `key`.
        # key = row('td', {'class': 'keytd'})[0].string
        greek_betacode_list = row('td', {'class': 'beta'})
        # `greek_betacode` fully specifies `greek_unicode`.
        # greek_unicode = row('td', {'class': 'greek'})

        for i, betacode in enumerate(greek_betacode_list):
            # In monier.xml, betacode entries are 1-indexed.
            print '{},{},{}'.format(L, betacode.string, i + 1)


if __name__ == '__main__':
    main()
