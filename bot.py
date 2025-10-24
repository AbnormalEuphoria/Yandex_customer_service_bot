import telebot
from telebot import types
import re
import time

bot = telebot.TeleBot('8404836007:AAEaeTzjz8MLr9GIiVqtkDRzRh8_s_y5h64') # Enter key here

USER_FILE = 'users.txt'

ADMIN_ID = 389486963

@bot.message_handler(commands=['send_to_users'])
def send_to_users(message):
    if message.from_user.id == ADMIN_ID:
        with open("users.txt") as f:
            users = f.read().splitlines()

        for user_id in users:
            bot.send_photo(user_id, open('images/investments/1.jpg', 'rb'),"Привет! Рекомендую ознакомиться с новой статьей по инвестированию: https://www.sberbank.ru/ru/person/investments/how_to_start_invest")

def save_user(user_id):
    # Читаем уже сохранённые ID, чтобы не дублировать
    with open(USER_FILE, "a+") as f:
        f.seek(0)
        users = f.read().splitlines()
        if str(user_id) not in users:
            f.write(f"{user_id}\n")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    save_user(user_id)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    welcome_btn = types.InlineKeyboardButton(text="Начать обучение", callback_data="start_learning")
    keyboard.add(welcome_btn)
    bot.send_photo(message.from_user.id, open('images/start/начало.jpg', 'rb') ,
                     "Доброго времени суток! Для того, чтобы начать обучение, пожалуйста, нажмите на кнопку \"Начать обучение\"", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "start_learning":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget = types.InlineKeyboardButton(text="Бюджетирование", callback_data="budget")
        savings = types.InlineKeyboardButton(text="Сбережения", callback_data="savings")
        investments = types.InlineKeyboardButton(text="Инвестиции", callback_data="investments")
        loans = types.InlineKeyboardButton(text="Кредиты", callback_data="loans")
        keyboard.add(budget, savings, investments, loans)
        bot.send_photo(call.message.chat.id,open('images/start/выбери блок.jpg', 'rb') , "Выберите одну из четырех тем, по которым вы бы хотели начать обучение:", reply_markup=keyboard)

# Бюджет

    elif call.data == "budget":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="budget_button_1")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/budget/1.jpg', 'rb') ,"""Что такое личный бюджет и зачем он нужен \n\nЛичный бюджет — это система планирования доходов и расходов. Основная цель — понимать, куда уходят деньги, и принимать обоснованные финансовые решения.
        \nБез бюджета сложно контролировать траты, накапливать сбережения или достигать финансовых целей.
        \nБюджетирование помогает избавиться от импульсивных покупок, формирует дисциплину и осознанное отношение к деньгам.
        """, reply_markup=keyboard)

    elif call.data == "budget_button_1":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="budget_button_2")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/budget/2.jpg', 'rb') , """Структура бюджета: доходы и расходы\n
Доходы — это все поступления денежных средств (зарплата, подработка, пособия, доход от аренды и т.п.).
\nРасходы делятся на:
- Обязательные(жильё, еда, транспорт, кредиты)
- Переменные(развлечения, покупки, подарки)
- Финансовые цели (накопления, инвестиции)
\nБюджет будет эффективным, если в нём предусмотрены все категории, включая непредвиденные расходы.""", reply_markup=keyboard)

    elif call.data == "budget_button_2":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="budget_button_3")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id,open('images/budget/3.jpg', 'rb'),"""Методы ведения бюджета
\nСамый простой способ — фиксировать все траты вручную в тетради или таблице Excel.
Современные альтернативы — мобильные приложения с аналитикой (CoinKeeper, ZenMoney и т.д.).
\nГлавное — регулярность. Даже самый простой метод будет работать, если его использовать систематически.

        """, reply_markup=keyboard)

    elif call.data == "budget_button_3":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="budget_button_4")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/budget/4.jpg', 'rb'),"""Правило 50/30/20
\nЭто популярная схема распределения доходов:
50% на обязательные расходы
30% на личные желания и образ жизни
20% на накопления и цели
\nМодель универсальна и подходит для большинства людей. При нестабильных доходах пропорции можно адаптировать, но главное — сохранять структуру.""", reply_markup=keyboard)

    elif call.data == "budget_button_4":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="budget_button_5")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Ошибки при ведении бюджета\n
-- Игнорирование мелких трат
-- Недооценка непредвиденных расходов
-- Отсутствие анализа итогов месяца
-- Жесткое ограничение, вызывающее стресс""", reply_markup=keyboard)

    elif call.data == "budget_button_5":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="budget_button_6")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Как оценить эффективность бюджета\n
