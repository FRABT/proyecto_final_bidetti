from django.shortcuts import render
from blog.models import Blog
from blog.forms import BlogForm
from django.views.generic.detail import DetailView
from django.views.generic import ListView


def blog_forms_view(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            data = blog_form.cleaned_data
            blog = Blog(
                date=data['date'],
                autor=data['autor'],
                title=data['title'],
                subtitle=data['subtitle'],
                body=data['body'],
            )
            blog.save()

            blogs = Blog.objects.all()
            context_dict = {
                'blogs': blogs
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog/blog_list.html"
            )

    blog_form = BlogForm(request.POST)
    context_dict = {
        'blog_form': blog_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog/blog_form.html'
    )

class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    fields = ['title', 'subtitle', 'date', 'autor', 'body']