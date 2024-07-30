from django.shortcuts import render
from django.http import HttpRequest
from .models import Twik
from .forms import Twikform
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisForm

# Create your views here.
# def first1(request):
#return render(request, 'index.html')#request send to index.html

def show_tweets(request):
    tweets = Twik.objects.all()
    return render(request,'tweets.html',{'tweets':tweets})

@login_required
def addTweet(request):
    if request.method == 'POST':
        form = Twikform(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('show_tweets')
    else:
        form=Twikform()
    return render(request, 'add_tweet.html', {'form': form})#it is in "POST" or not, it always "render" if used as "link" to add_tweet.html and if used in "form" ⭐"csrf token" then its used as "function" 

@login_required
def edit_tweet(request,id):
    tweet=get_object_or_404(Twik,pk=id, user=request.user)
    if request.method=='POST':
        form=Twikform(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('show_tweets')
    else:
      form=Twikform(instance=tweet)#what tweet is edited is called through "instance"
    return render(request, 'add_tweet.html', {'form': form})


@login_required
def delete_tweet(request,id):
    tweet = get_object_or_404(Twik, pk=id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('show_tweets')
    return render(request, 'delete_tweet.html', {'tweet': tweet})
    
def home(request):
    return redirect('show_tweets')     

def registration(request):
    if request.method =='POST':
        form = RegisForm(request.POST)
        if form.is_valid():
           user= form.save(commit=False)
           user.set_password(form.cleaned_data['password2'])
           user.save()
           login(request,user)
           return redirect('show_tweets')
    else:
        form = RegisForm()
    return render(request, 'registration/register.html', {'form': form})



    