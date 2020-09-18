import requests, json, time

webhookURL = "https://discordapp.com/api/webhooks/756434239989481522/PXId7eryZris6dD3S917GZYc98EyCmTUlVi-Wj5WHkqU6uE2FAryDDHT2oAhaYz116_f"

tags = "highres%20score:>=66%20rating:safe"

def sendImg():
    danbooruRequest = requests.get("https://danbooru.donmai.us/posts/random.json?tags=" + tags)
    danbooruImg = json.loads(danbooruRequest.text)
    requests.post(webhookURL, data={"content" : danbooruImg["large_file_url"] })
    requests.post(webhookURL, data={"content" : " Source: <https://danbooru.donmai.us/posts/" + str(danbooruImg["id"]) + ">" })
 
# Sends 3 pictures over the course of 18 hours
# Script was meant to be run as a daily scheduled task, hence sends 3 pictures over 18 hours after the last picture is sent,
# The script should run 6 hours later once again for a perfect 4 pictures within 24 hours loop
# Change count and sleep interval as you wish
count = 3
while count > 0: 
    errorFlag = False
    try:
        sendImg()
        count -= 1
        time.sleep(21600) #Sends one every 6 hours
    except Exception as a:
        if not errorFlag:
            errorFlag = True
            continue
        else:
            requests.post(webhookURL, data={"content" : "An unexpected error has occurred." })
            break
        
