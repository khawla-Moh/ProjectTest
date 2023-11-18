from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm

# Create your views here.


def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            myfrom= form.save(commit=False)
            myfrom.author=request.user
            myfrom.save()
            return redirect('/book/')
    else:
        form=BookForm()   
    return render(request,'book/new.html',{'form':form})


def edit_book(request,pk):
    book=Book.objects.get(id=pk)    
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            myfrom= form.save(commit=False)
            myfrom.author=request.user
            myfrom.save()
            return redirect('/book/')
    else:
        form=BookForm(instance=book)
    return render(request,'book/edit.html',{'form':form})

def delete_book(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()
    return redirect('/posts/')



def delete_post(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')
