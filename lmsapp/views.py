from django.shortcuts import render ,redirect
from .models import *
from .forms import BookForm ,CategoryForm
# Create your views here.
def index(request):
    context = {
        'books':Book.objects.all(),
        'category':Category.objects.all(),
        'form':BookForm(),
        'catform':CategoryForm(),
    }
    if request.method =='POST':
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    
    return render(request,'pages/index.html',context)

def books(request):
    context ={
        'category':Category.objects.all(),
        'books':Book.objects.all(),
        'catform':CategoryForm(),

    }
    return render(request,'pages/books.html',context)


def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save=BookForm(instance=book_id)
    
    
    context = {
        'form': book_save 
    }
    return render(request,'pages/update.html',context)


def delete(request):
    book_delete = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')