from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from blog.models import Blog,Category
def home(request):
    try:
        cat = request.GET['cat']
    except:
        cat = None
    if cat is None:
        blog = Blog.objects.all()[::-1] # SELECT * FROM blog
    else:
       blog = Blog.objects.filter(category_id=cat)

    cat= Category.objects.all()
    context = {
        'blog':blog,
        'cat':cat,
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def createCategory(request):
    if request.method=='GET':
        return render(request,'createcategory.html')
    else:
        t =request.POST['category']
        c = Category(title=t)
        c.save()
        return redirect('home')

def createBlog(reqeust):
    if reqeust.method=='GET':
        category = Category.objects.all()
        context = {
            'category':category,
        }
        return render(reqeust,'create-blog.html',context)
    else:
        title = reqeust.POST['title']
        description =reqeust.POST['description']
        image = reqeust.FILES['image']
        cate = reqeust.POST['category']
        b = Blog(title=title,description=description,image=image,category_id=cate)
        b.save()
        return redirect('home')

def details(request,id):
    blog = get_object_or_404(Blog,id=id)
    context = {
        'blog':blog
    }
    return render(request,'details.html',context)

def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('home')