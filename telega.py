from telebot import *
from random import *
bot = TeleBot('')
alll_pp = [
    [['.','.'], ['.','.'],['.','.']],
    [['.','.'],['.','.'],['.','.']],
    [['.','.'],['.','.'],['.','.']],
    [['.','.'],['.','.'],['.','.']],
    [['.','.'],['.','.'],['.','.']]
    ]
rl = [['.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.']]
uz = []
# pp = ['. .','. .','. .','. .','. .','. .','. .','. .','. .','. .','. .','. .','. .']
with open('3.txt','r') as f:
    r1 = f.read()
r1 = r1.split(',')
for i in range(3):
    r1.append(r1[i].split(' '))
for i in range(3):
    r1.pop(0)
print(r1)
with open('4.txt','r') as f:
    r2 = f.read()
r2 = r2.split('\n')
with open('id.txt','r') as f:
    ids = f.read()
ids = ids.split('\n')
for i in range(len(ids)):
    ids.append(ids[i].split(' '))
    ids[-1][1] = int(ids[-1][1])
for i in range(len(ids) // 2):
    ids.pop(0)
idds = []
for i in range(len(ids)):
    idds.append(ids[i][1])
print(idds)
# print(ids)
# print(alll_pp)
@bot.message_handler(commands=['id'])
def id(message):
    print(message.chat.id)
    bot.send_message(542387853,message.chat.id)
alk = 542387853
@bot.message_handler(commands=['a'])
def a(message):
    if message.chat.id == 542387853:
        global alk
        if alk == 542387853:
            alk = 1
        else:
            alk = 542387853
@bot.message_handler(commands=['start'])
def default_test(message):
    global alk
    if message.chat.id > 0:
        if message.chat.id == alk:
            print(uz)
            keyboard = types.InlineKeyboardMarkup(row_width=3)
            btn1 = types.InlineKeyboardButton(text='Посмотреть', callback_data ='button1')
            btn2 = types.InlineKeyboardButton(text='Выбрать', callback_data ='button2')
            btn3 = types.InlineKeyboardButton(text='Отправить', callback_data ='button3')
            btn4 = types.InlineKeyboardButton(text='Генерируем', callback_data ='button4')
            btn5 = types.InlineKeyboardButton(text='Смотреть', callback_data ='button5')
            btn6 = types.InlineKeyboardButton(text='Смena', callback_data ='button6')
            btn7 = types.InlineKeyboardButton(text='save', callback_data ='sav')
            keyboard.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7)
            bot.send_message(message.chat.id, '1',reply_markup = keyboard)
            print(1)
            # for i in range(len(all)):
            #     if message.chat.first_name in all[i]:
            #         bot.send_message(542387853, str(message.chat.id) + '  ' + message.chat.first_name)
            # print(message.chat.id, message.chat.first_name)
        elif message.chat.id in uz and message.chat.id in idds:
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton(text='Посмотреть (В горизонт.положении)', callback_data ='button1')
            keyboard.add(btn1)
            bot.send_message(message.chat.id, 'Выберите дейтвие для россадки',reply_markup = keyboard)
        elif message.chat.id in idds:
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton(text='Посмотреть (В горизонт.положении)', callback_data ='button1')
            btn2 = types.InlineKeyboardButton(text='Выбрать', callback_data ='button2')
            print(message.chat.first_name,message.chat.id)
            keyboard.add(btn1,btn2)
            bot.send_message(message.chat.id, 'Выберите дейтвие для россадки. \n Для правильного отображения при просмотре поверните телефон в горизонтальное положение',reply_markup = keyboard)
@bot.callback_query_handler(func=lambda c: c.data == 'button6')
def proces(callback_query: types.CallbackQuery):
    while 1:
        for i in range(len(ids)):
            if ids[i][1] == 542387853:
                ids[i][1] = 1
        i = randint(0,len(ids) - 1)
        if ids[i][1] != 542387853:
            ids[i][1] = 542387853
            bot.send_message(542387853, ids[i][0])
            break
