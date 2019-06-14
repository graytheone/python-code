student_tuples = [('join', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
t = student_tuples
#1.sorted with name
#(hint: use lambda)

def by_name(t):
	return str.lower(t[0])

sorted(t,key = by_name)	
#2.sorted with age
def by_age(t):
	return t[2]

sorted(t,key = by_age)

#3.sorted with grade
def by_grade(t):
	return str.lower(t[1])

sorted(t,key = by_grade)

