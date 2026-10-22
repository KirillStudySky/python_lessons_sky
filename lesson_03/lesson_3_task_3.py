from address import Address
from mailing import Mailing

from_addr = Address("454000", "Челябинск", "Александра Шмакова", "17А", "23")
to_addr = Address("457300", "Карталы", "Калмыкова", "4а", "7")

mail = Mailing(to_address=to_addr, from_address=from_addr,
               cost=300, track="RC123456789RU")

track_info = f"Отправление {mail.track} из "
from_info = f"{from_addr.formatted()}"
to_info = f" в {mail.to_address.formatted()}"
cost_info = f". Стоимость {mail.cost} рублей. "
print(track_info + from_info + to_info + cost_info)
