import random

class RoSiPa:

    list = ['rock', 'scissors', 'paper']
    result = {'플레이어의 승리' : 0,'컴퓨터의 승리' : 0,'무승부' : 0}

    def __init__(self):
        self.computer = random.choice(RoSiPa.list)
        self.player = input("rock/scissors/paper 중 하나를 적어주세요. : ")
        self.comparison()


    def comparison(self):

        if (self.computer == self.player.lower()) or (self.computer.upper() == self.player.upper()):
            print("무승부")
            self.result['무승부'] = self.result['무승부'] + 1
        
        else:

            if self.player.lower() != 'scissors' and self.player.lower() != 'rock' and self.player.lower() != 'paper':
           # 간혹 위에있는 조건문들과 겹쳐져 제외될 수 있는 조건없게될때 if 문으로 따로 실행 또는 맨위로 올려준다.
                print("선택지에 없는 입력입니다.")
                self.answer = input("다시 적으시겠습니까 ?(y/n) : ")
                self.retry()

            elif self.computer == 'rock':
                if self.player.lower() == 'paper':
                    print("winner")
                    self.result['플레이어의 승리' ] = self.result['플레이어의 승리' ] + 1
                elif self.player.lower() == 'scissors':
                    print("Loser")
                    self.result['컴퓨터의 승리'] = self.result['컴퓨터의 승리'] + 1

            elif self.computer == 'scissors':
                if self.player.lower() == 'rock':
                    print("winner")
                    self.result['플레이어의 승리' ] = self.result['플레이어의 승리' ] + 1
                elif self.player.lower() == 'paper':
                    print("Loser")
                    self.result['컴퓨터의 승리'] = self.result['컴퓨터의 승리'] + 1
            
            elif self.computer == 'paper':
                if self.player.lower() == 'scissors':
                    print("winner")
                    self.result['플레이어의 승리' ] = self.result['플레이어의 승리' ] + 1
                elif self.player.lower() == 'rock' :
                    print("Loser")
                    self.result['컴퓨터의 승리'] = self.result['컴퓨터의 승리'] + 1

        self.answer = input("다시 게임을 시도하시겠습니까?(y/n) : ") 
        self.retry()        
    
    def retry(self):
       
        if self.answer == 'y':
            self.__init__() 
        
        elif self.answer == 'n':
            print("게임을 종료하겠습니다.")
            self.printout_result()

        else :
            self.answer = input("허용되지 않는 입력입니다. 다시입력해주십시오 (y/n)")
            self.retry()

    def printout_result(self):
        print(f"플레이어의 승리 : {self.result['플레이어의 승리']}, 컴퓨터의 승리 : {self.result['컴퓨터의 승리']}, 무승부 : {self.result['무승부']}")
        #계속 프로그램이 아에 끝이 날때까지 값을 가지고 있어야하기때문에 __init__에서 초기화 시켜지 않는다.

a = RoSiPa()