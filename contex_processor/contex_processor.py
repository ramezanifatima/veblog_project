from blog.models import Article,Category

def recent_article (request):
    recent_a = Article.objects.all().order_by("-created")
    category = Category.objects.all()
    return {"recent_article": recent_a, 'category': category }