from django.shortcuts import render, redirect
from news.forms import ContactForm
from news.models import Contact
from django.views import View
from .models import News, Category
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


# Create your views here.
def page_404(request):
    return render(request, "news/404.html")


class DetailView(View):
    def get(self, request, news):
        slug = news
        news = News.published.get(slug=slug)
        categories = Category.objects.all()
        return render(
            request, "news/single_page.html", {"news": news, "categories": categories}
        )


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "news/contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("home")
        context = {"form": form}
        return render(request, "news/contact.html", context)


def Messages(request):
    messages = Contact.objects.all().order_by("-created_at")
    context = {"messages": messages}
    return render(request, "news/messages.html", context)


class NewsUpdateView(UpdateView):
    model = News
    template_name = "news/crud/update.html"
    fields = ("title", "body", "category", "image", "status")


def localNews(request):
    news = (
        News.published.all()
        .filter(category__name="Mahalliy")
        .order_by("-published_time")
    )
    return render(request, "news/category.html", {"news": news})


def abroadNews(request):
    news = (
        News.published.all().filter(category__name="Xorij").order_by("-published_time")
    )
    return render(request, "news/category.html", {"news": news})


def techNews(request):
    news = (
        News.published.all()
        .filter(category__name="Texnalogiya")
        .order_by("-published_time")
    )
    return render(request, "news/category.html", {"news": news})


def sportNews(request):
    news = (
        News.published.all().filter(category__name="Sport").order_by("-published_time")
    )
    return render(request, "news/category.html", {"news": news})
