# 🎫 Discord Ticket System Bot

A fully modular Discord ticket system built with Python (discord.py).  
Designed for professional server support, collaboration requests, and structured ticket management using modern Discord UI components (Select Menus + Buttons).

---

## 🚀 Features

- 🎯 Interactive dropdown ticket creation system
- 🔒 One active ticket per user protection
- 👮 Owner-only slash command access
- 📁 Dynamic category-based ticket routing system
- 🧠 Modular cog-based architecture
- ❌ Automatic ticket close system
- ⚙️ Fully configurable via `config.json`
- 🧩 Clean Discord UI (Select Menus + Buttons)
- 🚀 Slash command support

---

## 🧠 How It Works

1. Only users with the **Owner Role** can use `/ticket`
2. The bot sends a ticket panel
3. Users choose a ticket category from the dropdown menu
4. The bot automatically:

   - Creates a private ticket channel
   - Assigns correct permissions
   - Moves ticket to the selected category
   - Prevents duplicate tickets

5. Ticket can be closed with the close button

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Configure the bot

Rename:

```txt
config.json.example → config.json
```

Fill in:

- Bot token
- Owner role ID
- Staff role ID
- Ticket categories
- Embed information

---

### 3. Run the bot

```bash
python main.py
```

---

### 4. Use the bot

Run:

```txt
/ticket
```

Only users with the configured Owner Role can create ticket panels.

---

## 🔐 Permissions System

| Action | Permission |
|----------|-------------|
| Create ticket panel (`/ticket`) | Owner Role only |
| Create ticket | Everyone |
| Access ticket | User + Staff Role |
| Close ticket | Staff / Authorized users |

---

## 📁 Project Structure

```txt
cogs/
 └── ticket.py

main.py
config.json.example
requirements.txt
README.md
```

---

## ⚙️ Configuration Example

```json
{
    "token":"YOUR_BOT_TOKEN",

    "owner_role_id":123456789,
    "staff_role_id":987654321,

    "ticket_categories":{
        "💸Subscription":{
            "category_id":111111111,
            "description":"Subscription requests"
        },

        "📞Support":{
            "category_id":222222222,
            "description":"Support requests"
        },

        "🤝Collab":{
            "category_id":333333333,
            "description":"Collaboration requests"
        }
    },

    "embed_title":"Ticket System",
    "embed_description":"Open a ticket below",
    "embed_footer":"Support System"
}
```

---

## 🧱 Requirements

- Python 3.10+
- discord.py

---

## 🛡️ Security Notes

- Never upload your real `config.json`
- Never expose your bot token
- Use `.gitignore`
- Keep sensitive data private

---

## 📌 Notes

This bot is designed to be:

- Reusable
- Easy to configure
- Easy to extend
- Dynamic through configuration
- Portfolio and client ready

---

## 🧑‍💻 Tech Stack

- Python
- discord.py
- Discord UI Components
- Cogs architecture

---

## 🔥 Author

Easy-to-configure Discord Ticket System Bot built for portfolio use.