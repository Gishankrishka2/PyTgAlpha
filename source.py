import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('ð Owner ð', user_id="@N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton(text="ð´ Êá´Êá´ ð´",callback_data="hlp"),
                 InlineKeyboardButton("ð sá´á´Êá´á´ á´á´á´á´ ð", url="https://github.com/TeamAlphaTg/MemehubtgSl_Bot")
                 ],
                 [
                 InlineKeyboardButton("â sÊá´Êá´ â", switch_inline_query="share"),
                 InlineKeyboardButton("â sÊá´Êá´ á´ÊÉ´Ê â", switch_inline_query="cshare")
                 ]]
                  )
