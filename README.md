# CollationParser
STCN Collation Parser

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
{'FORMAAT': '4', 'KATERN_START': '*'}
4

{'CORRECTIE': '-*4'}
3

{'FORMAAT': '12', 'KATERN_END': 'G', 'KATERN_START': 'A'}
n_start: 1 s_start: A
n_end: 1 s_end: G
method1
12 7
87

{'FORMAAT': '8', 'KATERN_START': 'H'}
95

{'COMMENTAAR': 'H8 blank'}
Commentaar: H8 blank
95
Folia: 95

```

## Example

```
python .\collationParser.py

π1 †-3†`SUP`12`LO` *`SUP`2`LO` a-e`SUP`12`LO` A-K`SUP`12`LO` `SUP`2`LO`†`SUP`2`LO` χ1 L-2C`SUP`12`LO` 2D`SUP`2`LO` 2χ1 2E-3D`SUP`12`LO` 3E`SUP`4`LO` `SUP`2`LO`A`SUP`2`LO` 3χ1 3F`SUP`8`LO` 3G-4B`SUP`12`LO` 4C`SUP`4`LO` `SUP`2`LO`*`SUP`2`LO` 4χ1 4D`SUP`8`LO` 4E-4Z`SUP`12`LO` 5A`SUP`2`LO` 5χ1 5B-5S`SUP`12`LO` 5T`SUP`4`LO` `SUP`3`LO`*`SUP`2`LO` 6χ1 5V`SUP`8`LO` 5X-6X`SUP`12`LO` 6Y`SUP`4`LO` 6Z`SUP`2`LO` 7χ1 7A-7S`SUP`12`LO` 7T`SUP`6`LO` `SUP`4`LO`*`SUP`2`LO` 8χ1 7V`SUP`6`LO` 7X-8I`SUP`12`LO` 8K`SUP`10`LO` `SUP`5`LO`*`SUP`2`LO` 9χ1 8L`SUP`2`LO` 8M-9D`SUP`12`LO` 9E`SUP`10`LO` 10χ1 11χ1 9G`SUP`2`LO` 9H-9V`SUP`12`LO` 9X`SUP`4`LO` (3E4, 9X4 blank)

{'ONGESIGNEERD': 'π1'}
1

{'FORMAAT': '12', 'KATERN_END': '3†', 'KATERN_START': '†'}
n_start: 1 s_start: †
n_end: 3 s_end: †
method2
12 3
37

{'FORMAAT': '2', 'KATERN_START': '*'}
39

{'FORMAAT': '12', 'KATERN_END': 'e', 'KATERN_START': 'a'}
n_start: 1 s_start: a
n_end: 1 s_end: e
method1
12 5
99

{'FORMAAT': '12', 'KATERN_END': 'K', 'KATERN_START': 'A'}
n_start: 1 s_start: A
n_end: 1 s_end: K
method1
12 10
219

{'FORMAAT': '2', 'HERHALING': '2', 'KATERN_START': '†'}
221

{'ONGESIGNEERD': 'χ1'}
222

{'FORMAAT': '12', 'KATERN_END': '2C', 'KATERN_START': 'L'}
n_start: 1 s_start: L
n_end: 2 s_end: C
method3
12 17
426

{'FORMAAT': '2', 'KATERN_START': '2D'}
428

{'ONGESIGNEERD': '2χ1'}
429

{'FORMAAT': '12', 'KATERN_END': '3D', 'KATERN_START': '2E'}
n_start: 2 s_start: E
n_end: 3 s_end: D
method3
12 24
717

{'FORMAAT': '4', 'KATERN_START': '3E'}
721

{'FORMAAT': '2', 'HERHALING': '2', 'KATERN_START': 'A'}
723

{'ONGESIGNEERD': '3χ1'}
724

{'FORMAAT': '8', 'KATERN_START': '3F'}
732

{'FORMAAT': '12', 'KATERN_END': '4B', 'KATERN_START': '3G'}
n_start: 3 s_start: G
n_end: 4 s_end: B
method3
12 20
972

{'FORMAAT': '4', 'KATERN_START': '4C'}
976

{'FORMAAT': '2', 'HERHALING': '2', 'KATERN_START': '*'}
978

{'ONGESIGNEERD': '4χ1'}
979

{'FORMAAT': '8', 'KATERN_START': '4D'}
987

{'FORMAAT': '12', 'KATERN_END': '4Z', 'KATERN_START': '4E'}
n_start: 4 s_start: E
n_end: 4 s_end: Z
method3
12 20
1227

{'FORMAAT': '2', 'KATERN_START': '5A'}
1229

{'ONGESIGNEERD': '5χ1'}
1230

{'FORMAAT': '12', 'KATERN_END': '5S', 'KATERN_START': '5B'}
n_start: 5 s_start: B
n_end: 5 s_end: S
method3
12 17
1434

{'FORMAAT': '4', 'KATERN_START': '5T'}
1438

{'FORMAAT': '2', 'HERHALING': '3', 'KATERN_START': '*'}
1440

{'ONGESIGNEERD': '6χ1'}
1441

{'FORMAAT': '8', 'KATERN_START': '5V'}
1449

{'FORMAAT': '12', 'KATERN_END': '6X', 'KATERN_START': '5X'}
n_start: 5 s_start: X
n_end: 6 s_end: X
method3
12 24
1737

{'FORMAAT': '4', 'KATERN_START': '6Y'}
1741

{'FORMAAT': '2', 'KATERN_START': '6Z'}
1743

{'ONGESIGNEERD': '7χ1'}
1744

{'FORMAAT': '12', 'KATERN_END': '7S', 'KATERN_START': '7A'}
n_start: 7 s_start: A
n_end: 7 s_end: S
method3
12 18
1960

{'FORMAAT': '6', 'KATERN_START': '7T'}
1966

{'FORMAAT': '2', 'HERHALING': '4', 'KATERN_START': '*'}
1968

{'ONGESIGNEERD': '8χ1'}
1969

{'FORMAAT': '6', 'KATERN_START': '7V'}
1975

{'FORMAAT': '12', 'KATERN_END': '8I', 'KATERN_START': '7X'}
n_start: 7 s_start: X
n_end: 8 s_end: I
method3
12 12
2119

{'FORMAAT': '10', 'KATERN_START': '8K'}
2129

{'FORMAAT': '2', 'HERHALING': '5', 'KATERN_START': '*'}
2131

{'ONGESIGNEERD': '9χ1'}
2132

{'FORMAAT': '2', 'KATERN_START': '8L'}
2134

{'FORMAAT': '12', 'KATERN_END': '9D', 'KATERN_START': '8M'}
n_start: 8 s_start: M
n_end: 9 s_end: D
method3
12 17
2338

{'FORMAAT': '10', 'KATERN_START': '9E'}
2348

{'ONGESIGNEERD': '10χ1'}
2349

{'ONGESIGNEERD': '11χ1'}
2350

{'FORMAAT': '2', 'KATERN_START': '9G'}
2352

{'FORMAAT': '12', 'KATERN_END': '9V', 'KATERN_START': '9H'}
n_start: 9 s_start: H
n_end: 9 s_end: V
method3
12 14
2520

{'FORMAAT': '4', 'KATERN_START': '9X'}
2524

{'COMMENTAAR': '3E4, 9X4 blank'}
Commentaar: 3E4, 9X4 blank
2524
Folia: 2524


```
