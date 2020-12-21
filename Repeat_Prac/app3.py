from flask import Flask,render_template,request,jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbrepeats


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index3.html')

@app.route('/mypage',methods=['POST'])
def post_article():
   url_give = request.form['url_give']
   comment_give = request.form['comment_give']
   print(url_give)
   doc = data_Parse(url_give,comment_give)
   db.article.insert_one(doc)
   return jsonify({'result':'success'})


def data_Parse(url,comment):
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

   data = requests.get(url, headers=headers)
   soup = BeautifulSoup(data.text, 'html.parser')
   title = soup.select_one('meta[property="og:title"]')['content']
   description = soup.select_one('meta[property="og:description"]')['content']
   print(title+" "+description)
   img_url = soup.select_one('meta[property="og:image"]')['content']
   doc ={
      'title':title,
      'description': description,
      'url': url,
      'img_url': img_url,
      'comment' : comment
   }
   return doc

@app.route('/show',methods=['GET'])
def show():
   articles = list(db.article.find({},{'_id':False}))

   return jsonify({'result':'success','articles':articles})
   # doc={}
   # for article in articles:
   #    doc = {'title':article['title'],
   #    'description':article['description'],
   #    'url':article['url'],
   #    'comment':article['comment'],
   #    'img_url':article['img_url']
   #           }


if __name__ == '__main__':
   app.run('0.0.0.0',port=5005,debug=True)