В конце месяца нужно анализировать:
-- Насколько точно удалось спрогнозировать расходы
-- Получилось ли отложить запланированную сумму
-- Какие категории «проваливаются»
\nХороший бюджет — это тот, который помогает достигать целей и при этом не ухудшает качество жизни.""", reply_markup=keyboard)

    elif call.data == "budget_button_6":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Пройти тест", callback_data="budget_test")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Финал\n
Вы завершили изучение темы «Бюджетирование».
Если применять даже базовые принципы на практике, вы заметите улучшения в финансовом поведении уже через 1–2 месяца. Теперь давайте проверим, насколько хорошо вы усвоили материал. \nОтветьте на несколько вопросов.
""", reply_markup=keyboard)

    elif call.data == "budget_test":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_test_1_incorrect_1 = types.InlineKeyboardButton(text="Облигации", callback_data="budget_test_1_incorrect")
        budget_test_1_correct = types.InlineKeyboardButton(text="Кредитная карта", callback_data="budget_test_1_correct")
        budget_test_1_incorrect_2 = types.InlineKeyboardButton(text="ETF-фонды", callback_data="budget_test_1_incorrect")
        keyboard.add(budget_test_1_incorrect_1, budget_test_1_correct, budget_test_1_incorrect_2)
        bot.send_message(call.message.chat.id, "Что из перечисленного НЕ является инвестиционным инструментом?", reply_markup=keyboard)

    elif call.data == "budget_test_1_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_test_1_incorrect_1 = types.InlineKeyboardButton(text="Облигации",
                                                               callback_data="budget_test_1_incorrect")
        budget_test_1_correct = types.InlineKeyboardButton(text="Кредитная карта",
                                                           callback_data="budget_test_1_correct")
        budget_test_1_incorrect_2 = types.InlineKeyboardButton(text="ETF-фонды",
                                                               callback_data="budget_test_1_incorrect")
        keyboard.add(budget_test_1_incorrect_1, budget_test_1_correct, budget_test_1_incorrect_2)
        bot.send_message(call.message.chat.id, "Неправильно, попробуйте еще раз. \nЧто из перечисленного НЕ является инвестиционным инструментом?",
                         reply_markup=keyboard)

    elif call.data == "budget_test_1_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_2_incorrect_1 = types.InlineKeyboardButton(text="Использование только одного",
                                                               callback_data="budget_test_2_incorrect")
        budget_test_2_correct = types.InlineKeyboardButton(text="Вложение средств в разные активы для снижения риска",
                                                           callback_data="budget_test_2_correct")
        budget_test_2_incorrect_2 = types.InlineKeyboardButton(text="Покупка валюты и хранение её дома",
                                                               callback_data="budget_test_2_incorrect")
        keyboard.add(budget_test_2_correct, budget_test_2_incorrect_1, budget_test_2_incorrect_2)


        bot.send_message(call.message.chat.id, "Правильно! \nСледующий вопрос: Что означает диверсификация в инвестициях?", reply_markup=keyboard)

    elif call.data == "budget_test_2_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_2_incorrect_1 = types.InlineKeyboardButton(text="Использование только одного",
                                                               callback_data="budget_test_2_incorrect")
        budget_test_2_correct = types.InlineKeyboardButton(text="Вложение средств в разные активы для снижения риска",
                                                           callback_data="budget_test_2_correct")
        budget_test_2_incorrect_2 = types.InlineKeyboardButton(text="Покупка валюты и хранение её дома",
                                                               callback_data="budget_test_2_incorrect")
        keyboard.add(budget_test_2_correct, budget_test_2_incorrect_1, budget_test_2_incorrect_2)


        bot.send_message(call.message.chat.id, "Неправильно, попробуйте еще раз. \nЧто означает диверсификация в инвестициях?", reply_markup=keyboard)

    elif call.data == "budget_test_2_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_test_3_incorrect_1 = types.InlineKeyboardButton(text="Рыночный риск",
                                                               callback_data="budget_test_3_incorrect")
        budget_test_3_correct = types.InlineKeyboardButton(text="Инфляционное ожидание",
                                                           callback_data="budget_test_3_correct")
        budget_test_3_incorrect_2 = types.InlineKeyboardButton(text="Ликвидный риск",
                                                               callback_data="budget_test_3_incorrect")
        keyboard.add(budget_test_3_incorrect_1, budget_test_3_incorrect_2, budget_test_3_correct)


        bot.send_message(call.message.chat.id, "Правильно! \nСледующий вопрос: Какая из характеристик НЕ относится к рискам инвестирования?", reply_markup=keyboard)

    elif call.data == "budget_test_3_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_test_3_incorrect_1 = types.InlineKeyboardButton(text="Рыночный риск",
                                                               callback_data="budget_test_3_incorrect")
        budget_test_3_correct = types.InlineKeyboardButton(text="Инфляционное ожидание",
                                                           callback_data="budget_test_3_correct")
        budget_test_3_incorrect_2 = types.InlineKeyboardButton(text="Ликвидный риск",
                                                               callback_data="budget_test_3_incorrect")
        keyboard.add(budget_test_3_incorrect_1, budget_test_3_incorrect_2, budget_test_3_correct)


        bot.send_message(call.message.chat.id, "Неправильно, попробуйте еще раз. \nКакая из характеристик НЕ относится к рискам инвестирования?", reply_markup=keyboard)

    elif call.data == "budget_test_3_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_back_to_menu = types.InlineKeyboardButton(text="Вернуться в меню",
                                                           callback_data="start_learning")
        keyboard.add(budget_back_to_menu)

        bot.send_message(call.message.chat.id,
                         "Правильно! Поздравляю! Вы прошли тест.", reply_markup=keyboard)


