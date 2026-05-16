import asyncio
from discord.ext import commands
import discord
from discord import app_commands

class TicketPanel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

        self.staff_role = int(self.config["staff_role_id"])
        self.channel_categories = int(self.config["ticket_categories"])
        self.owner_role = int(self.config["owner_role_id"])
        self.user_tickets = {}

    @app_commands.command(name="ticket", description="Send ticket panel")
    async def ticket(self, interaction: discord.Interaction):
        if self.owner_role is None:
            return await interaction.response.send_message("Owner Role")
        embed = discord.Embed(
            title=self.config["embed_title"],
            description=self.config["embed_description"],
            color=discord.Color.dark_blue()
        )

        embed.set_footer(
            text=self.config["embed_footer"],
            icon_url=self.bot.user.display_avatar.url
        )

        await ctx.send(embed=embed, view=TicketView(self))


class TicketSelect(discord.ui.Select):
    def __init__(self, cog):
        self.cog = cog

        options = [
            discord.SelectOption(label="💸Subscription", description="Open subscription ticket"),
            discord.SelectOption(label="📞Support", description="Ask for help"),
            discord.SelectOption(label="🤝Collab", description="Collaboration request")
        ]



        super().__init__(
            placeholder="Choose ticket type",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        cog = self.cog
        user_id = interaction.user.id

        if user_id in cog.user_tickets:
            return await interaction.response.send_message(
                "❌ You already have a ticket open!",
                ephemeral=True
            )

        choice = self.values[0]
        category_id = cog.channel_categories[choice]
        category = interaction.guild.get_channel(category_id)

        channel = await interaction.guild.create_text_channel(
            name=f"{choice.lower()}-{interaction.user.name}",
            category=category,
            overwrites={
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                interaction.guild.get_role(cog.staff_role): discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=True
                )
            }
        )

        cog.user_tickets[user_id] = channel.id

        await interaction.response.send_message(
            f"✅ Ticket created: {channel.mention}",
            ephemeral=True
        )

        embed = discord.Embed(
            title="Ticket System",
            description=f"{interaction.user.mention} please wait for staff.",
            color=discord.Color.dark_blue()
        )

        await channel.send(embed=embed, view=TicketClose(cog))


class TicketView(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.add_item(TicketSelect(cog))


class TicketClose(discord.ui.View):
    def __init__(self, cog):
        super().__init__()
        self.cog = cog

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.red)
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):

        owner_id = None

        for user_id, channel_id in self.cog.user_tickets.items():
            if channel_id == interaction.channel.id:
                owner_id = user_id
                break

        if owner_id:
            self.cog.user_tickets.pop(owner_id, None)

        await interaction.response.send_message(
            "Ticket will be deleted in 10 seconds",
            ephemeral=True
        )

        await asyncio.sleep(10)
        await interaction.channel.delete()


async def setup(bot):
    await bot.add_cog(TicketPanel(bot))