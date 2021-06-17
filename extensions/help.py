import discord,data
from logger import logOutput
from discord.ext.commands import Cog
from discord_slash import cog_ext,SlashContext

helpData = data.load('help')
bot = data.load('bot')


class help(Cog):
	@cog_ext.cog_subcommand(base='help',name='command',description='help on commands')
	async def help_command(self,ctx:SlashContext,command):
		try: cmd = helpData.read([command])
		except KeyError: await ctx.send('unknown command name'); return
		e = discord.Embed(title=f'{command} help',color=bot.read(['config','embedColor']))
		e.add_field(name='usage',value=cmd['usage'],inline=False)
		e.add_field(name='permissions',value=cmd['permissions'],inline=False)
		e.add_field(name='description',value=cmd['description'],inline=False)
		await ctx.send(embed=e)

	@cog_ext.cog_subcommand(base='help',name='list',description='list all commands')
	async def help_list(self,ctx:SlashContext):
		await ctx.send(embed=discord.Embed(
			title='List of commands:',
			description='\n'.join(list(helpData.read().keys())),
			color=bot.read(['config','embedColor'])))
		logOutput('command list requested',ctx)




def setup(client): client.add_cog(help(client))