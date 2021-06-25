#1.
#女

#2.
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
	# calculate P(not A)
	not_a = 1 - p_a
	# calculate P(B)
	p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
	# calculate P(A|B)
	p_a_given_b = (p_b_given_a * p_a) / p_b
	return p_a_given_b
 
# P(A): P(女生)
# P(not A): P(男生)
p_a = 0.1
# P(B|A): P(長髮|女生)
p_b_given_a = 0.5
# P(B|not A): P(長髮|男生)
p_b_given_not_a = 0.1
# calculate P(A|B): P(女生|長髮)
result = bayes_theorem(p_a, p_b_given_a, p_b_given_not_a)
# summarize
# P(女生|長髮)
print('P(A|B) = {0}'.format(round(result * 100,2)))

#3.
#Anwer:透過貝式定理的運算，得出長髮男生的可能性大於女生，造成決策上的改變，所以以作業和投影片的例子可以看出，先驗分配的重要性，假設錯誤，決策可能就會錯誤。
