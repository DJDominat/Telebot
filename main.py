from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton('Главное меню⬅️')

# Main-Menu
btnInfo = KeyboardButton('❓Информация❓')
btnOther = KeyboardButton('Другое➡️')
btnCity = KeyboardButton('🗺Города🗺')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnOther, btnCity)


# Other Menu
btnInfo = KeyboardButton('❓Как использовать?❓')
btnSupport = KeyboardButton('💸Поддержать💸')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnSupport, btnMain)

#City Menu
btnStr = KeyboardButton('Стерлитамак')
btnUfa = KeyboardButton('Уфа')
btnBay = KeyboardButton('Баймак')
btnBele = KeyboardButton('Белебей')
btnBelorec = KeyboardButton('Белорецк')
btnBlag = KeyboardButton('Благвещенск')
btnIsh = KeyboardButton("Ишимбай")
btnKum = KeyboardButton('Кумертау')
btnMel = KeyboardButton('Мелеуз')
btnNeft = KeyboardButton('Нефтекамск')
btnOkt = KeyboardButton('Октябрьский')
btnSalav = KeyboardButton('Салават')
btnSib = KeyboardButton('Сибай')
btnTyi = KeyboardButton('Туймазы')
cityMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStr, btnUfa, btnBay, btnBele, btnBelorec, btnBlag, btnIsh, btnKum, btnMel, btnNeft, btnOkt, btnSalav, btnSib, btnTyi, btnMain)