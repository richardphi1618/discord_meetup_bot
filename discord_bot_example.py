from discord.ext import commands, tasks
import meetup_rest_api as mra 

target_channel_id = 800142295092953098 #change this to the channel id
bot = commands.Bot("!")

@tasks.loop(seconds=10) #change this to the interval you want to update 
async def update_announcements():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    update = mra._get_upcoming()

    if update != "No New Updates": await message_channel.send(update)
    else: pass
    
@update_announcements.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

update_announcements.start()
bot.run('ODAxMTk4NDU4NDU0MTQ3MDky.YAdMNg.ZN1Kb8pY7YpBe12pilfdb0jlc1o')