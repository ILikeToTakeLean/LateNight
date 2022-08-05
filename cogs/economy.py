import discord
import datetime
import animec
import time
import humanize
import json_files
import os
import json
import random
import humanize
import asyncio
import locale
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

async def open_account(user):
  users = await get_bank_data()
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 0
    users[str(user.id)]["bank"] = 0
  with open("json_files/economy.json", "w") as f:
    json.dump(users, f)
  return True

  
async def get_bank_data():
  with open("json_files/economy.json", "r") as f:
    users = json.load(f)
  return users

  
async def update_bank(user, change = 0, mode = "wallet"):
  users = await get_bank_data()
  users[str(user.id)][mode] += change
  with open("json_files/economy.json", "w") as f:
    json.dump(users, f)
  bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
  return bal

class workView(discord.ui.View):
    def __init__(self, x ,ctx, timeout=15.0):
        super().__init__(timeout=15.0)
        self.ctx = ctx
        self.x = x

    w1 = ["Builder", "Waiter", "Twitch Streamer"]
    w2 = ["Engineer", "YouTuber", "Barista"]
    w3 = ["Miner", "Chief", "Discord Moderator"]
    JobSet = random.choices([w1, w2, w3])
    OMG = JobSet[0]

    @discord.ui.button(label=OMG[0], style=discord.ButtonStyle.blurple)
    async def Job0(self, interaction: discord.Interaction, button: discord.Button):
        await open_account(interaction.user)
        users = await get_bank_data()
        rint = random.randint(100, 1000)
        embedwork = discord.Embed(title="Sucessfully finished working!", description=f"You worked as {button.label} and earned {rint} <a:LN_latenightcoin:943274431923486740>!", color=discord.Colour.random())
        embedwork.set_footer(text="Work again in 5min!")
        await interaction.response.edit_message(embed=embedwork, view=None)
        users[str(interaction.user.id)]["wallet"] += rint
        with open("json_files/economy.json", "w") as f:
            json.dump(users, f)
        self.stop()    

    @discord.ui.button(label=OMG[1], style=discord.ButtonStyle.blurple)
    async def Job1(self, interaction: discord.Interaction, button: discord.Button):
        await open_account(interaction.user)
        users = await get_bank_data()
        rint = random.randint(100, 1000)
        embedwork = discord.Embed(title="Sucessfully finished working!", description=f"You worked as {button.label} and earned {rint} <a:LN_latenightcoin:943274431923486740>!", color=discord.Colour.random())
        embedwork.set_footer(text="Work again in 5min!")
        await interaction.response.edit_message(embed=embedwork, view=None)
        users[str(interaction.user.id)]["wallet"] += rint
        with open("json_files/economy.json", "w") as f:
            json.dump(users, f)
        self.stop()    

    @discord.ui.button(label=OMG[2], style=discord.ButtonStyle.blurple)
    async def Job2(self, interaction: discord.Interaction, button: discord.Button):
        await open_account(interaction.user)
        users = await get_bank_data()
        rint = random.randint(100, 1000)
        embedwork = discord.Embed(title="Sucessfully finished working!", description=f"You worked as {button.label} and earned {rint} <a:LN_latenightcoin:943274431923486740>!", color=discord.Colour.random())
        embedwork.set_footer(text="Work again in 5min!")
        await interaction.response.edit_message(embed=embedwork, view=None)
        users[str(interaction.user.id)]["wallet"] += rint
        with open("json_files/economy.json", "w") as f:
            json.dump(users, f)
        self.stop()    

    async def on_timeout(self):
        self.clear_items()
        self.add_item(discord.ui.Button(label="Timeout", style=discord.ButtonStyle.red, disable=True))
        await self.ctx.edit(view=self)
        self.stop()

    async def interaction_check(self, interaction: discord.Interaction):
        if interaction.user.id == self.x.author.id:
            return True
        await interaction.response.send_message(f'You cannot use this interaction.', ephemeral=True)
        return False