@bot.callback_query_handler(func=lambda c: c.data == 'button1')
def process_callback_button1(callback_query: types.CallbackQuery):
    # prob = ' '
    # s = '.   I' + prob *40 + 'II' + prob * 40 + 'III\n' + '5. ' + alll_pp[0][0][0]  + prob * (30 - len(alll_pp[0][0][0])) + alll_pp[0][1][0]  + prob * (30 - len(alll_pp[0][1][0])) + alll_pp[0][2][0] + '\n' + '    ' + alll_pp[0][0][1] + prob * (30 - len(alll_pp[0][0][1]))  + alll_pp[0][1][1] + prob * (30 - len(alll_pp[0][1][1]))  + alll_pp[0][2][1] + '\n' '4. ' + alll_pp[1][0][0] + prob * (30 - len(alll_pp[1][0][0])) + alll_pp[1][1][0] +  prob * (30 - len(alll_pp[1][1][0])) + alll_pp[1][2][0] + '\n'
    # s += '    ' + alll_pp[1][0][1] + prob * (30 - len(alll_pp[1][0][1])) + alll_pp[1][1][1] + prob * (30 - len(alll_pp[1][0][1])) + alll_pp[1][2][1] + '\n' '3. ' + alll_pp[2][0][0]  + prob * (30 - len(alll_pp[2][0][0]))+ alll_pp[2][1][0]  + prob * (30 - len(alll_pp[2][1][0])) + alll_pp[2][2][0]  +'\n'+ '    '+ alll_pp[2][0][1] + prob * (30 - len(alll_pp[2][0][1])) + alll_pp[2][1][1] + prob * (30 - len(alll_pp[2][1][1])) + alll_pp[2][2][1] + prob * (30 - len(alll_pp[2][2][1])) + '\n'
    # s += '2. ' + alll_pp[3][0][0] + prob * (30 - len(alll_pp[3][0][0])) + alll_pp[3][1][0]  + prob * (30 - len(alll_pp[3][1][0])) + alll_pp[3][2][0] +'\n' + '    ' + alll_pp[3][0][1] + prob * (30 - len(alll_pp[3][0][1])) + alll_pp[3][1][1] + prob * (30 - len(alll_pp[3][1][1])) + alll_pp[3][2][1] + '\n'
    # s += '1. ' + alll_pp[4][0][0] + prob * (30 - len(alll_pp[4][0][0])) + alll_pp[4][1][0] + prob * (30 - len(alll_pp[4][1][0])) + alll_pp[4][2][0] + '\n' + '    ' + alll_pp[4][0][1] + prob * (30 - len(alll_pp[4][0][1])) + alll_pp[4][1][1] + prob * (30 - len(alll_pp[4][1][1])) + alll_pp[4][2][1]
    # bot.answer_callback_query(callback_query.id)
    n = 5
    a = '.    1                                         2                                         3\n'
    p = '                                         '
    for i in range(5):
        a += str(n) + '  '
        a += alll_pp[i][0][0]+ p + alll_pp[i][1][0]+ p + alll_pp[i][2][0]
        a += '\n    '
        a += alll_pp[i][0][1]+ p + alll_pp[i][1][1]+ p + alll_pp[i][2][1]
        a += '\n'
        n -= 1
    bot.send_message(callback_query.message.chat.id, a)
@bot.callback_query_handler(func=lambda c: c.data == 'sav')
def save(callback_query: types.CallbackQuery):
    n = 5
    a = '.    1                                         2                                         3\n'
    p = '                                         '
    for i in range(5):
        a += str(n) + '  '
        a += alll_pp[i][0][0]+ p + alll_pp[i][1][0]+ p + alll_pp[i][2][0]
        a += '\n    '
        a += alll_pp[i][0][1]+ p + alll_pp[i][1][1]+ p + alll_pp[i][2][1]
        a += '\n'
        n -= 1
    with open('r.txt','w') as f:
        f.write(a)
