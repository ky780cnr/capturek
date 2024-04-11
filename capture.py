import requests
import json
import time
import os
import pyfiglet
os.system('color 5')
os.system("cls")
print("loding")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
print("....")
time.sleep(4)
ky780cno = pyfiglet.figlet_format("ky780cno")
print(ky780cno)
time.sleep(5)
os.system("cls")
os.system('color 1')
ascii_banner = pyfiglet.figlet_format("capture")
print(ascii_banner)
print("__________________________________________________________________________")
print("TEAM Shadow Vanguard")
print("id Discord: ky780cnr") 
print("server team: https://discord.gg/rPxRQmnQ2S")
print("__________________________________________________________________________")
def send_message_to_webhook(webhook_url, username, message):
    try:
        
        payload = {
            'content': message,
            'username': username
        }
        response = requests.post(webhook_url, json=payload)

        if response.status_code == 200:
            print("[+]Message sent successfully.")
        else:
            print(f"[-]Error sending message. HTTP status code: {response.status_code}")
            #print("[+]Message sent successfully")

    except Exception as e:
        print(f"[-]Error sending message to webhook: {e}")
webhook_url = input("[@]Please enter your webhook URL: ")
print("________________________________________________________________")
username = input("[?]Please enter your profile name: ")
print("________________________________________________________________")
message = input("[!]Please enter your desired message: ")
print("=================================================================================================")
os.system("color 4")
while True:
    send_message_to_webhook(webhook_url, username, message+" @everyone")
    time.sleep(0.2)
