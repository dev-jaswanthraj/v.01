from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User
class Post(models.Model):
    cust = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 20000)
    image = models.FileField(null = True, blank = True)
    update = models.DateTimeField(auto_now=True,auto_now_add=False )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique = True, null = True, blank = True) 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})

    class Meta:
        ordering = ['-timestamp', '-update']

def create_sluge(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug = slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug,qs.first().id)
        return create_sluge(instance, new_slug = new_slug)
    return slug

def pre_save_recever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_sluge(instance)

pre_save.connect(pre_save_recever, sender=Post)