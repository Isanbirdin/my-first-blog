import telebot
from telebot import types
import requests

bot = telebot.TeleBot('1890315220:AAE847gJUW1sNW85qTFKc_V3RSRei15MlHI')

chat = '-433598889'

@bot.message_handler(commands = ['order', 'programmist', 'targetolog'])
def send_forward_order(message):
    bot.reply_to(message, 'Ваше сообщение доставлено и в скором времени пройдет проверку.🤩')
    if '/order' in message.text:
        bot.forward_message(-433598889, message.chat.id, message.id)
    if '/programmist' in message.text:
        bot.forward_message(-433598889, message.chat.id, message.id)
    if '/targetolog' in message.text:
        bot.forward_message(-433598889, message.chat.id, message.id)

@bot.message_handler(commands=['start', 'order_bot', 'help_admin', 'group_vk_link', 'work_us'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Заказать бота', callback_data = 'order')
    item2 = types.InlineKeyboardButton('Связаться с поддержкой', callback_data = 'help_admin')
    item3 = types.InlineKeyboardButton('Получить ссылку на паблик VK', callback_data = 'get_vk_link')
    item4 = types.InlineKeyboardButton('Работать у нас', callback_data = 'work_us')

    markup.add(item1,item2,item3,item4)

    bot.send_message(message.chat.id, f'''Я бот🤖. Приятно познакомиться, {message.from_user.first_name}.
💬Выбери, что нужно сделать:''', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'order':
            bot.send_message(call.message.chat.id, '''😜Оставьте заявку на покупку бота.😜
😇Ваше следующее сообщение пройдет проверку, по ее окончании вам напишет менеджер.
😏Пожалуйста, опишите все в мельчайших подробностях.
~~~~💬Функции бота.
~~~~💬Cоциальную сеть.
~~~~💬Бюджет.
✅Не забудь в начале сообщения ввести /order.''')
    if call.message:
        if call.data == 'help_admin':
            help_buttons = types.InlineKeyboardMarkup(row_width=1)

            help_buttons1 = types.InlineKeyboardButton('✅Telegram_admin.', callback_data = 'tg_admin')
            help_buttons2 = types.InlineKeyboardButton('✅VK_Group.', callback_data = 'vk_group')
            help_buttons3 = types.InlineKeyboardButton('✅VK_admin.', callback_data = 'vk_admin')

            help_buttons.add(help_buttons1,help_buttons2,help_buttons3)

            bot.send_message(call.message.chat.id, '''Вы можете написать нам в:''', reply_markup=help_buttons)

        if call.message:
            if call.data == 'tg_admin':
                bot.send_message(call.message.chat.id, '😎Telgram нашего админа: @tagirisan.💥')

            if call.data == 'vk_group':
                bot.send_message(call.message.chat.id, '🤤Наш паблик в VK: https://vk.com/remake_it_bot 💥')

            if call.data == 'vk_admin':
                bot.send_message(call.message.chat.id, '😎VK нашего админа: https://vk.com/tagirisan 💥')

        if call.message:
            if call.data == 'get_vk_link':
                bot.send_message(call.message.chat.id, '🤤Наш паблик в VK: https://vk.com/remake_it_bot 💥')

        if call.message:
            if call.data == 'work_us':
                work = types.InlineKeyboardMarkup(row_width=1)

                work_programmist = types.InlineKeyboardButton('Программистом', callback_data = 'work_programmist')
                work_targetolog = types.InlineKeyboardButton('Таргетологом', callback_data = 'work_targetolog')

                work.add(work_programmist, work_targetolog)

                bot.send_message(call.message.chat.id, '🤔Кем ты хочешь работать?', reply_markup=work)

        if call.message:
            if call.data == 'work_programmist':
                programm_contiue = types.InlineKeyboardMarkup(row_width=2)
                programm1 = types.InlineKeyboardButton('Далее', callback_data='programm1')

                programm_contiue.add(programm1)
                bot.send_message(call.message.chat.id, '''🤩Хочешь работать в нашем сообществе?🤩
😝Перед тем как присоединиться к нам, ответь себе на несколько вопросов😝:
~~~~✅Умеешь ли ты писать ботов для телеграма/вконтакте?
~~~~✅Готов ли ты работать на постоянке?
~~~~✅Сумеешь ли выполнять заказы в срок?
~~~~✅Умеешь деплоить ботов на сервер?
~~~~✅Есть ли у тебя портфолио с задеплоинными ботами?

😎Итоги:
~~~~😏Если на все вопросы ты ответил да или умею, то поздравляю, переходи к следующему шагу.🤗
''', reply_markup=programm_contiue)

        if call.message:
            if call.data == 'programm1':
                bot.send_message(call.message.chat.id, '''🤓Теперь напиши сообщение для админа.🤓
😏Перед текстом сообщения впишите /programmist.
👨‍💻После проверки он прочитает твое сообщение. Если ты сумеешь его заинтересовать, он обязательно даст знать:))''')


        if call.message:
            if call.data == 'work_targetolog':
                target_button = types.InlineKeyboardMarkup(row_width=2)
                target_button1 = types.InlineKeyboardButton('Даллее', callback_data = 'target1')
                target_button.add(target_button1)
                bot.send_message(call.message.chat.id, '''🤩Хочешь работать в нашем сообществе?🤩
😝Перед тем как присоединиться к нам, ответь себе на несколько вопросов😝:
~~~~✅Умеешь ли ты привлекать новых клиентов?
~~~~✅Умеешь ли ты продвигать сообщество?
~~~~✅Умеешь ли ты писать красивые посты?
~~~~✅Готов ли ты работать на постоянке?

😎Итоги:
~~~~😏Если на все вопросы ты ответил да или умею, то поздравляю, переходи к следующему шагу.🤗''', reply_markup=target_button)

        if call.message:
            if call.data == 'target1':
                bot.send_message(call.message.chat.id, '''🤓Теперь напиши сообщение для админа.🤓
😏Перед текстом сообщения впишите /targetolog.
👨‍💻После проверки он его прочитает. Если ты сумеешь его заинтересовать, он обязательно даст знать:))''')



bot.polling()
