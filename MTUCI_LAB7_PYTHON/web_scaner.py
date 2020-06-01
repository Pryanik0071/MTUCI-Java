import requests
from bs4 import BeautifulSoup


def get_all_urls(urls_list, all_urls, input_nubmer_deep):

    for url in urls_list:

        page_response = requests.get(url)  # GET запрос по нашему URL
        page_content = BeautifulSoup(page_response.content, "html.parser")  # Парсим HTML для работы с библиотекой BS
        all_tags_a = page_content.find_all('a')  # Ищем все тэги со значением <a>

        """ 1. Итерируемся по каждому тэгу в списке all_tags_a; 
            2. Вытягиваем значения атрибутов href из каждого тэга;
            3. Проверяем, чтобы не было None (пропускаем такие ссылки);
            4. Проверяем, чтобы в ссылке присутствовало либо http, либо https. Иначе имеем право скипнуть;
            5. Исключаем ранее известные ссылки. """

        urls = set()  # Создаём пустое множество (сюда складываем первые ссылки на стартовой странице)

        for tag_a in all_tags_a:  # 1
            result = tag_a.get('href')  # 2
            if result is not None and ('http://' in result or 'https://' in result) and tag_a not in all_urls:  # 3 4 5
                urls.add(result)

        list_2 = list(urls)  # Из множества делаем список, чтобы удобнее было итерироваться
        all_urls.extend(list_2)

        for out_url in list_2:
            print(out_url, input_nubmer_deep)

        urls_list = list_2.copy()
        list_2.clear()

    return urls_list


page_link = input("Введите стартовый url: ")  # Стартовая ссылка
deep = int(input("Введите глубину поиска: "))  # Глубина поиска
input_list = [page_link]  # Создаем список, в котором будут адреса, с которых надо вытащить urls
all_urls_list = []  # Общий список, в котором будут все уникальные urls, чтобы исключить повторения

for deep_number in range(1, deep + 1):
    input_list = get_all_urls(input_list, all_urls_list, deep_number)
