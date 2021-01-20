from discord.ext import commands, tasks
import meetup_rest_api as mra 

target_channel_id = 800142295092953098
bot = commands.Bot("!")

@tasks.loop(seconds=10)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    update = mra._get_upcoming()
    print(update)

    if update != "No New Updates":
        await message_channel.send(update)
    else:
        break

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
bot.run('Token_Secret')