import json
import asyncio
import websockets
import requests

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

RPC_ADDRESS = config.get("rpc_address")
DISCORD_WEBHOOK = config.get("discord_webhook")
MINER_ADDRESS = config.get("miner_address")


async def subscribe_to_blocks():
    while True:
        try:
            async with websockets.connect(RPC_ADDRESS, ping_interval=20, ping_timeout=60) as ws:
                message = {
                    "id": 1,
                    "jsonrpc": "2.0",
                    "method": "subscribe",
                    "params": {"notify": "new_block"}
                }
                await ws.send(json.dumps(message))

                while True:
                    response = await ws.recv()
                    data = json.loads(response)
                    print(data)
                    if (data.get("result", {}) != True) and data.get("result", {}).get("miner") == MINER_ADDRESS:
                        send_discord_notification()
        except websockets.exceptions.ConnectionClosedError as e:
            print("WebSocket connection lost, reconnecting...", e)
            await asyncio.sleep(5)  # Wait before reconnecting
        except Exception as e:
            print("Error processing WebSocket message:", e)
            await asyncio.sleep(5)


def send_discord_notification():
    if not DISCORD_WEBHOOK:
        print("Discord webhook URL not configured.")
        return

    payload = {
        "username": "Xelis Block Alert",
        "content": "@everyone",
        "embeds": [
            {
                "description": f"A new block has been mined by {MINER_ADDRESS}",
                "title": "New Xelis block found!"
            }
        ]
    }
    try:
        response = requests.post(DISCORD_WEBHOOK, json=payload, headers={"Content-Type": "application/json"})
        if response.status_code == 204:
            print("Discord notification sent!")
        else:
            print("Failed to send Discord notification:", response.text)
    except Exception as e:
        print("Error sending Discord webhook:", e)


if __name__ == "__main__":
    asyncio.run(subscribe_to_blocks())
