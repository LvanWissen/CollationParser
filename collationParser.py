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

import re

class CollationParser:
    """
    Initializes a CollationParser object. Feed the .parse() function with a
    string to get the amount of folia. It prints the sections. 
    """

    def __init__(self):
        """
        """

        decodestring = "abcdefghiklmnopqrstuvxyz"  # j and w removed
        self.decodestring = decodestring + decodestring.upper()

    def parse(self, s):
        """

        :param s: collation formula (str)
        :return: amount of folia (int)
        """

        folia = 0
        katernen = 0



        print(s)

        r = re.compile("""
                       (?P<ONGESIGNEERD>(?:(?:\d+)?[χπ]\d{1,2})+)|
                       (?:`SUP`(?P<DUBBEL>[χπ]+?)`LO`(?P<DUBBELKATERN>.+?) )?(?:`SUP`(?P<HERHALING>[\dχπ]+?)`LO`)?(?P<KATERN_START>[^ `\n]+?)(?:-(?P<KATERN_END>[^ `\n]+?))?(?:`SUP`(?P<FORMAAT>\d+?)`LO`)+?|
                       (?:\((?P<CORRECTIE>-.*?)\))|
                       (?:\((?P<COMMENTAAR>[^-]*?)\))
                       """, re.VERBOSE)

        entries = [m.groupdict() for m in r.finditer(s)]

        for e in entries:
            print()
            print({k:v for k,v in e.items() if v is not None})

            if e['KATERN_START'] and e['KATERN_END']:

                n_start, s_start = re.findall('(\d+)?([^ ]+)?', e['KATERN_START'])[0]
                n_end, s_end = re.findall('(\d+)?([^ ]+)?', e['KATERN_END'])[0]

                if not n_start:
                    n_start = 1
                else:
                    n_start = int(n_start)
                if not n_end:
                    n_end = 1
                else:
                    n_end = int(n_end)

                print('n_start:', n_start, 's_start:', s_start)
                print('n_end:', n_end, 's_end:', s_end)

                if e['KATERN_START'] in self.decodestring and e['KATERN_END'] in self.decodestring:
                    start = self.decodestring.index(e['KATERN_START'].lower())
                    end = self.decodestring.index(e['KATERN_END'].lower())
                    size = end - start + 1

                    print('method1')

                elif s_start == s_end and s_start not in self.decodestring:

                    size = n_end - n_start

                    print('method2')

                elif s_start in self.decodestring and s_end in self.decodestring:
                    start = self.decodestring.index(s_start.lower())
                    end = self.decodestring.index(s_end.lower())

                    if end < start:
                        size = 24 - (start - end) * (n_end - n_start) + 1
                    elif n_end == n_start:
                        size = end - start + 1
                    elif end == start:
                        size = 24 * (n_end - n_start)
                    else:
                        raise EnvironmentError

                    print('method3')

                print(int(e['FORMAAT']), size)
                folia += int(e['FORMAAT']) * size

            elif e['KATERN_START']:
                folia += int(e['FORMAAT'])

            elif e['ONGESIGNEERD']:
                folia += int(re.split('χ|π', e['ONGESIGNEERD'], 1)[1])

            elif e['CORRECTIE']:
                folia -= 1

            elif e['COMMENTAAR']:
                print('Commentaar:', e['COMMENTAAR'])

            print(folia)

        print("Folia:", folia)
        print()


        return folia


if __name__ == "__main__":
    cp = CollationParser()
   
    cp.parse("π1 †-3†`SUP`12`LO` *`SUP`2`LO` a-e`SUP`12`LO` A-K`SUP`12`LO` `SUP`2`LO`†`SUP`2`LO` χ1 L-2C`SUP`12`LO` 2D`SUP`2`LO` 2χ1 2E-3D`SUP`12`LO` 3E`SUP`4`LO` `SUP`2`LO`A`SUP`2`LO` 3χ1 3F`SUP`8`LO` 3G-4B`SUP`12`LO` 4C`SUP`4`LO` `SUP`2`LO`*`SUP`2`LO` 4χ1 4D`SUP`8`LO` 4E-4Z`SUP`12`LO` 5A`SUP`2`LO` 5χ1 5B-5S`SUP`12`LO` 5T`SUP`4`LO` `SUP`3`LO`*`SUP`2`LO` 6χ1 5V`SUP`8`LO` 5X-6X`SUP`12`LO` 6Y`SUP`4`LO` 6Z`SUP`2`LO` 7χ1 7A-7S`SUP`12`LO` 7T`SUP`6`LO` `SUP`4`LO`*`SUP`2`LO` 8χ1 7V`SUP`6`LO` 7X-8I`SUP`12`LO` 8K`SUP`10`LO` `SUP`5`LO`*`SUP`2`LO` 9χ1 8L`SUP`2`LO` 8M-9D`SUP`12`LO` 9E`SUP`10`LO` 10χ1 11χ1 9G`SUP`2`LO` 9H-9V`SUP`12`LO` 9X`SUP`4`LO` (3E4, 9X4 blank)")


