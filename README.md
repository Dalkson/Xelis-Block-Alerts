# Xelis Block Notifier

This script monitors the Xelis blockchain for new blocks mined by a specific address and sends notifications to a Discord webhook.

## Installation and Usage on Linux

### Prerequisites

Ensure you have the following installed on your Linux system:

- Python 3.8+
- `pip` (Python package manager)

### Step 1: Clone the Repository

```sh
git clone https://github.com/Dalkson/Xelis-Block-Alerts.git
cd Xelis-Block-Alerts
```

### Step 2: Create and Activate a Virtual Environment 

```sh
python3 -m venv venv
source venv/bin/activate  # For Bash
```

### Step 3: Install Required Dependencies

```sh
pip install -r requirements.txt
```

### Step 4: Configure the Script

Edit the `config.json` file in the project directory with your own webhook and miner address, additionally if you want to use your own RPC set that here:

```json
{
    "rpc_address": "wss://node.xelis.io/json_rpc",
    "discord_webhook": "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL",
    "miner_address": "xel:YOUR_MINER_ADDRESS"
}
```

### Step 5: Run the Script

```sh
python3 main.py
```

### Starting the script from outside the Virtual Environment 

```sh
./venv/bin/python3.11 main.py
```

### Running in the background

Either run it in a screen or make a service that runs the above command.


