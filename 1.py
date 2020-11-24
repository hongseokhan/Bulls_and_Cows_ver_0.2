from itertools import permutations
numbers = [str(x) for x in range(0,10)]
all_candidates_num_list = [str(candidate_num_list) for candidate_num_list in permutations(numbers,4)]

print(all_candidates_num_list)