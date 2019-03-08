def create_ad(category,title,description,cost,contact):
    return {
        'category': category,
        'title': title,
        'description': description,
        'cost': cost,
        'contact': contact
    }

def add_ad(container, ad):
    container.apend(ad)