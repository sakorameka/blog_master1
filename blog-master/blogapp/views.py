from django.core.paginator import Paginator
from django.db.models import Count , Q
from django.shortcuts import redirect, render , get_object_or_404
from django.views import View
from newsletter.models import NewsLetter
from django.contrib import messages


from .models import Post , Comment , Category , Tag


def category_count():
    return Post.objects.values('categories__text').annotate(Count('categories'))



class IndexView(View):
    def get(self , request , *args , **kwarg):
        context = {
            'posts':Post.objects.filter(featured = True), 
            'latest':Post.objects.order_by('-created_at')[:3]
        }
        return render(request ,  'index.html' ,  context)

    def post( self , request , *args , **kwargs):
        email = request.POST.get('email')
        newsl = NewsLetter()
        newsl.email = email
        newsl.save()
        messages.success(request, 'Thank you for subscribing to the newsletter of Cyber Crush')
        return redirect('home')




class BlogView(View):
    def get(self , request , *args , **kwargs):

        query= request.GET.get('query')
        tags = Tag.objects.all()
        if query:
            posts = Post.objects.filter(
                Q(title__icontains= query) |
                Q(text__icontains= query) 
            ).distinct()
            latest = Post.objects.order_by('-created_at')[:3]
            pagdinated_list = Paginator(posts , 5)
            page_num = request.GET.get('page' , 1)
            categories_count = category_count()
            post_list_on_current_page = pagdinated_list.page(page_num)
            context = {
                'obj_list':post_list_on_current_page ,
                'latest': latest, 
                'page_num':page_num, 
                'category_count':category_count , 
                'tags':tags
            }

        else:
            posts = Post.objects.all()
            pagdinated_list = Paginator(posts , 5)
            page_num = request.GET.get('page' , 1)
            categories_count = category_count()
            post_list_on_current_page = pagdinated_list.page(page_num)
            latest = Post.objects.order_by('-created_at')[:3]
            context = {
                'obj_list':post_list_on_current_page ,
                'latest':latest, 
                'page_num':page_num, 
                'category_count':category_count , 
                'tags':tags
            }

        return render(request ,  'blog.html' ,  context)





class PostView(View):
    def get(self , request , *args , **kwargs):
        slug = kwargs.get("slug")
        tags = Tag.objects.all()
        post_obj = get_object_or_404(Post , slug = slug)
        post_obj.views += 1
        post_obj.save()
        categories_count = category_count()
        latest = Post.objects.order_by('-created_at')[:3]
        context = {
            'post':post_obj , 
            'latest':latest, 
            'category_count':categories_count , 
            'tags':tags
        }
        return render(request ,  'post.html' , context)

class CommentView(View):
    def post(self , request , *args , **kwargs):
        slug = kwargs.get("slug")
        email   = request.POST.get('email') 
        name    = request.POST.get('name')
        comment = request.POST.get('comment')
        post_obj = get_object_or_404(Post , slug = slug)
        comment_obj = Comment.objects.create(name=name , email = email , comment_text = comment)
        comment_obj.save()
        post_obj.comments.add(comment_obj)
        return redirect('post-detail', slug)

class CategoryView(View):
    def get(self , request , *args , **kwargs):
        category  = kwargs.get('category').strip()
        cat = Category.objects.filter(text = category )
        posts  = Post.objects.filter(categories__in = cat)
        pagdinated_list = Paginator(posts , 5)
        page_num = request.GET.get('page' , 1)
        categories_count = category_count()
        post_list_on_current_page = pagdinated_list.page(page_num)
        latest = Post.objects.order_by('-created_at')[:3]
        context = {
            'obj_list':post_list_on_current_page ,
            'latest':latest, 
            'page_num':page_num, 
            'category_count':category_count
        }

        return render(request ,  'blog.html' ,  context)



class TagView(View):
    def get(self , request , *args , **kwargs):
        category  = kwargs.get('tag').strip()
        tag = Category.objects.filter(text = tag )
        posts  = Post.objects.filter(categories__in = tag)
        pagdinated_list = Paginator(posts , 5)
        page_num = request.GET.get('page' , 1)
        categories_count = category_count()
        post_list_on_current_page = pagdinated_list.page(page_num)
        latest = Post.objects.order_by('-created_at')[:3]
        context = {
            'obj_list':post_list_on_current_page ,
            'latest':latest, 
            'page_num':page_num, 
            'category_count':category_count
        }

        return render(request ,  'blog.html' ,  context)

