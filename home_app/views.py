from django.shortcuts import render
from blog.models import Article,Category
def home(request):
    article = Article.objects.all()
    category = Category.objects.all()
    recent_article = Article.objects.all().order_by('-created', '-update')
    return render(request, "home_app/index.html", {"item": article, 'recent_article': recent_article,'cat':category})