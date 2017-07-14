# CollationParser
STCN Collation Parser

## Example

```
python .\collationParser.py

π1 †-3†`SUP`12`LO` *`SUP`2`LO` a-e`SUP`12`LO` A-K`SUP`12`LO` 
`SUP`2`LO`†`SUP`2`LO` χ1 L-2C`SUP`12`LO` 2D`SUP`2`LO` 2χ1 
2E-3D`SUP`12`LO` 3E`SUP`4`LO` `SUP`2`LO`A`SUP`2`LO` 3χ1 3F`SUP`8`LO` 
3G-4B`SUP`12`LO` 4C`SUP`4`LO` `SUP`2`LO`*`SUP`2`LO` 4χ1 4D`SUP`8`LO` 
4E-4Z`SUP`12`LO` 5A`SUP`2`LO` 5χ1 5B-5S`SUP`12`LO` 5T`SUP`4`LO` 
`SUP`3`LO`*`SUP`2`LO` 6χ1 5V`SUP`8`LO` 5X-6X`SUP`12`LO` 6Y`SUP`4`LO` 
6Z`SUP`2`LO` 7χ1 7A-7S`SUP`12`LO` 7T`SUP`6`LO` `SUP`4`LO`*`SUP`2`LO` 
8χ1 7V`SUP`6`LO` 7X-8I`SUP`12`LO` 8K`SUP`10`LO` `SUP`5`LO`*`SUP`2`LO` 
9χ1 8L`SUP`2`LO` 8M-9D`SUP`12`LO` 9E`SUP`10`LO` 10χ1 11χ1 9G`SUP`2`LO` 
9H-9V`SUP`12`LO` 9X`SUP`4`LO` (3E4, 9X4 blank)

{'ONGESIGNEERD': 'π1'}
1

{'FORMAAT': '12', 'KATERN_START': '†', 'KATERN_END': '3†'}
n_start: 1 s_start: †
n_end: 3 s_end: †
method2
12 2
25

{'KATERN_START': '*', 'FORMAAT': '2'}
27

{'FORMAAT': '12', 'KATERN_START': 'a', 'KATERN_END': 'e'}
n_start: 1 s_start: a
n_end: 1 s_end: e
method1
12 5
87

{'FORMAAT': '12', 'KATERN_START': 'A', 'KATERN_END': 'K'}
n_start: 1 s_start: A
n_end: 1 s_end: K
method1
12 10
207

{'FORMAAT': '2', 'KATERN_START': '†', 'HERHALING': '2'}
209

{'ONGESIGNEERD': 'χ1'}
210

{'FORMAAT': '12', 'KATERN_START': 'L', 'KATERN_END': '2C'}
n_start: 1 s_start: L
n_end: 2 s_end: C
method3
12 17
414

{'KATERN_START': '2D', 'FORMAAT': '2'}
416

{'ONGESIGNEERD': '2χ1'}
417

{'FORMAAT': '12', 'KATERN_START': '2E', 'KATERN_END': '3D'}
n_start: 2 s_start: E
n_end: 3 s_end: D
method3
12 24
705

{'KATERN_START': '3E', 'FORMAAT': '4'}
709

{'FORMAAT': '2', 'KATERN_START': 'A', 'HERHALING': '2'}
711

{'ONGESIGNEERD': '3χ1'}
712

{'KATERN_START': '3F', 'FORMAAT': '8'}
720

{'FORMAAT': '12', 'KATERN_START': '3G', 'KATERN_END': '4B'}
n_start: 3 s_start: G
n_end: 4 s_end: B
method3
12 20
960

{'KATERN_START': '4C', 'FORMAAT': '4'}
964

{'FORMAAT': '2', 'KATERN_START': '*', 'HERHALING': '2'}
966

{'ONGESIGNEERD': '4χ1'}
967

{'KATERN_START': '4D', 'FORMAAT': '8'}
975

{'FORMAAT': '12', 'KATERN_START': '4E', 'KATERN_END': '4Z'}
n_start: 4 s_start: E
n_end: 4 s_end: Z
method3
12 20
1215

{'KATERN_START': '5A', 'FORMAAT': '2'}
1217

{'ONGESIGNEERD': '5χ1'}
1218

{'FORMAAT': '12', 'KATERN_START': '5B', 'KATERN_END': '5S'}
n_start: 5 s_start: B
n_end: 5 s_end: S
method3
12 17
1422

{'KATERN_START': '5T', 'FORMAAT': '4'}
1426

{'FORMAAT': '2', 'KATERN_START': '*', 'HERHALING': '3'}
1428

{'ONGESIGNEERD': '6χ1'}
1429

{'KATERN_START': '5V', 'FORMAAT': '8'}
1437

{'FORMAAT': '12', 'KATERN_START': '5X', 'KATERN_END': '6X'}
n_start: 5 s_start: X
n_end: 6 s_end: X
method3
12 24
1725

{'KATERN_START': '6Y', 'FORMAAT': '4'}
1729

{'KATERN_START': '6Z', 'FORMAAT': '2'}
1731

{'ONGESIGNEERD': '7χ1'}
1732

{'FORMAAT': '12', 'KATERN_START': '7A', 'KATERN_END': '7S'}
n_start: 7 s_start: A
n_end: 7 s_end: S
method3
12 18
1948

{'KATERN_START': '7T', 'FORMAAT': '6'}
1954

{'FORMAAT': '2', 'KATERN_START': '*', 'HERHALING': '4'}
1956

{'ONGESIGNEERD': '8χ1'}
1957

{'KATERN_START': '7V', 'FORMAAT': '6'}
1963

{'FORMAAT': '12', 'KATERN_START': '7X', 'KATERN_END': '8I'}
n_start: 7 s_start: X
n_end: 8 s_end: I
method3
12 12
2107

{'KATERN_START': '8K', 'FORMAAT': '10'}
2117

{'FORMAAT': '2', 'KATERN_START': '*', 'HERHALING': '5'}
2119

{'ONGESIGNEERD': '9χ1'}
2120

{'KATERN_START': '8L', 'FORMAAT': '2'}
2122

{'FORMAAT': '12', 'KATERN_START': '8M', 'KATERN_END': '9D'}
n_start: 8 s_start: M
n_end: 9 s_end: D
method3
12 17
2326

{'KATERN_START': '9E', 'FORMAAT': '10'}
2336

{'ONGESIGNEERD': '10χ1'}
2337

{'ONGESIGNEERD': '11χ1'}
2338

{'KATERN_START': '9G', 'FORMAAT': '2'}
2340

{'FORMAAT': '12', 'KATERN_START': '9H', 'KATERN_END': '9V'}
n_start: 9 s_start: H
n_end: 9 s_end: V
method3
12 14
2508

{'KATERN_START': '9X', 'FORMAAT': '4'}
2512

{'COMMENTAAR': '3E4, 9X4 blank'}
Commentaar: 3E4, 9X4 blank
2512

Folia: 2512

```
