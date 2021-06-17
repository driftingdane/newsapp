# importing api
from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
	newsapi = NewsApiClient(api_key = 'cdfb7cdd19604694a135548942692a90')
	top = newsapi.get_top_headlines(sources = 'bbc-news')
	
	l = top['articles']
	desc = []
	news = []
	img = []
	link = []
	
	for i in range(len(l)):
		f = l[i]
		news.append(f['title'])
		desc.append(f['description'])
		link.append(f['url'])
		img.append(f['urlToImage'])
		
	mylist = zip(news, desc, link, img)
	
	return render(request, 'index.html', context = {"mylist":mylist})
