from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import PostForm

# Create your views here.
def posts_home(request):
    return HttpResponse("<h1>Hello, this is a home page.<h1>")

def posts_list(request):
    queryset = News.objects.filter(draft=False)
    context = {
         "queryset" : queryset,
         "title" : "Lists"
    }
    return render(request, "post_list.html" , context)
    #return HttpResponse("<h1>This is a List.<h1>")

def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        #message succcess
        messages.success(request, "Successfully added this post")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Failed to add this post")

   # if request.method=="POST":
        #content= request.POST.get("content")
        #title= request.POST.get("title")
        #Post.objects.create(title=title, content=content)
        #Post.objects.create(content=content)

    context = {

        "form" : form,
    }
    return render(request, "post_form.html" , context)
    #return HttpResponse("<h1>Create.<h1>")

def posts_detail(request, id=None):
    instance = get_object_or_404(News, id=id)
    context = {
        "title" : "Detail",
        "instance" : instance,
    }
    return render(request, "post_detail.html" , context)
    #return HttpResponse("<h1>Detail.<h1>")

def posts_update(request, id=None):
    instance = get_object_or_404(News, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "Post is updated")
        return HttpResponseRedirect(instance.get_absolute_url)

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render (request, "post_form.html", context)
   # return HttpResponse("<h1>Update.<h1>")

def posts_delete(request, id=None):
    instance = get_object_or_404(News, id=id)
    instance.delete()
    return redirect("posts:list")
    return HttpResponse("<h1>Delete.<h1>")




