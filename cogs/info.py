import discord
import datetime
import random
import os
import animec
import asyncio
import psutil
import humanize
from discord.ext import commands
load_time = datetime.datetime.utcnow()
n = datetime.datetime.utcnow().timestamp()



class botinfo(discord.ui.Select):
  def __init__(self, messageauthor, message, bot):
    options = [
      discord.SelectOption(
        label="LateNight Team", description="The team behind the whole project!", emoji="🛡️"
      ),
      discord.SelectOption(
        label="Botinfos", description="Get infos about the bot.", emoji="ℹ️", default=True
      ), 
      discord.SelectOption(
        label="Miscellaneous", description="Get infos about non-specific items.", emoji="⚙️"
      )
    ]
    super().__init__(
      placeholder="Select something",
      options=options,
    )
    self.messageauthor = messageauthor
    self.message = message
    self.process = psutil.Process(os.getpid())
    self.bot = bot

  async def callback(self, interaction: discord.Interaction):
    if interaction.user != self.messageauthor:
      return await interaction.response.send_message("You can't use this interaction.", ephemeral=True)
    res = self.values[0]
    
    if res == "LateNight Team":
      embedb = discord.Embed(title="LateNight Team", description=f"<:LateNightDiscord_Developer:992855227843756154> - **Head-Developers:**\n> `Deprecated#8292`\n> `deceased#3037`\n\n<:LateNightDiscord_Staff:992855520299995238> - **Admins:**\n>  `Hussain#0007`\n> `zimin#1777`", color=0x71368a)
      embedb.timestamp = datetime.datetime.utcnow()
      embedb.set_footer(text="haha botinfos go brrrr")
      await interaction.response.edit_message(embed=embedb)
      
    elif res == "Botinfos":
      x = load_time - datetime.datetime.utcnow()
      y = humanize.precisedelta(x, minimum_unit="seconds")
      ramUsage = self.process.memory_full_info().rss / 1024**2
      embeda = discord.Embed(title="Botinfos!", description=f"""**Ping** 🏓\nThe bots ping is {(round(self.bot.latency * 1000))}ms!\n\n**Uptime** 📡\nThe bots uptime is {y} / <t:{round(n)}:R> / <t:{round(n)}>\n\n**Servers** 🖥️\n{str(len(self.bot.guilds))}\n
**Ram usage** 🧬
{ramUsage:.2f} MB""", color=0x71368a)
      embeda.timestamp = datetime.datetime.utcnow()
      embeda.set_footer(text="haha botinfos go brrrr")
      await interaction.response.edit_message(embed=embeda)
      
    elif res == "Miscellaneous":
      embed2 = discord.Embed(title="Misc!", description=f"**Commands 📂** \nThe bot has {len(self.bot.commands)} commands\n\n**Users 📢\n** The bot is visible to {len(list(map(str, [p.id for p in self.bot.users])))} users", color=discord.Colour.random()) 
      embed2.timestamp = datetime.datetime.utcnow()
      embed2.set_footer(text="haha botinfos go brrrr")
      await interaction.response.edit_message(embed=embed2)



class DropdownView(discord.ui.View):
    def __init__(self, messageauthor, message, bot):
        super().__init__()
        self.add_item(botinfo(messageauthor, message, bot))

