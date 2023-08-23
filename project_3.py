# from y import Member, Post
import sys
import os
# import bcrypt 다른방법의 해시화
import hashlib

class Member:

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password
        self.display()

    def display(self):
        print("<회원정보>")
        print(f"이름 : {self.name}\n아이디 : {self.username}\n")

        def hash_password(self, salt=None):
        if salt is None:
        #솔트랜덤생성
            salt = os.urandom(16)#리눅스 난수 생성
    
        #솔트와 비번 합쳐준다음에 결과 해쉬화
        password_salt_combi = self.password.encode('utf-8') + salt
        self.hashed_password = hashlib.sha256(password_salt_combi).hexdigest()
            
        return self.hashed_password, salt
    
    def verify_password(self):
        #해쉬화된 비번과 지금 인풋한 비번 맞는지 체크 
        input_hashed, _ = self.hash_password(self.password, self.salt)
        return input_hashed == self.hashed_password
    

class Post:

    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author


class Create_Mem():
    
    # add = 0
    members = []
    posts = []


    
    def login(self):
        if input("1.로그인하시겠습니까? 아니면 2.회원가입을 하시겠습니까?(1/2)\n") == '2':
            self.get_info()
        else:
            login_id = input("로그인해주십시오.\n아이디를 입력해주십시오. : \n")
            if not login_id == self.username:
                print("다시 시도 해주십시오\n")
                self.login()
            login_pw = input("\n 비밀번호를 입력해주십시오. : \n")
            if self.verify_password():
                print("로그인되셨습니다.")
                self.posting()

        
            

    def get_info(self):
        a = input("회원가입을 위한 정보를 제공해주시겠습니까?(y/n)")
        if a == 'y':
            print("\n이름,아이디,비번(순서대로 ','로 구분해 주세요.) : \n")
            self.text = sys.stdin.readline() # => str타입
            if self.text == '':
                print("다시 입력 부탁드립니다.\n")
                self.get_info()
            self.table  = self.text.maketrans({'\n' : '', ' ' : ''}) 
            # print(type(table)) # => dict타입
            self.info = self.text.translate(self.table) #text는 무조건 str이어야되고 table은 dic, 아니면 translate사용x
            self.name, self.username, self.password = self.info.split(',')
            # print(info) #=> split 결과값 리스트형태로 나타나줌
            Member.hash_password(self)
            a = input(f'\n{self.name, self.username, self.password}가 정확합니까?(y/n)\n')
            if  a == 'y' or a == '':
                self.make_mem()
            else:
                print("다시 입력 부탁드립니다.\n")
                self.get_info()
            
        elif a == 'n':
            print("종료하겠습니다.\n")
        
        else:
            self.get_info()
   
    def make_mem(self):
       
        mem = Member(self.name, self.username, self.password)
        # print(Create_Mem.members)
        Create_Mem.members.append(mem)
        # print(Create_Mem.members)
        print("멤버가 생성되었습니다.\n")
        self.posting()

    def posting(self):
        a = input("포스팅을 하시겠습니까?(y/n)\n")
        if a == 'y' or a == '':
            self.postinfo = input("제목,내용을 순서대로 ','로 구분해 적어주세요. :")
            if self.postinfo == '':
                self.posting()
            self.title, self.content = self.postinfo.split(',')
            # print(info) #=> split 결과값 리스트형태로 나타나줌
            a = input(f'\n{self.title, self.content, self.username}가 정확합니까?(y/n)\n')
            if  a == 'y' or  a == '':
                self.make_post()
            else:
                print("다시 입력 부탁드립니다.\n")
                self.posting()
            
        elif a == 'n':
            print("종료하겠습니다.\n")    
        
        else: 
            self.posting()
    
    def make_post(self):

        posting = Post(self.title, self.content, self.username)
        # print(Create_Mem.posts)
        Create_Mem.posts.append(posting)
        # print(Create_Mem.posts)
        print(f'<제목{self.title}>\n글쓴이 :{self.username}\n내용:\n{self.content}')
        print("포스팅 되었습니다.")

    
   


a = Create_Mem()
a.login()
