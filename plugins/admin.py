from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre
ADMIN = int(os.environ.get("ADMIN", 1217549670))
log_channel = int(os.environ.get("LOG_CHANNEL", ""))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("📈 Select Plan to upgrade...", quote=True, reply_markup=InlineKeyboardMarkup([
		           [
				   InlineKeyboardButton("🥉 Bʀᴏɴᴢᴇ", callback_data="vip1")
				   ], [
					InlineKeyboardButton("🥈 Sɪʟᴠᴇʀ ", callback_data="vip2")
				   ], [
					InlineKeyboardButton("🥇 Gᴏʟᴅ", callback_data="vip3")
					]]))


@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["ceasepower"]))
async def ceasepremium(bot, message):
	await message.reply_text(" POWER CEASE MODE", quote=True, reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("•× Limit 700MB ×•", callback_data="cp1"),
				    InlineKeyboardButton("•× Limit 850MB ×•", callback_data="cp2")
				   ], [
				    InlineKeyboardButton("•••× CEASE ALL POWER ×•••", callback_data="cp3")
				    ]]))


@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["resetpower"]))
async def resetpower(bot, message):
	    await message.reply_text(text=f"Do you really want to reset daily limit to default data limit 2GB ?",quote=True,reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("• YES ! Set as Default •",callback_data = "dft")],
				   [InlineKeyboardButton("❌ Cancel ❌",callback_data = "cancel")]
				   ]))

        			
@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 10737418240
	uploadlimit(int(user_id),10737418240)
	usertype(int(user_id),"🥉 **Bʀᴏɴᴢᴇ**")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 10 GB")
	await bot.send_message(user_id,"Hey you are Upgraded To Bʀᴏɴᴢᴇ. check your plan here /myplan")
	await bot.send_message(log_channel,f"⚡️ Plan Upgraded successfully 💥\n\nHey you are Upgraded To Bʀᴏɴᴢᴇ. check your plan here /myplan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 53687091200
	uploadlimit(int(user_id), 53687091200)
	usertype(int(user_id),"🥈 **Sɪʟᴠᴇʀ **")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 50 GB")
	await bot.send_message(user_id,"Hey you are Upgraded To Sɪʟᴠᴇʀ. check your plan here /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 107374182400
	uploadlimit(int(user_id), 107374182400)
	usertype(int(user_id),"🥇 ** Gᴏʟᴅ**")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 100 GB")
	await bot.send_message(user_id,"Hey you are Upgraded To Gᴏʟᴅ. check your plan here /myplan")

# CEASE POWER MODE @LAZYDEVELOPER

@Client.on_callback_query(filters.regex('cp1'))
async def cp1(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit  = 524288000
	uploadlimit(int(user_id),524288000)
	usertype(int(user_id),"**ACCOUNT DOWNGRADED**")
	addpre(int(user_id))
	await update.message.edit("ACCOUNT DOWNGRADED\nThe user can only use 100MB/day from Data qota")
	await bot.send_message(user_id,"⚠️ Warning ⚠️\n\n- ACCOUNT DOWNGRADED\nYou can only use 100MB/day from Data qota.\nCheck your plan here - /myplan\n- Contact Admin <a href='https://t.me/Praxxsh'>**A ᴅ ᴏ ʟ ғ 🔰 R ᴀ ᴍ**</a>")

@Client.on_callback_query(filters.regex('cp2'))
async def cp2(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit = 104857600
	uploadlimit(int(user_id), 104857600)
	usertype(int(user_id),"**ACCOUNT DOWNGRADED Lv-2**")
	addpre(int(user_id))
	await update.message.edit("ACCOUNT DOWNGRADED to Level 2\nThe user can only use 100MB/day from Data qota")
	await bot.send_message(user_id,"⛔️ Last Warning ⛔️\n\n- ACCOUNT DOWNGRADED to Level 2\nYou can only use 100MB/day from Data qota.\nCheck your plan here - /myplan\n- Contact Admin <a href='https://t.me/Praxxsh'>**A ᴅ ᴏ ʟ ғ 🔰 R ᴀ ᴍ**</a>")

@Client.on_callback_query(filters.regex('cp3'))
async def cp3(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit = 0
	uploadlimit(int(user_id), 0)
	usertype(int(user_id),"**POWER CEASED !**")
	addpre(int(user_id))
	await update.message.edit("All power ceased from the user.\nThis account has 0 mb renaming capacity ")
	await bot.send_message(user_id,"🚫 All POWER CEASED 🚫\n\n- All power has been ceased from you \nFrom now you can't rename files using me\nCheck your plan here - /myplan\n- Contact Admin <a href='https://t.me/Praxxsh'>**A ᴅ ᴏ ʟ ғ 🔰 R ᴀ ᴍ**</a>")

@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 1288490188
	uploadlimit(int(user_id), 1288490188)
	usertype(int(user_id),"**Free**")
	addpre(int(user_id))
	await update.message.edit("Daily Data limit has been reset successsfully.\nThis account has default 2 GB renaming capacity ")
	await bot.send_message(user_id,"Your Daily Data limit has been reset successsfully.\n\nCheck your plan here - /myplan\n- Contact Admin <a href='https://t.me/Praxxsh'>**A ᴅ ᴏ ʟ ғ 🔰 R ᴀ ᴍ**</a>")
