import discord
from discord.ext import commands
import os
from kpv import keep_alive
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix='')
x = 0
rotations = -1
rotatio = 0


@bot.event
async def on_ready():
    print('succesfuly logged in as {0.user}'.format(bot))


@bot.event
async def on_message(ctx):
    global x, rotations, rotatio
    if ctx.author.bot:
        if x == 3:
            try:
                await bot.wait_for('message', timeout=5.0)
            except asyncio.TimeoutError:
                print('outTime')
                await asyncio.sleep(3)
                x = 3
        else:
            return
    if ctx.author.bot:
        return

    if ctx.content.startswith('ok'):
        x = 3
    if ctx.content.startswith('cs'):
        x = 2
    if ctx.content.startswith('xd'):
        x = 1
    if ctx.content.startswith('based'):
        x = 0
        print('stoped')
    while x != 0:
        if x == 2:
            try:
                rotations += 1
                guild = ctx.guild
                await guild.create_text_channel(rotations)
            except:
                print('maximum reached')
                x = 0

        if x == 1:
            await ctx.channel.send('@everyone')
        try:
            if x == 3:
                guild = ctx.guild
                ch = await guild.create_text_channel(rotatio)
                rotatio += 1
                await ch.send('@everyone')
        except:
            guild = ctx.guild
            for chan in guild.text_channels:
                if x == 0:
                    continue
                await chan.send('@everyone')


keep_alive()
bot.run('token')
