from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Post
# Create your views here.


# def index(request):
#     return HttpResponse('test site')
# fr = 0
# lr = 10


def index(request, fr=1, lr=11, page=1, numpage=[1,]):
    filtrate = Post.objects.filter(published=True)
    lastPostList = filtrate.order_by('-postDatePublication')[fr-1:lr-1]
    return render(request, 'posts/main.html', {'lastPostList': lastPostList, 'mpage': page, 'mnumpage': numpage})


def page(request, page=1):
    n = len(Post.objects.filter(published=True))
    i = 1
    fr = 1
    to = 11
    while n >= 1:
        if page == i:
            break
        n -= 10
        fr += 10
        to += 10
        i += 1
    ar = [i + 1 for i in range(i)]
    # if not ar:
    #     ar = [1]
    return index(request, fr, to, page=page, numpage=ar) # render(request, 'posts/page.html', {'page': page})


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
