from pyrogram import filters
from pyrogram.types import Message

from Zenaku5GenX-Music import app
from Zenaku5GenX-Music.core.call import Dil

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Dil.stop_stream_force(message.chat.id)
