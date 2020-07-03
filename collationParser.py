# coding=utf-8

"""
STCN Collation Parser

Works on the collation formula that are used in the STCN
(https://www.kb.nl/organisatie/onderzoek-expertise/informatie-infrastructuur-diensten-voor-bibliotheken/short-title-catalogue-netherlands-stcn)

Inspired by https://github.com/albertmeronyo/CollationParser.

---

MIT License

Copyright (c) 2017 Leon van Wissen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging
import re
from itertools import cycle


class CollationParser:
    """
    Initializes a CollationParser object. Feed the .parse() function with a
    string to get the amount of folia. It prints the sections.
    """

    def __init__(self, verbose=False):
        """
        """

        if verbose:
            logging.basicConfig(format='%(message)s', level=logging.DEBUG)

        decodestring = "abcdefghiklmnopqrstvxyz"  # j, u and w removed
        self.decodestring = decodestring + decodestring.upper()

    def parse(self, s, use_parselist=False):
        """
        Parse function. Call with collation formula (string) as argument. It
        returns the amount of folia. Or specify `use_parselist` if you want
        more information on the individual collates. Then the output is a
        tuple of folia, parselist (list with dicts).

        :param s: collation formula (str)
        :param parselist:   return parselist with parse information (e.g. for
                            web interface or debug) as second variable in
                            return statement. (default False)
        :return: amount of folia (int)
        """

        folia = 0

        # To keep track of collates and sizes
        parselist = []

        logging.info(s)


        r = re.compile(
            r"""
# Met informatie erbij
  
# Zoek eerst naar een ongesigneerd vel met de vorm (cijfer)([letter])(cijfer) of (letter)(cijfer,cijfer,cijfer) of varianten hiervan.          
(?:(?<!-)(?P<ONGESIGNEERD>(?:(?:\d+)?\[?[χ*πa-zA-Z]+]?(?:\d{1,2}(?:,?\d?)+)+)+))|

# Zoek daarna naar dubbelkaternen en herhalingen.
(?:`SUP`(?P<DUBBEL>[χπ]+?)`LO`(?P<DUBBELKATERN>[^\d\s]+?) )?(?:`SUP`(?P<HERHALING>[\dχπ]+?)`LO`)?

# Zoek daarna naar een normaal katern met een startletter en mogelijk een eindletter. 
(?P<KATERN_START>[^ `\"\n]+?)(?:-(?P<KATERN_END>[^ `\n]+?))?

# Dit wordt altijd afgesloten met een formaatnotatie die bestaat uit één of meerdere cijfers.
(?:`SUP`(?P<FORMAAT>(?:\d+?)|

# Maar de notatie kan ook een slash (/) bevatten, die aangeeft dat de katernen volgens deze formaten (e.g. 8/4) ingebonden zijn.  
(?:\d+?(?:\/\d+)+?))`LO`)+?|

