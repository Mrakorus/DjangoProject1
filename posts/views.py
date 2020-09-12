from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Post, Category
# Create your views here.
from django.contrib.auth.models import User, Group

# def index(request):
#     return HttpResponse('test site')
# fr = 0
# lr = 10


def index(request, page=1): # , fr=1, lr=11,  numpage=[1]

    group = Group.objects.get_or_create(name="Members") # Group(name="Members")
    users = User.objects.all()
    for user in users:
        if user.is_staff:
            continue
        else:
            user.is_staff = True
            user.groups.add(group)
            user.save()

    fr = 0
    lr = fr + 10
    filtrate = Post.objects.filter(published=True)
    n = len(filtrate)
    i = 1
    while i != page:
        fr = lr
        lr = lr + 10
        i = i + 1

    ar = [ii + 1 for ii in range(n // 10)]
    lastPostList = filtrate.order_by('-postDatePublication')[fr:lr]
    if not ar:
        ar.append(1)
    elif n % 10 != 0:
        ar.append(ar[-1] + 1)
    # if not lastPostList:
    #     ar.pop()
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


def category(request, category_id):
    postsOfCateg = Post.objects.filter(category=category_id)
    allCategory = Category.objects.all()
    nowCategory = Category.objects.get(pk=category_id)
    return render(request, 'posts/category.html', {'postsOfCateg': postsOfCateg, 'allCategory': allCategory,
                                                   'nowCategory': nowCategory})




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
