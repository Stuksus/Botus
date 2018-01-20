import telebot
import re
import function
globalS = ['localhost','rooting','123123','bot','utf8mb4']
token = ""
bot = telebot.TeleBot(token)
slovar = ['БЛИН','БЛЕИН']
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
    if messageText[1]== None:
        messageText.pop(1)
    for i in range(0, longRes):
        for j in range(0, len(slovar)):
            if result[i] == slovar[j]:
                result[i] = 'фунтик'
                badWord +=1
                flag = True
                print('Сообщение удалено')
    if flag == True:
       result2 = ' '.join(result)
       result2 =result2.lower()
       endText = ' '.join(messageText)
       endText2 = endText + ' '+ result2
       bot.send_message(chatId, endText2)
       bot.delete_message(chatId, messageId)
    idUser = function.selectColumnDB(globalS,'idUser')
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

    if memberId == False:
        print("Этот пользователь уже есть в записях")
    else:
        stat =(badWord/countWord)*100
        args = [(str(userId), str(username), str(countWord), str(goodWord), str(badWord), str(int(stat)))]
        print(args)
        tets = function.insertDB(globalS,args)
        print(tets)


bot.polling(none_stop = True, interval=0)