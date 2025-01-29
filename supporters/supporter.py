import discord
from redbot.core import commands, Config, tasks

class SupportersRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.supporter_role_id = 1333878640836087939
        self.supporter_roles_ids = [
            1049435358921768960,
            1306140535714746380,
            1330228125421801563,
            1330245591120216086,
            1330253265081860157,
            1330808905181429824,
            1330253044570394634,
            1330252787786973184,
            1330251250255663184,
            1330249471354863700,
            689246700531220535,
            689246700531220532,
            689246700531220525
        ]
        self.check_supporters_task.start()

    def cog_unload(self):
        self.check_supporters_task.cancel()

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        guild = after.guild
        supporter_role = guild.get_role(self.supporter_role_id)
        if not supporter_role:
            return  # The "Supporters" role does not exist

        has_supporter_role = supporter_role in after.roles
        has_required_role = any(role.id in self.supporter_roles_ids for role in after.roles)

        if has_required_role and not has_supporter_role:
            await after.add_roles(supporter_role, reason="User gained a supporter role.")
        elif not has_required_role and has_supporter_role:
            await after.remove_roles(supporter_role, reason="User lost all supporter roles.")

    @commands.command()
    @commands.admin_or_permissions(manage_roles=True)
    async def check_supporters(self, ctx):
        """Manually checks and updates the Supporters role for all members."""
        await self.update_supporters_roles(ctx.guild)
        await ctx.send("Supporters role check completed.")

    @tasks.loop(minutes=30)
    async def check_supporters_task(self):
        """Periodically checks and updates the Supporters role for all members."""
        for guild in self.bot.guilds:
            await self.update_supporters_roles(guild)

    async def update_supporters_roles(self, guild):
        supporter_role = guild.get_role(self.supporter_role_id)
        if not supporter_role:
            return

        for member in guild.members:
            has_required_role = any(role.id in self.supporter_roles_ids for role in member.roles)
            has_supporter_role = supporter_role in member.roles
            
            if has_required_role and not has_supporter_role:
                await member.add_roles(supporter_role, reason="User gained a supporter role.")
            elif not has_required_role and has_supporter_role:
                await member.remove_roles(supporter_role, reason="User lost all supporter roles.")

async def setup(bot):
    await bot.add_cog(SupportersRole(bot))
