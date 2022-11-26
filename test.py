# dictionary = {
#     "персона": "человек",
#     "марафон": "гонка бегунов длиной около 26 миль",
#     "противостоять": "оставаться сильным, несмотря на давление",
#     "бежать": "двигаться со скоростью",
# }
# strings = []
# for key, item in dictionary.items():
#     strings.append("{}: {}".format(key.capitalize(), item))
# result = "; ".join(strings)
# print(result)

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    list = []
    for key in articles_dict:
        list.append(key)
    return list