# Сбережения (savings)


    elif call.data == "savings":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="savings_button_1")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/savings/1.jpg', 'rb'),"""Зачем нужны сбережения
\nСбережения — это финансовый резерв, который обеспечивает стабильность и защиту от неожиданностей.
Они позволяют:
- не влезать в долги при срочных расходах
- уверенно переживать потерю дохода
- реализовывать крупные цели (обучение, отдых, покупка техники)
\nСбережения — это основа финансовой безопасности.
""", reply_markup=keyboard)

    elif call.data == "savings_button_1":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="savings_button_2")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/savings/2.jpg', 'rb'), """Финансовая подушка безопасности
\nЭто сумма, которой достаточно для жизни в течение 3–6 месяцев без дохода.
Подсчёт: возьмите средние месячные расходы и умножьте на 3–6.
Пример: если вы тратите 50 000 рублей в месяц, подушка должна составлять от 150 000 до 300 000.
Деньги хранятся на надёжном, быстро доступном, но не рискованном счёте.
""", reply_markup=keyboard)

    elif call.data == "savings_button_2":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="savings_button_3")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/savings/3.jpg', 'rb'), """Как откладывать деньги регулярно\n
- Откладывайте сразу после получения дохода, а не «что останется»
- Начинайте с небольшой суммы (5–10%), затем увеличивайте
- Автоматизируйте накопления: настройте автопереводы
- Храните деньги отдельно от текущих средств — так меньше соблазнов потратить
""", reply_markup=keyboard)

    elif call.data == "savings_button_3":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="savings_button_4")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/savings/4.jpg', 'rb'), """Психология накоплений
\nВажно понимать свои финансовые привычки. Часто сбережения не формируются не из-за нехватки денег, а из-за отсутствия цели или дисциплины.
Полезно визуализировать цель, разбивать её на подцели и отслеживать прогресс.
\nСоздайте систему мотивации: поощряйте себя за достижение накоплений.
""", reply_markup=keyboard)

    elif call.data == "savings_button_4":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="savings_button_5")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Инструменты хранения сбережений\n
- Накопительные счета с процентом
- Краткосрочные депозиты
- Цифровые копилки в мобильных банках
\nСбережения не стоит инвестировать в рисковые инструменты — их задача не приносить доход, а сохранять средства.
""", reply_markup=keyboard)

    elif call.data == "savings_button_5":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="savings_button_6")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Распространённые ошибки\n