class whoisSelect(discord.ui.Select):
    def __init__(self, ctx, message, user):
        options = [
        discord.SelectOption(
            label="General Information", description="Get general information about yourself!"
        ),
        discord.SelectOption(
            label="Server member information", description="Get information of yourself according to this guild!"
        ),
        discord.SelectOption(
            label="Permissions", description="Get information about your permissions!"
        )]
        super().__init__(options=options, placeholder="Select something")
        self.ctx = ctx
        self.message = message
        self.user = user

    async def callback(self, interaction):
        res = self.values[0]
        voice_state = None if not self.user.voice else self.user.voice.channel
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in self.user.guild_permissions if p[1]])
        members = sorted(self.ctx.guild.members, key=lambda m: m.joined_at)
        foundere = "<:LateNightFounder:966355172102115420>"
        deve = """
<:LateNightDeveloper:966356003320918107>
        """
        votere = "<a:6_LN_tickyellow:951619262798262382>"
        buge = "<:LateNightBugHunter:966356933839835156>"
        desginere = "<:1_LN_zerotwopeace:901462836071522334>"
        admine = "<:LateNightAdministration:966350801012416632>"
        zimin = self.user.id == 802551341963673650
        lean = self.user.id == 703671503954378782
        kiki = self.user.id == 317708760535793686
        rainbot = self.user.id == 688293803613880334
        zulk = self.user.id == 892327232398319656
        vron = self.user.id == 879574308266070016
        tth = self.user.id == 749172471290134579
        ts = self.user.created_at.timestamp()
        tsj = self.user.joined_at.timestamp()
        if res == "General Information":
            embed1 = discord.Embed(title="", description=f"""
**User Nickname** - {self.user.nick}
**User ID** - {self.user.id}
**Link to Avatar** - [Here]({self.user.avatar.url})
**Status** - {str(self.user.status).title()}
**Activity** - {self.user.activity}
**Account age** - <t:{round(ts)}:R>
              """, color=discord.Colour.random())
            embed1.set_author(name=f"{self.user}", icon_url=f"{self.user.avatar.url}")
            embed1.set_footer(text=self.ctx.guild.name)
            embed1.set_thumbnail(url=self.user.avatar.url)
            embed1.timestamp = datetime.datetime.utcnow()
            if rainbot:
                embed1.add_field(name="**Special acknowledgements**", value=f"<:LateNightDeveloper:966356003320918107> - LateNight Head-Developer")
            elif lean:
                embed1.add_field(name="Special acknowledgements", value=f"{foundere} - LateNight Server Founder\n<:LateNightDeveloper:966356003320918107> - LateNight Head-Developer")
            elif zulk:
                embed1.add_field(name="Special acknowledgements", value=f"{foundere} - LateNight Server Founder")
            elif vron:
                embed1.add_field(name="Special acknowledgements", value=f"{votere} - LateNight Top Voter")
            elif tth:
                embed1.add_field(name="Special acknowledgements", value=f"{buge} - LateNight Bug Hunter")
            elif kiki:
                embed1.add_field(name="Special acknowledgements", value=f"{desginere} - LateNight Server Designer")
            elif zimin:
                embed1.add_field(name="Special acknowledgements", value=f"{admine} - LateNight Administrator")
            await interaction.response.edit_message(embed=embed1)
        elif res == "Server member information":
            embed2 = discord.Embed(title="", description=f"""
**Highest Role** - {self.user.top_role.mention}
**Roles** - {len(self.user.roles)}
**In voice channel** - {voice_state}
**Joined server** - <t:{round(tsj)}:R>
**Join position** - {str(members.index(self.user)+1)}
              """, color=discord.Colour.random())
            embed2.set_author(name=f"{self.user}", icon_url=f"{self.user.avatar.url}")
            embed2.set_footer(text=self.ctx.guild.name)
            embed2.set_thumbnail(url=self.user.avatar.url)
            embed2.timestamp = datetime.datetime.utcnow()
            await interaction.response.edit_message(embed=embed2)
        elif res == "Permissions":
            embed1 = discord.Embed(title="Permissions", description=f"`{perm_string}`", color=discord.Colour.random())
            await interaction.response.send_message(embed=embed1, ephemeral=True)

class whoisView(discord.ui.View):
    def __init__(self, ctx, message, user):
        super().__init__(timeout=120.0)
        self.ctx = ctx
        self.message = message
        self.user = user
        self.add_item(whoisSelect(ctx, message, user))

    async def interaction_check(self, interaction):
        if interaction.user.id == self.ctx.author.id:
            return True
        await interaction.response.send_message("This is not your Interaction", ephemeral=True)
        return False

    async def on_timeout(self):
        await self.message.edit(view=None)
        self.stop()

class serverinfoSelect

