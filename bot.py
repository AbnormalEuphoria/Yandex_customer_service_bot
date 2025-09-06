import telebot
from telebot import types
import re
import time

bot = telebot.TeleBot('') # Enter key here

@bot.message_handler(content_types=['text'])

def get_text_messages(message):


    if  message.text == "/start":
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)
        key_answer_1 = types.InlineKeyboardButton(text="Ах, Гастингс, вы знаете, что я не могу устоять перед подобной загадкой! Давайте приступим к делу немедленно!")
        bot.send_message(message.from_user.id, """ПРАВИЛА: 
1. Ответы писать капсом без пробелов, ошибок и опечаток на русском языке. 
2. Возьмите с собой блокнот и ручку на всякий случай. Они могут помочь в расследовании. Также следует взять ключи от машины и большую связку ключей. 
3. В случае затрудненности в какой-либо части расследования обращаться к Полине П.
4. Большая просьба не торопиться и решать в расслабленном режиме. Чтобы прочувствовать атмосферу игры, надо расслабиться и решать загадки в размеренном режиме. НОСИТЬСЯ СЛОМЯ ГОЛОВУ ОТ ЛОКАЦИИ К ЛОКАЦИИ ЗАПРЕЩЕНО. 
5. При выдаче адреса отвечать Капитану Гастинсу следует только при смене локации, находясь непосредственно по указанному адресу. Для соблюдения атмосферы таинтсвенности точное место не указано, но отмечены ориентиры.""")
        time.sleep(1)
        bot.send_message(message.from_user.id, "И ПОМНИТЕ: «Аромат лжи всегда оставляет след. Следуйте за запахом правды».")
        time.sleep(1)
        keyboard.add(key_answer_1)
        bot.send_message(message.from_user.id, "Дорогой друг, позвольте представить вам новое дело! «HARRINGTON & SONS» сообщает о необъяснимых пропажах из их транспортных средств. Я уверен, что ваше гениальное мышление поможет нам раскрыть эту тайну!", reply_markup=keyboard)
    elif message.text == "Ах, Гастингс, вы знаете, что я не могу устоять перед подобной загадкой! Давайте приступим к делу немедленно!":
        time.sleep(1)
        bot.send_message(message.from_user.id, "Для успешного раскрытия этого дела нам потребуется надлежащая подготовка. Соберите, пожалуйста, все необходимые материалы. В поисках Вам поможет эта карта.")
        bot.send_photo(message.from_user.id, open('map_1.jpg', 'rb'), """Построй маршрут по клеткам: 

1.   3↑     1→    7↑    8→
2.   3↑     1←    3↑    2←   1↓
3.   2↑     5←
4.   3↑      1←   8↑     3←    4↑      1←""")

    elif message.text == "СБЫТ" :
        time.sleep(1)
        bot.send_message(message.from_user.id, "Превосходная идея, сэр! Это именно то, что нам нужно! \n\nЯ предлагаю незамедлительно приступить к обследованию местных ломбардов. Уверен, там мы найдём важные улики!")
        time.sleep(1)
        bot.send_message(message.from_user.id, """В какой ломбард отправимся первым делом? \n\nПострой еще один дополнительный маршрут по клеткам: 

1.   3↑     1→    10↑""")

    elif message.text == "ЧЕСТНОЕСЛОВО":
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)
        key_answer_2 = types.InlineKeyboardButton(text="О, какое занимательное место!  Давайте же разгадаем этот шифр и проведём тщательное расследование!")
        time.sleep(1)
        bot.send_message(message.from_user.id, "просп. Художников, 27, корп. 1 (рядом с кофейней \"Сестры\"")
        time.sleep(1)
        keyboard.add(key_answer_2)
        bot.send_message(message.from_user.id, "Я тоже сразу подумал об этом месте, сэр! «Честное слово» — действительно самый популярный ломбард в округе. \n\nОднако, должен вас предупредить — там не жалуют посторонних, особенно людей нашей профессии. Нам придётся проявить смекалку и раздобыть их особый пароль чтобы завоевать доверие", reply_markup=keyboard)

    elif message.text == "О, какое занимательное место!  Давайте же разгадаем этот шифр и проведём тщательное расследование!":
        time.sleep(1)
        bot.send_photo(message.from_user.id, open('riddle_1.jpg', 'rb'),"Расшифруй текст:")

    elif message.text == "ШЕСТЕРЕНКАКРУТИТДЕЛО":
        time.sleep(1)
        bot.send_photo(message.from_user_id, open('qr_1.jpg', 'rb'))
        time.sleep(60)
        bot.send_message(message.from_user.id, """Да, в том ломбарде мы действительно нашли кое-что интересное, но я бы не стал ограничиваться только им. Есть ещё одно место, о котором я знаю, но название, увы, вылетело у меня из памяти.\n\n
Не припоминаете ли вы, мистер Пуаро?""")
        bot.send_photo(message.from_user.id, open('riddle_2.jpg', 'rb'), "Выполни действие и напиши полученное словосочетание")

    elif message.text == "ЖЕЛЕЗНЫЙКОНЬ":
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)
        key_answer_3 = types.InlineKeyboardButton(
            text="Вот мы и на месте, Гастингс!")

        time.sleep(1)
        bot.send_message(message.from_user.id, "Совершенно верно, сэр! Как же я мог упустить это из виду — ведь я сам заходил туда за запчастями для служебного транспорта! Теперь я точно вспомнил!")
        time.sleep(1)
        keyboard.add(key_answer_3)
        bot.send_message(message.from_user.id, "ул. Кустодиева, 16, корп. 1, рядом с салоном красоты Loreana", reply_markup=keyboard)

    elif message.text == "Вот мы и на месте, Гастингс!":
        time.sleep(1)
        bot.send_message(message.from_user.id, "Как бы вам сказать... Дело в том, что водители образовали тесный круг, куда непросто проникнуть. Чтобы завоевать их доверие, нам придётся действовать согласно их установленным порядкам, Придется отгадать еще одну загадку.")
        time.sleep(1)
        bot.send_photo(message.from_user.id, open('riddle_3.jpg', 'rb'), "Распутай геометрическую решетку")

    elif message.text == "ПАРОВОЙГРУЗОВИК":
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)
        key_answer_4 = types.InlineKeyboardButton(
            text="Предлагаю начать проверку с грузового отделения. Хардинг отпустил сегодня водителей и это играет нам на руку.")
        time.sleep(1)
        bot.send_photo(message.from_user.id, open('qr_2.jpg', 'rb'))
        time.sleep(60)
        keyboard.add(key_answer_4)
        bot.send_message(message.from_user.id, "О, весьма занимательно!Наличие украденных вещей в ломбардах — это явное свидетельство существования преступной сети. Позвольте указать на очевидный факт: водители и грузчики имеют прямой доступ к грузам, а бухгалтеры контролируют документацию. Не исключено, что кто-то из них использует своё положение для личного обогащения", reply_markup=keyboard)

    elif message.text == "Предлагаю начать проверку с грузового отделения. Хардинг отпустил сегодня водителей и это играет нам на руку.":
        time.sleep(1)
        bot.send_photo(message.from_user.id, open('riddle_4.jpg', 'rb'), "Соедините по точкам слово")

    elif message.text == "СУБАРУ":
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)
        key_answer_5 = types.InlineKeyboardButton(
            text="Гастингс, взгляните — посылка! Как же так можно вести дела?  Причиной всех убытков может быть банальная халатность и отсутствие порядка")
        time.sleep(1)
        keyboard.add(key_answer_5)
        bot.send_message(message.from_user.id, "Отправляйтесь к Субару Импреза, Осмотрите машину")
        time.sleep(300)
        bot.send_message(message.from_user.id, "", reply_markup=keyboard)


    elif message.text == "Гастингс, взгляните — посылка! Как же так можно вести дела?  Причиной всех убытков может быть банальная халатность и отсутствие порядка":
        time.sleep(1)
        bot.send_message(message.from_user.id, """Сэр,я полагаю,нам необходимо нанести визит бухгалтеру компании. Она сможет предоставить нам важную информацию о финансовых потоках и, что не менее важно,о сотрудниках. Это может пролить свет на наше расследование
Но предупреждаю сразу, что главный бухгалтер компании «Хардинг и сыновья» — настоящий профессионал своего дела. Она не допускает ни малейшей неразберихи в документах""")
        time.sleep(1)
        bot.send_photo(message.from_user.id, open('riddle_5.jpg', 'rb'), "Соедините буквы с их порядком")


    elif message.text == "ЭЛИЗАБЕТПАРКЕР":
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)
        key_answer_5 = types.InlineKeyboardButton(
            text="Мы пересекались расследовании пары дел. Её внимание к деталям восхитительно. Нам необходимо ознакомиться с информацией о сотрудниках компании")
        time.sleep(1)
        bot.send_message(message.from_user.id, "Адрес: проспект Художников, 31к1, а дальше сам знаешь (да, вплоть до квартиры)")
        time.sleep(1)
        keyboard.add(key_answer_5)
        bot.send_message(message.from_user.id, "Знаете мисс Паркер? Вот так совпадение!", reply_markup=keyboard)

    elif message.text == "Мы пересекались расследовании пары дел. Её внимание к деталям восхитительно. Нам необходимо ознакомиться с информацией о сотрудниках компании":
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)
        key_answer_6 = types.InlineKeyboardButton(
            text="О, какая досада — мисс Паркер, кажется, отсутствует, но её документы, несомненно, где-то здесь. Приступим к их поиску!")
        time.sleep(180)
        keyboard.add(key_answer_6)
        bot.send_message(message.from_user.id, "", reply_markup=keyboard)

    elif message.text == "О, какая досада — мисс Паркер, кажется, отсутствует, но её документы, несомненно, где-то здесь. Приступим к их поиску!":
        time.sleep(1)
        bot.send_message(message.from_user.id, "Найдите папку с информацией о сотрудниках. Изучите информацию. Сделайте выводы.")
        time.sleep(60)
        bot.send_message(message.from_user.id, "Найдите записку, оставленную Элизабет Паркер")
        time.sleep(60)
        bot.send_message(message.from_user.id, "Кажется, судьба подарила нам ещё одного помощника. Многолетний опыт общения с мисс Паркер убедил меня в её неподкупной честности. Возможно, она уже провела собственное расследование внутри компании и теперь желает, чтобы мы перепроверили его результаты")
        time.sleep(1)
        bot.send_message(message.from_user.id, "ЗАДАНИЕ: Купить что-то к чаю и оправиться в район \"Лондонпарк\" к чете Флорелли для проведения опроса")
        time.sleep(300)
        bot.send_message(message.from_user.id, "Сэр, прошу прощения, но меня срочно вызывают по служебным делам. Я вынужден откланяться.")

    else:
        bot.send_message(message.from_user.id, "К сожалению, я вас не понял.")



bot.polling(none_stop = True, interval = 0)



