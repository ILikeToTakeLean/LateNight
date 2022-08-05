# Copyright (C) 2022 LateNight Development

# This file is part of the LateNight project.

# The LateNight project can not be copied and/or distributed without the express
# permission of the LateNight Development team. 
import discord # Make sure that you have installed discord.py 2.0 (https://github.com/Rapptz/discord.py)
import os
import random
import asyncio
from discord.ext import commands



async def ch_pr():
    await bot.wait_until_ready()
    statuses = ["My prefix is: n! | LateNight", "I'm in " + str(len(bot.guilds)) +
        " servers. Wow, so many people think that this bot is cool!",
        "It's late already, you should go sleep."]
    while not bot.is_closed():
      status = random.choice(statuses)
      await bot.change_presence(activity=discord.Game(name=status))
      await asyncio.sleep(20)



class LateNight(commands.Bot):
    def __init__(self):
        super().__init__(["n!", "N!", "Æ!", "(ง'̀-'́)ง"], case_insensitive=True, intents=discord.Intents.all(), strip_after_prefix=True, owner_ids=[688293803613880334, 456458873453150208])

    async def setup_hook(self):
        await self.load_extension("jishaku")
        os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
        os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 
        os.environ["JISHAKU_HIDE"] = "True"
        await self.reload_extension("jishaku")
        self.remove_command("help")
        self.loop.create_task(ch_pr())

    async def close(self):
        await super().close()

    async def on_ready(self):
        print("main.py has been loaded.")


      
bot = LateNight()



@bot.command(pass_context=True)
async def loadcog(ctx, cog):
    if ctx.author.id in bot.owner_ids:
      try:
        emoji = "<:3_LN_tick:901466423837196288>"
        await bot.load_extension(f"cogs.{cog}")
        await ctx.message.delete()
        await ctx.send(emoji, delete_after=2.5)
      except Exception as e:
        await ctx.send(f"An exception has been made!\n\n```{e}```", delete_after=5.0)
        await ctx.message.delete()
    else:
        pass



@bot.command(pass_context=True)
async def unloadcog(ctx, cog):
    if ctx.author.id in bot.owner_ids:
      try:
        emoji = "<:3_LN_tick:901466423837196288>"
        await bot.unload_extension(f"cogs.{cog}")
        await ctx.message.delete()
        await ctx.send(emoji, delete_after=2.5)
      except Exception as e:
        await ctx.send(f"An exception has been made!\n\n```{e}```", delete_after=5.0)
        await ctx.message.delete()
    else:
        pass



@bot.command(pass_context=True)
async def reloadcog(ctx, cog):
    if ctx.author.id in bot.owner_ids:
      try:
        emoji = "<:3_LN_tick:901466423837196288>"
        await bot.reload_extension(f"cogs.{cog}")
        await ctx.message.delete()
        await ctx.send(emoji, delete_after=2.5)
      except Exception as e:
        await ctx.send(f"An exception has been made!\n\n```{e}```", delete_after=5.0)
        await ctx.message.delete()
    else:
        pass

      

@bot.command(pass_context=True)
async def reloadbot(ctx):
  if ctx.author.id in bot.owner_ids:
      try:
        emoji = "<:3_LN_tick:901466423837196288>"
        for filename in os.listdir("./cogs"):
          if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
        await ctx.send(emoji, delete_after=2.5)
      except Exception as e:
        await ctx.send(f"An exception has been made!\n\n```{e}```", delete_after=5.0)
        await ctx.message.delete()
  else:
    pass

bot.run(os.getenv("TOKEN"))
