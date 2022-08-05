import datetime
import discord
import json
from discord.ext import commands


class MarryApproving(discord.ui.View):
  def __init__(self, buttonuser, messageauthor, message, timeout=30):
    super().__init__(timeout=timeout)
    self.buttonuser = buttonuser
    self.messageauthor = messageauthor
    self.message = message
    
  async def interaction_check(self, interaction: discord.Interaction):
    if str(interaction.user.id) in str(self.buttonuser.id):
      return True
    await interaction.response.send_message(f'This interaction can only be used by {self.buttonuser}.', ephemeral=True)
    return False

  async def on_timeout(self):
    self.clear_items()
    self.add_item(discord.ui.Button(label="Timeouted ⏰", style=discord.ButtonStyle.red, disabled=True))
    await self.message.edit(view=self)
    self.stop()
  
  @discord.ui.button(label="Accept", style=discord.ButtonStyle.green)
  async def AcceptButton(self, interaction: discord.Interaction, child: discord.ui.Button):
    
    for child in self.children:
      child.disabled=True

    x = datetime.datetime.utcnow().timestamp()
    embedy = discord.Embed(title="Successfully proposed!", description=f"Congratulations! {self.messageauthor.mention} & {self.buttonuser.mention} are now officially married since <t:{round(x)}:R>", color=discord.Colour.green())
    embedy.set_thumbnail(url=interaction.guild.icon)
    embedy.set_author(name=self.messageauthor, icon_url=self.messageauthor.avatar)

    users = await self.get_profile_data()
    
    x = datetime.datetime.utcnow().timestamp()
    y = round(x)
    users[str(self.messageauthor)]["Married"] = "True"
    users[str(self.buttonuser)]["TStamp"] = y
    users[str(self.messageauthor)]["TStamp"] = y
    users[str(self.buttonuser)]["Married"] = "True"
    users[str(self.messageauthor)]["Partner"] = str(self.buttonuser)
    users[str(self.buttonuser)]["Partner"] = str(self.messageauthor)
    users[str(self.buttonuser)]["Guild"] = str(interaction.guild.name)
    users[str(self.messageauthor)]["Guild"] = str(interaction.guild.name)
    with open("json_files/marriage.json", "w") as f:
      json.dump(users, f)
    await interaction.response.edit_message(embed = embedy, view=self)
    
  @discord.ui.button(label="Deny", style=discord.ButtonStyle.red)
  async def DenyButton(self, interaction: discord.Interaction, child: discord.ui.Button):
    for child in self.children:
      child.disabled=True
    embedn = discord.Embed(title="Failed proposing!", description=f"I'm sorry to say this {self.messageauthor.mention}, but sadly {self.buttonuser.mention} declined you as their partner.", color=discord.Colour.red())
    embedn.set_thumbnail(url=interaction.guild.icon)
    embedn.set_author(name=self.messageauthor, icon_url=self.buttonuser.avatar)
    await interaction.response.edit_message(embed=embedn, view=self)


  async def get_profile_data(self):
    with open("json_files/marriage.json", "r") as f:
      users = json.load(f)
    return users
    
  async def open_account(self, user):
    users = await self.get_profile_data()
    if str(user) in users:
      return False
    else:
      users[str(user)] = {}
      users[str(user)]["Married"] = "False"
      users[str(user)]["Partner"] = "None"
      users[str(user)]["Guild"] = "None"
      users[str(user)]["TStamp"] = 0
      with open("json_files/marriage.json", "w") as f:
        json.dump(users, f)
      return True