- Отсутствие цели накоплений
- Доступ к деньгам «в два клика»
- Хранение сбережений дома
- Использование подушки на ненужные покупки
\nСбережения — это долгосрочный актив. Обращайтесь с ним внимательно.
""", reply_markup=keyboard)

    elif call.data == "savings_button_6":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Пройти тест", callback_data="savings_test")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Финал\n
Вы завершили тему «Сбережения».
Наличие даже небольшой, но стабильной финансовой подушки — один из главных признаков финансовой устойчивости.
\nТеперь давайте проверим, насколько хорошо вы усвоили материал. Ответьте на несколько вопросов.
""", reply_markup=keyboard)

    elif call.data == "savings_test":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_1_incorrect_1 = types.InlineKeyboardButton(text="Деньги, предназначенные для крупных покупок или развлечений", callback_data="savings_test_1_incorrect")
        budget_test_1_correct = types.InlineKeyboardButton(text="Сумма, покрывающая расходы на 3–6 месяцев жизни без дохода", callback_data="savings_test_1_correct")
        budget_test_1_incorrect_2 = types.InlineKeyboardButton(text="Доход от инвестиций, получаемый ежемесячно", callback_data="savings_test_1_incorrect")
        keyboard.add(budget_test_1_incorrect_1, budget_test_1_correct, budget_test_1_incorrect_2)
        bot.send_message(call.message.chat.id, "Что такое финансовая подушка безопасности?", reply_markup=keyboard)

    elif call.data == "savings_test_1_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_1_incorrect_1 = types.InlineKeyboardButton(
            text="Деньги, предназначенные для крупных покупок или развлечений",
            callback_data="savings_test_1_incorrect")
        budget_test_1_correct = types.InlineKeyboardButton(
            text="Сумма, покрывающая расходы на 3–6 месяцев жизни без дохода", callback_data="savings_test_1_correct")
        budget_test_1_incorrect_2 = types.InlineKeyboardButton(text="Доход от инвестиций, получаемый ежемесячно",
                                                               callback_data="savings_test_1_incorrect")
        keyboard.add(budget_test_1_incorrect_1, budget_test_1_correct, budget_test_1_incorrect_2)
        bot.send_message(call.message.chat.id, "Неправильно, попробуйте еще раз. \nЧто такое финансовая подушка безопасности?",
                         reply_markup=keyboard)

    elif call.data == "savings_test_1_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_2_incorrect_1 = types.InlineKeyboardButton(text="Брать кредит и класть эти средства на депозит",
                                                               callback_data="savings_test_2_incorrect")
        budget_test_2_correct = types.InlineKeyboardButton(text="Откладывать  сразу после получения дохода, даже небольшую сумму",
                                                           callback_data="savings_test_2_correct")
        budget_test_2_incorrect_2 = types.InlineKeyboardButton(text="Откладывать оставшиеся деньги в конце месяца",
                                                               callback_data="savings_test_2_incorrect")
        keyboard.add(budget_test_2_correct, budget_test_2_incorrect_1, budget_test_2_incorrect_2)


        bot.send_message(call.message.chat.id, "Правильно! \nСледующий вопрос: Как лучше всего формировать сбережения?", reply_markup=keyboard)

    elif call.data == "savings_test_2_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_2_incorrect_1 = types.InlineKeyboardButton(text="Брать кредит и класть эти средства на депозит",
                                                               callback_data="savings_test_2_incorrect")
        budget_test_2_correct = types.InlineKeyboardButton(
            text="Откладывать  сразу после получения дохода, даже небольшую сумму",
            callback_data="savings_test_2_correct")
        budget_test_2_incorrect_2 = types.InlineKeyboardButton(text="Откладывать оставшиеся деньги в конце месяца",
                                                               callback_data="savings_test_2_incorrect")
        keyboard.add(budget_test_2_correct, budget_test_2_incorrect_1, budget_test_2_incorrect_2)


        bot.send_message(call.message.chat.id, "Неправильно, попробуйте еще раз. \nКак лучше всего формировать сбережения?", reply_markup=keyboard)

    elif call.data == "savings_test_2_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_3_incorrect_1 = types.InlineKeyboardButton(text="Хранить подушку безопасности на отдельном накопительном счёте",
                                                               callback_data="savings_test_3_incorrect")
        budget_test_3_correct = types.InlineKeyboardButton(text="Держать все сбережения дома наличными",
                                                           callback_data="savings_test_3_correct")
        budget_test_3_incorrect_2 = types.InlineKeyboardButton(text="Автоматически переводить часть зарплаты на депозит",
                                                               callback_data="savings_test_3_incorrect")
        keyboard.add(budget_test_3_incorrect_1, budget_test_3_incorrect_2, budget_test_3_correct)


        bot.send_message(call.message.chat.id, "Правильно! Следующий вопрос: Какая из практик хранения сбережений является ошибочной?", reply_markup=keyboard)

    elif call.data == "savings_test_3_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_3_incorrect_1 = types.InlineKeyboardButton(
            text="Хранить подушку безопасности на отдельном накопительном счёте",
            callback_data="savings_test_3_incorrect")
        budget_test_3_correct = types.InlineKeyboardButton(text="Держать все сбережения дома наличными",
                                                           callback_data="savings_test_3_correct")
        budget_test_3_incorrect_2 = types.InlineKeyboardButton(
            text="Автоматически переводить часть зарплаты на депозит",
            callback_data="savings_test_3_incorrect")
        keyboard.add(budget_test_3_incorrect_1, budget_test_3_incorrect_2, budget_test_3_correct)


        bot.send_message(call.message.chat.id, "Неправильно, попробуйте еще раз. \nКакая из практик хранения сбережений является ошибочной?", reply_markup=keyboard)

    elif call.data == "savings_test_3_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_back_to_menu = types.InlineKeyboardButton(text="Вернуться в меню",
                                                           callback_data="start_learning")
        keyboard.add(budget_back_to_menu)

        bot.send_message(call.message.chat.id,
                         "Правильно! Поздравляю! Вы прошли тест.", reply_markup=keyboard)


