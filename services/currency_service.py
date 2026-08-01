import requests
from datetime import datetime

URL = "https://open.er-api.com/v6/latest/USD"


def get_rates():
    response = requests.get(URL, timeout=10)

    response.raise_for_status()

    data = response.json()

    update_time = datetime.fromtimestamp(
        data["time_last_update_unix"]
    ).strftime("%d.%m.%Y • %H:%M")

    return {
        "rates": data["rates"],
        "update_time": update_time
    }


if __name__ == "__main__":
    print(get_rates())