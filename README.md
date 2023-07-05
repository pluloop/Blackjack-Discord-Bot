# Blackjack-Discord-Bot
A Discord bot to play the popular card game Blackjack!

### How to set up: (You must have Discord)
1. Go to Developer Portal and press new application to make your bot.
2. On the sidebar, go to "Bot"; scroll down; and under "Privileged Gateway Intents", select "PRESENSE INTENT", "SERVER MEMBERS INTENT", and "MESSAGE CONTENT INTENT."
3. On the sidebar, go to OAuth2; below, press URL Generator; under scopes, select "bot"; and under bot permissions select "Administrator."
4. Scroll down and copy the Generated URL, paste the URL into a new tab and add bot to server of choice.
5. After, create a project and copy and paste code from main.py and apikeys.py into it.
6. Go back to Developer Portal and on the side bar, press "Bot"; press "Reset Token" and copy it; assign it to variable "bot_token" (make sure it is a string)
7. Replace "from apikeys import api_keys_list" if needed if you made a different named file.
8. In the terminal, type pip install discord.py
And that is it! Everything should be all good and ready to go.

**Reminder** *Make sure to put your own token!*
![image](https://github.com/pluloop/Blackjack-Discord-Bot/assets/113864920/19ee7d09-c51d-4947-9dbd-b3b3a7926ab4)
