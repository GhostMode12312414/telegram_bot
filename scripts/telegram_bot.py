import asyncio
from aiogram import Bot, types
from aiogram.types import InputFile
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InputFile
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile

bot = Bot(token='7970424106:AAGt_99D7xo52pY8dcRcWrddNQXLhirhYkI')
dp = Dispatcher()



@dp.message(CommandStart())
async def greeting(message: types.Message):

    """
    Что делает функция:
        1) Функция приветствует игрока, отправляет фото
        2) Функция погружает игрока в правила игры
        
    Порядок выполнения функции:
        1) Создается переменная text, в которой хранится приветствие и правила игры
        2) Создается переменная name_player, в которой мы узнаем юзернейм игрока
        3) Создается переменная photo с путем к фото
        4) И с помощью answer_photo все соединяется в одно и отправляется пользователю
    """

    text = '''Меня зовут Стив.\n
Я — последний выживший из Сектора 13,
сейчас Ночной Город балансирует на 
грани хаоса, «Инквизиторы» - группировка, превращающая людей в биороботов.\n
Ты — наша последняя надежда.\n
Твоя задача — дойти в их главно командующее здание и найти центральный узел...'''
    name_player =  message.from_user.username
    photo = FSInputFile(r"C:\Users\valera\Desktop\bot\photo\Основной персонаж.jpg")
    await message.answer_photo(photo, caption=f'Приветствую {name_player}, {text}')
    




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())  # Правильный способ запуска асинхронного кода