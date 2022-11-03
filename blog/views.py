from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django_tables2 import SingleTableView
from .tables import PostTable
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class PostTableListView(SingleTableView):
	model = Post
	table_class = PostTable
	template_name = 'blog/tables.html'



# Create your views here.
'''posts = [
	{
		'Author' : 'Faiyaz Khan',
		'Title' : 'Blog Posts 1',
		'Content' : 'Content Of First Post',
		'Date_posted' : 'October 22 2022'
	},


	{
		'Author' : 'Rushikesh Jamodkar',
		'Title' : 'Blog Posts 2',
		'Content' : 'Content Of Second Post',
		'Date_posted' : 'November 23 2022'
	},


	{ 
		'Author' : 'Deep Aware',
		'Title' : 'Blog Posts 3',
		'Content' : 'Content Of Third Post',
		'Date_posted' : 'December 22 2022'
	}
]

'''


def home(request):
	Context = 	{
		'posts' : Post.objects.all()
				}
	return render(request, 'blog/home.html', Context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-Date_posted']
	paginate_by = 6


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 6

	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return Post.objects.filter(Author = user).order_by('-Date_posted')


class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin,  CreateView):
	model = Post
	fields = ['Tittle', 'Content']

	def form_valid(self, form):
		form.instance.Author = self.request.user
		return super().form_valid(form)

	

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['Tittle', 'Content']

	def form_valid(self, form):
		form.instance.Author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.Author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.Author:
			return True
		return False


def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})



