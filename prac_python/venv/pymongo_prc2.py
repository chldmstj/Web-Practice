from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

matrics_star = db.movies.find_one({'title':'매트릭스'})['star']

movies = list(db.movies.find({}))
doc=[]
for movie in movies:
    if movie['star'] == matrics_star:
      print(movie['title'])
      #doc.append(movie['title'])


print("#######################")


target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']
movies = list(db.movies.find({'star':target_star}))

for movie in movies:
    print(movie['title'])



db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})