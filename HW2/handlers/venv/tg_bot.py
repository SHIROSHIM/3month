from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
executor.start_polling(dp, skip_updates=True)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"здраствуйте {message.from_user.first_name}")
    await message.answer("This is an answer method!")
    await message.reply("This is an reply method!")




    @dp.message_handler(commands=['quiz'])
    async def quiz_1(message: types.Message):
        markup = InlineKeyboardMarkup()
        button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
        markup.add(button_call_1)

        question = "Какая самая высокая точка на земле?"
        answers = [
            "Макалу",
            "Канченджанга",
            "Эверест",
            "Дхаулагири I",
            "Чогори",
        ]

        await bot.send_poll(
            chat_id=message.from_user.id,
            question=question,
            options=answers,
            is_anonymous=True,
            type='quiz',
            correct_option_id=1,
            explanation="неправильно!",
            reply_markup=markup
        )

    @dp.callback_query_handler(text="button_call_1")
    async def quiz_2(call: types.CallbackQuery):
        markup = InlineKeyboardMarkup()
        button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
        markup.add(button_call_2)

        question = "Когда создали python?"
        answers = [
            "1978",
            "1999",
            "2007",
            "1980",
            "1233",
            "7777",
        ]

        await bot.send_poll(
            chat_id=call.from_user.id,
            question=question,
            options=answers,
            is_anonymous=True,
            type='quiz',
            correct_option_id=3,
            explanation="неправильно!",
            reply_markup=markup
        )

    @dp.message_handler()
    async def echo(message: types.Message):
        # print(message)
        await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
