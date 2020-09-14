import telepot
token = '1311289571:AAGJOWN-z5jKzJvJjhzF2u1jI6eRhHMlc7E'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe()) 
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)
