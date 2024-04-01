from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, LoginForm, PostForm
from .models import Post, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#Home
def Home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

#About
def About(request):
    return render(request, 'blog/about.html')

#About
def Contact(request):
    return render(request, 'blog/contact.html')

#Dashboard
def Dashboard(request, id):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=id)
        full_name = request.user.get_full_name
        return render(request, 'blog/dashboard.html', {'posts': posts, 'full_name': full_name})
    else:
        return HttpResponseRedirect('/login/')

#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                id = user.id
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return HttpResponseRedirect('/dashboard/%s' %id)
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        id = user.id
        return HttpResponseRedirect('/dashboard/%s' %id)

#Register
def Register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations! You have become an author")
            form.save()
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form':form})

#Update Post
def Update_post(request, id):
    if request.user.is_authenticated:
        pi = Post.objects.get(pk=id)
        if pi.author == request.user:    
            if request.method == 'POST':
                pi = Post.objects.get(pk=id)
                form = PostForm(request.POST, instance=pi)
                if form.is_valid():
                    form.save()
            else:
                pi = Post.objects.get(pk=id)
                form = PostForm(instance=pi)
            return render(request, 'blog/updatepost.html', {'form': form})
        else:
            messages.error(request, "Forbidden Action")
            return HttpResponseRedirect('/')    
    else:
        return HttpResponseRedirect('/login/')
    
#Add Post
def Add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')
    
#Delete Post
def Delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            id = request.user.id
            return HttpResponseRedirect('/dashboard/%s' %id)
        else:
            messages.error(request, "Forbidden Action")
            return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/login/')
    
#View Post
def View_post(request, id):
        post = Post.objects.get(pk=id)
        return render(request, 'blog/viewpost.html', {'post':post})

#View Author
def View_Author(request, id):
        post = Post.objects.filter(author=id)
        user = User.objects.get(pk = id)
        full_name = user.get_full_name
        return render(request, 'blog/viewauthor.html', {'posts':post, 'full_name': full_name})