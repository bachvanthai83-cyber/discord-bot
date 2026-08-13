# -*- coding: utf-8 -*-
import discord
from discord.ext import commands

TOKEN ="MTUzNzI4NjI4NzkyNzgxMjE0Nw.Gark6N.6B7x_zpYrovVpp68dvjhB9e9ZoDCD3tT2UZHLs"
KING_ID = 1337402131174391873
CHANNEL_ID =1537294132702355536

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user} ready!")


@bot.event
async def on_voice_state_update(member, before, after):
    if member.id == KING_ID and before.channel is None and after.channel is not None:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send("\U0001F451 **Nhà vua dã giáng lâm vào phòng voice!**")


@bot.event
async def on_presence_update(before, after):
    if after.id == KING_ID:
        if (
            before.status == discord.Status.offline
            and after.status == discord.Status.online
        ):
            channel = bot.get_channel(CHANNEL_ID)
            if channel:
                await channel.send("👑 **Nhà vua đã giáng lâm vào phòng voice!**")


bot.run(TOKEN)
