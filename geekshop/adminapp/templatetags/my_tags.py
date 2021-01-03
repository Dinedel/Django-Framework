from django import template
from django.conf import settings


register = template.Library()


def media_folder_products(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    products_images/product1.jpg --> /media/products_images/product1.jpg
    """
    if not string:
        string = 'product_images/default.jpg'
    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_folder_users')
def media_folder_users(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users_avatars/user1.jpg --> /media/users_avatars/user1.jpg
    """
    if not string:
        string = 'users_avatars/default.jpg'
    return f'{settings.MEDIA_URL}{string}'


#Первый аргумент — имя, под которым фильтр будет доступен в шаблонах, второй — имя python-функции.
#Или можно было использовать декоратор как у @register.filter(name='media_folder_users'), то же самое.
register.filter('media_folder_products', media_folder_products)
