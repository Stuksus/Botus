import telebot
token = "489178856:AAFWlsgZCc-uh_em5e4v-wsLAoP8vX29V44"
bot = telebot.TeleBot(token)
slovar = ['БЛЯДЬ','БЛЯТЬ','ЕБАТЬ','ХУЙ','ЧЛЕН','ПИЗДА','НАХУЙ','ЖОПА','БЛЯ','СУКА','БЛЯЯ','ОТПИЗДИТЬ','ПИЗДИТЬ','ОТПИЗЖУ','ПИЗДИЛИ','ПОПИЗЖУ','СПИЗДИЛИ','НАФИГ','ЗАЕБИСЬ','БЛИН','БЛЕИН']
endText = ''

# print(messageId)
# print(chatId)
# print(message)
# print(text)
# print(len(text.split(' ')))
@bot.message_handler(content_types=["text"])
def handel_text(message):
    messageId = message.message_id
    chatId = message.chat.id
    text = message.text
    text = text.upper()
    delen =text.split(' ')
    delenWithOut = text.split(',')
    longSpace = len(text.split(' '))
    longWithOut =len(text.split(','))
    if longWithOut > longSpace:
        for i in range(0, longWithOut):
            for j in range(0, len(slovar)):
                if delenWithOut[i] == slovar[j]:
                    delenWithOut[i]= 'фунтик'
                    endText = ' '.join(delenWithOut)
                    bot.send_message(chatId,endText)
                    bot.delete_message(chatId, messageId)

                    print('Сообщение удалено')
    else:
        for i in range(0, longSpace):
            for j in range(0, len(slovar)):
                if delen[i] == slovar[j]:
                    bot.delete_message(chatId, messageId)
                    print('Сообщение удалено')




bot.polling(none_stop = True, interval=0)