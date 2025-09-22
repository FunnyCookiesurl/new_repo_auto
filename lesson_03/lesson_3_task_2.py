from smartphone import Smartphone

catalog = [
    Smartphone("Iphone", "17 Pro", "+79881551622"),
    Smartphone("Samsung", "S365", "+79885551622"),
    Smartphone("Nokia", "3310", "+79881555622"),
    Smartphone("Xiaomi", "Miyi1234", "+79881551522"),
    Smartphone("Huawei", "Z100", "+79881331622")
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.user_number}")
