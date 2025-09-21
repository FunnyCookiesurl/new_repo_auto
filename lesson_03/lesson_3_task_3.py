from user_address import Address
from mail import Mailing

to_address = Address("123456", "New York", "5th Avenue", "10", "5A")
from_address = Address(
    "654321", "Los Angeles", "Sunset Boulevard", "20", "10B"
)
mailing = Mailing(to_address, from_address, 15.75, "TRACK123456")

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.home} - "
      f"{mailing.from_address.apartment} в {mailing.to_address.index}, "
      f"{mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.home} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
