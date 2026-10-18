from datetime import datetime
import requests

def fetch_data():
    try:
        response = requests.get("https://typicode.com", timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        pass
    return {}

def generate_log(log_data=None):
    if log_data is None:
        post = fetch_data()
        post_title = post.get("title", "No title found")
        log_data = [
            "User logged in",
            "User updated profile",
            f"Fetched API Post Title: {post_title}",
            "Report exported"
        ]
        
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list of log entries.")
        
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    generate_log()