class DivorceApproving(discord.ui.View):
  def __init__(self, messageauthor, message, mentioneduser, timeout=30):
    super().__init__(timeout=timeout)
    self.messageauthor = messageauthor
    self.message = message
    self.mentioneduser = mentioneduser

  async def interaction_check(self, interaction: discord.Interaction):
    if str(interaction.user.id) in str(self.messageauthor.id):
      return True
    await interaction.response.send_message(f'This interaction can only be used by {self.messageauthor}.', ephemeral=True)
    return False

  async def on_timeout(self):
    self.clear_items()
    self.add_item(discord.ui.Button(label="Timeouted ⏰", style=discord.ButtonStyle.red, disabled=True))
    await self.message.edit(view=self)
    self.stop()

  @discord.ui.button(label="Continue", style=discord.ButtonStyle.green)
  async def AceceptButton(self, interaction: discord.Interaction, child: discord.ui.Button):
    for child in self.children:
      child.disabled=True
    embedn = discord.Embed(title="You divorced your partner.", description=f"You have successfully divorced {self.mentioneduser}...", color=discord.Colour.red())
    embedn.set_thumbnail(url=self.messageauthor.avatar)
    embedn.set_author(name=self.messageauthor, icon_url=self.messageauthor.avatar)
    with open("json_files/marriage.json", "r") as f:
      users = json.load(f)
    users[str(self.messageauthor)]["Married"] = "False"
    users[str(self.mentioneduser)]["TStamp"] = 0
    users[str(self.messageauthor)]["TStamp"] = 0
    users[str(self.mentioneduser)]["Married"] = "False"
    users[str(self.messageauthor)]["Partner"] = ""
    users[str(self.mentioneduser)]["Partner"] = ""
    users[str(self.mentioneduser)]["Guild"] = ""
    users[str(self.messageauthor)]["Guild"] = ""
    with open("json_files/marriage.json", "w") as f:
      json.dump(users, f)      
    await interaction.response.edit_message(embed=embedn, view=self)
    
  
  @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
  async def DenyButton(self, interaction: discord.Interaction, child: discord.ui.Button):
    for child in self.children:
      child.disabled=True
    embedn = discord.Embed(title="Cancelled divorcing.", description=f"You didn't divorce your partner.", color=discord.Colour.green())
    embedn.set_thumbnail(url=self.messageauthor.avatar)
    embedn.set_author(name=self.messageauthor, icon_url=self.messageauthor.avatar)
    await interaction.response.edit_message(embed=embedn, view=self)

    

class marry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def marry(self, ctx, member: discord.Member):
      await self.open_account(ctx.author)
      await self.open_account(member)
      users = await self.get_profile_data()
      a = users[str(ctx.author)]["Married"]
      b = users[str(member)]["Married"]
      if a == "True":
        await ctx.reply("You can't betray your partner! smh")
      elif b == "True":
        await ctx.reply("The mentioned user already has a partner!")
      elif member.mention == ctx.author.mention:
        await ctx.reply("You can't marry yourself!")
      else:
        embed = discord.Embed(title="Proposing", description=f"Hey {member.mention}! {ctx.author.mention} wants to marry you, will you accept them as your Husband/Wife?", color=discord.Colour.green())
        embed.set_thumbnail(url=ctx.guild.icon)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar)
        p = await ctx.reply(embed=embed)        
        await p.edit(view=MarryApproving(member, ctx.author, p))


  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def status(self, ctx, user: discord.Member = None):
          user = user or ctx.author
          await self.open_account(user)
          users = await self.get_profile_data()
          a = users[str(user)]["Married"]
          b = users[str(user)]["TStamp"]
          c = users[str(user)]["Partner"]
          d = users[str(user)]["Guild"]
          if b == 0:
            embed1 = discord.Embed(title="", description=f"**{user} isn't married yet.**", color=discord.Colour.random())
            embed1.set_thumbnail(url=user.avatar)
            embed1.set_author(name="Relationship status", icon_url=user.avatar)
            await ctx.send(embed=embed1)
          else:
            embed2 = discord.Embed(title="", description=f"__Marriage status is {a}.__\n**Current relationship between {user} and {c} goes since <t:{b}> / <t:{b}:R>.** \n`They both married in the guild {d}`", color=discord.Colour.random())
            embed2.set_thumbnail(url=user.avatar)
            embed2.set_author(name="Relationship status", icon_url=user.avatar)
            await ctx.send(embed=embed2)



    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def divorce(self, ctx):
      await self.open_account(ctx.author)
      users = await self.get_profile_data()
      a = users[str(ctx.author)]["Married"]
      c = users[str(ctx.author)]["Partner"]
      if a == "False":
        await ctx.reply("You're not married!")
      if a == "True":
        embed = discord.Embed(title="Oh oh!", description=f"{ctx.author.mention} do you really want to divorce {c}? I bet they won't be happy about this...", color=discord.Colour.red())
        embed.set_footer(text="Think twice!", icon_url=ctx.author.avatar)
        embed.set_thumbnail(url=ctx.author.avatar)
        embed.timestamp = datetime.datetime.utcnow()
        divorceclass = await ctx.reply(embed=embed)
        await divorceclass.edit(view=DivorceApproving(ctx.author, divorceclass, c))

            
      
    async def open_account(self, user):
      users = await self.get_profile_data()
      if str(user) in users:
        return False
      else:
        users[str(user)] = {}
        users[str(user)]["Married"] = "False"
        users[str(user)]["Partner"] = "None"
        users[str(user)]["Guild"] = "None"
        users[str(user)]["TStamp"] = 0
      with open("json_files/marriage.json", "w") as f:
        json.dump(users, f)
      return True
  
    async def get_profile_data(self):
      with open("json_files/marriage.json", "r") as f:
        users = json.load(f)
      return users

async def setup(bot):
    await bot.add_cog(marry(bot))