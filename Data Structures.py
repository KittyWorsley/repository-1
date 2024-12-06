my_list = [3,6,9,12,15,18,20,24,28,32]

print(my_list)
def sum_list(numbers):
    return("Sum:", sum(numbers))
          
def large_list(numbers):
    return("Largest:", max(numbers))


def reversed_list(numbers):
    return("reverse:", numbers[::-1])

def small_list(numbers):
    return("smallest:", min(numbers))

print(large_list(my_list))
         
print(reversed_list(my_list))
print(small_list(my_list))
