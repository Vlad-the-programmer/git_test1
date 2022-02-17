
from tabulate import tabulate
import LogCon
# f22 =(a→b)→((a∧!b)→c)
#Part1 with the table1
print('      Part 1:\n')
table1 =[ ['a', ' b',' b!','a ∧ b ','a ∨ b','a -> b','a~b', 'a xor b'],
[False, False,LogCon.NOT(False),LogCon.AND(False, False),LogCon.OR(False, False), LogCon.IMP0(False, False),LogCon.EQV(False, False),LogCon.XOR(False, False)], 
[False,True, LogCon.NOT(False), LogCon.AND(False, True) ,LogCon.OR(False, True), LogCon.IMP0(False, True),LogCon.EQV(False, True),LogCon.XOR(False, True)],
[ True,False,LogCon.NOT(True),LogCon.AND(True, False),LogCon.OR(True, False), LogCon.IMP0(True, False),LogCon.EQV(True, False),LogCon.XOR(True, False)],
[ True,True,LogCon.NOT(True),LogCon.AND(True, True),LogCon.OR(True, True), LogCon.IMP0(True, True),LogCon.EQV(True, True),LogCon.XOR(True, True)]
]
#Forms the table1
print(tabulate(table1, tablefmt="fancy_grid"))

#Part2 with the table 2
print('      Part 2:\n')
print('   My function is f22 =(a!→b!)→((a∧!b)→c)\n')
table2 = [ ['a', ' b', 'c','Result'],
[False, False,False,LogCon.Result(False, False, False)], 
[False,False,True,LogCon.Result(False, False, True)],
[False, True,False,LogCon.Result(False, True, False)],
[False, True,True,LogCon.Result(False, True, True)], 
[True, False,False,LogCon.Result(True, False, False)],
[True,False,True,LogCon.Result(True, False, True)],
[True, True,False,LogCon.Result(True, True, False)],
[True, True,True,LogCon.Result(True, True, True)]
]

#Forms the table2
print(tabulate(table2, tablefmt="fancy_grid"))





























