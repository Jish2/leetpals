import requests
import datetime


def get_user_badges(username):
    url = "https://leetcode.com/graphql"
    headers = {"Content-Type": "application/json", "Referer": "https://leetcode.com"}
    payload = {
        "query": """ query getUserProfile($username: String!) { matchedUser(username: $username) { badges { icon } } } """,
        "variables": {"username": username},
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["data"]["matchedUser"]["badges"]
    except Exception as e:
        print(e)
    return None


def user_is_cracked_at_leetcode(username):
    badges = get_user_badges(username)
    prev_month = (datetime.datetime.now().month - 1) % 13
    current_year = datetime.datetime.now().year

    for badge in badges:
        if f"{current_year}-{prev_month}" in badge["icon"]:
            return True

    return False
