# Given a sequence of M and N with M representing increasing and N representing decreasing, 
# output the smallest number that follows this pattern.

# Input    : NN         Output   : 321
# Input    : MMMM       Output   : 12345
# Input    : NNNN       Output   : 54321
# Input    : MMNM       Output   : 2314

def sequence(pattern:string)->integer:
    if len(pattern) == 0: return '-1'


