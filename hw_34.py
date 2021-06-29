import statsmodels.stats.proportion
# H0: Pa = Pb
# H1: Pa != Pb
A = [75, 30] # 有開信的個數
B = [300, 300] #各組實驗總個數

z, p = statsmodels.stats.proportion.proportions_ztest(A, B, alternative='smaller')
print('{:.8f}'.format(p))
A = [75, 30] # 有開信的個數
B = [300, 300] #各組實驗總個數

z, p = statsmodels.stats.proportion.proportions_ztest(A, B, alternative='larger')
print('{:.8f}'.format(p))
A = [75, 30] # 有開信的個數
B = [300, 300] #各組實驗總個數

z, p = statsmodels.stats.proportion.proportions_ztest(A, B, alternative='two-sided')
print('{:.8f}'.format(p))