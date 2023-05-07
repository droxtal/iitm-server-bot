import discord
from discord import app_commands
from discord.ext import commands


class Slash(commands.Cog):
    """
    This Class is for Slash Commands.
    """

    def __init__(self, client):
        self.client = client

    # Help Command (Ephemeral)
    @app_commands.command(name='help', description='Displays list of commands and their usage')
    @app_commands.describe(command="Input Command Name")
    async def help(self, interaction: discord.Interaction, command: str=None):
        """
        Displays list of commands and their usage
        """
        if command=='help':
            output=discord.Embed(
                title="Help",
                description="Displays list of commands and their usage",
                color=0x00ff00)
        elif not command:
            output=discord.Embed(
                title="Help",
                description="""Hi 👋 I am ServerBot.
                Right now I can't do much. Seriously, your pet can do more tricks than me.
                If you have any ideas or feature suggestion for me please put them in #server-suggestions. My devlopers would love to have your suggestions.
                If you yourself want to teach me new tricks head over to https://github.com/droxtal/iitm-server-bot
                
                Here's a quick guide to use the /help command
                1. Type '/help' (without quotes)
                2. Hit space
                3. Type a command name that you want to know more about. You can refer the list of bot's slash commands that discord provides.
                
                Syntax: /help <some command>
                
                
                """,
                color=0x00ff00)
        else:
            output=discord.Embed(title="Error",description="Command not found",color=0xff0000)
        await interaction.response.send_message(embed=output, ephemeral=True)


async def setup(client):
    await client.add_cog(Slash(client))
