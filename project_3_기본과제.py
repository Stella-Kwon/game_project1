
import sys 

class Member:

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password
        self.display()
    def display(self):
        print("<회원정보>")
        print(f"이름 : {self.name}\n닉네임 : {self.username}\n")


class Post:

    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author


#빈 리스트 생성
members = []
posts = []


#3개의 멤버생성 -> 리스트 붙이기
mem1 = Member('수민','tnals','tnals1234')
members.append(mem1)
mem2 = Member('철수','joe','joe1234')
members.append(mem2)
mem3 = Member('영희','elle','qwert1234')
members.append(mem3)


#멤버이름만 나오게 만들기
for member in members:
    #클라스인스턴스를 돌면서 그안에 들어가 name 호출
    print(member.name)
print('\n')


#Post()인스턴스 생성하고 posts리스트에 붙이기
posts.append(
    Post("post1-1","안녕하세요?",mem1.username)
    )
posts.append(
    Post("post1-2","반갑습니다.",mem1.username)
    )
posts.append(
    Post("post1-3","수민입니다.",mem1.username)
    )


posts.append(
    Post("post2-1","안녕하세요????",mem2.username)
    )
posts.append(
    Post("post2-2","반갑습니다....",mem2.username)
    )
posts.append(
    Post("post2-3","철수입니다....",mem2.username)
    )


posts.append(
    Post("post3-1","안녕하세요!",mem3.username)
    )
posts.append(
    Post("post3-2","반갑습니다!",mem3.username)
    )
posts.append(
    Post("post3-3","영희입니다!",mem3.username)
    )

print(posts)
print(members)
# mem1_P1 = Post("post1-1","안녕하세요?",mem1.username)
# mem1_P2 = Post("post1-2","반갑습니다.",mem1.username) 
# mem1_P3 = Post("post1-3","수민입니다.",mem1.username)
  
# mem2_P1 = Post("post2-1","안녕하세요????",mem2.username)
# mem2_P2 = Post("post2-2","반갑습니다....",mem2.username)
# mem2_P3 = Post("post2-3","철수입니다....",mem2.username)

# mem3_P1 = Post("post3-1","안녕하세요!",mem3.username)  
# mem3_P2 = Post("post3-2","반갑습니다!",mem3.username)
# mem3_P3 = Post("post3-3","영희입니다!",mem3.username)
  
# posts.append(mem1_P1)
# posts.append(mem1_P2)
# posts.append(mem1_P3)
# posts.append(mem2_P1)
# posts.append(mem2_P2)
# posts.append(mem2_P3)
# posts.append(mem3_P1)
# posts.append(mem3_P2)
# posts.append(mem3_P3)



#특정유저 작성한 게시글의 제목을 프린트
for post in posts:
    if post.author == mem1.username:
        print(f'{post.title}')
print('\n')


#특정단어가 content 포함된 게시글의 제목 모두 프린트
for post in posts:
    if '!' in post.content :
        print(f'{post.title}')
print('\n')





#두개의 다름이 없음, 그저 좀더 확실히 str으로 취급해주기 위해 map 사용 , 수가 입력받아질수있으니.
# p, q, r = sys.stdin.readline().split()

# print("p : ", p)
# print("q : ", q)
# print("r : ", r)
# print(type(p))
# p, q, r = map(str, sys.stdin.readline().split())

# print("p : ", p)
# print("q : ", q)
# print("r : ", r)
# print(type(p))
