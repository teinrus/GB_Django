from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Привет, я Евгений, разработчик АСУТП и начинающий Python-разработчик.</p>
    """

    logger.info("Пользователь посетил страницу 'главная'")
    
    return HttpResponse(html)

def about(request):

    html = """
    <h1>Обо мне</h1>
    <p>Меня зовут Евгений, я разработчик АСУТП и начинающий Python-разработчик.</p>
    """
    

    logger.info("Пользователь посетил страницу 'о себе'")
    
    return HttpResponse(html)
