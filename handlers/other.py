from aiogram import types, Dispatcher
from create_bot import dp
import json
import string


# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()

    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id,message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send, )

