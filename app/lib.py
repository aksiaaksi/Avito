def create_ad(category,title,description,cost,contact,area):
    return {
        'category': category,
        'title': title,
        'description': description,
        'cost': cost,
        'contact': contact,
        'area': area
    }

def add_ad(container, ad):
    container.append(ad)

def search_by_districts(container, area, title):
    search_lowercased = area.strip().lower()
    title_ad = title.strip().lower()

    result = []
    for ad in container:
            for i in ad['area']:
                if search_lowercased == i.lower():
                    result.append(ad)
                    continue

    return result

def price_search(container, price):
    result = []

    for ad in container:
        if price == ad['cost']:
            result.append(ad)

    return result

