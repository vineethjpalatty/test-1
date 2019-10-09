from django.shortcuts import render, redirect

from .models import ModelPost
from django.views import View
from .forms import PostForm
class Blog(View):
    def get(self,request):
        form = PostForm()
        return render(request, 'posts/hello.html', {
            'form': form,
        })
    def post(self,request):
        form = PostForm(request.POST,request.FILES)
        form.save()
        print(form)



        return redirect('display')




def BlogView2(request):
    posts=ModelPost.objects.all()
    form=PostForm

    if 'q' in request.GET:
        search_term = request.GET['q']
        print(search_term)
        posts = posts.filter(title__icontains=search_term)
    print(posts)
    args={'posts':posts,'form':form}
    return render(request,"posts/show.html",args)