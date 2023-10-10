import requests

# Blockonomics API endpoint URL
BLOCKONOMICS_API_URL = "https://www.blockonomics.co/api/searchhistory"

# Replace with your Blockonomics API key
API_KEY = "YOUR API KEY"

def get_bitcoin_balance(transaction_id, bitcoin_address):
    try:
        # Create headers with API key
        headers = {"Authorization": f"Bearer {API_KEY}"}

        # Define the request payload
        payload = {
            "addr": bitcoin_address
        }

        # Make the API request
        response = requests.post(BLOCKONOMICS_API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            # Parse the response JSON
            data = response.json()

            # Iterate through the transaction history
            final_balance = 0
            for transaction in data.get("history", []):
                for addr in transaction.get("addr", []):
                    if addr == bitcoin_address:
                        final_balance += transaction.get("value", 0)

            return final_balance

        # If the request was unsuccessful, raise an exception
        raise Exception("API request failed")

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Input transaction ID and Bitcoin address from the user
    transaction_id = input("Enter Bitcoin Transaction ID: ")
    bitcoin_address = input("Enter Bitcoin Address: ")

    # Get the Bitcoin balance
    balance = get_bitcoin_balance(transaction_id, bitcoin_address)

    if balance is not None:
        print(f"Output: {balance / 100000000} BTC")

