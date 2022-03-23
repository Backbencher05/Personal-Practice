from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'testapp/home.html')

def movie_news_views(request):
    news1 = 'In telgu DevDas movie is not good'
    news2 = 'salman Updating minimum 100 crore for the movie'
    news3 = 'Solali slowly getting merrage'
    news4 = 'In telgu DevDas movie is not good'
    news5 = 'Amitabh back again'

    my_dict = {'news1': news1,'news2': news2,'news3': news3,'news4': news4,'news5': news5}
    return render(request,'testapp/mnews.html', my_dict)
    
def politics_news_view(request):
    return render(request, 'testapp/ponews.html')

def sport_news_view(request):
    return render(request, 'testapp/spnews.html')
    
