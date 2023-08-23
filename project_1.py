import random
from datetime import datetime
import os


class UpDown:

    # i = 0 
    # 클래스변수로 두면 밑에 클래스를 다시 실행해야하고 __init__안에 넣어서 초기화시켜 그걸 불러오는게 더 나은 방법일수도 

    def __init__(self):
        print("UpDown 게임에 오신걸 환영합니다!\n")
        self.i = 0 #여기다 따로 초기화
        self.start_answer = input("게임을 시작할까요?(y/n)")
        self.start_game()

    def start_game(self):       
        if(self.start_answer == 'y'):
            self.menual()
        elif (self.start_answer == 'n'):
            print("게임을 종료합니다.")
            os.system('clear')
        else :
            self.start_answer = input("다시입력해주십시오.\n게임을 시작할까요?(y/n)")
            self.start_game()

    def menual(self):
        enter = input("1 부터 100까지의 정수를 입력해주십시오.(enter를 눌러주세요.)")
        if not enter == "":
            print("죄송합니다. enter를 눌러주십시오.")
            self.menual()
        self.create_num()

    def create_num(self):
            self.create_random = random.randint(1, 101)
            print(f'random_num : {self.create_random}')
            self.ask_input()

    def ask_input(self):
            self.i = self.i+1
            print(f'<{self.i}>번쨰 시도하겠습니다.')

            try: 
                self.input_num = int(input('정수를 넣어주세요 : '))
            except ValueError:
                print("숫자가 아닙니다")
                self.ask_input()
        
            if self.input_num > 100:
                print('100이상의 숫자는 입력할 수 없습니다.')
                self.ask_input()
            elif self.input_num < 1:
                print('숫자는 0보다 큰 숫자입니다.')
                self.ask_input()
           
            self.try_again()
            

    def try_again(self):
        
        while True:
            if self.input_num > self.create_random:
                print("힌트 : DOWN")
                self.ask_input()
                break

            elif self.input_num == self.create_random:
                self.answer = input('계속 플레이 하시겠습니까?(y/n) : ') 
                #플레이에 다시응하면 시도한만큼의 -1
                #다시응하지않고 플레이취소하면 시도한만큼 계속 플레이 하겠냐고 물어본다....
                #아무래도 while룹에서 벗어나지 않은상태에서 계속 다른 함수를 들락날락거리면서 시도한 수많큼 마지막에 물어보게되는듯.
                #그래서 모든 조건문에 break를 주면..? 더 이상 물어보지않는다.
                self.replay()
                break
                #안해주면 계속 와일룹으로 들어와서 input('계속 플레이 하시겠습니까?(y/n) : ') 물어봄.

            else:
                print("힌트 : Up")
                self.ask_input()
                break
            # self.i = self.i + 1
            #인풋에서 계속해주므로 필요없음
    
    
    def replay(self):
        # self.answer = input('계속 플레이 하시겠습니까?(y/n) : ')
        if self.answer == 'y':
            os.system('clear')
            print('저번 시도 횟수 :  %d' %(self.i))
            self.__init__()
            # UpDown()
        elif self.answer == 'n':
            print('게임을 종료하겠습니다.')
            
        else:
            self.answer = input('잘못 입력하셨습니다.\n다시 입력해 주십시오(y/n):')
            self.replay()
            

       
a = UpDown()

   


