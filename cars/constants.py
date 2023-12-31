CAR_CATEGORIES = (
    ('Легковушка', 'Легковушка'),
    ('Минивэн', 'Минивэн'),
    ('Внедорожник', 'Внедорожник'),
    ('Автобус', 'Автобус'),
    ('Кроссовер', 'Кроссовер'),
)

BRAND_CHOICES = (
    ('Мерседес-бенц', 'Мерседес-бенц'),
    ('Лендровер', 'Лендровер'),
    ('БМВ', 'БМВ'),
    ('Вольво', 'Вольво'),
    ('Шевролед', 'Шевролед'),
    ('Фольксваген', 'Фольксваген'),
    ('Хонда', 'Хонда'),
    ('Ауди', 'Ауди'),
    ('Хендай', 'Хендай'),
    ('Форд', 'Форд'),
    ('Киа', 'Киа'),
    ('Лексус', 'Лексус'),
    ('Мицубиси', 'Мицубиси'),
    ('Рено', 'Рено'),
    ('Опель', 'Опель'),
    ('Субару', 'Субару'),
    ('Мазда', 'Мазда'),
    ('Порше', 'Порше'),
    ('Дэу', 'Дэу'),
    ('Лада', 'Лада'),
    ('Сузуки', 'Сузуки'),
    ('Инфинити', 'Инфинити'),
    ('Ссанг Йонг', 'Ссанг Йонг'),
    ('Ниссан', 'Ниссан'),
    ('Тойота', 'Тойота'),
)

TRANSMISSION_TYPES = (
    ('Механическая', 'Механическая'),
    ('Автоматическая', 'Автоматическая'),
    ('Другое', 'Другое'),
)

STEERING_TYPES = (
    ('Левый', 'Левый'),
    ('Правый', 'Правый'),
)

BODY_TYPES = (
    ('Седан', 'Седан'),
    ('Купе', 'Купе'),
    ('Хэтчбек', 'Хэтчбек'),
    ('Лифтбек', 'Лифтбек'),
    ('Фастбэк', 'Фастбэк'),
    ('Универсал', 'Универсал'),
    ('Кроссовер', 'Кроссовер'),
    ('Внедорожник', 'Внедорожник'),
    ('Легковой фургон', 'Легковой фургон'),
    ('Минивэн', 'Минивэн'),
    ('Компактвэн', 'Компактвэн'),
    ('Микровэн', 'Микровэн'),
    ('Кабриолет', 'Кабриолет'),
    ('Родстер', 'Родстер'),
    ('Тарга', 'Тарга'),
    ('Ландо', 'Ландо'),
    ('Лимузин', 'Лимузин'),
)

DRIVE_TYPES = (
    ('Передний', 'Передний'),
    ('Задний', 'Задний'),
    ('Полный', 'Полный'),
)

FUEL_TYPES = (
    ('Бензин', 'Бензин'),
    ('Бензин/Газ', 'Бензин/Газ'),
    ('Газ', 'Газ'),
    ('Дизель', 'Дизель'),
    ('Электрический', 'Электрический'),
    ('Другое', 'Другое'),
)

SEATING_CAPACITY = (
    ('2 пассажира', '2 пассажира'),
    ('5 пассажиров', '5 пассажиров'),
    ('8 пассажиров', '8 пассажиров'),
    ('Другое', 'Другое'),
)

CONDITION_CHOICES = (
    ('Хорошее', 'Хорошее'),
    ('Идеальное', 'Идеальное'),
    ('Новое', 'Новое'),
)

CURRENCY_CHOICES = (
    ('Сом (KGS)', 'Сом (KGS)'),
    ('Доллар (USD)', 'Доллар (USD)'),
    ('Евро (EUR)', 'Евро (EUR)'),
)

SAFETY_EQUIPMENT_CHOICES = (
    ('Наличие огнетушителя', 'Наличие огнетушителя'),
    ('Наличие аптечки', 'Наличие аптечки'),
    ('Наличие запасного колеса', 'Наличие запасного колеса'),
    ('Наличие подушка безопасности', 'Наличие подушка безопасности'),
    ('Наличие инструментов аварийной ситуации', 'Наличие инструментов аварийной ситуации'),
    ('Наличие авторегистратора', 'Наличие авторегистратора'),
)

COLOR_CHOICES = (
    ('Серебристый', 'Серебристый'),
    ('Черный', 'Черный'),
    ('Белый', 'Белый'),
    ('Серый', 'Серый'),
    ('Бежевый', 'Бежевый'),
    ('Бирюзовый', 'Бирюзовый'),
    ('Бордовый', 'Бордовый'),
    ('Бронза', 'Бронза'),
    ('Хамелеон', 'Хамелеон'),
    ('Жёлтый', 'Жёлтый'),
    ('Зеленый', 'Зеленый'),
    ('Золотой', 'Золотой'),
    ('Коричневый', 'Коричневый'),
    ('Фиолетовый', 'Фиолетовый'),
    ('Синий', 'Синий'),
    ('Красный', 'Красный'),
    ('Оранжевый', 'Оранжевый'),
    ('Розовый', 'Розовый'),
    ('Сиреневый', 'Сиреневый'),
    ('Вишня', 'Вишня'),
    ('Баклажан', 'Баклажан'),
    ('Голубой', 'Голубой'),
)

AMENITIES_CHOICES = (
    ('Кондиционер', 'Кондиционер'),
    ('Датчик парковки', 'Датчик парковки'),
    ('Подогрев сидений и руля', 'Подогрев сидений и руля'),
    ('Детское кресло', 'Детское кресло'),
)
