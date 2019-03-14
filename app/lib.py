def create_ad(category,title,description,cost,contact,area):

    """
    >>> create_ad('авто', 'ваз2101', '2011 года выпуска' ,100_000, '+7988123456', 'Новосавиновский')
    {'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000, 'contact': '+7988123456', 'area': 'Новосавиновский'}

    """
    return {
        'category': category,
        'title': title,
        'description': description,
        'cost': cost,
        'contact': contact,
        'area': area
    }

def add_ad(container, ad):

    """
    >>> add_ad([], {'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000, 'contact': '+7988123456', 'area': 'Новосавиновский'})
    """

    container.append(ad)

def search_by_districts(container, area):

    """
    >>> search_by_districts([{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000, 'contact': '+7988123456', 'area': 'Новосавиновский'},{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100_000, 'contact': '+7988123456', 'area': 'Вахитовский'}],'Новосавиновский')
    [{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000, 'contact': '+7988123456', 'area': 'Новосавиновский'}]
    """
    search_lowercased = area.strip().lower()
    result = []
    for ads in container:
        if search_lowercased == ads['area'].lower():
            result.append(ads)
    return result


def search_by_price(container, price):
    result = []

    for ad in container:
        if price <= ad['cost']:
            result.append(ad)

    return result

