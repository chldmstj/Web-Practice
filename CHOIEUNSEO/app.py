from flask import Flask,render_template,request,jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import random
client = MongoClient('localhost',27017)
db = client.dbEUNSEO


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo',methods=['POST'])
def post_article():
   title_receive = request.form['title_give']
   content_recieve = request.form['content_give']
   db.memo.insert_one(SORT(title_receive,content_recieve))
   return jsonify({'result':'success'})


def SORT (title_receive,content_recieve):
    card_id = str(random.randint(0,10000))
    edit_box_id = 'edit_box_id'+card_id
    edit_title_id = 'edit_title'+card_id
    edit_text_id = 'edit_text'+card_id
    doc = {
        'card_id': card_id,
        'edit_box_id': edit_box_id,
        'title': title_receive,
        'content': content_recieve,
        'edit_title_id': edit_title_id,
        'edit_text_id': edit_text_id
    }
    return doc

@app.route('/delete',methods=['POST'])
def DEL ():
    title = request.form['title']


    db.memo.delete_one({'title':title})
    return jsonify({'result':'success'})

@app.route('/edit',methods=['POST'])
def Edit ():
    title = request.form['title']
    card_id = request.form['card_id']
    content = request.form['content']
    db.memo.update_one({'card_id': card_id}, {'$set': {'title': title,'content':content}})
    return jsonify({'result':'success'})

@app.route('/memo',methods=['GET'])
def show():
   memos = list(db.memo.find({},{'_id':False}))
   print(memos)

   return jsonify({'result':'success','memos':memos})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5005,debug=True)