# Инвестиции (investments)

    elif call.data == "investments":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="investments_button_1")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/investments/1.jpg', 'rb'), """Что такое инвестиции и зачем они нужны
\nИнвестиции — это вложения капитала с целью его увеличения.
Они помогают:
- Защитить деньги от инфляции
- Создать пассивный доход
- Достичь крупных целей (квартира, пенсия, бизнес)
\nВ отличие от сбережений, инвестиции предполагают риск. Это осознанный и стратегический процесс.
""", reply_markup=keyboard)

    elif call.data == "investments_button_1":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="investments_button_2")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/investments/2.jpg', 'rb'), """Инвестиционные инструменты
\nСуществуют разные классы активов:
- Акции - доли в компаниях
- Облигации - долговые бумаги с фиксированным доходом
- ETF и ПИФы - фонды, объединяющие разные активы
- Недвижимость
- Драгметаллы
\nУ каждого инструмента — свой уровень риска, ликвидности и доходности.
""", reply_markup=keyboard)

    elif call.data == "investments_button_2":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="investments_button_3")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/investments/3.jpg', 'rb'), """Принципы грамотного инвестирования
\n- Вкладывай только свободные средства
- Диверсифицируй вложения (разные классы активов)
- Не поддавайся эмоциям
- Определи горизонт: на какой срок инвестируешь
\nИнвестиции — это не азарт, а расчёт.
""", reply_markup=keyboard)

    elif call.data == "investments_button_3":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="investments_button_4")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/investments/4.jpg', 'rb'), """Риски и как ими управлять
\nЛюбые инвестиции могут не оправдать ожиданий. Основные виды рисков:
- Рыночный (падение стоимости активов)
- Ликвидный (трудности с продажей)
- Эмитентский (банкротство компании)
\nРиски уменьшаются с помощью анализа, диверсификации и выбора надёжных инструментов.
""", reply_markup=keyboard)

    elif call.data == "investments_button_4":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="investments_button_5")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Как начать инвестировать
\n- Изучите основы: читайте литературу, смотрите лекции
- Откройте брокерский счёт
- Начните с малого: даже 1 000–2 000 рублей
- Выберите простые инструменты: фонды, облигации
\nРегулярность важнее суммы. Главное — войти в привычку.
""", reply_markup=keyboard)

    elif call.data == "investments_button_5":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="investments_button_6")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Ошибки начинающих
