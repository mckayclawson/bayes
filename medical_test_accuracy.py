'''
This file contains a very straight forward implementation of bayes theorm 
to illustrate the inaccuracy of so called "accurate" medical tests
'''

def main():
	#the probability of having a disease P(event1)
	e1 = float(raw_input("enter the probability of having the disease: "))
	#the probability of testing positive P(event2)
	e2 = raw_input("enter the probability of testing positive (hit enter if unknown): ")
	#the accuracy of the test P(event1|event2)
	acc = float(raw_input("enter the accuracy of the test: "))
	#the false positive rate for the test
	false_pos = float(raw_input("enter the false positive rate for the test: "))
	if e2 == "":
		e2 = derive_prob_event2(e1, acc, false_pos)
	else:
		e2 = float(e2)

	print "the chances of having a disease with a probability of " + str(e1) + " given an accuracy rate of " + str(acc) + " and a false positive rate of " + str(false_pos) + " are " + "{0:.2f}".format(bayesian_probability(e1, e2, acc) * 100) + "%"
'''
A simple implementation of bayes theorm: P(event1|event2) = (P(event1) * P(event2|event1)) / P(event2)
@param1 - probability of event1 
@param2 - probability of event2
@param3 - probability of event2 given even1
'''
def bayesian_probability(e1, e2, e2_given_e1):
	return ((e1 * e2_given_e1) / e2)
	
def derive_prob_event2(event1, accuracy, false_positive_rate):
	return ((event1 * accuracy) + (false_positive_rate * (1.0 - event1)))


main()
