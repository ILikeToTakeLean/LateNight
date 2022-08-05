import datetime
import discord
import random
import wikipedia
from aiohttp import request
from discord.ext import commands



class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


  
    @commands.command(description="Get your/the mentioned users avatar.", aliases=["avatar"])
    @commands.bot_has_permissions(embed_links=True)
    async def av(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author
        png = str(user.avatar.with_format("png"))
        jpg = str(user.avatar.with_format("jpg"))
        webp = str(user.avatar.with_format("webp"))
        embed = discord.Embed(title="", description=f"Avatar of {user.mention}", color=discord.Colour.purple())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_image(url=f"{user.avatar.url}")
        embed.set_footer(text=f"Hottie! | Issued by {ctx.author}")
        AvatarView = discord.ui.View()
        AvatarView.add_item(discord.ui.Button(style=discord.ButtonStyle.url, url=png, label="PNG"))
        AvatarView.add_item(discord.ui.Button(style=discord.ButtonStyle.url, url=jpg, label="JPG"))
        AvatarView.add_item(discord.ui.Button(style=discord.ButtonStyle.url, url=webp, label="WEBP"))
      
        await ctx.reply(embed=embed, view=AvatarView)          

  
    @commands.command(description="Get the invite link for the bot.", aliases=["inv"])
    @commands.bot_has_permissions(embed_links=True)
    async def invite(self, ctx):
        embed = discord.Embed(title="Invite me!", description="Hey! Thank you for using my bot. You can invite me through [this link!](https://discord.com/oauth2/authorize?client_id=868817426937184306&scope=bot&permissions=8)", color=discord.Colour.purple())
        embed.set_footer(text="If you need help, make sure to contact one of the developers! deceased#3037 / Deprecated#8292")
        await ctx.reply(embed=embed)

  
  
    @commands.command(description="Get the link for the support server.")
    @commands.bot_has_permissions(embed_links=True)
    async def support(self, ctx):
      embed = discord.Embed(title="Support server", description="Hey, if you have some problems with the bot, make sure to join our support server and contact a developer. [Join here](https://discord.gg/XsmSy5emwt)", color=discord.Colour.purple())
      await ctx.reply(embed=embed)


  
    @commands.command(description="Use this command to get the vote links for the bot, as well as the support server.")
    @commands.bot_has_permissions(embed_links=True)
    async def vote(self, ctx):
      embed = discord.Embed(title="", description="📧 - [Vote for me!](https://top.gg/bot/868817426937184306/vote)\n📧 - [Vote for the support server](https://top.gg/servers/897866866557603890/vote)", color=discord.Colour.purple())
      embed.set_footer(text="You voted you hot")
      await ctx.reply(embed=embed)
      

  
    def wiki_summary(self, arg, features="lxml"):
      definition = wikipedia.summary(arg, sentences=6, chars=1000, auto_suggest=True, redirect=True)
      return definition

    @commands.command(description="Use this command to search for something on wikipedia.")
    @commands.bot_has_permissions(embed_links=True)
    async def wikipedia(self, ctx):
      try:
          message_content = ctx.message.content
          search = discord.Embed(title=f"**Searching...**", description=self.wiki_summary(message_content), color=discord.Colour.random())
          await ctx.reply(embed=search)
      except:
          eembed = discord.Embed(title="Error!", description="Something went wrong while fetching the data.", color=discord.Colour.dark_red())
          await ctx.reply(embed=eembed)

  

    @commands.command(description="Use this command to hug someone!")
    @commands.bot_has_permissions(embed_links=True)
    async def gif(self, ctx, search: str):
      url = f"https://g.tenor.com/v1/search?q={search}&key={tenorkey}&contentfilter=high" # I have removed the variable "tenorkey" as it had my API Key included.
      if search:
          async with request("GET", url, headers={}) as response:
            if response.status == 200:
              data = await response.json()
              content = data["results"]
              gifUrl = content[random.randint(0, len(content))]['url']
              await ctx.reply(gifUrl)
            else:
              await ctx.reply(f"API Exception. Server returned {response.status}")
      else:
            await ctx.reply("You need to input a search term.")


async def setup(bot):
    await bot.add_cog(utility(bot))
