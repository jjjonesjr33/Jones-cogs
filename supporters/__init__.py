import json
from pathlib import Path
from .supporter import SupportersRole

# Load the end user data statement from the info.json file
with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]

# Setup the cog for Redbot
async def setup(bot):
    cog = SupportersRole(bot)
    await bot.add_cog(cog)
