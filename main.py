from instabot import Bot
bot=Bot()
bot.login(username="_______",password="_________")
print("Logged in Successfully !")
bot.follow("chennaiipl")
# bot.upload_photo()
bot.send_message("I LOVE MSDHONI",["chennaiipl","virat.kohli"])
print("Message Send Successfully !")
following=bot.get_user_following("virat.kohli")
for Following in following:
    print(bot.get_user_info(following))
print("Successfully Fetched !")