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

def search_by_districts(container, area):
    search_lowercased = area.strip().lower()
    result = []
    for ads in container:
        for ad in ads['area']:
            if search_lowercased == ad.lower():
                result.append(ads)
                continue

    return result

def search_by_price(container, price):
    result = []

    for ad in container:
        if price <= ad['cost']:
            result.append(ad)

    return result

