# Discord Bot for Minecraft Server Management

This Python script (`bot.py`) creates a Discord bot that allows users to manage a Minecraft server. The bot interacts with Discord messages to start, stop, check the status, ping, and get the player list of the Minecraft server. It uses the `mcstatus` library to monitor the Minecraft server's status.

SERVER MUST BE RUNNING ON A LINUX DISTRO WITH THE SCREEN TOOL

## Prerequisites

- Python environment with necessary dependencies installed (e.g., `mcstatus`, `discord`, `dotenv`)
- Discord bot token (`DISCORD_TOKEN`) and other environment variables configured in a `.env` file
- Minecraft server directory (`MINECRAFT_DIR`) and server IP addresses (`SERVER_IP_PUBLIC`, `SERVER_IP_LOCAL`) configured in the `.env` file
- A Minecraft server with a batch or sh file to run the server
- The screen tool in Linux

## Code Description

### Imports

- `os`: For interacting with the operating system
- `random`: For generating random numbers (unused in this script)
- `mcstatus.JavaServer`: For querying Minecraft server status
- `discord`: For creating the Discord bot
- `dotenv.load_dotenv`: For loading environment variables from the `.env` file

### Environment Variables

- `TOKEN`: Discord bot token
- `MINECRAFT_DIR`: Directory of the Minecraft server
- `SERVER_IP_PUBLIC`: Public IP address of the Minecraft server
- `SERVER_IP_LOCAL`: Local IP address of the Minecraft server
- `RUN_SERVER_COMMAND`: Command to run the Minecraft server

### Discord Client Initialization

- Initializes a Discord client with specified intents.

### Event Handlers

1. **`on_ready()`**: Prints a message when the bot is connected to Discord.
2. **`on_message(message)`**: Handles incoming messages from Discord users.

### Message Processing

- Processes messages based on their content and responds accordingly:
  - Starts the server (`x start`)
  - Pings the server or checks its status (`x ping` or `x status`)
  - Stops the server (`x stop`)
  - Retrieves the list of online players (`x players`)
  - Displays help message (`x help`)
  - Responds with a provocative message if "sex mod" is mentioned


## Usage

- Ensure the necessary environment variables are correctly set in the `.env` file.
- Run the script (`bot.py`) to start the Discord bot.
- Interact with the bot on Discord using the specified commands.