\n- Инвестирование без понимания
- Ставка на «горячие» советы
- Попытка быстро разбогатеть
- Игнорирование комиссий
\nИнвестиции требуют спокойствия, терпения и системного подхода.
""", reply_markup=keyboard)

    elif call.data == "investments_button_6":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Пройти тест", callback_data="investments_test")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Финал
\nВы завершили изучение темы «Инвестиции».
Сделав первые шаги осознанно, вы можете создать источник капитала на долгосрочную перспективу. Теперь давайте проверим, насколько хорошо вы усвоили материал. Ответьте на несколько вопросов.
""", reply_markup=keyboard)

    elif call.data == "investments_test":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_1_incorrect_1 = types.InlineKeyboardButton(
            text="Быстрое получение прибыли любой ценой",
            callback_data="investments_test_1_incorrect")
        budget_test_1_correct = types.InlineKeyboardButton(
            text="Сохранение капитала от инфляции, создание дохода и достижение долгосрочных целей", callback_data="investments_test_1_correct")
        budget_test_1_incorrect_2 = types.InlineKeyboardButton(text="Использование всех сбережений для игры на бирже",
                                                               callback_data="investments_test_1_incorrect")
        keyboard.add(budget_test_1_incorrect_1, budget_test_1_correct, budget_test_1_incorrect_2)
        bot.send_message(call.message.chat.id, "Какая основная цель инвестирования?", reply_markup=keyboard)

    elif call.data == "investments_test_1_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_1_incorrect_1 = types.InlineKeyboardButton(
            text="Быстрое получение прибыли любой ценой",
            callback_data="investments_test_1_incorrect")
        budget_test_1_correct = types.InlineKeyboardButton(
            text="Сохранение капитала от инфляции, создание дохода и достижение долгосрочных целей",
            callback_data="investments_test_1_correct")
        budget_test_1_incorrect_2 = types.InlineKeyboardButton(text="Использование всех сбережений для игры на бирже",
                                                               callback_data="investments_test_1_incorrect")
        keyboard.add(budget_test_1_incorrect_1, budget_test_1_correct, budget_test_1_incorrect_2)
        bot.send_message(call.message.chat.id,
                         "Неправильно, попробуйте еще раз. \nКакая основная цель инвестирования?",
                         reply_markup=keyboard)

    elif call.data == "investments_test_1_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_2_incorrect_1 = types.InlineKeyboardButton(text="Использование только надёжных банковских вкладов",
                                                               callback_data="investments_test_2_incorrect")
        budget_test_2_correct = types.InlineKeyboardButton(
            text="Вложение средств в разные классы активов для снижения рисков",
            callback_data="investments_test_2_correct")
        budget_test_2_incorrect_2 = types.InlineKeyboardButton(text="Использование только надёжных банковских вкладов",
                                                               callback_data="investments_test_2_incorrect")
        keyboard.add(budget_test_2_correct, budget_test_2_incorrect_1, budget_test_2_incorrect_2)

        bot.send_message(call.message.chat.id, "Правильно! \nСледующий вопрос: Что означает диверсификация в инвестициях?",
                         reply_markup=keyboard)

    elif call.data == "investments_test_2_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_2_incorrect_1 = types.InlineKeyboardButton(text="Использование только надёжных банковских вкладов",
                                                               callback_data="investments_test_2_incorrect")
        budget_test_2_correct = types.InlineKeyboardButton(
            text="Вложение средств в разные классы активов для снижения рисков",
            callback_data="investments_test_2_correct")
        budget_test_2_incorrect_2 = types.InlineKeyboardButton(text="Использование только надёжных банковских вкладов",
                                                               callback_data="investments_test_2_incorrect")
        keyboard.add(budget_test_2_correct, budget_test_2_incorrect_1, budget_test_2_incorrect_2)

        bot.send_message(call.message.chat.id,
                         "Неправильно, попробуйте еще раз. \nЧто означает диверсификация в инвестициях?",
                         reply_markup=keyboard)

    elif call.data == "investments_test_2_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_3_incorrect_1 = types.InlineKeyboardButton(
            text="Банк, в котором вы держите вклад, обанкротился",
            callback_data="investments_test_3_incorrect")
        budget_test_3_correct = types.InlineKeyboardButton(text="Компания, чьи акции вы купили, резко снизилась в цене из-за кризиса",
                                                           callback_data="investments_test_3_correct")
        budget_test_3_incorrect_2 = types.InlineKeyboardButton(
            text="Вы забыли перевести деньги на брокерский счёт",
            callback_data="investments_test_3_incorrect")
        keyboard.add(budget_test_3_incorrect_1, budget_test_3_incorrect_2, budget_test_3_correct)

        bot.send_message(call.message.chat.id,
                         "Правильно! \nСледующий вопрос: Какая из ситуаций может привести к рыночному риску?",
                         reply_markup=keyboard)

    elif call.data == "investments_test_3_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_3_incorrect_1 = types.InlineKeyboardButton(
            text="Банк, в котором вы держите вклад, обанкротился",
            callback_data="investments_test_3_incorrect")
        budget_test_3_correct = types.InlineKeyboardButton(
            text="Компания, чьи акции вы купили, резко снизилась в цене из-за кризиса",
            callback_data="investments_test_3_correct")
        budget_test_3_incorrect_2 = types.InlineKeyboardButton(
            text="Вы забыли перевести деньги на брокерский счёт",
            callback_data="investments_test_3_incorrect")
        keyboard.add(budget_test_3_incorrect_1, budget_test_3_incorrect_2, budget_test_3_correct)

        bot.send_message(call.message.chat.id,
                         "Неправильно, попробуйте еще раз. \nКакая из ситуаций может привести к рыночному риску?",
                         reply_markup=keyboard)

    elif call.data == "investments_test_3_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_back_to_menu = types.InlineKeyboardButton(text="Вернуться в меню",
                                                         callback_data="start_learning")
        keyboard.add(budget_back_to_menu)

        bot.send_message(call.message.chat.id,
                         "Правильно! Поздравляю! Вы прошли тест.", reply_markup=keyboard)


