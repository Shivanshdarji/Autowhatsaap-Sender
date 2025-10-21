# 💬 AutoWhatsApp-Sender 🤖  
Automate WhatsApp messages, images, and group chats with Python using **PyWhatKit**!  
Send texts, images, and more — all without manual effort. Perfect for reminders, bulk messages, or fun automation! 🚀  

---

## 🧠 What is AutoWhatsApp-Sender?
**AutoWhatsApp-Sender** is a Python-based automation tool that uses the `pywhatkit` library to:
- Automatically send WhatsApp messages to **individuals** or **groups**
- Send **images with captions**
- Perform **Google searches**, **YouTube video playback**, and more!

This tool helps you save time and schedule messages with full automation power.

---

## ⚙️ Installation

### Step 1: Install Python (if not already installed)
Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Step 2: Install PyWhatKit

pip install pywhatkit
Step 3: Install Other Optional Dependencies
pip install pyautogui
pip install wikipedia
pip install requests

💻 How It Works

PyWhatKit uses web.whatsapp.com and automates message typing and sending through your default browser.
Just make sure:

You’re logged into WhatsApp Web

You have a stable internet connection

Your browser remains open during execution
🚀 Basic Usage Examples
🟢 1. Send a WhatsApp Message to an Individual
import pywhatkit

# Format: phone number (with country code), message, hour, minute
pywhatkit.sendwhatmsg("+911234567890", "Hello from AutoWhatsApp-Sender!", 22, 30)

🕒 This will open WhatsApp Web at 10:30 PM and send your message automatically.

🟡 2. Send a Message Instantly (Without Scheduling)
pywhatkit.sendwhatmsg_instantly("+911234567890", "Hey! This is an instant message.")


⚡ Sends the message immediately without waiting for a scheduled time.

🔵 3. Send a Message to a WhatsApp Group
pywhatkit.sendwhatmsg_to_group("ABCD123EFGHijklMN", "Hello Group! Auto message test.", 21, 45)


📋 Group ID can be found from the group’s invite link (e.g., “https://chat.whatsapp.com/ABCD123EFGHijklMN”
).

🟣 4. Send a Group Message Instantly
pywhatkit.sendwhatmsg_to_group_instantly("ABCD123EFGHijklMN", "This is an instant group message!")

🖼️ 5. Send an Image with Caption
pywhatkit.sendwhats_image("+911234567890", "C:/Users/You/Pictures/sample.jpg", "Check out this image!")


🖼️ Sends an image with an optional caption.

🔍 6. Perform a Google Search
pywhatkit.search("Python programming tutorials")


🌐 Opens a Google search in your default browser.

🎵 7. Play a YouTube Video
pywhatkit.playonyt("Imagine Dragons Believer")


▶️ Automatically opens YouTube and plays the searched video.

📜 8. Convert Text to Handwriting
pywhatkit.text_to_handwriting("Hello, this is handwritten text!", "output.png", [0, 0, 138])


✍️ Creates a handwritten-style image from your text.

🧠 9. Get Information from Wikipedia
pywhatkit.info("Python programming language", lines=3)


📘 Fetches a short Wikipedia summary.

⚠️ Important Notes

WhatsApp Web must be logged in.

Time should be set 1-2 minutes ahead to allow the browser to load.

The script does not bypass WhatsApp security, it just automates your actions.

Use responsibly! 🚫 Don’t spam.

🧩 Example Full Project Script
import pywhatkit as kit

print("💬 AutoWhatsApp-Sender Starting...")

# Send to individual
kit.sendwhatmsg("+911234567890", "Hey there! This is an automated message.", 22, 15)

# Send to group
kit.sendwhatmsg_to_group("ABCD123EFGHijklMN", "Good night everyone!", 22, 30)

# Send image
kit.sendwhats_image("+911234567890", "C:/Users/You/Pictures/greet.jpg", "Good Morning 🌞")

print("✅ Messages scheduled successfully!")
