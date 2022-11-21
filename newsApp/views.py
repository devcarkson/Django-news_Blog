from django.shortcuts import render
import requests
import http.client, urllib.parse

# Create your views here.
def index(request):
    # conn = http.client.HTTPConnection('api.mediastack.com')

    # params = urllib.parse.urlencode({
    #     'access_key': 'YGuFRSQyZrkQhaJ6Ykpz8tQD9Qr09zVQ',
    #     'categories': '-general,-sports',
    #     'sort': 'published_desc',
    #     'limit': 10,
    #     })

    # conn.request('GET', '/v1/news?{}'.format(params))

    # res = conn.getresponse()
    # data = res.read()

    # print(data.decode('utf-8'))
    # return render(request, 'newsbox/index.html')
    
    

    r = requests.get('http://api.mediastack.com/v1/news?access_key=ed2338c4636d543f5ac15ec9f2c69e55&countries=us')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    published_at = []
    for i in data :
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
        published_at.append(i['published_at'])
    news = zip(title,description,image,url)
    context = {'news':news}
    return render(request, 'newsbox/index.html',context )

    

    # url = "https://api.apilayer.com/world_news/extract-news?url={url}&analyze={analyze}"

    # payload = {}
    # headers= {
    # "apikey": "YGuFRSQyZrkQhaJ6Ykpz8tQD9Qr09zVQ"
    # }

    # response = requests.request("GET", url, headers=headers, data = payload)

    # status_code = response.status_code
    # result = response.text
    # context ={'status_code':status_code,'result':result}
    # return render(request, 'newsbox/index.html', context)
        
        