@bot.callback_query_handler(func=lambda c: c.data == 'button2')
def process_callback_button2(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton(text='1',callback_data = 'r1')
        btn2 = types.InlineKeyboardButton(text='2',callback_data = 'r2')
        btn3 = types.InlineKeyboardButton(text='3',callback_data = 'r3')
        keyboard.add(btn1,btn2,btn3)
        bot.send_message(callback_query.message.chat.id, 'Выберите ряд(1 - ряд у двери)',reply_markup = keyboard)
    else:
        bot.send_message(callback_query.message.chat.id, 'Вы уже выбрали свое место')
@bot.callback_query_handler(func=lambda c: c.data == 'r1')
def r11(callback_query: types.CallbackQuery):
    for i in range(len(ids)):
        if callback_query.message.chat.id in ids[i]:
            name = ids[i][0]
    if name not in r1[0]:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='1',callback_data = 'p11')
        btn2 = types.InlineKeyboardButton(text='2',callback_data = 'p12')
        btn3 = types.InlineKeyboardButton(text='3',callback_data = 'p13')
        keyboard.add(btn3,btn2,btn1)
        bot.send_message(callback_query.message.chat.id, 'Выберите парту',reply_markup = keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton(text='1',callback_data = 'r1')
        btn2 = types.InlineKeyboardButton(text='2',callback_data = 'r2')
        btn3 = types.InlineKeyboardButton(text='3',callback_data = 'r3')
        keyboard.add(btn1,btn2,btn3)
        bot.send_message(callback_query.message.chat.id, 'Выберите другой ряд(1 - ряд у двери)',reply_markup = keyboard)
@bot.callback_query_handler(func=lambda c: c.data == 'p11')
def p11(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[4][0][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[4][0][0] == '.' or alll_pp[4][0][1] == '.':
            if flag:
                flag = False
                for i in range(6):
                    if rl[0][i] == '.':
                        rl[0][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[4][0][1] == '.':
                        alll_pp[4][0][1] = name
                    else:
                        alll_pp[4][0][0] = name
                    print(rl)
                    print(alll_pp)
                    uz.append(callback_query.message.chat.id)
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p12')
def p12(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[3][0][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[3][0][0] == '.' or alll_pp[3][0][1] == '.':
            if flag:
                flag = False
                for i in range(6):
                    if rl[0][i] == '.':
                        rl[0][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[3][0][1] == '.':
                        alll_pp[3][0][1] = name
                    else:
                        alll_pp[3][0][0] = name
                    print(rl)
                    print(alll_pp)
                    uz.append(callback_query.message.chat.id)
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p13')
def p13(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[2][0][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[2][0][0] == '.' or alll_pp[2][0][1] == '.':
            if flag:
                flag = False
                for i in range(6):
                    if rl[0][i] == '.':
                        rl[0][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[2][0][1] == '.':
                        alll_pp[2][0][1] = name
                    else:
                        alll_pp[2][0][0] = name
                    print(rl)
                    print(alll_pp)
                    uz.append(callback_query.message.chat.id)
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'r2')
def r12(callback_query: types.CallbackQuery):
    
    for i in range(len(ids)):
        if callback_query.message.chat.id in ids[i]:
            name = ids[i][0]
    if name not in r1[1]:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='1',callback_data = 'p21')
        btn2 = types.InlineKeyboardButton(text='2',callback_data = 'p22')
        btn3 = types.InlineKeyboardButton(text='3',callback_data = 'p23')
        btn4 = types.InlineKeyboardButton(text='4',callback_data = 'p24')
        btn5 = types.InlineKeyboardButton(text='5',callback_data = 'p25')
        keyboard.add(btn5,btn4,btn3,btn2,btn1)
        bot.send_message(callback_query.message.chat.id, 'Выберите парту',reply_markup = keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton(text='1',callback_data = 'r1')
        btn2 = types.InlineKeyboardButton(text='2',callback_data = 'r2')
        btn3 = types.InlineKeyboardButton(text='3',callback_data = 'r3')
        keyboard.add(btn1,btn2,btn3)
        bot.send_message(callback_query.message.chat.id, 'Выберите другой ряд(1 - ряд у двери)',reply_markup = keyboard)
# -------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda c: c.data == 'p21')
def p21(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[4][1][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[4][1][0] == '.' or alll_pp[4][1][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[1][i] == '.':
                        rl[1][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[4][1][1] == '.':
                        alll_pp[4][1][1] = name
                    else:
                        alll_pp[4][1][0] = name
                    uz.append(callback_query.message.chat.id)
                    
                    
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p22')
def p22(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[3][1][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[3][1][0] == '.' or alll_pp[3][1][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[1][i] == '.':
                        rl[1][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[3][1][1] == '.':
                        alll_pp[3][1][1] = name
                    else:
                        alll_pp[3][1][0] = name
                    uz.append(callback_query.message.chat.id)
                print(rl)
                print(alll_pp)    
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p23')
def p23(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[2][1][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[2][1][0] == '.' or alll_pp[2][1][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[1][i] == '.':
                        rl[1][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[2][1][1] == '.':
                        alll_pp[2][1][1] = name
                    else:
                        alll_pp[2][1][0] = name
                    uz.append(callback_query.message.chat.id)
                print(rl)
                print(alll_pp)       
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p24')
def p24(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[1][1][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[1][1][0] == '.' or alll_pp[1][1][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[1][i] == '.':
                        rl[1][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[1][1][1] == '.':
                        alll_pp[1][1][1] = name
                    else:
                        alll_pp[1][1][0] = name
                    uz.append(callback_query.message.chat.id)
                    
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p25')
def p25(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[0][1][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[0][1][0] == '.' or alll_pp[0][1][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[1][i] == '.':
                        rl[1][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[0][1][1] == '.':
                        alll_pp[0][1][1] = name
                    else:
                        alll_pp[0][1][0] = name
                    uz.append(callback_query.message.chat.id)
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')

# -------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda c: c.data == 'r3')
def r13(callback_query: types.CallbackQuery):
    for i in range(len(ids)):
        if callback_query.message.chat.id in ids[i]:
            name = ids[i][0]
    if name not in r1[2]:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='1',callback_data = 'p31')
        btn2 = types.InlineKeyboardButton(text='2',callback_data = 'p32')
        btn3 = types.InlineKeyboardButton(text='3',callback_data = 'p33')
        btn4 = types.InlineKeyboardButton(text='4',callback_data = 'p34')
        btn5 = types.InlineKeyboardButton(text='5',callback_data = 'p35')
        keyboard.add(btn5,btn4,btn3,btn2,btn1)
        bot.send_message(callback_query.message.chat.id, 'Выберите парту',reply_markup = keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton(text='1',callback_data = 'r1')
        btn2 = types.InlineKeyboardButton(text='2',callback_data = 'r2')
        btn3 = types.InlineKeyboardButton(text='3',callback_data = 'r3')
        keyboard.add(btn1,btn2,btn3)
        bot.send_message(callback_query.message.chat.id, 'Выберите другой ряд(1 - ряд у двери)',reply_markup = keyboard)
# ----------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda c: c.data == 'p31')
def p31(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[4][2][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[4][2][0] == '.' or alll_pp[4][2][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[2][i] == '.':
                        rl[2][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[4][2][1] == '.':
                        alll_pp[4][2][1] = name
                    else:
                        alll_pp[4][2][0] = name
                    uz.append(callback_query.message.chat.id)
                    
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p32')
def p32(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[3][2][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[3][2][0] == '.' or alll_pp[3][2][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[2][i] == '.':
                        rl[2][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[3][2][1] == '.':
                        alll_pp[3][2][1] = name
                    else:
                        alll_pp[3][2][0] = name
                    uz.append(callback_query.message.chat.id)
                print(rl)
                print(alll_pp)    
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p33')
def p33(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[2][2][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[2][2][0] == '.' or alll_pp[2][2][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[2][i] == '.':
                        rl[2][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[2][2][1] == '.':
                        alll_pp[2][2][1] = name
                    else:
                        alll_pp[2][2][0] = name
                    uz.append(callback_query.message.chat.id)
                print(rl)
                print(alll_pp)       
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p34')
def p34(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[1][2][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[1][2][0] == '.' or alll_pp[1][2][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[2][i] == '.':
                        rl[2][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[1][2][1] == '.':
                        alll_pp[1][2][1] = name
                    else:
                        alll_pp[1][2][0] = name
                    uz.append(callback_query.message.chat.id)
                    
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
@bot.callback_query_handler(func=lambda c: c.data == 'p35')
def p35(callback_query: types.CallbackQuery):
    if callback_query.message.chat.id not in uz:
        for i in range(len(ids)):
            if ids[i][1] == callback_query.message.chat.id:
                name = ids[i][0]
        for i in range(len(r2)):
            if name in r2[i]:
                name2 = r2[i].split(' ')
                if name == name2[0]:
                    name2 = name2[1]
                else:
                    name2 = name2[0]
                if name2 == '.':
                    name2 = None
        flag = True
        for i in range(2):
            if alll_pp[0][2][i] != name2:
                pass
            else:
                bot.send_message(callback_query.message.chat.id,'Поменяйте соседа')
                flag = False
        if alll_pp[0][2][0] == '.' or alll_pp[0][2][1] == '.':
            if flag:
                flag = False
                for i in range(10):
                    if rl[2][i] == '.':
                        rl[2][i] = name
                        flag = True
                        break
                if flag:
                    if alll_pp[0][2][1] == '.':
                        alll_pp[0][2][1] = name
                    else:
                        alll_pp[0][2][0] = name
                    uz.append(callback_query.message.chat.id)
        else:
            bot.send_message(callback_query.message.chat.id,'Парта занята')
# --------------------------------------------------------------------------------------------------------
strs = []
@bot.callback_query_handler(func=lambda c: c.data == 'button4')
def process_callback_button4(callback_query: types.CallbackQuery):
    with open('1.txt','r') as file:
        ss = file.read()
    ss = ss.split(' ')
    sks = []
    strr = ''
    strs = []
    for i in range(5):
        for j in range(3):
            a = randint(0,len(ss) - 1)
            sks.append(ss[a])
            strr += ss[a]
            if j < 2:
                strr += ', '
            ss.pop(a)
        
        strs.append(strr)
        strr = ''
    with open('2.txt','w') as f:
        for i in range(len(strs)):
            f.write(strs[i] + '\n')
@bot.callback_query_handler(func=lambda c: c.data == 'button3')
def gg(callback_query: types.CallbackQuery):
    with open('2.txt','r') as f:
        ak = f.read()
        ak = ak.split('\n')
        re = ''
        re += 'Понеділок:' + ak[0] + '\n'
        re += 'Вівторок:' + ak[1] + '\n'
        re += 'Середа:' + ak[2] + '\n'
        re += 'Четвер:' + ak[3] + '\n'
        re += "П'ятниця:" + ak[4] + '\n'
    bot.send_message(-1001321048197,re)
# @bot.message_handler(commands=['gg'])
# def gg(message):
#     with open('2.txt','r') as f:
#         ak = f.read()
#         ak = ak.split('\n')
#         re = ''
#         re += 'Понеділок:' + ak[0] + '\n'
#         re += 'Вівторок:' + ak[1] + '\n'
#         re += 'Середа:' + ak[2] + '\n'
#         re += 'Четвер:' + ak[3] + '\n'
#         re += "П'ятниця:" + ak[4] + '\n'
#     bot.send_message(-1001321048197,re)
@bot.callback_query_handler(func=lambda c: c.data == 'button5')
def gg1(callback_query: types.CallbackQuery):
    with open('2.txt','r') as f:
        ak = f.read()
        ak = ak.split('\n')
        re = ''
        re += 'Понеділок:' + ak[0] + '\n'
        re += 'Вівторок:' + ak[1] + '\n'
        re += 'Середа:' + ak[2] + '\n'
        re += 'Четвер:' + ak[3] + '\n'
        re += "П'ятниця:" + ak[4] + '\n'
    bot.send_message(542387853,re)
# @bot.message_handler(commands=['phone'])
# def get_phone(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     btn2 = types.KeyboardButton(text = 'Телефон', request_contact = True)
#     keyboard.add(btn2)
#     bot.send_message(message.chat.id, '12312', reply_markup = keyboard)        
#     keyboard = types.ReplyKeyboardRemove() 


bot.polling(none_stop=True)