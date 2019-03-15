from app.lib import  create_ad,add_ad, search_by_districts, search_by_price

def test_create_ad():

    data =  {'category': 'авто',
             'title': 'ваз2101',
             'description': '2011 года выпуска',
             'cost': 100000,
             'contact': '+7988123456',
             'area': 'Новосавиновский'
             }

    result = create_ad(data['category'], data['title'], data['description'], data['cost'], data['contact'], data['area'])


    assert data == result

def test_add_ad():

    container = []
    ad = create_ad('авто', 'ваз2101', '2011 года выпуска', 100000,'+7988123456','Новосавиновский')

    add_ad(container, ad)

    assert ad in container



def test_search_by_price():

    test_search = [{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000, 'contact': '+7988123456', 'area': 'Новосавиновский'}]

    container = [{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000, 'contact': '+7988123456', 'area': 'Новосавиновский'},{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 40_000, 'contact': '+7988123456', 'area': 'Вахитовский'}]
    result = []
    price = 90_000

    search_result = search_by_price(container,price)

    assert test_search == search_result



def test_search_by_districts():

    test_search = [{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000,'contact': '+7988123456', 'area': 'Новосавиновский'}]

    container = [{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000,'contact': '+7988123456', 'area': 'Новосавиновский'}, {'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 40_000, 'contact': '+7988123456', 'area': 'Вахитовский'}]

    areas = { 'Приволжский', 'Новосавиновский'}

    search_result = search_by_districts(container,areas)

    assert test_search == search_result

