import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('Ok!')


async def go_to_geektech():
    await bot.send_message(
        chat_id=chat_id,
        text="пора в Гиктек"
    )


async def go_to_Geektech():
    await bot.send_message(
        chat_id=chat_id,
        text="пора в Гиктек"
    )


async def scheduler():
    aioschedule.every().friday.at("19:20").do(go_to_geektech())
    aioschedule.every().tuesday.at("19:20").do(go_to_Geektech())

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'notify' in word.text)