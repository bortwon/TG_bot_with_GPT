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


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    """
    Function to greet the user.
    :param message: command '/start'
    :return: welcome message
    """
    await message.answer('Привет!\nЯ бот, который станет для тебя другом и помощником.\nНапиши мне что-нибудь!')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    """
    Function to help the user.
    :param message: command '/help'
    :return: sending a message about the capabilities of the bot
    """
    await message.answer('Задай мне интересующий тебя вопрос или скажи, что я могу для тебя сделать. \n'
                         'Через мгновение я пришлю тебе ответ на твое сообщение.')


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