class searchView(discord.ui.View):
    def __init__(self, ctx, message):
        super().__init__(timeout=15.0)
        self.ctx = ctx
        self.message = message

    async def on_timeout(self):
        self.clear_items()
        self.add_item(discord.ui.Button(label="Timeout", style=discord.ButtonStyle.red, disable=True))
        await self.message.edit(view=self)
        self.stop()

    async def interaction_check(self, interaction: discord.Interaction):
        if interaction.user.id == self.ctx.author.id:
            return True
        await interaction.response.send_message(f'You cannot use this interaction.', ephemeral=True)
        return False

    @discord.ui.button(label="Garden", style=discord.ButtonStyle.blurple)
    async def gardenButton(self, interaction: discord.Interaction, button: discord.Button):
        await open_account(self.ctx.author)
        users = await get_bank_data()
        searching = random.randrange(50, 600)
        gembed = discord.Embed(title="Searching around the garden...", description=f"As you're searching through the garden, you find {searching} <a:LN_latenightcoin:943274431923486740>!",color=discord.Colour.random())
        gembed.set_footer(text=self.ctx.guild.name)
        gembed.timestamp = datetime.datetime.utcnow()
        await interaction.response.edit_message(embed=gembed, view=None)
        users[str(self.ctx.author.id)]["wallet"] += searching
        with open("json_files/economy.json", "w") as f:
            json.dump(users, f)
        self.stop()

    @discord.ui.button(label="Bar", style=discord.ButtonStyle.blurple)
    async def BarButton(self, interaction: discord.Interaction, button: discord.Button):
        await open_account(self.ctx.author)
        users = await get_bank_data()
        searching = random.randrange(50, 600)
        gembed = discord.Embed(title="Searching around the bar...", description=f"As you're searching through the bar, you find {searching} <a:LN_latenightcoin:943274431923486740>!",color=discord.Colour.random())
        gembed.set_footer(text=self.ctx.guild.name)
        gembed.timestamp = datetime.datetime.utcnow()
        await interaction.response.edit_message(embed=gembed, view=None)
        users[str(self.ctx.author.id)]["wallet"] += searching
        with open("json_files/economy.json", "w") as f:
            json.dump(users, f)
        self.stop()

    @discord.ui.button(label="House", style=discord.ButtonStyle.blurple)
    async def HouseButton(self, interaction: discord.Interaction, button: discord.Button):
        await open_account(self.ctx.author)
        users = await get_bank_data()
        searching = random.randrange(50, 600)
        gembed = discord.Embed(title="Searching around the house...", description=f"As you're searching through the house, you find {searching} <a:LN_latenightcoin:943274431923486740>!",color=discord.Colour.random())
        gembed.set_footer(text=self.ctx.guild.name)
        gembed.timestamp = datetime.datetime.utcnow()
        await interaction.response.edit_message(embed=gembed, view=None)
        users[str(self.ctx.author.id)]["wallet"] += searching
        with open("json_files/economy.json", "w") as f:
            json.dump(users, f)
            self.stop()

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def work(self, ctx):
        embed = discord.Embed(title="Choose a job!", description="Choose as what you want to work.", color=discord.Colour.random())
        p = await ctx.send(embed=embed)
        view = workView(ctx, p)
        await p.edit(view=view)

    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow it down bro, don't overwork yourself.",description=f"You can work again in {humanize.naturaldelta(error.retry_after)}.", color=discord.Colour.dark_red())
            em.set_footer(text=ctx.guild.name)
            em.timestamp = datetime.datetime.utcnow()
            await ctx.reply(embed=em)
        elif isinstance(error, commands.errors.BotMissingPermissions):
          await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def math(self, ctx):
      emoji = "<a:LN_latenightcoin:943274431923486740>"
      await open_account(ctx.author)
      users = await get_bank_data()
      n1 = random.randint(51, 500)
      n2 = random.randint(51, 500)
      n3 = n1 + n2
      n4 = str(n3)
      embed = discord.Embed(title="Time for math!", description=f"What is **{n1} + {n2}**?", color=discord.Colour.random())
      embed.set_footer(text="You have 15 seconds to answer.")
      await ctx.send(embed=embed)
      def check(m):
        return m.content == n4 and m.channel == ctx.channel
      try:
          msg = await ctx.bot.wait_for('message', check=check,timeout=15.0)
      except asyncio.TimeoutError:
        await ctx.reply(f"Time's up! The correct answer was {n4}.")
        pass
      except discord.errors.HTTPException:
        pass
      else:
        await open_account(msg.author)
        users = await get_bank_data()
        await ctx.send(f"{msg.author.mention} got the correct answer! The number was {n4}.\n20{emoji} have been added to your balance.")
        users[str(ctx.author.id)]["wallet"] += 25
        with open("json_files/economy.json", "w") as f:
          json.dump(users, f)
    @math.error
    async def math_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"*You can use this command again in {humanize.naturaldelta(error.retry_after)}*\n> Message deletes once the cooldown is up.", delete_after=error.retry_after)
      
  
    @commands.command(aliases=["bal"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def balance(self, ctx, user: discord.Member = None):
      emoji = "<a:LN_latenightcoin:943274431923486740>"
      if user == None:
        user = ctx.author
      await open_account(user)
      users = await get_bank_data()
      wallet_amt = users[str(user.id)]["wallet"]
      bank_amt = users[str(user.id)]["bank"]
      total_amt = bank_amt + wallet_amt
      embed = discord.Embed(title="", color=discord.Colour.purple())
      embed.set_author(name=user, icon_url=user.avatar_url)
      embed.add_field(name="🪙 - Total amount", value=f"{total_amt:,} {emoji}", inline=False)
      embed.add_field(name="👛 - Wallet amount", value=f"{wallet_amt:,} {emoji}", inline=False)
      embed.add_field(name="🏦 - Bank amount", value=f"{bank_amt:,} {emoji}")
      embed.set_thumbnail(url=ctx.guild.icon_url)
      if total_amt <50000:
        embed.set_footer(text="Broke ass mf")
      else:
        embed.set_footer(text="Wanna be my sugar daddy?")
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.reply(embed=embed)
    @balance.error
    async def balance_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"*You can use this command again in {humanize.naturaldelta(error.retry_after)}*\n> Message deletes once the cooldown is up.", delete_after=error.retry_after)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def search(self, ctx):
        rembed = discord.Embed(title="Where do you want to search?", description="You can either search in:\n`Garden`\n`Bar`\n`House`", color=discord.Colour.purple())
        rembed.set_footer(text=ctx.guild.name)
        rembed.timestamp = datetime.datetime.utcnow()
        msg = await ctx.reply(embed=rembed)
        view = searchView(ctx, msg)
        await msg.edit(view=view)
    
    @search.error
    async def search_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow it down bro, even searching needs time.",description=f"You can search again in {humanize.naturaldelta(error.retry_after)}.", color=discord.Colour.dark_red())
            em.set_footer(text=ctx.guild.name)
            em.timestamp = datetime.datetime.utcnow()
            await ctx.reply(embed=em)
        elif isinstance(error, commands.errors.BotMissingPermissions):
          await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def beg(self, ctx):
      user = ctx.author
      await open_account(ctx.author)
      users = await get_bank_data()
      begging = random.randrange(0, 200)
      if begging == 0:
        embed1 = discord.Embed(title="", description="**Someone just wanted to give you money, as he was giving you the money someone just robbed you both... You lost 300 coins.**", 
        color=discord.Colour.dark_red())
        embed1.set_footer(text=ctx.guild.name)
        embed1.timestamp = datetime.datetime.utcnow()
        await ctx.reply(embed=embed1)
        users[str(user.id)]["wallet"] -= 300 
        with open("json_files/economy.json", "w") as f:
          json.dump(users, f)
      else:
        name_list = ["Keanu reeves", "John becker", "Mario basto", "Jax tray"]
        name_list_r = random.choice(name_list)
        talk = ["Take this my friend!", "Don't buy drugs with it!"]
        talk_r = random.choice(talk)
        embed = discord.Embed(title=f"{name_list_r} just gave you {begging} coins!", description=f" \"**{talk_r}**\"", color=discord.Colour.purple())
        embed.set_footer(text=ctx.guild.name)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        users[str(user.id)]["wallet"] += begging
        with open("json_files/economy.json", "w") as f:
          json.dump(users, f)
    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow it down bro, even begging needs time.",description=f"You can beg again in {humanize.naturaldelta(error.retry_after)}.", color=discord.Colour.dark_red())
            em.set_footer(text=ctx.guild.name)
            em.timestamp = datetime.datetime.utcnow()
            await ctx.reply(embed=em)
        elif isinstance(error, commands.errors.BotMissingPermissions):
          await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

      
    @commands.command(aliases=["wd", "with"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def withdraw(self, ctx, amount=None, member: discord.Member=None):
      emoji = "<a:LN_latenightcoin:943274431923486740>"
      users = await get_bank_data()
      user = ctx.author
      await open_account(ctx.author)
      try:
        if amount == None:
          await ctx.reply("you playin' with me? You gotta enter an amount that you want to withdraw.")
          return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount >bal[1]:
          await ctx.reply("You don't have that much money.")
          return
        if amount <0:
          await ctx.reply("Can't withdraw negative money smh.")
          return
        await update_bank(ctx.author, amount)
        await update_bank(ctx.author, -1*amount, "bank")
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        users1 = await get_bank_data()
        new_wallet = users1[str(user.id)]["wallet"]
        new_bank = users1[str(user.id)]["bank"]
        embed = discord.Embed(title="Successfully withdrew money!", description=f"**Withdrew:** {amount:,} {emoji}\n**New wallet amount:** {new_wallet:,} {emoji}\n**New bank amount:** {new_bank:,} {emoji}", color=discord.Colour.random())
        embed.set_footer(text=ctx.guild.name)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.reply(embed=embed)
      except ValueError:
        await ctx.reply("Lmao, are you trying to withdraw from someone else? That's not how it works buddy.")
    @withdraw.error
    async def withdraw_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"*You can use this command again in {humanize.naturaldelta(error.retry_after)}*\n> Message deletes once the cooldown is up.", delete_after=error.retry_after)


    @commands.command(aliases=["dep", "depo"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def deposit(self, ctx, amount=None, member: discord.Member=None):
      emoji = "<a:LN_latenightcoin:943274431923486740>"
      users = await get_bank_data()
      user = ctx.author
      await open_account(ctx.author)
      try:
        if amount == None:
          await ctx.reply("you playin' with me? You gotta enter an amount that you want to deposit")
          return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount >bal[0]:
          await ctx.reply("You don't have that much money.")
          return
        if amount <0:
          await ctx.reply("Can't deposit negative money smh.")
          return
        await update_bank(ctx.author, -1*amount)
        await update_bank(ctx.author, amount, "bank")
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        users1 = await get_bank_data()
        new_wallet = users1[str(user.id)]["wallet"]
        new_bank = users1[str(user.id)]["bank"]
        embed = discord.Embed(title="Successfully deposited money!", description=f"**Deposited:** {amount:,} {emoji}\n**New wallet amount:** {new_wallet:,} {emoji}\n**New bank amount:** {new_bank:,} {emoji}", color=discord.Colour.random())
        embed.set_footer(text=ctx.guild.name)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.reply(embed=embed)
      except ValueError:
        await ctx.reply("Lmao, are you trying to deposit to someone else? That's not how it works buddy.")
    @deposit.error
    async def deposit_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"*You can use this command again in {humanize.naturaldelta(error.retry_after)}*\n> Message deletes once the cooldown is up.", delete_after=error.retry_after)


    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def give(self, ctx, member: discord.Member, amount=None):
      emoji = "<a:LN_latenightcoin:943274431923486740>"
      users = await get_bank_data()
      user = ctx.author
      await open_account(ctx.author)
      await open_account(member)
      if amount == None:
        await ctx.reply("you playin' with me? You gotta enter an amount that you want to give.")
        return
      bal = await update_bank(ctx.author)
      amount = int(amount)
      if amount >bal[0]:
        await ctx.reply("You don't have that much money.")
        return
      if amount <0:
        await ctx.reply("Can' negative money smh.")
        return
      embed = discord.Embed(title="Hm...", description=f"Do you really want to give {member.name} {amount} {emoji}?", color=discord.Colour.random())
      embed.set_footer(text=ctx.guild.name)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_thumbnail(url=ctx.guild.icon_url)
      msg = await ctx.reply(embed=embed, components=[[Button(style=ButtonStyle.green, label="Send"), Button(style=ButtonStyle.red, label="Cancel")]])
      res = await self.bot.wait_for("button_click")
      if res.component.label == "Send":
        await update_bank(ctx.author, -1*amount,"wallet")
        await update_bank(member, amount, "wallet")
        embed1 = discord.Embed(title=f"You gave {member} the money!", description=f"Given money: {amount} {emoji}", color=discord.Colour.green())
        embed1.set_footer(text=ctx.guild.name)
        embed1.timestamp = datetime.datetime.utcnow()
        embed1.set_thumbnail(url=ctx.guild.icon_url)
        await res.respond(type=7, embed=embed1, components=[[Button(style=ButtonStyle.green, label="Send", disabled=True), Button(style=ButtonStyle.red, label="Cancel", disabled=True)]])
      elif res.component.label == "Cancel":
        embed2 = discord.Embed(title="You cancelled the interaction!", description=f"You decided to not give money to {member}.", color=discord.Colour.dark_red())
        await res.respond(type=7, embed=embed2, components=[[Button(style=ButtonStyle.green, label="Send", disabled=True), Button(style=ButtonStyle.red, label="Cancel", disabled=True)]])
        pass
    @give.error
    async def give_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)
      elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MissingRequiredArgument")
        await ctx.reply(embed=embed)
      elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"*You can use this command again in {humanize.naturaldelta(error.retry_after)}*\n> Message deletes once the cooldown is up.", delete_after=error.retry_after)
  
          
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def rob(self, ctx, member: discord.Member = None):
      if member is None:
        await ctx.reply("Bruh, who you wanna rob?")
        return
      emoji = "<a:LN_latenightcoin:943274431923486740>"
      await open_account(ctx.author)
      await open_account(member)
      bal = await update_bank(member)
      if bal[0]<100:
        await ctx.reply("Not worth it to rob someone who's that broke lmao")
        return
      earnings = random.randrange(0, bal[0])
      await update_bank(ctx.author, earnings)
      await update_bank(member, -1*earnings)
      if member == ctx.author:
        await ctx.reply("Bruh, you really trying to rob yourself?!")
      else:
        embed = discord.Embed(title="Sneaky!", description=f"You robbed {member} and got {earnings} {emoji}!", color=discord.Colour.purple())
        embed.set_footer(text=ctx.guild.name)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.reply(embed=embed)
    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            x = (round(error.retry_after)) + round(datetime.datetime.utcnow().timestamp())
            em = discord.Embed(title=f"Chill bro, you want him to call the cops on you?!",description=f"You can rob again in <t:{round(x)}:R>. / <t:{round(x)}>", color=discord.Colour.dark_red())
            em.set_footer(text=ctx.guild.name)
            em.timestamp = datetime.datetime.utcnow()
            await ctx.reply(embed=em)
        elif isinstance(error, commands.errors.BotMissingPermissions):
          await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
            color=discord.Colour.dark_red())
            embed.set_footer(text="commands.MemberNotFound")
            await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
      emoji = "<a:LN_latenightcoin:943274431923486740>"
      await open_account(ctx.author)
      users = await get_bank_data()
      embed = discord.Embed(title="Daily claimed!", description=f"You claimed your 25,000 daily {emoji}!", color=discord.Colour.random())
      await ctx.reply(embed=embed)
      users[str(ctx.author.id)]["wallet"] += 25000
      with open("json_files/economy.json", "w") as f:
        json.dump(users, f)
    @daily.error
    async def daily_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        x = (round(error.retry_after)) + round(datetime.datetime.utcnow().timestamp())
        em = discord.Embed(title="Chill, i'm not made out of money.", description=f"You can claim another daily in <t:{round(x)}:R>. / <t:{round(x)}>", color=discord.Colour.red())
        em.set_footer(text=ctx.guild.name)
        em.timestamp = datetime.datetime.utcnow()
        await ctx.reply(embed=em)
      elif isinstance(error, commands.errors.BotMissingPermissions):
          await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command(aliases = ["elb"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def economyleaderboard(self, ctx, x=5):
      emoji = "<a:LN_latenightcoin:943274431923486740>"
      users = await get_bank_data()
      leader_board = {}
      total = []
      for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)
      total = sorted(total,reverse=True)   
      embed = discord.Embed(title = f"Top {x} Richest People" , description="Top richest Economy players!", color=discord.Colour.purple())
      index = 1
      for amt in total:
          id_ = leader_board[amt]
          member = self.bot.get_user(id_)
          name = member
          embed.add_field(name = f"{index}. {name}" , value = f"{amt:,} {emoji}",  inline = False)
          if index == x:
              break
          else:
              index += 1
      await ctx.send(embed=embed)
    @economyleaderboard.error
    async def economyleaderboard_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"*You can use this command again in {humanize.naturaldelta(error.retry_after)}*\n> Message deletes once the cooldown is up.", delete_after=error.retry_after)



async def setup(bot):
    await bot.add_cog(economy(bot))