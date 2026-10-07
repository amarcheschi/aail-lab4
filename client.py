import requests


def main():
    # URL of the Flask API running in Docker
    url = "http://localhost:8000/predict"

    # Sample input features
    data = {
        "features": [5.1, 3.5, 1.4, 0.2]
    }

    # Send the POST request
    response = requests.post(url, json=data)

    # Print the response received from the server
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    main()