# Er kunnen ook losse gesigneerde bladen zijn
(?:(?P<GESIGNEERDE_LOSSE_BLADEN>(?P<KATERN_START_LOS>[^# `\"\n]+?)(?:-(?P<KATERN_END_LOS>[^ `\n]+?))?))1|

# Eventueel is er een correctienotatie, waarbij een blad van een katern ontbreekt.
(?:\((?P<CORRECTIE>-.*?)\))|

# En als er nog commentaar toegevoegd is, dan wordt dat ook meegenomen. 
(?:\((?P<COMMENTAAR>[^-]*?)\))
            """, re.VERBOSE
            )

        entries = [m.groupdict() for m in r.finditer(s)]

        for e in entries:
            size = 0

            logging.info("")
            logging.info({k:v for k,v in e.items() if v is not None})

            if e['KATERN_START'] and e['KATERN_END']:

                openingbrackets = '(['
                closingbrackets = ')]'

                if (e['KATERN_START'][0] in openingbrackets
                    and e['KATERN_START'][-1] in closingbrackets):
                    e['KATERN_START'] = e['KATERN_START'][1:-1]
                elif (e['KATERN_START'][0] in openingbrackets
                      and e['KATERN_END'][-1] in closingbrackets):
                    e['KATERN_START'] = e['KATERN_START'][1:]
                    e['KATERN_END'] = e['KATERN_END'][:-1]
                if (e['KATERN_END'][0] in openingbrackets
                    and e['KATERN_END'][-1] in closingbrackets):
                    e['KATERN_END'] = e['KATERN_END'][1:-1]

                # Example: <***>1 and <***>38
                if '<' in e['KATERN_START'] and '>' in e['KATERN_START']:
                    s_start, n_start = re.findall(r'(?:<([^ ]+)>)?(\d+)?',
                                                  e['KATERN_START'])[0]
                else:
                    n_start, s_start = re.findall(r'(\d+)?([^ ]+)?',
                                                e['KATERN_START'])[0]

                if '<' in e['KATERN_END'] and '>' in e['KATERN_END']:
                    s_end, n_end = re.findall(r'(?:<([^ ]+)>)?(\d+)?',
                                                  e['KATERN_END'])[0]
                else:
                    n_end, s_end = re.findall(r'(\d+)?([^ ]+)?', e['KATERN_END'])[0]


                if not n_start:
                    n_start = 1
                else:
                    n_start = int(n_start)
                if not n_end:
                    n_end = 1
                else:
                    n_end = int(n_end)

                logging.info('n_start: {} \t s_start: {}'.format(n_start,
                                                                 s_start))
                logging.info('n_end: {} \t s_end: {}'.format(n_end, s_end))

                # In case of changing size in collate
                if "/" in e["FORMAAT"]:
                    changing_sizes = e["FORMAAT"].split("/")

                    decodestring = self.decodestring[:23]

                    if n_start == n_end:
                        if s_start == s_end and '*' in s_start:
                            letters = ['*', '**'] # correct?
                        else:
                            letters = decodestring[decodestring.index(s_start.lower()):decodestring.index(s_end.lower()) + 1]
                    elif n_end > n_start:
                        if s_start == s_end and ('*' in s_start or s_start == ''):
                            letters = '*' * (n_end - n_start)
                        else:
                            letters = decodestring[decodestring.index(s_start.lower()):] + decodestring * (n_end - n_start -1) + decodestring[:decodestring.index(s_end.lower())+1]
                    elif n_end < n_start and n_end == 0:
                        n_end = n_start #guess
                        s_end = 'O' #typo?
                        letters = decodestring[decodestring.index(s_start.lower()):] + decodestring * (n_end - n_start -1) + decodestring[:decodestring.index(s_end.lower())+1]
                    else:
                        logging.info('Cannot parse {s} ({e})'.format(s=s, e=e))

                    dummycollates = zip(letters, cycle(changing_sizes))

                    for _, c_size in dummycollates:
                        size += int(c_size)

                    e['OMVANG'] = size
                    parselist.append(e)

                    folia += size

                    logging.debug('Method: Changing collate sizes')
                    logging.info("Cumulatief aantal: {}\n---".format(folia))

                    continue

                # Begin and end collation mark
                elif (e['KATERN_START'] in self.decodestring
                    and e['KATERN_END'] in self.decodestring):

                    start = self.decodestring.index(e['KATERN_START'].lower())
                    end = self.decodestring.index(e['KATERN_END'].lower())
                    size = end - start + 1 #  inclusive

                    logging.debug('Method: Begin and end collation mark')

                # Just one collation mark in group
                elif (s_start == s_end
                      and s_start not in self.decodestring):

                    size = n_end - n_start + 1 #  inclusive

                    logging.debug('Method: Just one collation mark in group')

                # If the group exceeds the alphabet and starts over
                elif (s_start in self.decodestring
                      and s_end in self.decodestring
                      and s_start != ''
                      and s_end != ''):

                    start = self.decodestring.index(s_start.lower())
                    end = self.decodestring.index(s_end.lower())

                    logging.debug("Start index: {} \nEnd index: {}".format(start, end))

                    if end < start:
                        size = 23 - (start - end) * (n_end - n_start) + 1
                    elif n_end == n_start:
                        size = end - start + 1
                    elif end == start:
                        size = 23 * (n_end - n_start) + 1 # inclusive
                    elif end > start:
                        size = (end - start + 1) + 23 * (n_end - n_start)
                    else:
                        logging.info(s)
                        raise EnvironmentError

                    logging.debug(
                        'Method: Group exceeds the alphabet and starts over'
                        )

                # In case of no letters
                elif s_start == '' and s_end == '':
                    size = n_end - n_start + 1

                    logging.debug('Method: no letters')

                logging.info("Formaat: {}\tOmvang:{}".format(e['FORMAAT'],
                                                             size))
                folia += int(e['FORMAAT']) * size

            # Just one collate
            elif e['KATERN_START']:
                try:
                    folia += int(e['FORMAAT'])
                except ValueError:
                    logging.info('Cannot parse {s} ({e})'.format(s=s, e=e))
                size = 1

            # Unsigned comment
            elif e['ONGESIGNEERD']:

                if ',' in e['ONGESIGNEERD']:
                    try:
                        size = int(e['ONGESIGNEERD'].split(',')[-1])
                    except ValueError:
                        size = int(re.split(r'[χ*π\[a-zA-Z\]]+', e['ONGESIGNEERD'].split(',')[0], 1)[1])
                else:
                    size = int(re.split(r'[χ*π\[a-zA-Z\]]+', e['ONGESIGNEERD'], 1)[1])

                folia += size
                e['OMVANG'] = size

            elif e['GESIGNEERDE_LOSSE_BLADEN']:

                if (e['KATERN_START_LOS'] in self.decodestring
                    and e['KATERN_END_LOS'] in self.decodestring):

                    start = self.decodestring.index(e['KATERN_START_LOS'].lower())
                    end = self.decodestring.index(e['KATERN_END_LOS'].lower())
                    size = end - start + 1 #  inclusive

                    folia += size

                    logging.debug('Method: Begin and end collation mark of unsigned leaves')


            # Correction
            elif e['CORRECTIE']:
                folia -= 1
                size = -1

            # Further comments
            elif e['COMMENTAAR']:
                logging.info('Commentaar: {}'.format(e['COMMENTAAR']))

            logging.info("Cumulatief aantal: {}\n---".format(folia))

            # for parselist information (e.g. in the web interface)
            if e['FORMAAT']:
                try:
                    e['OMVANG'] = size * int(e['FORMAAT'])
                except ValueError:
                    logging.info('Cannot parse {s} ({e})'.format(s=s, e=e))

            parselist.append(e)

        logging.info("\nFolia: {}".format(folia))

        if use_parselist:
            return folia, parselist
        else:
            return folia

if __name__ == "__main__":
    cp = CollationParser(verbose=True)

    # Examples
    # print(cp.parse("1#π1,2,3 A-H`SUP`12/8/4`LO`", use_parselist=True) )

    # print(cp.parse(")(-2)(`SUP`2`LO`",  use_parselist=True))

    # print(cp.parse("*1",  use_parselist=True))

    # print(cp.parse("[*]1 2*1 3*1 and 67 engraved folia",  use_parselist=True))

    print(cp.parse("π1,2 *1,2,3 A-H1 and engraved folia", use_parselist=True))





    # cp.parse("π1 †-3†`SUP`12`LO` *`SUP`2`LO` a-e`SUP`12`LO` A-K`SUP`12`LO` `SUP`2`LO`†`SUP`2`LO` χ1 L-2C`SUP`12`LO` 2D`SUP`2`LO` 2χ1 2E-3D`SUP`12`LO` 3E`SUP`4`LO` `SUP`2`LO`A`SUP`2`LO` 3χ1 3F`SUP`8`LO` 3G-4B`SUP`12`LO` 4C`SUP`4`LO` `SUP`2`LO`*`SUP`2`LO` 4χ1 4D`SUP`8`LO` 4E-4Z`SUP`12`LO` 5A`SUP`2`LO` 5χ1 5B-5S`SUP`12`LO` 5T`SUP`4`LO` `SUP`3`LO`*`SUP`2`LO` 6χ1 5V`SUP`8`LO` 5X-6X`SUP`12`LO` 6Y`SUP`4`LO` 6Z`SUP`2`LO` 7χ1 7A-7S`SUP`12`LO` 7T`SUP`6`LO` `SUP`4`LO`*`SUP`2`LO` 8χ1 7V`SUP`6`LO` 7X-8I`SUP`12`LO` 8K`SUP`10`LO` `SUP`5`LO`*`SUP`2`LO` 9χ1 8L`SUP`2`LO` 8M-9D`SUP`12`LO` 9E`SUP`10`LO` 10χ1 11χ1 9G`SUP`2`LO` 9H-9V`SUP`12`LO` 9X`SUP`4`LO` (3E4, 9X4 blank)")
    #cp.parse("*`SUP`4`LO` A-5S`SUP`4`LO` (A)-(2D)`SUP`4`LO` *`SUP`4`LO`(-*4) 2*`SUP`4`LO` A-2F`SUP`4`LO` 2G1 *`SUP`4`LO` A-3R`SUP`4`LO` π`SUP`2`LO` *-4*`SUP`12`LO` 5*`SUP`10`LO` A-2F`SUP`12`LO` (2F11,12 blank) π1 2π`SUP`2`LO` A-2I`SUP`8`LO` (2I7,8 blank) *-2*`SUP`4`LO` A-3R`SUP`4`LO` */2*`SUP`4`LO` 3*-9*`SUP`4`LO` a`SUP`4`LO` b`SUP`4`LO`(-b4) A-5C`SUP`4`LO` (5C4 blank) <***>`SUP`2`LO` A-2E`SUP`4`LO` 2F1 2G-2H`SUP`2`LO` A`SUP`4`LO`(A1+χ1) B-4C`SUP`4`LO` 4D`SUP`6`LO` 2*-3*`SUP`4`LO` a-c`SUP`4`LO` d`SUP`2`LO` e-r`SUP`4`LO` s`SUP`2`LO` t-y`SUP`4`LO` z`SUP`6`LO` (4D6 blank)")
    #cp.parse('[A-B]`SUP`4`LO`')
    # cp.parse('[A-B]`SUP`8`LO`')
    #cp.parse('*`SUP`4`LO`(-*4) A-G`SUP`12`LO` H`SUP`8`LO` (H8 blank)')
    # cp.parse('1-110`SUP`4`LO` 111`SUP`2`LO`')
    # cp.parse('π1 A`SUP`6`LO` χ1 B-D`SUP`8`LO` E`SUP`6`LO` 2χ1 F-H`SUP`8`LO` I`SUP`6`LO` 3χ1 K-M`SUP`8`LO` N`SUP`6`LO` 4χ1 O-Q`SUP`8`LO` R`SUP`6`LO` 5χ1 S-V`SUP`8`LO` X`SUP`6`LO` 6χ1 Y-2A`SUP`8`LO` 2B`SUP`6`LO` 7χ1 2C-2E`SUP`8`LO` 2F`SUP`6`LO` 8χ1 2G-2I`SUP`8`LO` 2K`SUP`6`LO` 9χ1 2L-2N`SUP`8`LO` 2O`SUP`6`LO` 10χ1 2P-2R`SUP`8`LO` 2S`SUP`6`LO` 11χ1 2T-2X`SUP`8`LO` 2Y`SUP`6`LO` 12χ1 2Z-3B`SUP`8`LO` 3C`SUP`6`LO` 13χ1 3D-3F`SUP`8`LO` 3G`SUP`6`LO` 14χ1 3H-3I`SUP`8`LO` 15χ1 3K`SUP`6`LO` 16χ1 3L-3N`SUP`8`LO` 3O`SUP`6`LO` 17χ1 3P=3R`SUP`8`LO` 3S`SUP`6`LO` 18χ1 3T-3X`SUP`8`LO` 3Y`SUP`6`LO` 19χ1 3Z-4B`SUP`8`LO` 4C`SUP`6`LO` 20χ1 4D-4F`SUP`8`LO` 4G`SUP`6`LO` 21χ1 4H-4K`SUP`8`LO` 4L`SUP`6`LO` 22χ1 4M-4O`SUP`8`LO` 4P`SUP`6`LO` 23χ1 4Q-4S`SUP`8`LO` 4T`SUP`6`LO` 24χ1 4V-4Y`SUP`8`LO` 4Z`SUP`6`LO` 25χ1 5A-5C`SUP`8`LO` 5D`SUP`6`LO` 26χ1 5E-5G`SUP`8`LO` 5H`SUP`6`LO` 27χ1 5I-5K`SUP`8`LO` 5L`SUP`4`LO` 28χ1 5M`SUP`6`LO` 29χ1 5N-5P`SUP`8`LO` 5Q`SUP`6`LO` 30χ1 5R-5T`SUP`8`LO` 5V`SUP`6`LO` 31χ1 5X-5Z`SUP`8`LO` 6A`SUP`6`LO` 32χ1 6B-6D`SUP`8`LO` 6E`SUP`6`LO` 33χ1 6F-6H`SUP`8`LO` 6I`SUP`6`LO` 34χ1 6K-6M`SUP`8`LO` 6N`SUP`6`LO` 35χ1 6O-6Q`SUP`8`LO` 6R`SUP`6`LO` 36χ1 6S-6V`SUP`8`LO` 6X`SUP`6`LO` 37χ1 6Y-7A`SUP`8`LO` 7B`SUP`6`LO` 38χ1 7C-7F`SUP`8`LO` 39χ1 7G`SUP`6`LO` 40χ1 7H-7K`SUP`8`LO` 7L`SUP`6`LO` 41χ1 7M-7O`SUP`8`LO` 7P`SUP`6`LO` 42χ1 7Q-7S`SUP`8`LO` 7T`SUP`6`LO` 43χ1 7V-7Y`SUP`8`LO` 7Z`SUP`6`LO` 44χ1 8A-8C`SUP`8`LO` 8D`SUP`6`LO` 45χ1 8E-8G`SUP`8`LO` 8H`SUP`6`LO` 46χ1 8I-8L`SUP`8`LO` 8M`SUP`6`LO` 47χ1 8N-8P`SUP`8`LO` 8Q`SUP`6`LO` 48χ1 8R-8T`SUP`8`LO` 8V`SUP`6`LO` 49χ1 8X-8Y`SUP`8`LO` 50χ1 8Z`SUP`6`LO` 51χ1 9A-9C`SUP`8`LO` 9D`SUP`6`LO` 52χ1 9E-9G`SUP`8`LO` 9H`SUP`6`LO` 53χ1 9I-9L`SUP`8`LO` 9M`SUP`6`LO` 54χ1 9N-9P`SUP`8`LO` 9Q`SUP`6`LO` 55χ1 9R-9T`SUP`8`LO` 9V`SUP`6`LO` 56χ1 9X-9Z`SUP`8`LO` 10A`SUP`6`LO` 57χ1 10B-10D`SUP`8`LO` 10E`SUP`6`LO` 58χ1 10F-10H`SUP`8`LO` 10I`SUP`6`LO` 59χ1 10K-10M`SUP`8`LO` 10N`SUP`6`LO` 60χ1 10O-10Q`SUP`8`LO` 10R`SUP`6`LO` 61X1 10S-10V`SUP`8`LO` 10X`SUP`6`LO` 62X1 10Y-11A`SUP`8`LO` 63χ1 11B`SUP`6`LO` 64χ1 11C-11E`SUP`8`LO` 11F`SUP`6`LO` 65χ1 11G-11I`SUP`8`LO` 11K`SUP`6`LO` 66χ1 11L-11N`SUP`8`LO` 11O`SUP`6`LO` 67χ1 11P-11R`SUP`8`LO` 11S`SUP`6`LO` 68χ1 11T-11X`SUP`8`LO` 11Y`SUP`6`LO` 69χ1 11Z-12B`SUP`8`LO` 12C`SUP`6`LO` 70χ1 12D-12F`SUP`8`LO` 12G`SUP`6`LO` 71χ1 12H-12K`SUP`8`LO` 12L`SUP`6`LO` 72χ1 12M-12N`SUP`8`LO` 12O`SUP`4`LO` 73χ1 12P`SUP`6`LO` 74χ1 12Q-12S`SUP`8`LO` 12T`SUP`6`LO` 75χ1 12V-12Y`SUP`8`LO` 12Z`SUP`6`LO` 76χ1 13A-13C`SUP`8`LO` 13D`SUP`6`LO` 77χ1 13E-13F`SUP`8`LO` 13G`SUP`4`LO`(13G4 blank) 13H`SUP`6`LO` 78χ1 13I-13L`SUP`8`LO` 13M`SUP`6`LO` 79χ1 13N-13P`SUP`8`LO` 13Q`SUP`6`LO` 80χ1 13R-13S`SUP`8`LO` 13T4 13V`SUP`6`LO` 81χ1 13X`SUP`8`LO`(-13X6,7,8) 13Y-13Z`SUP`8`LO` 14A`SUP`6`LO` 82χ1 14B`SUP`8`LO` 14C`SUP`8`LO`(-14C8) 14D`SUP`8`LO` 14E`SUP`8`LO`(-14E8) 14F`SUP`6`LO` 83χ1 14G-14H`SUP`8`LO` 14I`SUP`8`LO`(-14I7,8) 14K`SUP`6`LO` 84χ1 14L-14M`SUP`8`LO` 14N`SUP`6`LO` 85χ1 14O`SUP`6`LO` (14O6 blank)')
