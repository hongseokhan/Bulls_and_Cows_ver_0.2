from itertools import permutations
def make_all_candidates_num_list():
    numbers = [str(x) for x in range(0,10)]
    all_candidates_num_list = [list(num_list) for num_list in permutations(numbers,4)]
    return all_candidates_num_list

a = make_all_candidates_num_list()
print(a)
