import example_functions
import random

def main():
    list_to_sort = random.sample(range( 1000), 1000)
    example_functions.bad_sort(list_to_sort)
    example_functions.builtin_sort(list_to_sort)

main()
