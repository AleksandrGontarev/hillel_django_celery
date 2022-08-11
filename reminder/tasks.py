from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

from reminder.models import Author, Quotes

import requests


@shared_task
def send(email, text_reminder):
    send_mail(
        'Reminder',
        text_reminder,
        'gontarevsanya@gmail.com',
        [email, ],
        fail_silently=False,
    )


def find_request(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


@shared_task
def parse_news():
    flag_out = False
    head_url = "https://quotes.toscrape.com/"
    url = "https://quotes.toscrape.com/"
    z = 0
    while find_request(url).find_all("div", {"class": "quote"}):
        quote = find_request(url).find_all("div", {"class": "quote"})
        for i in quote:
            text_quote = i.span.text
            name_author = i.small.text
            link_author = head_url + i.a.get("href")
            r2 = requests.get(link_author)
            s = BeautifulSoup(r2.content, "html.parser")
            description = s.find("div", {"class": "author-description"}).text
            if not Quotes.objects.filter(text=text_quote).exists():
                b = Author.objects.get_or_create(name=name_author,
                                                 defaults={'description': description})
                Quotes.objects.get_or_create(text=text_quote,
                                             authors=b[0])
                z += 1
            if z == 5:
                flag_out = True
                break
        if flag_out:
            break
        if not find_request(url).find('li', {'class': 'next'}):
            email = "sanya@gmail.com"
            text_reminder = "no more quote"
            send(email=email, text_reminder=text_reminder)
            break
        next_page = find_request(url).find('li', {'class': 'next'})
        link_next_page = next_page.a.get("href")
        url = head_url + link_next_page
