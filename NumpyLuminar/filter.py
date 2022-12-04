#filter

import numpy as np
a=np.array([41,43,46,50,45,38,57,29,65,41])
print(a)

#above 43
b=a>43
print(b)

c=a[b]
print(c)

