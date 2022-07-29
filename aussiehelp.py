import discord
from discord.ext import commands


class AnAussieHelpCommand(commands.MinimalHelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Discord Help", colour=discord.Colour.random())
        for cog, commands in mapping.items():
            filterer = await self.filter_commands(commands, sort=True)
            commands = [self.get_command_signature(c) for c in filterer]
            commands = "\n".join(commands)
            if commands:
                cog_name = getattr(cog, "qualified_name", "No Category")
                if cog_name != "Hidden" and cog_name != "Error":
                    embed.add_field(name=cog_name, value=f"\n`{commands}`", inline=False)
        await self.get_destination().send(embed=embed)


    async def send_command_help(self, command):
        try:
            example = command.extras['example']
        except KeyError:
            example = None

        desc = command.description if command.description else "There is no description"

        embed = discord.Embed(title=f"a!{command.name}",
                              color=discord.Colour.random())
        embed.add_field(name="**Description:**", value=desc, inline=False)

        if len(command.aliases):
            #i just got Golder06's code because I had no idea how to get aliases
            aliases = [command.qualified_name]
            aliases.extend(command.aliases)
            aliases = [f"`a!{alias}`" for alias in aliases]
            embed.add_field(name="**Aliases:**", value=', '.join(aliases), inline=False)

        bob = f"{self.get_command_signature(command)}"
        if example:
            bob += f"\nExample: `a!{command.name} {example}`"

        embed.add_field(name="**Use**:", value=f"{self.get_command_signature(command)}", inline=False)

        await self.get_destination().send(embed=embed)