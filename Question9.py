# Q9. Generate a Student's t-distribution plot using Python's matplotlib library, with the degrees of freedom
# parameter set to 10.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

dof = 10

x = np.linspace(-5,5,400)
print(x)

t_distribution = t.pdf(x,df=dof)
print(t_distribution)

plt.plot(x,t_distribution)