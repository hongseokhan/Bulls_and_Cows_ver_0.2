from random import choice,sample 
from itertools import permutations
from player import Player

class Computer(Player):
    
    def __init__(self):
        super().__init__()
        self.__zero_strikes_and_balls_count = (0,0)
        self.__candidates_num_list = self._make_all_candidates_num_list()
    
    @property
    def candidates_num_list(self):
        return self.__candidates_num_list
    
    @candidates_num_list.setter
    def candidates_num_list(self,candidates_num_list):
        self.__candidates_num_list = candidates_num_list 
    
    def _random_defense_num_list_generator(self):
        self._defense_num_list = [str(x) for x in sample(range(0,10),4)]

    def _update_strikes_and_balls_count_candidates_num_list(self,attack_num_list,candidates_num_list):
        strikes,balls = (0,0)
        for i in range(4):
            if attack_num_list[i] == candidates_num_list[i]:
                strikes += 1
            elif attack_num_list[i] in candidates_num_list:
                balls += 1
        return (strikes,balls)

    def _make_all_candidates_num_list(self):
        numbers = [str(x) for x in range(0,10)]
        all_candidates_num_list = [list(num_list) for num_list in permutations(numbers,4)]
        return all_candidates_num_list

    def _make_set_same_strikes_and_ball_candidates_num_list(self,attacker,attack_num_list):
            attacker_info = (attack_num_list,attacker.strikes,attacker.balls)
            for attack_num_list in attacker_info:
                self.__candidates_num_list = [list(num_list) for num_list in self.__candidates_num_list if self._update_strikes_and_balls_count_candidates_num_list(attack_num_list,num_list) ==(attacker.strikes,attacker.balls)]
                return self.__candidates_num_list                  
    
    def _step_one_input_num_list(self,attacker):
            all_candidates_num_list = self._make_all_candidates_num_list()
            attack_num_list = choice(all_candidates_num_list)
            print(attack_num_list)
            return attack_num_list
    
    def _input_attack_num_list(self,attacker,attack_num_list,steps):
            while True:
                candidates_num_list = self._make_set_same_strikes_and_ball_candidates_num_list(attacker,attack_num_list)
                print(len(candidates_num_list))
                attack_num_list = choice(candidates_num_list)
                print(attack_num_list)
                return attack_num_list

        








                    
                