# Кредит (loans)

    elif call.data == "loans":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="loans_button_1")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/loans/1.jpg', 'rb'), """Что такое кредит и когда он оправдан
\nКредит — это заём денег у банка или другой организации с обязательством возврата суммы с процентами.
Он может быть полезен при:
- Покупке жилья
- Финансировании образования
- Неотложных медицинских расходах
\nВажно, чтобы кредит был осознанным решением, а не импульсивной реакцией на дефицит денег.
""", reply_markup=keyboard)

    elif call.data == "loans_button_1":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="loans_button_2")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/loans/2.jpg', 'rb'), """Виды кредитов
\n- Потребительский
- Ипотека
- Кредитные карты
- Автокредит
\nУ каждого вида — свои условия, ставки и риски. Важно внимательно читать договоры и оценивать реальную стоимость кредита, включая все комиссии.
""", reply_markup=keyboard)

    elif call.data == "loans_button_2":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="loans_button_3")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/loans/3.jpg', 'rb'), """Платёжеспособность и расчёт кредитной нагрузки
\nЕжемесячные платежи по всем кредитам не должны превышать 30–35% от дохода.
Перед оформлением кредита рассчитайте:
- Сумму ежемесячного платежа
- Срок
- Общую переплату
\nПри сомнении — откажитесь.
""", reply_markup=keyboard)

    elif call.data == "loans_button_3":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="loans_button_4")
        keyboard.add(budget_button_1)
        bot.send_photo(call.message.chat.id, open('images/loans/4.jpg', 'rb'), """Опасности и последствия необдуманных кредитов
\n- Задержка платежей ведёт к штрафам и испорченной кредитной истории
- Просрочки могут привести к искам и судебным взысканиям
- Психологическая нагрузка и стресс
\nКредит — это ответственность, а не подарок.
""", reply_markup=keyboard)

    elif call.data == "loans_button_4":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="loans_button_5")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Как гасить кредиты быстрее
\n- Вносите дополнительные платежи при возможности
- Сократите срок, а не сумму
- Перекредитуйтесь на лучших условиях
\nРаннее погашение может существенно сократить переплату.
""", reply_markup=keyboard)

    elif call.data == "loans_button_5":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Далее", callback_data="loans_button_6")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Что делать при финансовых трудностях
\n- Свяжитесь с банком заранее
- Запросите кредитные каникулы или реструктуризацию
- Не берите новые кредиты для погашения старых
\nВременное снижение дохода — не конец. Главное — действовать, а не игнорировать проблему.
""", reply_markup=keyboard)

    elif call.data == "loans_button_6":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_button_1 = types.InlineKeyboardButton(text="Пройти тест", callback_data="loans_test")
        keyboard.add(budget_button_1)
        bot.send_message(call.message.chat.id, """Финал
