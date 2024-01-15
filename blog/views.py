from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Category, Comment, Like
from django.core.paginator import Paginator
from  .forms import MassageForm
from django.views.generic import ListView, DetailView , FormView
from .models import Massage
from .mixins import LoginRequestMixin
# def b_details (request,slug) :
#     article = get_object_or_404(Article, slug=slug)
#     if request.method == 'POST':
#         text = request.POST.get('text_body')
#         parent_id = request.POST.get('parent')
#         Comment.objects.create(text=text,user=request.user,article=article,parent_id=parent_id)
#     return render(request, 'blog/article_detail.html', {'article': article})
# def list_blog (request) :
#     article = Article.objects.all()
#     page_number = request.GET.get('page')
#     paginator = Paginator(article, 1)
#     object_list = paginator.get_page(page_number)
#     return render(request, 'blog/article_list.html', {'article': object_list })

def list_cstegory(request,pk) :
    category = get_object_or_404(Category, id=pk)
    article = category.articles.all()
    return render(request, "blog/category_article_list.html", {'article':article})

def sidbar (request):
    return render(request, "includes/sidebar.html", {})


# def serch(request):   سرچ تابع
#     s = request.GET.get('serch')
#     result = Article.objects.filter(title__icontains=s)
#     page_number = request.GET.get('page')
#     paginator = Paginator(result, 1)
#     object_list = paginator.get_page(page_number)
#     return  render(request, 'blog/article_list.html', {'article': object_list})

# def contact (request):
#
#
#     if request.method == 'POST':
#         form = MassageForm(data=request.POST)
#         if form.is_valid():
#             text = form.cleaned_data['text']
#             print(text)
#     else:
#         form = MassageForm()
#
#     return render(request,'blog/contact.html',{'form':form})


class blog_list (LoginRequestMixin, ListView):
  model = Article
  paginate_by = 1



class blog_details (DetailView):
    model = Article
    context_object_name = "article"
    def post_redirect_url(self):
        text = self.request.POST.get('text_body')
        parent_id = self.request.POST.get('parent')
        Comment.objects.create(text=text,user=self.request.user,article=self.request,parent_id=parent_id)
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)

            if self.request.user.like.filter(article__slug=self.object.slug , user__id=self.request.user.id).exists():
                context['liked'] = True
            else:
                context ['iked'] = False
            return context


class Contact (FormView):
    template_name = 'blog/contact.html'
    form_class = MassageForm
    success_url = "/"
    def form_valid(self, form):
        form_data = form.cleaned_data
        Massage.objects.create(**form_data)
        return super().form_valid(form)


def like(request, slug , pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug , user__id=request.user.id)
            like.delete()
            return JsonResponse({'response':'onliked'})
        except:
            Like.objects.create(article_id=pk, user_id=request.user.id)
            return JsonResponse({'response': 'liked'})
