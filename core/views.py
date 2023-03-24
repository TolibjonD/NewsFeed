from django.shortcuts import render
from django.utils import timezone
from news.models import News, Category


def home_page(request):
    latest_news = News.published.all().order_by("-published_time")[:5]
    categories = Category.objects.all().order_by("name")
    local_news_main = (
        News.published.all()
        .filter(category__name="Mahalliy")
        .order_by("-published_time")[:1]
    )
    local_news = (
        News.published.all()
        .filter(category__name="Mahalliy")
        .order_by("-published_time")[1:6]
    )
    abroad_news = (
        News.published.all()
        .filter(category__name="Xorij")
        .order_by("-published_time")[1:4]
    )
    main_abroad_news = (
        News.published.all()
        .filter(category__name="Xorij")
        .order_by("-published_time")[:1]
    )
    tech_news = (
        News.published.all()
        .filter(category__name="Texnalogiya")
        .order_by("-published_time")[1:4]
    )
    main_tech_news = (
        News.published.all()
        .filter(category__name="Texnalogiya")
        .order_by("-published_time")[:1]
    )
    sport_news = (
        News.published.all()
        .filter(category__name="Sport")
        .order_by("-published_time")[1:4]
    )
    main_sport_news = (
        News.published.all()
        .filter(category__name="Sport")
        .order_by("-published_time")[:1]
    )
    photots = News.published.all().order_by("-published_time")[:7]
    current_date = timezone.now()
    context = {
        "latest_news": latest_news,
        "categories": categories,
        "local_news_main": local_news_main,
        "local_news": local_news,
        "time": current_date,
        "main_abroad": main_abroad_news,
        "abroad": abroad_news,
        "tech_news": tech_news,
        "main_tech": main_tech_news,
        "photos": photots,
        "sport": sport_news,
        "main_sport": main_sport_news,
    }
    return render(request, "index.html", context)
