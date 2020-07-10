# CollationParser
[![GitHub release](https://img.shields.io/github/release/LvanWissen/CollationParser.svg)](https://gitHub.com/lvanwissen/CollationParser/releases/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3938878.svg)](https://doi.org/10.5281/zenodo.3938878)

STCN Collation Parser [=Vellenteller]

Presented at NBV 2018, June 1st 2018, Vrije Universiteit Amsterdam. 

## How to use

```python
    from CollationParser import CollationParser
    parser = CollationParser()
    
    folia = parser.parse('*`SUP`4`LO`(-*4) A-G`SUP`12`LO` H`SUP`8`LO` (H8 blank)')
```

Or for a more informative output:

```python
    from CollationParser import CollationParser    
    parser = CollationParser(verbose=True)
    
    folia = parser.parse('*`SUP`4`LO`(-*4) A-G`SUP`12`LO` H`SUP`8`LO` (H8 blank)')
```

Output:
```
{'KATERN_START': '*', 'FORMAAT': '4'}
Cumulatief aantal: 4
---

{'CORRECTIE': '-*4'}
Cumulatief aantal: 3
---

{'KATERN_START': 'A', 'KATERN_END': 'G', 'FORMAAT': '12'}
n_start: 1 	 s_start: A
n_end: 1 	 s_end: G
Method: Begin and end collation mark
Formaat: 12	Omvang:7
Cumulatief aantal: 87
---

{'KATERN_START': 'H', 'FORMAAT': '8'}
Cumulatief aantal: 95
---

{'COMMENTAAR': 'H8 blank'}
Commentaar: H8 blank
Cumulatief aantal: 95

```

## Example

```
python .\collationParser.py

π1 †-3†`SUP`12`LO` *`SUP`2`LO` a-e`SUP`12`LO` A-K`SUP`12`LO` `SUP`2`LO`†`SUP`2`LO` χ1 L-2C`SUP`12`LO` 2D`SUP`2`LO` 2χ1 2E-3D`SUP`12`LO` 3E`SUP`4`LO` `SUP`2`LO`A`SUP`2`LO` 3χ1 3F`SUP`8`LO` 3G-4B`SUP`12`LO` 4C`SUP`4`LO` `SUP`2`LO`*`SUP`2`LO` 4χ1 4D`SUP`8`LO` 4E-4Z`SUP`12`LO` 5A`SUP`2`LO` 5χ1 5B-5S`SUP`12`LO` 5T`SUP`4`LO` `SUP`3`LO`*`SUP`2`LO` 6χ1 5V`SUP`8`LO` 5X-6X`SUP`12`LO` 6Y`SUP`4`LO` 6Z`SUP`2`LO` 7χ1 7A-7S`SUP`12`LO` 7T`SUP`6`LO` `SUP`4`LO`*`SUP`2`LO` 8χ1 7V`SUP`6`LO` 7X-8I`SUP`12`LO` 8K`SUP`10`LO` `SUP`5`LO`*`SUP`2`LO` 9χ1 8L`SUP`2`LO` 8M-9D`SUP`12`LO` 9E`SUP`10`LO` 10χ1 11χ1 9G`SUP`2`LO` 9H-9V`SUP`12`LO` 9X`SUP`4`LO` (3E4, 9X4 blank)

{'ONGESIGNEERD': 'π1'}
Cumulatief aantal: 1
---

{'KATERN_START': '†', 'KATERN_END': '3†', 'FORMAAT': '12'}
n_start: 1 	 s_start: †
n_end: 3 	 s_end: †
Method: Just one collation mark in group
Formaat: 12	Omvang:3
Cumulatief aantal: 37
---

{'KATERN_START': '*', 'FORMAAT': '2'}
Cumulatief aantal: 39
---

{'KATERN_START': 'a', 'KATERN_END': 'e', 'FORMAAT': '12'}
n_start: 1 	 s_start: a
n_end: 1 	 s_end: e
Method: Begin and end collation mark
Formaat: 12	Omvang:5
Cumulatief aantal: 99
---

{'KATERN_START': 'A', 'KATERN_END': 'K', 'FORMAAT': '12'}
n_start: 1 	 s_start: A
n_end: 1 	 s_end: K
Method: Begin and end collation mark
Formaat: 12	Omvang:10
Cumulatief aantal: 219
---

{'HERHALING': '2', 'KATERN_START': '†', 'FORMAAT': '2'}
Cumulatief aantal: 221
---

{'ONGESIGNEERD': 'χ1'}
Cumulatief aantal: 222
---

{'KATERN_START': 'L', 'KATERN_END': '2C', 'FORMAAT': '12'}
n_start: 1 	 s_start: L
n_end: 2 	 s_end: C
Start index: 10 
End index: 2
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:16
Cumulatief aantal: 414
---

{'KATERN_START': '2D', 'FORMAAT': '2'}
Cumulatief aantal: 416
---

{'ONGESIGNEERD': '2χ1'}
Cumulatief aantal: 417
---

{'KATERN_START': '2E', 'KATERN_END': '3D', 'FORMAAT': '12'}
n_start: 2 	 s_start: E
n_end: 3 	 s_end: D
Start index: 4 
End index: 3
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:23
Cumulatief aantal: 693
---

{'KATERN_START': '3E', 'FORMAAT': '4'}
Cumulatief aantal: 697
---

{'HERHALING': '2', 'KATERN_START': 'A', 'FORMAAT': '2'}
Cumulatief aantal: 699
---

{'ONGESIGNEERD': '3χ1'}
Cumulatief aantal: 700
---

{'KATERN_START': '3F', 'FORMAAT': '8'}
Cumulatief aantal: 708
---

{'KATERN_START': '3G', 'KATERN_END': '4B', 'FORMAAT': '12'}
n_start: 3 	 s_start: G
n_end: 4 	 s_end: B
Start index: 6 
End index: 1
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:19
Cumulatief aantal: 936
---

{'KATERN_START': '4C', 'FORMAAT': '4'}
Cumulatief aantal: 940
---

{'HERHALING': '2', 'KATERN_START': '*', 'FORMAAT': '2'}
Cumulatief aantal: 942
---

{'ONGESIGNEERD': '4χ1'}
Cumulatief aantal: 943
---

{'KATERN_START': '4D', 'FORMAAT': '8'}
Cumulatief aantal: 951
---

{'KATERN_START': '4E', 'KATERN_END': '4Z', 'FORMAAT': '12'}
n_start: 4 	 s_start: E
n_end: 4 	 s_end: Z
Start index: 4 
End index: 22
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:19
Cumulatief aantal: 1179
---

{'KATERN_START': '5A', 'FORMAAT': '2'}
Cumulatief aantal: 1181
---

{'ONGESIGNEERD': '5χ1'}
Cumulatief aantal: 1182
---

{'KATERN_START': '5B', 'KATERN_END': '5S', 'FORMAAT': '12'}
n_start: 5 	 s_start: B
n_end: 5 	 s_end: S
Start index: 1 
End index: 17
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:17
Cumulatief aantal: 1386
---

{'KATERN_START': '5T', 'FORMAAT': '4'}
Cumulatief aantal: 1390
---

{'HERHALING': '3', 'KATERN_START': '*', 'FORMAAT': '2'}
Cumulatief aantal: 1392
---

{'ONGESIGNEERD': '6χ1'}
Cumulatief aantal: 1393
---

{'KATERN_START': '5V', 'FORMAAT': '8'}
Cumulatief aantal: 1401
---

{'KATERN_START': '5X', 'KATERN_END': '6X', 'FORMAAT': '12'}
n_start: 5 	 s_start: X
n_end: 6 	 s_end: X
Start index: 20 
End index: 20
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:24
Cumulatief aantal: 1689
---

{'KATERN_START': '6Y', 'FORMAAT': '4'}
Cumulatief aantal: 1693
---

{'KATERN_START': '6Z', 'FORMAAT': '2'}
Cumulatief aantal: 1695
---

{'ONGESIGNEERD': '7χ1'}
Cumulatief aantal: 1696
---

{'KATERN_START': '7A', 'KATERN_END': '7S', 'FORMAAT': '12'}
n_start: 7 	 s_start: A
n_end: 7 	 s_end: S
Start index: 0 
End index: 17
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:18
Cumulatief aantal: 1912
---

{'KATERN_START': '7T', 'FORMAAT': '6'}
Cumulatief aantal: 1918
---

{'HERHALING': '4', 'KATERN_START': '*', 'FORMAAT': '2'}
Cumulatief aantal: 1920
---

{'ONGESIGNEERD': '8χ1'}
Cumulatief aantal: 1921
---

{'KATERN_START': '7V', 'FORMAAT': '6'}
Cumulatief aantal: 1927
---

{'KATERN_START': '7X', 'KATERN_END': '8I', 'FORMAAT': '12'}
n_start: 7 	 s_start: X
n_end: 8 	 s_end: I
Start index: 20 
End index: 8
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:12
Cumulatief aantal: 2071
---

{'KATERN_START': '8K', 'FORMAAT': '10'}
Cumulatief aantal: 2081
---

{'HERHALING': '5', 'KATERN_START': '*', 'FORMAAT': '2'}
Cumulatief aantal: 2083
---

{'ONGESIGNEERD': '9χ1'}
Cumulatief aantal: 2084
---

{'KATERN_START': '8L', 'FORMAAT': '2'}
Cumulatief aantal: 2086
---

{'KATERN_START': '8M', 'KATERN_END': '9D', 'FORMAAT': '12'}
n_start: 8 	 s_start: M
n_end: 9 	 s_end: D
Start index: 11 
End index: 3
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:16
Cumulatief aantal: 2278
---

{'KATERN_START': '9E', 'FORMAAT': '10'}
Cumulatief aantal: 2288
---

{'ONGESIGNEERD': '10χ1'}
Cumulatief aantal: 2289
---

{'ONGESIGNEERD': '11χ1'}
Cumulatief aantal: 2290
---

{'KATERN_START': '9G', 'FORMAAT': '2'}
Cumulatief aantal: 2292
---

{'KATERN_START': '9H', 'KATERN_END': '9V', 'FORMAAT': '12'}
n_start: 9 	 s_start: H
n_end: 9 	 s_end: V
Start index: 7 
End index: 19
Method: Group exceeds the alphabet and starts over
Formaat: 12	Omvang:13
Cumulatief aantal: 2448
---

{'KATERN_START': '9X', 'FORMAAT': '4'}
Cumulatief aantal: 2452
---

{'COMMENTAAR': '3E4, 9X4 blank'}
Commentaar: 3E4, 9X4 blank
Cumulatief aantal: 2452
---

Folia: 2452

```


## Docker demo

~~Demo and flask webserver available in [separate repository](https://github.com/LvanWissen/collatieparser-docker)~~ (deprecated)

## Questions / requests / bugs?
[E-mail](mailto:leon@vwissen.nl)! 
