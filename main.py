import openai
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import Message
from config import config


BOT_TOKEN: str = config.bot_token.get_secret_value()
openai.api_key = config.openai_api_token.get_secret_value()


bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message()
async def answer(message: Message):
    """
    Function for responding to a user using GPT.
    :param message: message from user
    :return: answer to user
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    answer = response['choices'][0]['text'].strip()
    await message.reply(text=answer)


if __name__ == '__main__':
    dp.run_polling(bot)
