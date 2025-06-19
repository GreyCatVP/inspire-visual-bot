
def get_visual_inspiration(query=None):
    if query and 'coffee' not in query.lower():
        return ["Пока доступна только подборка по 'coffee packaging'."]

    return [
        {
            "title": "Minimalist Coffee Packaging Design",
            "image": "https://tse3.mm.bing.net/th?id=OIP.oo4ennCDOpRPZtqvXrOesQHaE8&pid=Api",
            "insight": "Белый и чёрный пакеты, чистый логотип, максимум воздуха",
            "link": "https://www.behance.net/gallery/177496879/minimalist-coffee-packaging-design"
        },
        {
            "title": "Coffee Packaging design",
            "image": "https://tse3.mm.bing.net/th?id=OIP.OK3WFaCp_SMGsFFJaAZ0qgHaFn&pid=Api",
            "insight": "Иллюстрации, мягкая палитра, природная тема",
            "link": "https://www.behance.net/gallery/151704491/Coffee-Packaging-design"
        },
        {
            "title": "MOOD coffee packaging",
            "image": "https://tse3.mm.bing.net/th?id=OIP.KYQUBH23ciS3k53bJT6nvgHaEo&pid=Api",
            "insight": "Чёрно-белый цилиндр, премиум-шрифт, строгий стиль",
            "link": "https://www.behance.net/gallery/62444969/MOOD-coffee-packaging"
        }
    ]
