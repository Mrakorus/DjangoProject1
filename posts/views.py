from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Post
# Create your views here.


# def index(request):
#     return HttpResponse('test site')

def index(request):
    lastPostList = Post.objects.order_by('-postDatePublication')[:10]
    return render(request, 'posts/main.html', {'lastPostList': lastPostList})


def detail(request, postId):
    try:
        a = Post.objects.get(id=postId)
    except:
        raise Http404('Пост не найден')
    return render(request, 'posts/detail.html', {'post': a})





# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
#
# def vote(request, question_id):
#   return HttpResponse("You're voting on question %s." % question_id)#
