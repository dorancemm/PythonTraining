def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def permutations(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]
    list_aux = []
    for i in range(len(list)):
        m = list[i]
        list_residual = list[:i] + list[i+1:]
        for p in permutations(list_residual):
            list_aux.append([m] + p)
    return list_aux
    
# Example Factorial
number = 5
result = factorial(number)
print (f"The factorial of {number} is {result}")

# Permutations
numbers_list = [1, 2, 3]
print('Permutations of ', numbers_list, 'ist', permutations(numbers_list))
