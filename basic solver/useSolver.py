import SolveBH
import ast

cube = [0,0,0,0,0,0,0,0,0,
         3,3,3,3,3,3,3,3,3,
         4,4,4,4,4,4,4,4,4,
         1,1,1,1,1,1,1,1,1,
         2,2,2,2,2,2,2,2,2,
         5,5,5,5,5,5,5,5,5]

cube = ast.literal_eval(input('Representation of your cube : '))
convertRes, res = SolveBH.solve(cube)
print(res)
