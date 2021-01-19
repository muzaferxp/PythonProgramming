


#method 1  #it imports every thing from the module
'''
import sample_module


print(sample_module.state)
print(sample_module.name)


num = sample_module.mult(10,5)

print(num)


'''


#method 2
'''
#from sample_module import mult,sub

from sample_module import *

num = mult(5,6)

print(num)

print(sub(5,4))

print(add(6,8))
'''

#method 3
from sample_module import division as dv
from datetime import *

date = datetime.now()


print(date)

print(dv(8,4))
