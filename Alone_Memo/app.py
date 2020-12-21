from flask import Flask,render_template,request,jsonify
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
#client = MongoClient('mongodb://EUNSEO:1234@15.165.235.114', 27017)
client=MongoClient('localhost',27017)
db = client.dbmemo
app = Flask(__name__)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/memo',methods=['POST'])
def post():
    post_url = request.form['url_give']
    post_comment = request.form['comment_give']
    data = requests.get(post_url)
    soup = BeautifulSoup(data.text,'html.parser')
    title = soup.select_one('meta[property="og:title"]')['content']
    description = soup.select_one('meta[property="og:description"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    if(title=='None'): title = 'Loading Fail'
    if(description=='None'): description = 'Loading Fail'
    if(image=='None'): image = 'https://d2ur7st6jjikze.cloudfront.net/offer_photos/29590/185689_medium_1525763241.jpg?1525763241'

    db.post.insert_one({'post_url':post_url, 'post_comment':post_comment,
                        'title':title,'description':description,
                        'image':image})




    print(('title:{}\ndescrption:{}\nimage:{}').format(title,description,image))



    return jsonify({'result':'success'})

@app.route('/memo',methods=['GET'])
def readData():
    posts = list(db.post.find({},{'_id':False}))
    # for post in posts:
    #     print(('post_url: {} post_comment: {} title: {} description: {} image: {}').format(
    #         post['post_url'],post['post_comment'],post['title'],post['description'],post['image']))
    print(posts)

    return jsonify({'result':'success','articles':posts})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5050, debug=True)
