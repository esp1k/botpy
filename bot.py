import config
from aiogram import Bot, Dispatcher, executor, types 

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message : types.Message):
  if message.text == 'Привет':
    await massage.answer('И тебе привет!')

executor.start_polling(dp, skip_updates=True)
