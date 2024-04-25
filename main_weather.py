import requests
import datetime
from pprint import pprint
from config import btoken, token
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import main as btn

bot = Bot(token=btoken)
dp = Dispatcher(bot=bot)
lst = ['❓Информация❓', 'Главное меню⬅️', 'Другое➡️', '❓Как использовать?❓', '💸Поддержать💸', '🗺Города🗺']
citys = ['Стерлитамак', 'Уфа', 'Баймак', 'Белебей', 'Белорецк', 'Благвещенск', "Ишимбай", 'Кумертау', 'Мелеуз',
         'Нефтекамск', 'Октябрьский', 'Салават', 'Сибай', 'Туймазы']


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку о погоде!", reply_markup=btn.mainMenu)


@dp.message_handler()
async def get_weather(message: types.Message):
    if message.text == '❓Информация❓':
        await bot.send_message(message.from_user.id,
                               f'Этот бот создан для того чтобы Пользователи могли удобно узнать:\n'
                               f'Погоду\nТемперату\nВлажность воздуха\nДавление\nСкорость ветра\n'
                               f'Восход и закат солнца\nДлительность светового дня!')

    elif message.text == 'Главное меню⬅️':
        await bot.send_message(message.from_user.id, 'Главное меню⬅️', reply_markup=btn.mainMenu)

    elif message.text == 'Другое➡️':
        await bot.send_message(message.from_user.id, 'Другое➡️', reply_markup=btn.otherMenu)

    elif message.text == '❓Как использовать?❓':
        await bot.send_message(message.from_user.id,
                               f'Чтобы использовать бота нужно отправить название города на любом языке\n'
                               'Например: Москва\n'
                               'Или же вы можете выбрать город из списка\n(Пока что доступны только города Башкирии)')
    elif message.text == '💸Поддержать💸':
        await bot.send_message(message.from_user.id, f'Поддержать автора: https://www.donationalerts.com/r/dj_dominat')

    elif message.text == '🗺Города🗺':
        await bot.send_message(message.from_user.id, '🗺Города🗺', reply_markup=btn.cityMenu)

    smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_temp = data["main"]["temp"]
        country = data["sys"]["country"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        feel = data["main"]["feels_like"]

        weather = data["weather"][0]["main"]
        if weather in smile:
            wd = smile[weather]
        else:
            wd = 'Не пойму что за погода такая...'
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenth_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        if message.text == 'Стерлитамак':
            file = open('str.jpg', 'rb')
        elif message.text == 'Уфа':
            file = open('ufa.png', 'rb')
        elif message.text == 'Баймак':
            file = open('bay.png', 'rb')
        elif message.text == 'Белебей':
            file = open('bele.png', 'rb')
        elif message.text == 'Белорецк':
            file = open('belorec.png', 'rb')
        elif message.text == 'Благвещенск':
            file = open('blag.png', 'rb')
        elif message.text == 'Ишимбай':
            file = open('ish.jpg', 'rb')
        elif message.text == 'Кумертау':
            file = open('kum.png', 'rb')
        elif message.text == 'Мелеуз':
            file = open('mel.png', 'rb')
        elif message.text == 'Нефтекамск':
            file = open('Neftekamsk.jpg', 'rb')
        elif message.text == 'Октябрьский':
            file = open('okt.png', 'rb')
        elif message.text == 'Салават':
            file = open('salavat.png', 'rb')
        elif message.text == 'Сибай':
            file = open('sib.jpg', 'rb')
        elif message.text == 'Туймазы':
            file = open('tyi.png', 'rb')

        if message.text in citys:
            await bot.send_photo(message.chat.id, file,
                                 f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}***\n"
                                 f"Погода в {city}, {country}\nТемпература: {cur_temp}C \n{wd}\n"
                                 f"Ощущается как: {feel}C\n"
                                 f"Влажность воздуха: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind_speed} м/с\n"
                                 f"Восход солнце: {sunrise_time}\nЗакат: {sunset_time}\nСветовой день: {lenth_of_day}\n"
                                 f"***Хорошего дня!***")
        else:
            await bot.send_message(message.from_user.id,
                                   f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}***\n"
                                   f"Погода в {city}, {country}\nТемпература: {cur_temp}C \n{wd}\n"
                                   f"Ощущается как: {feel}C\n"
                                   f"Влажность воздуха: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind_speed} м/с\n"
                                   f"Восход солнце: {sunrise_time}\nЗакат: {sunset_time}\nСветовой день: {lenth_of_day}\n"
                                   f"***Хорошего дня!***")

    except:
        if message.text not in lst:
            await message.reply('\U00002620 Проверьте название города \U00002620')


if __name__ == "__main__":
    executor.start_polling(dp)
