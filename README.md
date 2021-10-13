# npc-spinner
Used for spinning NPCs based on desired traits.  

## Usage 
There are now three interfaces:
 * GET /npc - generates an NPC, query params for race, gender, archtype, and trait count
 * POST /npc_slack - Same as above but designed for Slack integration.  Returns the same data in slack-response format.
 * Discord bot - more details below
 
 
## Discord Bot
In /discord_bot, you'll find a file `bot.py` which contains a very simnple discord bot interface.  You can follow these helpful instructions on DevDungeon on how to set up your discord bot - follow along, but use this code instead of the sample they've provided (be sure to enter your key where specified in order to connect to your server).  

https://www.devdungeon.com/content/make-discord-bot-pythaon

 
## Acknowledgements
Personality traits from MIT's Ideonomy site - http://ideonomy.mit.edu/essays/traits.html

Racial First/Last names from Amon Kareth: Vault of Death - https://amon-kareth-vault-of-death.obsidianportal.com/wiki_pages/pregenerated-names

Discord bot setup - DevDungeon https://www.devdungeon.com/content/make-discord-bot-pythaon
 
