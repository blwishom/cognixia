import codecademylib
import numpy as np
from matplotlib import pyplot as plt


#generating random numbers based on probability
emails = np.random.binomial(500, .05, size=10000)

plt.hist(emails)
plt.show()

#generating probability of email responses based on specific numbers
no_emails = np.mean(emails==0)
print(no_emails)
b_test_emails = np.mean(emails==8)
print(b_test_emails)
