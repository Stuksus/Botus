import telebot
import re

token = ""
bot = telebot.TeleBot(token)
slovar = ['БЛИН','БЛЕИН']
endText = ''
test_grup = ['-308755034']


@bot.message_handler(content_types=["text"])
def handel_text(message):

    flag = False

    messageId = message.message_id
    chatId = message.chat.id
    firs_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    text = message.text
    text = text.upper()
    for i in range(0,len(test_grup)):
        if username == test_grup[i]:
            print("Этот пользователь уже есть в записях")
        else:
            test_grup.append(username)

    p2 = re.compile(r'(\W+)')
    result = p2.split(text)
    print(result)
    longRes = len(result)
    messageText = [firs_name,last_name,'(',username,')','отправил: ']
    if messageText[1]== None:
        messageText.pop(1)

    for i in range(0, longRes):
        for j in range(0, len(slovar)):
            if result[i] == slovar[j]:
                result[i] = 'фунтик'
                flag = True
                print('Сообщение удалено')
    if flag == True:
       messageText.extend(result)
       endText = ' '.join(messageText)
       endText = endText.lower()
       bot.send_message(chatId, endText)
       bot.delete_message(chatId, messageId)



bot.polling(none_stop = True, interval=0)