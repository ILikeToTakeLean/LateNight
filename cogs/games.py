import discord
import datetime
import asyncio
import random
from discord.ext import commands
import time
import humanize

class gtnView(discord.ui.View):
    def __init__(self, ctx, message):
        super().__init__()
        self.ctx = ctx
        self.message = message

    @discord.ui.button(label="Easy", style=discord.ButtonStyle.green)
    async def easygtn(self, interaction, button):
        number1 = random.randint(1,25)
        embed = discord.Embed(title="Guess the Number!", description="The number is between 1-25!\nYou have 10 seconds to guess.\nDifficulty = `Easy`", color=discord.Colour.green())
        self.clear_items()
        embed.set_footer(text="Good Luck!")
        await self.message.edit(embed=embed, view=self)
        print(number1)
        number2 = str(number1)
        def check(m):
          return m.content == number2 and m.channel == channel
        try:
          msg = await self.ctx.bot.wait_for('message', check=check,timeout=10.0)
        except asyncio.TimeoutError:
          await self.ctx.reply(f"Time's up! The correct answer was {number1}.")
          pass
        except discord.errors.HTTPException:
          pass
        else:
          await self.ctx.send(f"{msg.author.mention} got the correct answer! The number was {number2}")  
        self.stop()


    @discord.ui.button(label="Medium", style=discord.ButtonStyle.blurple)
    async def mediumgtn(self, interaction, button):
        number1 = random.randint(1,50)
        embed = discord.Embed(title="Guess the Number!", description="The number is between 1-50!\nYou have 20 seconds to guess.\nDifficulty = `Medium`", color=discord.Colour.blurple())
        self.clear_items()
        embed.set_footer(text="Good Luck!")
        await self.message.edit(embed=embed, view=self)
        print(number1)
        number2 = str(number1)
        def check(m):
          return m.content == number2 and m.channel == self.ctx.channel
        try:
          msg = await self.ctx.bot.wait_for('message', check=check,timeout=20.0)
        except asyncio.TimeoutError:
          await self.ctx.reply(f"Time's up! The correct answer was {number1}.")
          pass
        except discord.errors.HTTPException:
          pass
        else:
          await self.ctx.send(f"{msg.author.mention} got the correct answer! The number was {number2}")
        self.stop()

    @discord.ui.button(label="Hard", style=discord.ButtonStyle.red)
    async def hardgtn(self, interaction, button):
        number1 = random.randint(1,100)
        embed = discord.Embed(title="Guess the Number!", description="The number is between 1-100!\nYou have 30 seconds to guess.\nDifficulty = `Hard`", color=discord.Colour.red())
        self.clear_items()
        embed.set_footer(text="Good Luck!")
        await self.message.edit(embed=embed, view=self)
        print(number1)
        number2 = str(number1)
        def check(m):
          return m.content == number2 and m.channel == self.ctx.channel
        try:
          msg = await self.ctx.bot.wait_for('message', check=check,timeout=30.0)
        except asyncio.TimeoutError:
          await self.ctx.reply(f"Time's up! The correct answer was {number1}.")
          pass
        except discord.errors.HTTPException:
          pass
        else:
          await self.ctx.send(f"{msg.author.mention} got the correct answer! The number was {number2}")
        self.stop()
    
    async def interaction_check(self, interaction):
        if interaction.user.id == self.ctx.author.id:
            return True
        await interaction.response.send_message(f'You cannot use this interaction.', ephemeral=True)
        return False

    async def on_timeout(self):
        await self.message.edit(view=None)
        self.stop()

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def gtn(self, ctx):
      channel = ctx.message.channel
      embeddif = discord.Embed(title="Choose your difficulty!", description="**Green / Easy** - Guess a number from 1-25 in 10 seconds.\n**Blue / Medium** - Guess a number from 1-50 in 20 seconds.\n**Red / Hard** - Guess a number from 1-100 in 30 seconds.", color=discord.Colour.purple())
      msg = await ctx.reply(embed=embeddif)
      view = gtnView(ctx, msg)
      await msg.edit(view=view)

    @gtn.error
    async def gtn_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command(aliases=['rps'])
    @commands.bot_has_permissions(embed_links=True)
    async def rockpaperscissors(self, ctx, user: discord.Member = None):
        embed = discord.Embed(title="Rock Paper Scissors:", description=f"Choose between `rock`, `paper` and `scissors`.", colour=discord.Colour.random())
        msg = await ctx.reply(embed=embed, components=[[Button(style=ButtonStyle.green, label="🪨 - Rock"), Button(style=ButtonStyle.red, label="📰 - Paper"), Button(style=ButtonStyle.blue, label="✂️ - Scissors")]])
        res = await self.bot.wait_for("button_click", timeout = 30)
        bot = random.choice(['🪨 - Rock', '📰 - Paper', '✂️ - Scissors'])
        if res.component.label == bot:
          embed = discord.Embed(title="Tie!", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "🪨 - Rock" and bot == "📰 - Paper":
          embed = discord.Embed(title="I won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "📰 - Paper" and bot == "✂️ - Scissors":
          embed = discord.Embed(title="I won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "✂️ - Scissors" and bot == "🪨 - Rock":
          embed = discord.Embed(title="I won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "📰 - Paper" and bot == "🪨 - Rock":
          embed = discord.Embed(title="You won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "✂️ - Scissors" and bot == "📰 - Paper":
          embed = discord.Embed(title="You won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "🪨 - Rock" and bot == "✂️ - Scissors":
          embed = discord.Embed(title="You won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
    @gtn.error
    async def gtn_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


async def setup(bot):
  await bot.add_cog(games(bot))