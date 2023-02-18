"""

This is a echo bot.


It echoes any incoming text messages.

"""

import logging
from checkWord import checkWord

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5698464249:AAEE5vhMaXy5sBgq4RNRj453ac-b9qPYGcc'

# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Uz_imlo Botiga Xush Kelibsiz!")


@dp.message_handler(commands=['help'])
async def sendWiki(message: types.Message):
    await message.answer("Botdan foydalanish uchun so'z yuboring")


@dp.message_handler()
async def sendWiki(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅{text.capitalize()}\n"
    await message.answer(response)
    
if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
