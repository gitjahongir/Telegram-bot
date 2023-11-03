from aiogram import Dispatcher,Bot,executor,types 
import random

bot = Bot(token="6952639973:AAFK8WS8lJcBMmP-sXeq6fvQ-zD7QhzLZxw")

dp = Dispatcher(bot=bot)

@dp.message_handler(text=("Salom" or "salom"))
async def salom_function(message:types.Message):
    words = ["Salom!","Hush kelibsiz!","Assalomu Alaykum!","Nima istaysiz?","Qanday yordam berishim mumkin?"]
    await message.answer(random.choice(words))
    print(message)

if __name__ == "__main__":
    executor.start_polling(dp)
