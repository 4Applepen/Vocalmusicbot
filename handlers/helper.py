from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import command, other_filters2, other_filters



@Client.on_message(command("help") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""💞 Ciao questi sono i comandi che puoi usare con **{bn}** - __Vocal music bot__.
I comandi sono i seguenti.

🔥 **Users Commands :**
⚜️ /play - **[ Solo gruppi ]** > __Riproduce il file audio di risposta o il video di YouTube tramite il collegamento.__
⚜️ /song - **[ Gruppi & DM ]** > __Carica la canzone cercata nella chat.__
⚜️ /ytplay - **[ Solo gruppi ]** > __Riproduce il brano direttamente dalla ricerca di YouTube.__
⚜️ /repo - **[ DM Only ]** > __Ottiene il codice sorgente e il video tutorial di YouTube.__


🔰 **Admin & Sudo Users Commands :**
⚜️ /pause - **[Solo gruppi ]** > __Metti in pausa la musica della chat vocale.__
⚜️ /resume - **[Solo gruppi ]** > __Riprendi la musica della chat vocale.__
⚜️ /skip - **[Solo gruppi ]** > __Salta la musica corrente in riproduzione nella chat vocale.__
⚜️ /stop - **[Solo gruppi ]** > __Clears The Queue as well as ends Voice Chat Music.__""")

@Client.on_message(command("help") & other_filters)
async def ghelp(_, message: Message):
    await message.reply_text(f"**{bn} :-** Hey! DM per ottenere tutti i comandi😉")
