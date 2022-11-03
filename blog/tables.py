import django_tables2 as table
from .models import Post

class PostTable(table.Table):
	class Meta:
		model = Post
		template_name = "django_tables2/bootstrap.html"
		fields = ('Tittle', 'Date_posted', 'Author', 'Content')