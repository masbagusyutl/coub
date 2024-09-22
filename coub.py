import time
import requests
import json
from datetime import datetime, timedelta

# Task list yang diberikan
TASK_LIST = [
    {"id": 1, "type": "welcome", "title": "Welcome Task", "price": 10, "icon": "welcome", "status": "ready-to-claim"},
    {"id": 2, "type": "checkin", "title": "Daily Check-in", "price": 5, "icon": "checkin", "status": "ready-to-start", "repeatable": True},
    {"id": 3, "type": "watch", "title": "Watch 10 Coub", "price": 20, "icon": "video-octagon", "status": "ready-to-start"},
    {"id": 4, "type": "share", "title": "Share 3 Coub", "price": 15, "icon": "share", "status": "ready-to-start"},
    {"id": 5, "type": "refferals", "title": "Invite 3 Friends", "price": 50, "icon": "people", "status": "ready-to-start"},
    {"id": 6, "type": "twitter", "title": "Follow on Twitter", "price": 10, "icon": "twitter", "status": "ready-to-start"},
    {"id": 7, "type": "telegram", "title": "Follow on Telegram", "price": 10, "icon": "telegram", "status": "ready-to-start"},
    {"id": 9, "type": "youtube", "title": "Follow on YouTube", "price": 10, "icon": "youtube", "status": "ready-to-start"},
    {"id": 10, "type": "vote", "title": "Vote Probably", "price": 25, "icon": "vote", "status": "ready-to-start"},
    {"id": 8, "type": "onboarding", "title": "Complete Onboarding", "price": 100, "icon": "onboarding", "status": "ready-to-start"},
    {"id": 11, "type": "vote-bonus", "title": "Vote Bonus", "price": 25, "icon": "vote", "status": "ready-to-start"},
    {"id": 12, "type": "watch-25-random", "title": "Watch 25 Random Coubs", "price": 10, "icon": "watch", "status": "ready-to-start", "repeatable": True},
    {"id": 13, "type": "watch-25-rising", "title": "Watch 25 Rising Coubs", "price": 10, "icon": "watch", "status": "ready-to-start", "repeatable": True},
    {"id": 14, "type": "watch-25-recommendations", "title": "Watch 25 Recommended Coubs", "price": 10, "icon": "watch", "status": "ready-to-start", "repeatable": True},
    {"id": 15, "type": "like-5-random", "title": "Like 5 Random Coubs", "price": 5, "icon": "like", "status": "ready-to-start", "repeatable": True},
    {"id": 16, "type": "like-5-rising", "title": "Like 5 Rising Coubs", "price": 5, "icon": "like", "status": "ready-to-start", "repeatable": True},
    {"id": 17, "type": "like-5-recommendations", "title": "Like 5 Recommended Coubs", "price": 5, "icon": "like", "status": "ready-to-start", "repeatable": True},
    {"id": 18, "type": "share-wtf-video", "title": "Share WTF Story", "price": 30, "icon": "share-coub", "status": "ready-to-start"},
    {"id": 20, "type": "support-tweet", "title": "Like & Share #FreeDurov", "price": 50, "icon": "twitter", "status": "ready-to-start"},
    {"id": 19, "type": "share-story", "title": "Share Story", "price": 5, "icon": "share-story", "status": "ready-to-start", "repeatable": True},
    {"id": 21, "type": "oasis-tweet", "title": "#Oasis Like & Retweet", "price": 5, "icon": "twitter", "status": "ready-to-start", "repeatable": False},
    {"id": 23, "type": "charli-summer-share", "title": "#BratSummer Like & Retweet", "price": 5, "icon": "twitter", "status": "ready-to-start", "repeatable": False},
    {"id": 22, "type": "charli-summer-create", "title": "#BratSummer Create Coub", "price": 25, "icon": "coub", "status": "ready-to-start", "repeatable": False},
    {"id": 24, "type": "like-retweet", "title": "Like & Retweet", "price": 5, "icon": "twitter", "status": "ready-to-start", "repeatable": False},
    {"id": 25, "type": "edit-channel", "title": "Edit Channel", "price": 5, "icon": "coub", "status": "ready-to-start", "repeatable": False},
    {"id": 26, "type": "like-5-sports", "title": "Like 5 Sports Coubs", "price": 5, "icon": "like", "status": "ready-to-start", "repeatable": True},
    {"id": 27, "type": "holder-reward", "title": "Holder Reward", "price": 10, "icon": "buy-crypto", "status": "ready-to-start", "repeatable": True}
]


# Fungsi untuk membaca Authorization token dari data.txt
def read_authorizations(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Fungsi untuk cek hadiah (get_user_rewards)
def get_user_rewards(authorization):
    headers = {
        "authorization": f"Bearer {authorization}",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    }
    url = "https://rewards.coub.com/api/v2/get_user_rewards"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Successfully retrieved user rewards.")
        return response.json()  # Mengembalikan respon hadiah
    else:
        print(f"Failed to retrieve user rewards. Status code: {response.status_code}")
        return None

# Fungsi untuk menyelesaikan tugas (complete_task)
def complete_task(authorization, task_id, task_title):
    headers = {
        "authorization": f"Bearer {authorization}",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    }
    params = {"task_reward_id": task_id}
    url = "https://rewards.coub.com/api/v2/complete_task"
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        print(f"Task '{task_title}' (ID: {task_id}) completed successfully.")
        return response.json()
    else:
        print(f"Failed to complete task '{task_title}' (ID: {task_id}). Status code: {response.status_code}")
        return None

# Fungsi utama untuk menjalankan tugas dari beberapa akun
def process_accounts(file_path):
    authorizations = read_authorizations(file_path)
    account_count = len(authorizations)
    print(f"Total Accounts: {account_count}")

    for i, auth in enumerate(authorizations, 1):
        print(f"Processing Account {i}/{account_count}")

        # Cek hadiah untuk setiap akun
        rewards = get_user_rewards(auth)
        if rewards:
            print(f"User rewards: {json.dumps(rewards, indent=2)}")

        # Proses setiap tugas yang ada di TASK_LIST
        for task in TASK_LIST:
            task_id = task['id']
            task_title = task['title']
            task_price = task['price']
            task_status = task['status']

            # Hanya jika task status adalah 'ready-to-start' atau 'ready-to-claim'
            if task_status in ["ready-to-start", "ready-to-claim"]:
                print(f"Task: {task_title}, Price: {task_price}, Status: {task_status}")

                # Selesaikan tugas
                result = complete_task(auth, task_id, task_title)
                if result:
                    print(f"Response: {json.dumps(result, indent=2)}")

            time.sleep(1)  # Jeda sejenak sebelum tugas berikutnya

        print("Waiting 5 seconds before processing next account...\n")
        time.sleep(5)  # Jeda 5 detik sebelum akun berikutnya

    print("All accounts processed. Starting 1 day countdown...")

    # Hitung mundur 1 hari
    countdown(1)

# Fungsi untuk hitung mundur
def countdown(days):
    end_time = datetime.now() + timedelta(days=days)
    while datetime.now() < end_time:
        remaining_time = end_time - datetime.now()
        print(f"Time left: {remaining_time}", end='\r')
        time.sleep(1)
    print("\nCountdown complete. Restarting process...")

# Menangani error agar program terus berjalan
def safe_execute(func, *args):
    try:
        func(*args)
    except Exception as e:
        print(f"An error occurred: {e}. Continuing with the next task...")

# Main program
if __name__ == "__main__":
    file_path = "data.txt"  # File yang berisi Authorization token
    while True:
        safe_execute(process_accounts, file_path)
