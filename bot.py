from pyrogram import Client, filters
import re
import os

# Fetch bot credentials from environment variables
API_ID = int(os.getenv("API_ID"))  
API_HASH = os.getenv("API_HASH")  
BOT_TOKEN = os.getenv("BOT_TOKEN")  

# Fetch channel usernames from environment variables
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")  
DEST_CHANNEL = os.getenv("DEST_CHANNEL")  

# Predefined caption template
CAPTION_TEMPLATE = """𝖪𝖾𝗒 𝖴𝗉𝖽𝖺𝗍𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒  ✅

Key - `{}`

𝗡𝗼𝘁𝗲 : 
𝖨𝖿 𝖸𝗈𝗎 𝖲𝗁𝖺𝗋𝖾 𝖳𝗁𝗂𝗌 𝖯𝗈𝗌𝗍 ♻️
(𝟤𝟢𝟢 𝖲𝗁𝖺𝗋𝖾 - 𝟥𝖣𝖺𝗒𝗌 𝖪𝖾𝗒 𝖥𝗋𝖾𝖾)
(𝟣𝟢𝟢𝟢 𝖲𝗁𝖺𝗋𝖾 - 𝟥𝟢 𝖣𝖺𝗒𝗌 𝖪𝖾𝗒𝗌 𝖥𝗋𝖾𝖾)

💬 𝗕𝘂𝘆  - @LocalxCheats ✅
💬 𝗕𝘂𝘆  - @LocalxCheats ✅

       **𝗦𝗵𝗮𝗿𝗲 𝗮𝗻𝗱 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 🤍**
https://t.me/+gfQmH-wcGWllMTFl"""

# Initialize bot
bot = Client("apk_forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.channel & filters.document & filters.chat(SOURCE_CHANNEL))
async def forward_apk(client, message):
    # Extract the key from the source channel
    caption_text = message.caption or ""  # Ensure caption is a string
    key_match = re.search(r"Key\s*-\s*(\S+)", caption_text)
    extracted_key = key_match.group(1) if key_match else "Unknown"

    # Format the key for One-Tap Copy (Mono Text)
    formatted_key = f"`{extracted_key}`"  # Single backticks for Telegram Mono Text

    # Create the final caption with the formatted key
    formatted_caption = CAPTION_TEMPLATE.format(formatted_key)

    # Forward the APK without forward tags
    await client.send_document(
        chat_id=DEST_CHANNEL,
        document=message.document.file_id,
        caption=formatted_caption
    )

    print(f"APK forwarded with key: {extracted_key}")

# Start bot
print("Bot is running...")
bot.run()