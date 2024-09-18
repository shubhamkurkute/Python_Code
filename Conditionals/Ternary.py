# Simplest conditional operator
# Syntax : <expr1> if <conditional_expr> else <expr2>
# Stores exp1 if condition is true otherwise returns exp2.

raining = False
print("Lets go to the", 'beach' if not raining else 'library')

age = 20
s = "minor" if age < 18 else 'adult'
print(s)
