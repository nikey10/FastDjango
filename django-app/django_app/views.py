import requests
from django.shortcuts import render, redirect

API_URL = "http://localhost:8001/books/"

def book_list(request):
    response = requests.get(API_URL)
    books = response.json()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    response = requests.get(f'{API_URL}{pk}/')
    book = response.json()
    return render(request, 'book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        new_book = {
            'title': request.POST['title'],
            'author': request.POST['author'],
            'price': float(request.POST['price'])
        }
        requests.post(API_URL, json=new_book)
        return redirect('book_list')
    return render(request, 'book_form.html', {'form_action': 'Create'})

def book_edit(request, pk):
    response = requests.get(f'{API_URL}{pk}/')
    book = response.json()

    if request.method == 'POST':
        updated_book = {
            'title': request.POST['title'],
            'author': request.POST['author'],
            'price': float(request.POST['price'])
        }
        requests.put(f'{API_URL}{pk}/', json=updated_book)
        return redirect('book_list')
    return render(request, 'book_form.html', {'book': book, 'form_action': 'Update'})

def book_delete(request, pk):
    if request.method == 'POST':
        requests.delete(f'{API_URL}{pk}/')
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book_id': pk})
