from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Book, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class Book_List(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/books_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list_book'] = Category.objects.all()
        return context


class Category_list(ListView):
    model = Book
    template_name = 'books/books_list.html'

    def get_queryset(self):
        category_list_type = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Book.objects.filter(category=category_list_type)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list_book"] = Category.objects.all()
        return context


class Book_Detail(DetailView):
    model = Book
    context_object_name = "book_detail"


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'file', 'photo', 'category', 'description', 'author', 'page', 'isbn', 'publisher', 'year',
              'lanquages', 'country']
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'file', 'photo', 'category', 'description', 'author', 'page', 'isbn', 'publisher', 'year',
              'lanquages', 'country']
    success_url = reverse_lazy('book_list')


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')


class Search_Book(ListView):
    paginate_by = 3
    template_name = 'books/books_list.html'

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
