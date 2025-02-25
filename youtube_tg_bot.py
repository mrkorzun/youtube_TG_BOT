# pip install pytube aiogram


import os
import pytube
from aiogram import Bot, Dispatcher, types
import asyncio



# 🔑 Вставь свой Telegram API-ключ
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# 📌 Функция для скачивания видео
def download_youtube_video(url):
  """Скачивает видео с YouTube и возвращает путь к файлу"""
  yt = pytube.YouTube(url)
  stream = yt.streams.get_highest_resolution()
  file_path = stream.download(output_path="downloads/")
  return file_path

# 📌 Обработчик команд
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
  await message.reply("Привет! Отправь мне ссылку на YouTube-видео, и я скачаю его для тебя.")



@dp.message_handler()
async def handle_message(message: types.Message):
  url = message.text
  await message.reply("⏳ Загружаю видео...")
  video_path = download_youtube_video(url)
  await message.reply_document(types.InputFile(video_path))
  os.remove(video_path) # Удаляем файл после отправки

# 📌 Запуск бота
async def main():
  await dp.start_polling()

asyncio.run(main())