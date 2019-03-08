from lib import create_ad, add_ad


ads = []

hello1 = create_ad (
    'авто',
    'ваз2101',
    '2011 года выпуска',
    100_000,
    '+7988123456',
    'Новосавиновский'
)
hello2 =  create_ad (
    'авто',
    'rr',
    '2018 года выпуска',
    20_000_000,
    '+7988123000',
    'Московский'
)

add_ad(ads, hello1)
add_ad(ads, hello2)

#print(ads)


cost = 100_000
#search_lowercased = area.strip().lower()
result = []

for ad in ads:
    if cost == ad['cost']:
       result.append(ad)

print(result)
