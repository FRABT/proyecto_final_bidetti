from django.shortcuts import render
from comment.models import Comment
from comment.forms import CommentForm


def comment(request):
    comments = Comment.objects.all()

    context_dict = {
        'comments' : comments
    }

    return render(
        request=request,
        context=context_dict,
        template_name="comment/comment.html"
    )

def comment_forms_view(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            comment = Comment(
                date=data['date'],
                title=data['title'],
                body=data['body'],
            )
            comment.save()

            comments = Comment.objects.all()
            context_dict = {
                'comments': comments
            }
            return render(
                request=request,
                context=context_dict,
                template_name="comment/comment.html"
            )

    comment_form = CommentForm(request.POST)
    context_dict = {
        'comment_form': comment_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='comment/comment_forms.html'
    )