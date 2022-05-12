import telebot
from telebot import types
import re

bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    keyboard= types.ReplyKeyboardMarkup(row_width = 2,resize_keyboard = True)
    key_thanks = types.InlineKeyboardButton(text = 'Спасибо', callback_data = 'Спасибо')
    key_restore = types.InlineKeyboardButton(text = "Я утратил доступ к аккаунту", callback_data = "Я утратил доступ к аккаунту")
    key_password = types.InlineKeyboardButton(text = "Я забыл пароль" , callback_data = "Я забыл пароль")
    key_challenge = types.InlineKeyboardButton(text = "Я не могу пройти дополнительную проверку")
    key_2fa = types.InlineKeyboardButton(text = "Трудности с двухфакторной аутентификацией")
    key_null = types.InlineKeyboardButton(text = "У меня есть другой вопрос")
    key_data_change = types.InlineKeyboardButton(text = "Я хочу изменить данные")
    key_change_number = types.InlineKeyboardButton(text = "Я хочу изменить номер телефона")
    key_services_question = types.InlineKeyboardButton(text = "У меня вопрос про сервисы Яндекс")
    key_security = types.InlineKeyboardButton(text = "У меня вопрос про защиту аккаунта")
    key_change_question = types.InlineKeyboardButton(text = "Я хочу изменить ответ на контрольный вопрос")
    key_change_data = types.InlineKeyboardButton(text = "Я хочу изменить личные данные")
    key_pdd = types.InlineKeyboardButton(text = "Я пользуюсь почтой для домена")
    key_2fa_troubles = types.InlineKeyboardButton(text = "Не подходит одноразовый пароль")
    key_2fa_enabling = types.InlineKeyboardButton(text = "Не могу подключить 2FA")
    key_demand_change = types.InlineKeyboardButton(text = "Яндекс просит сменить пароль")
    key_2fa_setup = types.InlineKeyboardButton(text = "Я хочу защитить свой аккаунт")
    key_hacking = types.InlineKeyboardButton(text = "Мой аккаунт взломали")
    key_access_true = types.InlineKeyboardButton(text = "Да, у меня есть доступ")
    key_access_false = types.InlineKeyboardButton(text = "Нет, у меня нет доступа")
    key_sms2fa = types.InlineKeyboardButton(text = "Я хочу подтверждать вход по SMS")
    key_ya_key = types.InlineKeyboardButton(text = "Я хочу настроить вход по одноразовым паролям")
    key_plus = types.InlineKeyboardButton(text = "Яндекс Плюс")
    key_music = types.InlineKeyboardButton(text = "Яндекс Музыка")
    key_eda = types.InlineKeyboardButton(text = "Яндекс Еда")
    key_taxi = types.InlineKeyboardButton(text = "Яндекс Такси")
    key_ID = types.InlineKeyboardButton(text = "Яндекс ID")
    if  message.text == "Привет" or message.text == "/start" or message.text == "привет":
        keyboard.add(key_restore, key_data_change, key_services_question, key_security)
        bot.send_message(message.from_user.id, "Здравствуйте, я - Бот Службы поддержки Яндекс. Чем я могу вам помочь?", reply_markup=keyboard)
    elif message.text == "У меня есть другой вопрос" or message.text == "/help" :
        keyboard.add(key_restore, key_data_change, key_services_question, key_security)
        bot.send_message(message.from_user.id, "Уточните, пожалуйста, с чем связан ваш вопрос?", reply_markup = keyboard)
    elif message.text == "Я хочу изменить данные" :
        keyboard.add(key_change_number, key_change_question, key_change_data, key_pdd, key_null)
        bot.send_message(message.from_user.id, "Что именно вы хотите изменить?", reply_markup = keyboard)
    elif message.text == "Я утратил доступ к аккаунту" or re.search(r'\b(по|у)теря(н|л|ла|ли) доступ\b', message.text, re.I) or re.search(r'\bутра(тил|тила|тили|чен) доступ\b', message.text, re.I) or re.search(r'\bдоступ утра(тил|тила|тили|чен)\b', message.text, re.I) or re.search(r'\bдоступ (по|у)теря(н|л|ла|ли)\b', message.text, re.I):
        keyboard.add(key_password, key_challenge, key_2fa, key_demand_change, key_pdd, key_null)
        bot.send_message(message.from_user.id, "Уточните, пожалуйста, с чем именно связаны трудности?", reply_markup=keyboard)
    elif message.text == "Я забыл пароль" or re.search(r'\bзабы(л|ла|ли|т) пароль\b', message.text, re.I):
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Если вы забыли пароль для входа на Яндекс, попробуйте сбросить его самостоятельно. "
                                               "Для этого следуйте инструкциям на странице https://passport.yandex.ru/passport?mode=restore .\n\n"
                                               "Если автоматически восстановить доступ не получилось, то вы можете связаться со Службой поддержки на странице https://yandex.ru/support/id/feedback.html .", reply_markup=keyboard)
    elif message.text == "Я не могу пройти дополнительную проверку":
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Когда вы входите с нового или чужого устройства, Яндекс может посчитать попытку входа подозрительной. В таком случае вам необходимо будет пройти дополнительную проверку.\n"
                                               "\nВведите код из SMS, последние четыре цифры входящего номера или ответ на контрольный вопрос. Если у вас есть авторизация на другом устройстве, то вы также можете войти в аккаунт с помощью QR-кода. Для этого выберите \"Вход по QR-коду\" на странице авторизации.\n"
                                               "\nЕсли пройти дополнительную проверку не получается, то вы можете связаться со Службой поддержки на странице https://yandex.ru/support/id/feedback.html ", reply_markup=keyboard)
    elif message.text == "Трудности с двухфакторной аутентификацией":
        keyboard.add(key_2fa_enabling, key_2fa_troubles, key_null)
        bot.send_message(message.from_user.id, "С чем именно у вас возникают трудности?", reply_markup = keyboard)
    elif message.text == "Не подходит одноразовый пароль":
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Скорее всего, для получения одноразовых паролей вводится неверный пин-код. Яндекс Ключ не проверяет правильность пин-кода, но с паролем, полученным с помощью неверного пин-кода, авторизоваться не удастся\n"
                                               "\nПожалуйста, попробуйте вспомнить правильный пин-код и авторизоваться заново. Если вспомнить пин-код так и не удастся, то вы можете связаться со Службой поддержки на странице https://yandex.ru/support/id/feedback.html ", reply_markup = keyboard)
    elif message.text == "Не могу подключить 2FA":
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Такое может получаться, если при на аккаунте уже начиналось включение двухфакторной аутентификации, или при получении одноразовых паролей вводился неверный пин-код.\n"
                                               "\nПожалуйста, попробуйте ввести правильный пин-код или удалить аккаунт из Яндекс Ключа и начать процедуру заново.\n"
                                               "\nПодробнее о включении двухфакторной аутентификации вы можете найти в нашей Справке на странице https://yandex.ru/support/id/authorization/twofa-on.html", reply_markup = keyboard)

    elif message.text == "Я пользуюсь почтой для домена":
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Если ваш аккаунт находится на домене, который не принадлежит Яндексу, то для изменения данных или восстановления доступа, пожалуйста, обратитесь к владельцу домена, от которого вы получали почтовый ящик.", reply_markup = keyboard)

    elif message.text == "Я хочу изменить номер телефона":
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Вы можете изменить номер телефона на странице https://passport.yandex.ru/profile/phones . Для этого нажмите на текущий номер телефона и подтвердите замену кодами из SMS, которые мы отправим на оба номера.\n "
                                               "\nЕсли у вас нет доступа к привязанному номеру, выберите пункт \"Нет доступа к номеру\". В таком случае SMS придет только на актуальный номер, но замена произойдет только через 30 дней. Это сделано для увеличения защиты аккаунтов от злоумышленников.\n "
                                               "\nОднако, замену номера можно ускорить с помощью Службы поддержки, но только в том случае, если при регистрации аккаунта были указаны ваши реальные данные. Для этого, пожалуйста, перейдите на страницу https://yandex.ru/support/id/feedback.html и выберите \"Хочу изменить номер телефона\".", reply_markup = keyboard)

    elif message.text == "Я хочу изменить ответ на контрольный вопрос":
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Вы можете изменить ответ на контрольный вопрос на странице https://passport.yandex.ru/profile/change-hint. Если ответ на предыдущий контрольный вопрос забыт, то восстановить его можно только с помощью Службы поддержки. Для этого, пожалуйста, заполните анкету на странице https://yandex.ru/support/id/feedback.html", reply_markup = keyboard)

    elif message.text == "Я хочу изменить личные данные" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Изменить личные данные можно на странице управления аккаунтом (https://passport.yandex.ru/profile)", reply_markup = keyboard)

    elif message.text == "Яндекс просит сменить пароль" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Ваш аккаунт, скорее всего, взломан, или пароль был найден в публичном доступе. Чтобы защитить свой аккаунт от взлома, пароль необходимо изменить. \n"
                                               "\nЕсли вы не можете восстановить доступ к аккаунту с помощью телефона или контрольного вопроса, пожалуйста, заполните анкету на странице https://passport.yandex.ru/restoration/form", reply_markup = keyboard)

    elif message.text == "У меня вопрос про защиту аккаунта" :
        keyboard.add(key_demand_change, key_2fa_setup, key_hacking, key_null)
        bot.send_message(message.from_user.id, "С чем связан ваш вопрос?", reply_markup = keyboard)

    elif message.text == "Мой аккаунт взломали" :
        keyboard.add(key_access_true, key_access_false, key_null)
        bot.send_message(message.from_user.id, "Уточните, пожалуйста, есть ли у вас сейчас доступ к вашему аккаунту?", reply_markup = keyboard)

    elif message.text == "Да, у меня есть доступ" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Первым делом проверьте ваш компьютер на наличие вирусов с помощью антивирусной программы, после чего, пожалуйста, следуйте нашим рекомендациям, которые помогут обезопасить ваш аккаунт: \n"
                                               "\n 1) Убедитесь, что на странице https://passport.yandex.ru/profile/phones указаны только ваши номера и не запущено изменение или удаление защищенного номера. \nЕсли вы еще не привязали номер телефона к своему аккаунту, сделайте это. Актуальный номер телефона защищает аккаунт надежнее, чем адрес почты или контрольный вопрос. \n"
                                               "\n 2) Удалите незнакомые адреса на странице https://passport.yandex.ru/profile/emails. \nПомните, что вам принадлежат все адреса с вашим логином на доменах Яндекса, например, <ваш логин>@yandex.com, <ваш логин>@yandex.kz или <ваш логин>@ya.ru. Это алиасы вашего почтового ящика, удалить их нельзя. \n"
                                               "\n 3) Если вы авторизуетесь в Яндексе через аккаунт социальной сети, проверьте, не взломан ли этот аккаунт — с его помощью злоумышленник мог получить доступ к вашим данным на Яндексе. \n"
                                               "\n 4) Смените пароль для вашего аккаунта на странице https://passport.yandex.ru/profile/access, чтобы закрыть доступ тем, кто мог узнать ваш пароль.\n"
                                               "\n 5) Если вы пользуетесь устройством на базе Android или iOS, настройте двухфакторную аутентификацию на странице https://yandex.ru/support/id/authorization/twofa.html — самый надежный способ защиты Яндекс ID.", reply_markup = keyboard)

    elif message.text == "Нет, у меня нет доступа" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Пожалуйста, проверьте ваш компьютер на наличие вирусов с помощью антивирусной программы, после чего попробуйте восстановить доступ автоматически на странице https://passport.yandex.ru/passport?mode=restore .\n\nЕсли сделать это самостоятельно не получается, заполните анкету для службы поддержки https://yandex.ru/support/id/support-restore.html", reply_markup = keyboard)

    elif message.text == "Я хочу защитить свой аккаунт" :
        keyboard.add(key_sms2fa, key_ya_key)
        bot.send_message(message.from_user.id, "Двухфакторная аутентификация - самый надежный способ защитить свой аккаунт от злоумышленников. Уточните, пожалуйста, вы хотите подтверждать вход с помощью SMS или одноразовых паролей?", reply_markup = keyboard)

    elif message.text == "Я хочу подтверждать вход по SMS" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Если у вас включено подтверждение входа по номеру телефона в настройках аккаунта, при попытке входа мы отправим SMS или позвоним на основной номер, привязанный к вашему Яндекс ID. Введите код из SMS или последние четыре цифры входящего номера для входа в аккаунт.\n"
                                               "\nДля включения входа по SMS: \n"
                                               "\n1) Откройте страницу Управления аккаунтом (https://passport.yandex.ru/profile/)\n"
                                               "\n2) В разделе Пароли и авторизация нажмите Способ входа и включите опцию Пароль + СМС.\n"
                                               "\n3) Подтвердите действие — введите код из SMS.\n"
                                               "\nПодробнее про вход по SMS вы можете прочитать в нашей Справке https://yandex.ru/support/id/security/login-challenge.html#phone-confirm", reply_markup = keyboard)

    elif message.text == "Я хочу настроить вход по одноразовым паролям" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Вы можете включить двухфакторную аутентификацию в настройках аккаунта (https://passport.yandex.ru/profile).\n"
                                               "\nВам понадобится приложение Яндекс Ключ, которое можно установить на мобильное устройство на базе iOS или Android. Устройство, которое не поддерживает установку приложений (например, Amazon Kindle Fire), использовать не получится.\n"
                                               "\nПодробную инструкцию по включению двухфакторной аутентификации вы можете найти в нашей Справке https://yandex.ru/support/id/authorization/twofa-on.html", reply_markup = keyboard)

    elif message.text == "У меня вопрос про сервисы Яндекс" :
        keyboard.add(key_eda, key_plus, key_music, key_ID, key_taxi)
        bot.send_message(message.from_user.id, "К какому сервису Яндекса у вас вопрос?", reply_markup = keyboard)

    elif message.text == "Яндекс Плюс" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Со службой поддержки Яндекс Плюс вы можете связаться по ссылке https://yandex.ru/support/plus-ru/troubleshooting.html", reply_markup = keyboard)

    elif message.text == "Яндекс Музыка" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Вы можете связаться со службой поддержки Яндекс Музыки по ссылке https://yandex.ru/support/music/troubleshooting/feedback.html", reply_markup = keyboard)

    elif message.text == "Яндекс Такси" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Для связи с сервисом Яндекс Такси, пожалуйста, воспользуйтесь формой обратной связи на странице https://taxi.yandex.ru/support/", reply_markup = keyboard)

    elif message.text == "Яндекс Еда" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Вы можете связаться с сервисом Яндекс Еда по ссылке https://yandex.ru/support/eda/feedback.html", reply_markup = keyboard)

    elif message.text == "Яндекс ID" :
        keyboard.add(key_null, key_thanks)
        bot.send_message(message.from_user.id, "Для связи с сервисом Яндекс ID, пожалуйста, воспользуйтесь ссылкой https://yandex.ru/support/id/feedback.html", reply_markup = keyboard)

    elif message.text == "Спасибо":
        keyboard = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.from_user.id, "Рад был помочь! Пожалуйста, обращайтесь снова, если возникнут какие-либо вопросы", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "К сожалению, я вас не понял. Пожалуйста, напишите /help")



bot.polling(none_stop = True, interval = 0)



