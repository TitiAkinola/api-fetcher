import requests

def check_api(url):
    try:
        # 5-second timeout prevents the script from hanging
        response = requests.get(url, timeout=5)
        # 200-299 status codes are considered "UP"
        if 200 <= response.status_code < 300:
            print(f"✅ UP: {url} (Status: {response.status_code})")
        else:
            print(f"⚠️ DOWN: {url} (Status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"❌ DOWN: {url} (Error: {e})")

if __name__ == "__main__":
    target_url = "https://www.google.com"
    check_api(target_url)
