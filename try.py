import telebot
import re
import function
globalC = ['localhost','rooting','123123','bot','utf8mb4']
token = ""
bot = telebot.TeleBot(token)
slovar = ['БЛЯДЬ','БЛЯТЬ','ЕБАТЬ','ЕБАЛ','ХУЙ','ЧЛЕН','ПИЗДА','ЕБАНЫЙ','ПИЗДЕЦ','СУЧИЙ','АХУЕ','ВПАДЛУ','ХЕР','ХРЕН','НАБУХАЛАСЬ','СПИЗДНУТЬ','НАЕБЕНИТЬСЯ','ГИТЛЕР','НАХУЙ','ЖОПА','БЛЯ','СУКА','БЛЯЯ','ОТПИЗДИТЬ','ПИЗДИТЬ','ОТПИЗЖУ','ПИЗДИЛИ','ПОПИЗЖУ','СПИЗДИЛИ','НАФИГ','ЗАЕБИСЬ','БЛИН','ПРИКОЛ','БЛЕИН']
endText = ''



@bot.message_handler(content_types=["text"])
def handel_text(message):

    badWord = 0
    flag = False
    memberId = False
    messageId = message.message_id
    chatId = message.chat.id
    firs_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    userId = message.from_user.id
    text = message.text
    text = text.upper()
    p2 = re.compile(r'(\W+)')
    result = p2.split(text)
    print(result)
    allWord = re.findall(r'\w+',text)
    print(allWord)
    countWord = len(allWord)
    print(countWord)
    longRes = len(result)

    messageText = [firs_name,last_name,'(',username,')','отправил: ']
    if messageText[0]== None:
        messageText.pop(0)
    if messageText[1]== None:
        messageText.pop(1)
    if messageText[2]== None:
        messageText.pop(2)
    if messageText[3]== None:
        messageText.pop(3)
    for i in range(0, longRes):
        for j in range(0, len(slovar)):
            if result[i] == slovar[j]:
                result[i] = 'фунтик'
                badWord +=1
                flag = True

    if flag == True:
       result2 = ' '.join(result)
       result2 =result2.lower()
       endText = ' '.join(messageText)
       endText2 = endText + ' '+ result2
       bot.send_message(chatId, endText2)
       bot.delete_message(chatId, messageId)
       print('Сообщение удалено')




    idUser = function.selectColumnDB(globalC,'idUser')
    goodWord = countWord - badWord
    print(idUser)
    print(len(idUser))
    print(countWord)
    print(badWord)
    print(userId)
    print(goodWord)
    for i in range(0, len(idUser)):
        print(idUser[i]["idUser"])
        if userId != idUser[i]["idUser"]:
            memberId = True
        else:
            memberId = False
            break

    if memberId == False:

        function.update(globalC,str(userId),str(username),str(countWord),str(badWord),str(goodWord))
        print("Этот пользователь уже есть в записях")
    else:
        stat =(badWord/countWord)*100
        args = [(str(userId), str(username), str(countWord), str(badWord), str(goodWord), str(int(stat)))]
        print(args)
        tets = function.insertDB(globalC,args)
        print(tets)


bot.polling(none_stop = True, interval=0)