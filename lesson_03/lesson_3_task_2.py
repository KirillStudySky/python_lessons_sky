from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Mi 8", "+79801324789"),
    Smartphone("Apple", "iPhone 17", "+79110000001"),
    Smartphone("Samsung", "A 24", "+79333987657"),
    Smartphone("Honor", "View 20", "+79120847585"),
    Smartphone("Nokia", "Xpressmusic", "+79222555777"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}.{phone.phone_number}")
