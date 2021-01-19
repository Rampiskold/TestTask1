from django import template
from django.core.mail import send_mail
from landing.forms import SendMailToConsoleForm
from landing.models import News, Tags


register = template.Library()


# Функция сброса самой популярной новости
def reset_values_is_main():
    News.objects.all().update(main=False)


# Тег популярных новостей
@register.inclusion_tag('landing/blocks/popular_news.html')
def popular_news():
    popular_news = {}

    reset_values_is_main()

    if News.objects.all().exists():
        news_max_views = News.objects.latest('number_views')
        news_max_views.main = True
        news_max_views.save()

        popular_news = News.objects.order_by('-number_views')[:5]
    return {"popular_news": popular_news}


# Тег самых новых новостей
@register.inclusion_tag('landing/blocks/new_news.html')
def new_news():
    new_news = {}
    if News.objects.all().exists():
        new_news = News.objects.order_by('-created_date')[:3]
    return {"new_news": new_news}


# Тег отправки сообщения в консоль с помощью почты
@register.inclusion_tag('landing/blocks/send_message_to_console.html')
def send_mail(request):
    form = SendMailToConsoleForm()
    if request.method == 'POST':
        form = SendMailToConsoleForm(request.POST)
        if form.is_valid():
            send_mail(
                'Форма обратной связи',
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['to@example.com'],
                fail_silently=False,
            )
    return {"form": form}


# Тег отфильтрованных новостей по tags
@register.inclusion_tag('landing/blocks/news_filtered_by_tag.html')
def news_filtered_by_tag():
    news_filtered_by_tag = {}
    if News.objects.all().exists():
        news_filtered_by_tag = News.objects.filter(tags_id=2).order_by('-created_date')[:5]
    return {"news_filtered_by_tag": news_filtered_by_tag}
