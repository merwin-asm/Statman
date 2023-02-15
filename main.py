"""
A tool for constantly changin discord status...
"""

import requests as r
import time
import random
from rich import print

ascii_art = """
  ______   ________       ________  __       __            __ 
 /      \ /        |     /        |/  \     /  |          /  \  /  |
/$$$$$$  |$$$$$$$$/______$$$$$$$$/ $$  \   /$$ |  ______  $$  \ $$ |
$$ \__$$/    $$ | /      \  $$ |   $$$  \ /$$$ | /      \ $$$  \$$ |
$$      \    $$ | $$$$$$  | $$ |   $$$$  /$$$$ | $$$$$$  |$$$$  $$ |
 $$$$$$  |   $$ | /    $$ | $$ |   $$ $$ $$/$$ | /    $$ |$$ $$ $$ |
/  \__$$ |   $$ |/$$$$$$$ | $$ |   $$ |$$$/ $$ |/$$$$$$$ |$$ |$$$$ |
$$    $$/    $$ |$$    $$ | $$ |   $$ | $/  $$ |$$    $$ |$$ | $$$ |
 $$$$$$/     $$/  $$$$$$$/  $$/    $$/      $$/  $$$$$$$/ $$/   $$/"""

headers = {
         "authorization" : "",
        "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        } 

url  = 'https://discord.com/api/v9/users/@me/settings' 

print(f"[green]{ascii_art}[/green]\n")

print("[blue]Your Authorization Token : [/blue]",end="")
token = input("")
headers["authorization"] = token
print("")
print("""
[bold][yellow]    << OPTIONS >> [/yellow][/bold]
[blue]  - > 0 - Word By Word
  - > 1 - Cascading Animation
  - > 2 - Loading 
  - > 3 - Loading + Text[/blue]
[yellow] >> [/yellow]""", end="")
option = input("")
payload = {
        "custom_status": {

            "text":""
            }
}
a = r.patch(url , headers=headers, json=payload)

if a.status_code == 401:
    print("[red]Invaild Token..[/red]")
    quit()

if option == "0":
    stats_inp = input("All Status (Seperate using '///') : ").split("///")

    while True:
        for status in stats_inp:
            payload = {
        "custom_status": {

            "text": status}
            }
            a = r.patch(url , headers=headers, json=payload)
            print(f"[green] {a.status_code}  :  Currrent : {status} [/green]")
            time.sleep(1)
        time.sleep(1.5)

elif option == "1":
    status = input("Status : ")

    while True:
        a_ = ""
        for s in status:
            a_ = a_ + s
            payload = {
        "custom_status": {

            "text": a_}
            }
            a = r.patch(url , headers=headers, json=payload)
            print(f"[green] {a}  :  Currrent : {status} [/green]")
            time.sleep(0.1)
        a_ = ""
        time.sleep(1)

elif option == "2":
    www = input("Slim or Thicc (|/❚) - (0/1)  : ") 
    if www == "0":
        status = "|"*10
        l = 10
    else:
        status = "❚"*5
        l = 5
    while True:
        a_ = ""
        ad = round(100/l)
        p = 0
        for s in status:
            p += ad
            if p > 100:
                p = 0

            a_ = a_ + s 
            sp = ""
            
            payload = {
        "custom_status": {

            "text": a_  +  f" {sp}{p}%"}
            }
            a = r.patch(url , headers=headers, json=payload)
            print(f"[green] {a}  :  Currrent : {a_} [/green]")
            time.sleep(0.25)
        a_ = ""
        time.sleep(3)

elif option == "3":
    www = input("Slim or Thicc (|/❚) - (0/1)  : ") 
    if www == "0":
        status = "|"*10
        l = 10
    else:
        status = "❚"*5
        l = 5
    while True:
        a_ = ""
        ad = round(100/l)
        p = 0
        for s in status:
            p += ad
            if p > 100:
                p = 0

            a_ = a_ + s 
            sp = ""
            
            payload = {
        "custom_status": {

            "text": a_  +  f" {sp}{p}%"}
            }
            a = r.patch(url , headers=headers, json=payload)
            print(f"[green] {a}  :  Currrent : {a_} [/green]")
            time.sleep(0.25)
        a_ = ""
    
        payload = {
        "custom_status": {

            "text": status_}
            }
        a = r.patch(url , headers=headers, json=payload)
        print(f"[green] {a}  :  Currrent : {status_} [/green]")

        time.sleep(2)
        
