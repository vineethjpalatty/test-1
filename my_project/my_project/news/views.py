from django.shortcuts import render, redirect
import requests
from .models import Editorial
from .forms import EditorialForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def news(request):
    url = 'https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=f9454a944cd14fdea4fb920d5a5378af'

    news_data = []
    r = requests.get(url).json()

    for i in range(9):
        city_news = \
            {

                'title': r['articles'][i]['title'],
                'description' : r['articles'][i]['description'],
                'image': r['articles'][i]['urlToImage'],
                'url': r['articles'][i]['url']
            }
        news_data.append(city_news)

    context = {

                'news_data': news_data
              }

    return render(request, 'news.html', context)


def category(request, tag):
    url = "https://newsapi.org/v2/everything?q={}&apiKey=f9454a944cd14fdea4fb920d5a5378af"
    category = tag
    category_data = []
    a = category

    c = requests.get(url.format(category)).json()

    for i in range(9):
        category_news = \
            {

                'title': c['articles'][i]['title'],
                'description': c['articles'][i]['description'],

                'url': c['articles'][i]['url']
            }
        category_data.append(category_news)
    #
    context = {
                'name': a,
                'category_data': category_data
              }

    return render(request, 'category.html', context)





def about(request):
    return render(request,'about.html')

@user_passes_test(lambda u: u.is_superuser,login_url='/falseuser/')
def editorial(request):

    if request.method == 'POST':

        form = EditorialForm(request.POST)
        form.save()
        return redirect('editorial')
    else:
        form = EditorialForm()
        return render(request,'editorial.html',{
            'form': form,
        })

def falseuser(request):
    return render(request,'falseuser.html')

def articles(request):
    article = Editorial.objects.all()
    form=EditorialForm()

    args= {'form':form,'article':article}

    return render(request,'articles.html',args)


@user_passes_test(lambda u: u.is_superuser,login_url='/falseuser/')
def delete_article(request, article_name):
        Editorial.objects.get(Heading=article_name).delete()
        return redirect('articles')