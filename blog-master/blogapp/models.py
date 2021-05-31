from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from tinymce import HTMLField



User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    text = models.CharField(max_length=225 , unique=True)
    def __str__(self):
        return self.text

class Post(models.Model):
    title                 = models.CharField(max_length=255 , unique=True)
    text                  = models.TextField()
    created_at            = models.DateField( auto_now_add=True)
    views                 = models.IntegerField( null= True , blank=True , default=0)
    header_img            = models.ImageField()
    featured              = models.BooleanField(default=False)
    slug                  = models.SlugField(null= True , blank=True , unique= True)


    #  Relations 
    author                 = models.ForeignKey(Author , on_delete=models.CASCADE)
    categories             = models.ManyToManyField(Category)
    tags                   = models.ManyToManyField('Tag')
    prev_post              = models.ForeignKey('self', related_name='previous' , null= True , blank= True,   on_delete = models.SET_NULL)
    next_post              = models.ForeignKey('self', related_name='next'  ,  null= True , blank= True ,  on_delete = models.SET_NULL)
    comments               = models.ManyToManyField('Comment', null=True , blank=True  )
    img_for_editor         = models.ImageField( null = True ,   blank= True )
    img_url                = models.CharField( max_length=255 ,  null=True , blank=True , default='none.png')
    content = HTMLField(null= True  , blank=True )

    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        self.slug   =  slugify(self.title)
        try:
            self.img_url  = self.img_for_editor.url
        except:
            pass
        super().save(*args , **kwargs)
    
    def get_absolute_url(slef):
        return  reverse('post-detail' , kwargs={'slug':slef.slug})
    
    def get_comment_count(slef):
        return slef.comments.all().count()


class Comment(models.Model):
    name            =  models.CharField( max_length=255)
    email           = models.EmailField()
    comment_text    = models.TextField()
    # reply_comments  = models.ManyToManyField('self')
    timestamp       = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment_text


class Tag(models.Model):
    text = models.CharField(max_length=225 , unique=True)
    def __str__(self):
        return self.text