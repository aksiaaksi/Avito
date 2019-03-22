container = [{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000, 'contact': '+7988123456', 'area': 'Новосавиновский'},{'category': 'авто', 'title': 'ваз2101', 'description': '2011 года выпуска', 'cost': 100000, 'contact': '+7988123456', 'area': 'вахитовский'}]
area = 'Новосавиновский'
search_lowercased = area.strip().lower()
result = []
for ad in container:
        if search_lowercased == ad['area'].lower():
            result.append(ad)
print(result)