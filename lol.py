import logging
import os

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'TYPE HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['ping'])
async def send_pong(message: types.Message):
    pong=""
    hostname='VDS IP HERE'
    response = os.system('ping -c 5 ' + hostname)
    if response == 0:
      pong=(' is up!')
    else:
      pong=( ' is down!')
    await message.reply(pong)

@dp.message_handler(commands=['REP'])
async def send_pong(message: types.Message):
    passwrd="ls"
    response = os.system(passwrd)
    await message.reply(response)


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
