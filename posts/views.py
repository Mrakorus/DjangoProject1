from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Post
# Create your views here.


# def index(request):
#     return HttpResponse('test site')
# fr = 0
# lr = 10


def index(request, page=1): # , fr=1, lr=11,  numpage=[1]
    fr = 0
    lr = fr + 10
    filtrate = Post.objects.filter(published=True)
    n = len(filtrate)
    i = 1
    while i != page:
        fr = lr
        lr = lr + 10
        i = i + 1

    ar = [ii + 1 for ii in range((n // 10) + 1)]
    lastPostList = filtrate.order_by('-postDatePublication')[fr:lr]
    return render(request, 'posts/main.html', {'lastPostList': lastPostList, 'mpage': page, 'mnumpage': ar})


# def page(request, page=1):

    # if not ar:
    #     ar = [1]
    # return index(request, fr, to, page=page, numpage=ar) # render(request, 'posts/page.html', {'page': page})


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