\nВы завершили тему «Кредиты».
Разумное использование заёмных средств может быть полезным, но только при полной осознанности и понимании последствий. Теперь давайте проверим, насколько хорошо вы усвоили материал. Ответьте на несколько вопросов.
""", reply_markup=keyboard)

    elif call.data == "loans_test":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_1_incorrect_1 = types.InlineKeyboardButton(
            text="До 50% от дохода, если кредит одобрен банком",
            callback_data="loans_test_1_incorrect")
        budget_test_1_correct = types.InlineKeyboardButton(
            text="Не более 30–35% от ежемесячного дохода", callback_data="loans_test_1_correct")
        budget_test_1_incorrect_2 = types.InlineKeyboardButton(text="Главное — чтобы хватало на оплату, точного процента нет",
                                                               callback_data="loans_test_1_incorrect")
        keyboard.add(budget_test_1_incorrect_1, budget_test_1_correct, budget_test_1_incorrect_2)
        bot.send_message(call.message.chat.id, "Какой уровень кредитной нагрузки считается допустимым?", reply_markup=keyboard)

    elif call.data == "loans_test_1_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_1_incorrect_1 = types.InlineKeyboardButton(
            text="До 50% от дохода, если кредит одобрен банком",
            callback_data="loans_test_1_incorrect")
        budget_test_1_correct = types.InlineKeyboardButton(
            text="Не более 30–35% от ежемесячного дохода", callback_data="loans_test_1_correct")
        budget_test_1_incorrect_2 = types.InlineKeyboardButton(
            text="Главное — чтобы хватало на оплату, точного процента нет",
            callback_data="loans_test_1_incorrect")
        keyboard.add(budget_test_1_incorrect_1, budget_test_1_correct, budget_test_1_incorrect_2)
        bot.send_message(call.message.chat.id,
                         "Неправильно, попробуйте еще раз. \nКакой уровень кредитной нагрузки считается допустимым?",
                         reply_markup=keyboard)

    elif call.data == "loans_test_1_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_2_incorrect_1 = types.InlineKeyboardButton(text="Ждать, пока банк сам предложит решение",
                                                               callback_data="loans_test_2_incorrect")
        budget_test_2_correct = types.InlineKeyboardButton(
            text="Связаться с банком и обсудить варианты реструктуризации или отсрочки",
            callback_data="loans_test_2_correct")
        budget_test_2_incorrect_2 = types.InlineKeyboardButton(text="Взять новый кредит, чтобы временно перекрыть старый",
                                                               callback_data="loans_test_2_incorrect")
        keyboard.add(budget_test_2_correct, budget_test_2_incorrect_1, budget_test_2_incorrect_2)

        bot.send_message(call.message.chat.id, "Правильно! \nСледующий вопрос: Что делать в первую очередь при потере дохода и наличии кредита?",
                         reply_markup=keyboard)

    elif call.data == "loans_test_2_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_2_incorrect_1 = types.InlineKeyboardButton(text="Ждать, пока банк сам предложит решение",
                                                               callback_data="loans_test_2_incorrect")
        budget_test_2_correct = types.InlineKeyboardButton(
            text="Связаться с банком и обсудить варианты реструктуризации или отсрочки",
            callback_data="loans_test_2_correct")
        budget_test_2_incorrect_2 = types.InlineKeyboardButton(text="Взять новый кредит, чтобы временно перекрыть старый",
                                                               callback_data="loans_test_2_incorrect")
        keyboard.add(budget_test_2_correct, budget_test_2_incorrect_1, budget_test_2_incorrect_2)

        bot.send_message(call.message.chat.id,
                         "Неправильно, попробуйте еще раз. \nЧто делать в первую очередь при потере дохода и наличии кредита?",
                         reply_markup=keyboard)

    elif call.data == "loans_test_2_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_3_incorrect_1 = types.InlineKeyboardButton(
            text="Увеличение  срока кредита для снижения ежемесячных платежей",
            callback_data="loans_test_3_incorrect")
        budget_test_3_correct = types.InlineKeyboardButton(text="Рефинансирование или частичное досрочное погашение",
                                                           callback_data="loans_test_3_correct")
        budget_test_3_incorrect_2 = types.InlineKeyboardButton(
            text="Использование кредитных карт для оплаты взносов по другим кредитам",
            callback_data="loans_test_3_incorrect")
        keyboard.add(budget_test_3_incorrect_1, budget_test_3_incorrect_2, budget_test_3_correct)

        bot.send_message(call.message.chat.id,
                         "Правильно! \nСледующий вопрос: Какая стратегия помогает быстрее погасить кредит и уменьшить переплату?",
                         reply_markup=keyboard)

    elif call.data == "loans_test_3_incorrect":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        budget_test_3_incorrect_1 = types.InlineKeyboardButton(
            text="Увеличение  срока кредита для снижения ежемесячных платежей",
            callback_data="loans_test_3_incorrect")
        budget_test_3_correct = types.InlineKeyboardButton(text="Рефинансирование или частичное досрочное погашение",
                                                           callback_data="loans_test_3_correct")
        budget_test_3_incorrect_2 = types.InlineKeyboardButton(
            text="Использование кредитных карт для оплаты взносов по другим кредитам",
            callback_data="loans_test_3_incorrect")
        keyboard.add(budget_test_3_incorrect_1, budget_test_3_incorrect_2, budget_test_3_correct)

        bot.send_message(call.message.chat.id,
                         "Неправильно, попробуйте еще раз. \nКакая стратегия помогает быстрее погасить кредит и уменьшить переплату?",
                         reply_markup=keyboard)

    elif call.data == "loans_test_3_correct":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        budget_back_to_menu = types.InlineKeyboardButton(text="Вернуться в меню",
                                                         callback_data="start_learning")
        keyboard.add(budget_back_to_menu)

        bot.send_message(call.message.chat.id,
                         "Правильно! Поздравляю! Вы прошли тест.", reply_markup=keyboard)

bot.polling(none_stop = True, interval = 0)



