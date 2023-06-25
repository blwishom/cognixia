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



sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# Calculate sunflowers_normal here:
# Generate 5,000 random samples with the same mean and standard deviation as sunflowers:
sunflowers_normal = np.random.normal(loc=sunflowers_mean, scale=sunflowers_std, size=5000)


plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='observed', normed=True)
plt.hist(sunflowers_normal,
        range=(11, 15), histtype='step', linewidth=2,
       label='normal', normed=True)
plt.legend()
plt.show()

# Calculate probabilities here:
experiments = np.random.binomial(200, .1, size=5000)
prob = np.mean(experiments < 20)
print(prob)
