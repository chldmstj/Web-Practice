from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
db.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})

all_users = list(db.users.find({}))

same_ages= list(db.users.find({'age':21}))

print(all_users[0])
print("#####")
print(all_users[0]['name'])
print("######")
for user in all_users:
    print(user)

print("#####")
for user in same_ages:
    print(user)

print("#####")

user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)


print("####")

# 생김새
#db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })

# 예시 - 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print(user)

print("############")

db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print(user)