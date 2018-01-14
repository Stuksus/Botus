import telebot
import re
token = ""
bot = telebot.TeleBot(token)
slovar = ['БЛИН','БЛЕИН']
locat = []
endText = ''
messageText = []
result = []

#[;,.\s(\w+)]for g in range(0, len(delen[i])):
   # if delen[i][g] == ',' or '.' or '!' or '?':  # заменить на регулярки for g in range(0,len(delen[i])):
          #  if delen[i][g] == ',' or '.' or '!' or '?': #заменить на регулярки

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
    delen =text.split(' ')
    print(text)
    print(delen)

    p2 = re.compile(r'(\W+)')
    result = p2.split(text)
    print(result)
  #  delenWithOut = text.split(',')
    longRes = len(result)
    longSpace = len(text.split(' '))
   # longWithOut =len(text.split(','))
    messageText = [firs_name,last_name,'(',username,')','отправил: ']
    if messageText[1]== None:
        messageText.pop(1)

    for i in range(0, longRes):

        #result= re.findall(r'(\W+)',text)

        for j in range(0, len(slovar)):
            if result[i] == slovar[j]:
                result[i] = 'фунтик'
                flag = True
                print('Сообщение удалено')
    if flag == True:
       messageText.extend(result)
       endText = ' '.join(messageText)
       bot.send_message(chatId, endText)
       bot.delete_message(chatId, messageId)

#посичтить листы в конце

bot.polling(none_stop = True, interval=0)
