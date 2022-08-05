import discord
import datetime
from discord.ext import commands



class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


  
    @commands.command(aliases=["clear", "deletemessages"])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(read_messages = True, manage_messages = True, read_message_history = True)
    async def purge(self, ctx, amount: int):
      if amount <1:
        ee = discord.Embed(title="Error!", description="You can't delete no messages!", color=discord.Colour.dark_red())
        await ctx.reply(embed=ee)
      elif amount >100:
        ee = discord.Embed(title="Error!", description="You can't delete more than 100 message at once!", color=discord.Colour.dark_red())
        await ctx.reply(embed=ee)
      else:
        count_members = {}
        messages = ctx.channel.history(limit=amount)
        async for message in messages:
          if str(message.author) in count_members:
            count_members[str(message.author)] += 1
          else:
            count_members[str(message.author)] = 1
        new_string = []
        messages_deleted = 0
        for author, message_deleted in list(count_members.items()):
          new_string.append(f"**{author}**: `{message_deleted}`")
          messages_deleted += message_deleted
        final_string = "\n".join(new_string)
        await ctx.channel.purge(limit=amount +1)
        await ctx.send(f"> {messages_deleted} messages were removed. \n\n{final_string}", delete_after=7.5)

  
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members = True, read_message_history = True, embed_links=True)
    async def ban(self, ctx, user: discord.Member, *, reason="No reason given."):
      timestampd = datetime.datetime.utcnow().timestamp()
      if user == ctx.message.author:
        embede = discord.Embed(title="Error!", description="You can't ban yourself!", color=discord.Colour.dark_red())
        await ctx.reply(embed=embede)
      elif user.top_role >= ctx.author.top_role:
        embedrole = discord.Embed(title="Error!", description="You can't ban someone who has a higher role then yourself.", color=discord.Colour.dark_red())
        await ctx.reply(embed=embedrole)
      else:
          try:
              embeddm = discord.Embed(title="User has been banned!", color=discord.Colour.dark_red())
              embeddm.add_field(name="Banned User", value=f"{user} / {user.id}", inline=False)
              embeddm.add_field(name="Moderator", value=f"{ctx.author} / {ctx.author.id}", inline=False)
              embeddm.add_field(name="Reason", value=reason, inline=False)
              embeddm.add_field(name="Time of the ban", value=f"<t:{round(timestampd)}> / <t:{round(timestampd)}:R>", inline=False)
              embeddm.add_field(name="DM Status", value="The user has been DMed about the ban.", inline=False)
              embeddm.set_thumbnail(url=ctx.guild.icon_url)
              await user.send(embed=embeddm)
              embedch = discord.Embed(title="User has been banned!", color=discord.Colour.dark_red())
              embedch.add_field(name="Banned User", value=f"{user} / {user.id}", inline=False)
              embedch.add_field(name="Moderator", value=f"{ctx.author} / {ctx.author.id}", inline=False)
              embedch.add_field(name="Reason", value=reason, inline=False)
              embedch.add_field(name="Time of the ban", value=f"<t:{round(timestampd)}> / <t:{round(timestampd)}:R>", inline=False)
              embedch.add_field(name="DM Status", value="The user has been DMed about the ban.", inline=False)
              embedch.set_thumbnail(url=ctx.guild.icon_url)
              await user.ban(reason=reason)
              await ctx.send(embed=embedch)
          except:
              embedch1 = discord.Embed(title="User has been banned", color=discord.Colour.dark_red())
              embedch1.add_field(name="Banned User", value=f"{user} / {user.id}", inline=False)
              embedch1.add_field(name="Moderator", value=f"{ctx.author} / {ctx.author.id}", inline=False)
              embedch1.add_field(name="Reason", value=reason, inline=False)
              embedch1.add_field(name="Time of the ban", value=f"<t:{round(timestampd)}> / <t:{round(timestampd)}:R>", inline=False)
              embedch1.add_field(name="DM Status", value="The user couldn't be DMed about the ban.", inline=False)
              embedch1.set_thumbnail(url=ctx.guild.icon_url)
              await ctx.send(embed=embedch1)



    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members = True, read_message_history = True, embed_links=True)
    async def softban(self, ctx, user: discord.Member, *, reason="No reason given."):
      timestampd = datetime.datetime.utcnow().timestamp()
      if user == ctx.message.author:
        embede = discord.Embed(title="Error!", description="You can't softban yourself!", color=discord.Colour.dark_red())
        await ctx.reply(embed=embede)
      elif user.top_role >= ctx.author.top_role:
        embedrole = discord.Embed(title="Error!", description="You can't softban someone who has a higher role then yourself.", color=discord.Colour.dark_red())
        await ctx.reply(embed=embedrole)
      else:
          try:
            embeddm = discord.Embed(title=f"You have been softbanned from {ctx.guild.name}!", description=f"**Moderator:** {ctx.author}\n**Reason:**  {reason}\n**Date:** <t:{round(timestampd)}:R> / <t:{round(timestampd)}>", color=discord.Colour.dark_red())
            embeddm.set_thumbnail(url=user.avatar_url)
            await user.send(embed=embeddm)
            embedch = discord.Embed(title="User has been softbanned!", description=f"**{user}** / **{user.id}** has been successfully banned.\n**Reason:** {reason}\n**Date:** <t:{round(timestampd)}:R> / <t:{round(timestampd)}>\n**DM Status:** The user has been DMed about the softban.", color=discord.Colour.dark_red())
            embedch.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embedch)
            await user.ban(delete_message_days=7)
            await user.unban()
          except:
            embedch1 = discord.Embed(title="User has been softbanned!", description=f"**{user}** / **{user.id}** has been successfully softbanned.\n**Reason:** {reason}\n**Date:** <t:{round(timestampd)}:R> / <t:{round(timestampd)}>\n**DM Status:** I wasn't able to DM the user about the softban.", color=discord.Colour.dark_red())
            embedch1.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embedch1)
            await user.ban(delete_message_days=7)
            await user.unban()



async def setup(bot):
    await bot.add_cog(moderation(bot))