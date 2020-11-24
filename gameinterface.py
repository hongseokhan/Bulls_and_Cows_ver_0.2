from human import Human
from computer import Computer

class Gameinterface:

    
    def _strikes_and_balls_counter(self,attacker,defender,attack_num_list):
        attacker.strikes = 0
        attacker.balls = 0
        for n,nvalue in enumerate(attack_num_list):    
            for m,mvalue in enumerate(defender.defense_num_list):
                if nvalue == mvalue:
                    if n == m:
                        attacker.strikes += 1
                    else:
                        attacker.balls += 1
            
        attacker.trys += 1

    def _attack_result(self,attacker):
        if attacker.strikes ==0 and attacker.balls == 0:
            print(f'<{attacker.trys}차 시도>, Nothing 입니다.')
            print('-----------------------------------------------')
        
        else:
            print(f'<{attacker.trys}차시도> {attacker.strikes}스트라이크 {attacker.balls}볼 입니다.')
            print('-----------------------------------------------')  
                
    def _game_result(self,player1,player2):
        
        if player2.strikes == 4 and player1.strikes == 4:
            print('\n 동점입니다 다시 한번 붙어 보세요')
        
        elif player1.strikes == 4:
            print('\n player1님 축하합니다')
            print(f'{player1.trys}회 시도만에 성공 했습니다\n')
            print(f'player2 가지고 있는 수비 숫자는 {player2.__defense_num_list}입니다')
            print('==============================================')
            print('\n player2님 아쉽습니다')
            print(f'{player2.trys}회 시도만에 게임에 패배 했습니다.')
            print(f'player1이 가지고 있는 수비 숫자는 {player1.__defense_num_list}입니다')
        
        elif player2.strikes == 4:        
            print('\n player2님 축하합니다')
            print(f'{player2.trys}회 시도만에 성공 했습니다\n')
            print(f'player1 가지고 있는 수비 숫자는 {player2.__defense_num_list}입니다')
            print('==============================================')
            print('\n player1님 아쉽습니다')
            print(f'{player1.trys}회 시도만에 게임에 패배 했습니다')
            print(f'player2 가지고 있는 수비 숫자는 {player2.__defense_num_list}입니다')   

    def gamerun(self):
        
        mode = input('\n 게임모드를 선택하세요:    ')
        
        if mode == '1':
            print("PVE 대전모드 입니다.")
            player1  = Computer()
            player2  = Human()
            print('player1의 수비 4자리 숫자가 랜덤으로 생성되었습니다')
            player1._random_defense_num_list_generator()
            print('player2의 수비 4자리 숫자를 선택해주세요')
            player2._input_defense_num_list()
            steps = 0
            while True:
                print('-----------------------------------------------')
                print('플레이어 1의 공격차례 입니다.')
                player1_attack_num_list = player1._input_attack_num_list(player1,steps)
                self._strikes_and_balls_counter(player1, player2, player1_attack_num_list)
                self._attack_result(player1)
                steps += 1
                print('플레이어 2의 공격차례 입니다.')
                player2_attack_num_list = player2._input_attack_num_list()
                self._strikes_and_balls_counter(player2, player1, player2_attack_num_list)
                self._attack_result(player2)
                if player1.strikes == 4 or player2.strikes == 4:
                    self._game_result(player1,player2)
        elif mode == '2':
            print("PVP 대전모드 입니다.")
            player1  = Human()
            player2  = Human()
            print('player1의 수비 4자리 숫자를 선택해주세요')
            player1._input_defense_num_list()
            print('player2의 수비 4자리 숫자를 선택해주세요')
            player2._input_defense_num_list()
                
                
            while True:
                print('-----------------------------------------------')
                print('플레이어 1의 공격차례 입니다.')
                player1_attack_num_list = player1._input_attack_num_list()
                self._strikes_and_balls_counter(player1, player2, player1_attack_num_list)
                self._attack_result(player1)
                
                    
                print('플레이어 2의 공격차례 입니다.')
                player2_attack_num_list = player1._input_attack_num_list()
                self._strikes_and_balls_counter(player2, player1, player2_attack_num_list)
                self._attack_result(player2)
                if player1.strikes == 4 or player2.strikes == 4:
                    self._game_result(player1,player2)

                    break
                
                