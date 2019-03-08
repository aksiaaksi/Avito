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
    container.apend(ad)