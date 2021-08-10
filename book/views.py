from typing import Reversible
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.utils.text import slugify
from .models import book
from django.core.paginator import Paginator
from .form import bookForm
from django.urls import reverse
from .filters import booktFilter
from django.contrib.auth.decorators import login_required
@login_required
def bookList(request):
    bookList=book.objects.all()

    myfilter=booktFilter(request.GET,queryset=bookList)
    bookList=myfilter.qs

    paginator=Paginator(bookList,1)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={'bookList':page_obj,'myfilter':myfilter}
    return render(request,'book/bookList.html',context)

@login_required
def bookDetails(request,slug):
    bookDetails=book.objects.get(slug=slug)
    context={'book':bookDetails}
    return render(request,'book/bookDetails.html',context)

@login_required
def addBook(request):
    if request.method=='POST':
        form=bookForm(request.POST,request.FILES)
        if form.is_valid():
            print ('valid')
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('books:bookList'))

    else :
        form=bookForm()


    return render(request,'book/addBook.html',{'form':form})
@login_required
def editBook(request,slug):
    editBook=book.objects.get(slug=slug)
    if (request.method=='POST'):
        form=bookForm(request.POST,instance=editBook)
        if form.is_valid:
            form.save()
        context={'book':editBook}
        return render(request,'book/bookDetails.html',context)
            
    else :
        form=bookForm(instance=editBook)
    return render(request,'book/editBook.html',{'form':form})

# Create your views here.
