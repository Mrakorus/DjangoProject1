from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Post, Category
# Create your views here.
from django.contrib.auth.models import User, Group

# def index(request):
#     return HttpResponse('test site')
# fr = 0
# lr = 10

def initUsr():
    group = Group.objects.get(name="Members")
    users = User.objects.all()
    for user in users:
        if user.is_staff:
            continue
        else:
            user.is_staff = True
            user.groups.add(group)
            user.save()


gpage = 1

def pagePrep(filtrate):
    initUsr()
    fr = 0
    lr = fr + 10
    global gpage
    n = len(filtrate)
    i = 1
    while i != gpage:
        fr = lr
        lr = lr + 10
        i = i + 1

    ar = [ii + 1 for ii in range(n // 10)]
    lastPostList = filtrate.order_by('-postDatePublication')[fr:lr]
    if not ar:
        ar.append(1)
    elif n % 10 != 0:
        ar.append(ar[-1] + 1)
    return {'lastPostList': lastPostList, 'mpage': gpage, 'mnumpage': ar}


# def sendCtgs(request):
#     ctgs = Category.objects.all()
#     return render(request, 'base.html', {'allCategory': ctgs})


def index(request, page=1): # , fr=1, lr=11,  numpage=[1]
    global gpage
    gpage = page
    initUsr()
    filtrate = Post.objects.filter(published=True)
    resdict = pagePrep(filtrate)
    resdict['allCategory'] = Category.objects.all()
    return render(request, 'posts/main.html', resdict)


# def page(request, page=1):

    # if not ar:
    #     ar = [1]
    # return index(request, fr, to, page=page, numpage=ar) # render(request, 'posts/page.html', {'page': page})


def detail(request, postId):
    initUsr()
    try:
        a = Post.objects.get(id=postId)
        b = Category.objects.all()
    except:
        raise Http404('Пост не найден')
    return render(request, 'posts/detail.html', {'post': a, 'allCategory': b})


def category(request, category_id, pg=1):
    initUsr()
    global gpage
    gpage = pg
    postsOfCateg = Post.objects.filter(category=category_id, published=True)
    resdict = dict()
    resdict.update(pagePrep(postsOfCateg))
    resdict['allCategory'] = Category.objects.all()
    resdict['nowCategory'] = Category.objects.get(pk=category_id)
    return render(request, 'posts/category.html', resdict)




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