class serverinfoView(discord.ui.View):
    def __init__(self, ctx, message):
        super().__init__(timeout=120.0)
        self.ctx = ctx
        self.message = message

    async def interaction_check(self, interaction):
        if interaction.user.id == self.ctx.author.id:
            return True
        await interaction.response.send_message("This is not your Interaction", ephemeral=True)
        return False

    async def on_timeout(self):
        await self.message.edit(view=None)
        self.stop()

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process(os.getpid())


    @commands.command(aliases=["botinfos"])
    @commands.bot_has_permissions(embed_links=True)
    async def botinfo(self, ctx):
      x = load_time - datetime.datetime.utcnow()
      y = humanize.precisedelta(x, minimum_unit="seconds")
      ramUsage = self.process.memory_full_info().rss / 1024**2
      embed = discord.Embed(title="Botinfos!", description=f"""
              **Ping** 🏓\nThe bots ping is {(round(self.bot.latency * 1000))}ms!\n\n**Uptime** 📡\nThe bots uptime is {y} / <t:{round(n)}:R> / <t:{round(n)}>\n\n**Servers** 🖥️\n{str(len(self.bot.guilds))}\n
**Ram usage** 🧬
{ramUsage:.2f} MB
              """, color=0x71368a)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text="haha botinfos go brrrr")
      msg = await ctx.reply(embed=embed)
      await msg.edit(view=DropdownView(ctx.author, msg, self.bot))


  
    @commands.command(aliases=["ei", "ej", "einfo"])
    @commands.bot_has_permissions(embed_links=True, external_emojis=True)
    async def emojiinfo(self, ctx, emoji: discord.Emoji):
      emoji = await emoji.guild.fetch_emoji(emoji.id)
      is_managed = "Yes" if emoji.managed else "No"
      is_animated = "Yes" if emoji.animated else "No"
      requires_colons = "Yes" if emoji.require_colons else "No"
      creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
      can_use_emoji = "Everyone" if not emoji.roles else " ".join(role.name for role in emoji.roles)

      description = f"""
**__General:__**
**Name:** {emoji.name}
**ID:** {emoji.id}
**URL:** [Link to emoji]({emoji.url})
**Author:** {emoji.user.mention}
**Time Created:** {creation_time}
**Usable by:** {can_use_emoji}

**__Other:__**
**Animated:** {is_animated}
**Managed:** {is_managed}
**Requires colons:** {requires_colons}
**Guild Name:** {emoji.guild.name}
**Guild ID:** {emoji.guild.id}
        """
      embed = discord.Embed(title=f"**Emoji information for** `{emoji.name}`", description=description, color=0x71368a)
      embed.set_thumbnail(url=emoji.url)
      await ctx.reply(embed=embed)

    @commands.command(aliases=["userinfo", "ui"])
    @commands.bot_has_permissions(embed_links=True)
    async def whois(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        embed = discord.Embed(title="Userinfo!", description=f"""
**Select something from the dropdown menu to see infos about yourself!**
        """, color=discord.Colour.random())
        embed.set_author(name=f"{ctx.author}", icon_url=f"{user.avatar.url}")
        embed.set_footer(text=ctx.guild.name)
        embed.timestamp = datetime.datetime.utcnow()
        message = await ctx.send(embed=embed)
        view = whoisView(ctx, message, user)
        await message.edit(view=view)
  
    @commands.command(aliases=["si", "sv"])
    @commands.bot_has_permissions(embed_links=True)
    async def serverinfo(self, ctx):
        emoji_count = len(ctx.guild.emojis)
        online = 0
        for i in ctx.guild.members:
          if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
            online += 1
        created_at = ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
        bot = 0
        human = 0
        for member in ctx.guild.members:
          if member.bot:
            bot=bot+1
          else:
            human = human+1
        a = random.randrange(1, 10000)
        b = ["a", "b", "c", "d", "f", "g"]
        c = random.choice(b)
        d = str(a)+c      
        gembed = discord.Embed(title="Server information", description="**Choose a category from the dropdown menu, to see specific information about this server.**", color=discord.Colour.random())
        gembed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar.url}")
        gembed.set_footer(text=ctx.guild.name)
        gembed.timestamp = datetime.datetime.utcnow()
        await ctx.reply(embed=gembed)

    @serverinfo.error
    async def serverinfo_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def anime(self, ctx, *, query = None):
      async with ctx.typing():
        if query is None:
          await ctx.reply("You need to input an anime to search for!")
          return
        try:
            anime = animec.Anime(query)
        except:
            embederror = discord.Embed(title="Error!", description="No corresponding Anime is found for the search query!", color=0xFF0000)
            await ctx.reply(embed=embederror)
            return
        async with ctx.typing():
          embedanime = discord.Embed(title=f"ENG Name: {anime.title_english} / Japanese Name: {anime.title_jp} / Alt Names: {anime.alt_titles}", url=anime.url, description=f"{anime.description[:300]}[...]({anime.url})", color=0x71368a)
          animeprod = ", ".join(anime.producers)
          embedanime.add_field(name="Producers", value=f"{animeprod[:50]}[...]({anime.url})")
          embedanime.add_field(name="Broadcast", value=str(anime.broadcast))
          embedanime.add_field(name="Rating", value=str(anime.rating))
          embedanime.add_field(name="Status", value=str(anime.status))
          embedanime.add_field(name="Genres", value=", ".join(anime.genres))
          embedanime.add_field(name="Top Anime List", value=str(anime.popularity))
          embedanime.add_field(name="Type", value=str(anime.type))
          embedanime.add_field(name="NSFW Status", value=str(anime.is_nsfw()))
          embedanime.add_field(name="Episodes", value= str(anime.episodes))
          embedanime.set_thumbnail(url=anime.poster)
          animerec = ", ".join(anime.recommend())
          embedanime.set_footer(text=f"Similar animes: {animerec[:50]}...")
          if str(anime.is_nsfw()) == "True":
            if ctx.channel.is_nsfw() == True:
              await ctx.reply(embed=embedanime)
            elif ctx.channel.is_nsfw() != True:
              embedee = discord.Embed(title="Error!", description="Due the fact that this command is marked as NSFW, you need to use this command in an NSFW channel. If you don't know how you're able to make a channel available for NSFW commands/set the channel to NSFW, click [Here](https://www.minitool.com/news/nsfw-discord.html) to see a tutorial for it.", color=discord.Colour.dark_red())
              await ctx.reply(embed=embedee)
          else:
            embedanime.set_thumbnail(url=anime.poster)
            await ctx.reply(embed=embedanime)
            pass
    @anime.error
    async def anime_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command(alises=["aw", "awaifu", "animew"])
    @commands.bot_has_permissions(embed_links=True)
    async def animewaifu(self, ctx, *, query = None):
        if query is None:
          await ctx.reply("You need to input a waifu to search for!")
          return
        try:
            char = animec.Charsearch(query)
        except:
            embederror = discord.Embed(title="Error!", description="No corresponding Anime Character is found for the search query!", color=0xFF0000)
            await ctx.reply(embed=embederror)
            return
        embedchar = discord.Embed(title=char.title, url=char.url, color=0x71368a)
        embedchar.set_image(url=char.image_url)
        embedchar.set_footer(text=f", ".join(list(char.references.keys())[:2]))
        await ctx.reply(embed=embedchar)
    @animewaifu.error
    async def animewaifu_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def animenews(self, ctx, amount:int=5):
      async with ctx.typing():
          news = animec.Aninews(amount)
          links = news.links
          titles = news.titles
          descriptions = news.description
          embed = discord.Embed(title="Latest Anime News", color=0x71368a)
          embed.set_thumbnail(url=news.images[0])
          for i in range(amount):
              embed.add_field(name=f"{i+1}) {titles[i]}", value=f"{descriptions[i][:100]}...\n[Read more]({links[i]})", inline=False)
          await ctx.reply(embed=embed)
    @animenews.error
    async def animenews_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command(aliases=["ri"])
    @commands.bot_has_permissions(embed_links=True)
    async def roleinfo(self, ctx, role: discord.Role = None):
      x = random.randint(0, 999)
      m = str(x)
      if role is None:
        await ctx.reply("Mention an existing role!")
        return
      perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in role.permissions if p[1]])
      embedm = discord.Embed(title=f"Role Infos", color=role.color)
      embedm.add_field(name="Role Name / ID", value=f"<@&{role.id}> / {role.id}", inline=False)
      embedm.add_field(name="Role Created At", value=f"<t:{round(role.created_at.timestamp())}> / <t:{round(role.created_at.timestamp())}:R>", inline=False)
      embedm.add_field(name="Role Members", value=len(role.members), inline=False)
      embedm.add_field(name="Role Position", value=role.position, inline=False)
      embedm.add_field(name="Hexa Color", value=f"{str(role.color)}")
      embedm.set_thumbnail(url=ctx.guild.icon_url)
      msg = await ctx.reply(embed=embedm, components=[Select(
        placeholder="Select something",
        options=[
          SelectOption(label="Infos", value="1", description="Get infos about the mentioned role!"),
          SelectOption(label="Values", value="2", description="Get the values about the mentioned role!"),
          SelectOption(label="Permissions", value="3", description="Get the permissions about the mentioned role!")],
          custom_id=m)])
      while True:
        try:
          msg = await self.bot.wait_for("select_option", check=lambda inter: inter.custom_id == m and inter.user == ctx.author, timeout=30.0)
          res = msg.values[0]
          if res == "1":
            await msg.edit_origin(embed=embedm)
          if res == "2":
            embedv = discord.Embed(title="Role Values", color=role.color)
            embedv.add_field(name="Role Mentionable by everyone?", value=role.mentionable, inline=False)
            embedv.add_field(name="Displayed from others?", value=f"{role.hoist}", inline=False)
            embedv.add_field(name="Nitro Role", value=role.is_premium_subscriber(), inline=False)
            embedv.add_field(name="Bot Role", value=role.is_bot_managed(), inline=False)
            embedv.set_thumbnail(url=ctx.guild.icon_url)
            await msg.edit_origin(embed=embedv)
          if res == "3":
            embedp = discord.Embed(title="Role Permissions", description=perm_string, color=role.color)
            await msg.send(embed=embedp)
        except asyncio.TimeoutError:
          pass


async def setup(bot):
    await bot.add_cog(info(bot))