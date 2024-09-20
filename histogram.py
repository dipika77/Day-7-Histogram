
#histograms
#instructions
'''Build a histogram of life_exp, with 5 bins. Can you tell which bin contains the most observations?
Build another histogram of life_exp, this time with 20 bins. Is this better?'''

# Build histogram with 5 bins
plt.hist(life_exp, bins = 5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clean up again
plt.show()
plt.clf()


#instructions
'''Build a histogram of life_exp with 15 bins.
Build a histogram of life_exp1950, also with 15 bins. Is there a
big difference with the histogram for the 2007 data?'''

# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins = 15)

# Show and clear plot again
plt.show()
plt.clf()