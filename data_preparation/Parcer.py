import json
import random
import time
import requests
from bs4 import BeautifulSoup as bs


def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                      "/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/"
                      "537.36"
    }
    project_data_list = []

    iteration_count = 59  # количество страниц
    print(f"Всего итераций: #{iteration_count}")

    # сохраняем каждую страницу
    for page in range(1, iteration_count+1):
        real_url = url + "page-" + str(page)
        req = requests.get(real_url, headers)  # get запрос
        with open("pages_site/project" + str(page) + ".html", "w",
                  encoding="utf-8") as file:
            file.write(req.text)
        # открываем полученные страницы
        with open("pages_site/project" + str(page) + ".html",
                  encoding="utf-8") as file:
             src = file.read()

        soup = bs(src, "lxml")
        # получаем список объектов книг класса "product-list__item"
        articles = soup.find_all(class_="product-list__item")

        project_urls = []
        # находим ссылки
        for article in articles:
            project_url = "https://book24.ru" + article.find("div",
                    class_="product-card__image-holder").find("a").get("href")
            project_urls.append(project_url)

        for project_url in project_urls:
            req = requests.get(project_url, headers)
            project_name = project_url.split('/')[-2]

            with open(f"data/{project_name}.html", "w",
                      encoding="utf-8") as file:
                file.write(req.text)

            with open(f"data/{project_name}.html", encoding="utf-8") as file:
                src = file.read()

            soup = bs(src, "lxml")
            project_data = soup.find("div", class_="product-detail-page__body")

            (project_name, project_author, project_section, project_publish,
             project_age, project_years, project_pages, project_rating,
             project_obl, project_descrip) = (
                "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN",
                "NaN", "NaN"
            )
            # картинки обложек книг
            try:
                project_obl = "https:" + project_data.find(
                    "picture", class_="product-poster__main-picture"
                ).find("img").get("src")
            except Exception:
                project_obl = "NaN"
            # название
            try:
                if project_data.find(
                        "div", class_="product-characteristic__label-holder"
                ).find("span").text == " Автор: ":
                    project_name = project_data.find(
                        "div", class_="product-detail-page__title-holder"
                    ).find("h1").text
                    project_name = project_name.split(':')[-1][1:]
            except Exception:
                project_name = "NaN"

            # автор
            try:
                project_author = project_data.find(
                    "div", class_="product-characteristic__value"
                ).find("a").text
            except Exception:
                project_author = "NaN"
            # описание
            project_descrip = ""
            try:
                project_desc = project_data.find(
                    "div", class_="product-about__text"
                ).find_all("p")
                for desc in project_desc:
                    project_descrip += desc.text
            except Exception:
                project_descrip = "NaN"

            # раздел, издательство, возрастное ограничение, год издания,
            # количество страниц
            try:
                project_charac = soup.find(
                    "div", class_="product-detail-page__main-holder"
                )
                harac = project_charac.find_all(
                    class_="product-characteristic__item-holder"
                )
                slov = [" Раздел: ", " Издательство: ",
                        " Возрастное ограничение: ", " Год издания: ",
                        " Количество страниц: "]
                for har in harac:
                    try:
                        if har.find(
                                "span", class_="product-characteristic__label"
                        ).text == slov[0]:
                            project_section = har.find("a", class_=
                            "product-characteristic-link smartLink").text
                    except Exception:
                        project_section = "NaN"
                    try:
                        if har.find(
                                "span", class_="product-characteristic__label"
                        ).text == slov[1]:
                            project_publish = har.find("a", class_=
                            "product-characteristic-link smartLink").text
                    except Exception:
                        project_publish = "NaN"
                    try:
                        if har.find("span", class_=
                        "product-characteristic__label").text == slov[2]:
                            project_age = har.find("div", class_=
                            "product-characteristic__value").text
                    except Exception:
                        project_age = "NaN"
                    try:
                        if har.find("span", class_=
                        "product-characteristic__label").text == slov[3]:
                            project_years = har.find("div", class_=
                            "product-characteristic__value").text
                    except Exception:
                        project_years = "NaN"
                    try:
                        if har.find("span", class_=
                        "product-characteristic__label").text == slov[4]:
                            project_pages = har.find("div", class_=
                            "product-characteristic__value").text
                    except Exception:
                        project_pages = "NaN"
            except Exception:
                project_section = "NaN"
                project_publish = "NaN"
                project_age = "NaN"
                project_years = "NaN"
                project_pages = "NaN"
            # рейтинг
            try:
                project_rating = project_data.find("div", class_=
                "product-detail-page__more-information").find(
                    "span", class_="rating-widget__main-text").text
            except Exception:
                project_rating = "NaN"

            project_data_list.append(
                {
                    "name": project_name,
                    "author": project_author,
                    "section": project_section,
                    "publish": project_publish,
                    "age": project_age,
                    "year": project_years,
                    "pages": project_pages,
                    "rating": project_rating,
                    "cove": project_obl,
                    "description": project_descrip.strip()
                }
            )
        iteration_count -= 1
        print(f"Итерация #{page} завершена, осталось #{iteration_count}")
        if iteration_count == 0:
            print(f"Сбор данных завершен")
        time.sleep(random.randrange(2, 4))

    with open("project_book.json", "a", encoding="utf-8") as file:
        json.dump(project_data_list, file, indent=4, ensure_ascii=False)


get_data('https://book24.ru/catalog/samorazvitie-1756/')
