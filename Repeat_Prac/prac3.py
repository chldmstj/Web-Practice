import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

lists = soup.select('table.list_ranking > tbody >tr')
ranks = soup.select_one('td.ac > img')['alt']

for list in lists :

    title = list.select_one('div.tit5 > a')
    if title is not None:
        title = title['title']
        rank = list.select_one('td.ac > img')['alt']
        point = list.select_one('td.point').text
        print("{} {} {}".format(rank,title,point))
    #print(rank,title,point)
    #print(title)

#print(list)
#print(ranks)

#############################
# (입맛에 맞게 코딩)
#############################