import requests
import time

# Predefined ASCII art
ascii_art = '''
 .M"""bgd      db      `7MMF'  `7MMF' .g8""8q.   
,MI    "Y     ;MM:       MM      MM .dP'    `YM. 
`MMb.        ,V^MM.      MM      MM dM'      `MM 
  `YMMNq.   ,M  `MM      MMmmmmmmMM MM        MM 
.     `MM   AbmmmqMA     MM      MM MM.      ,MP 
Mb     dM  A'     VML    MM      MM `Mb.    ,dP' 
P"Ybmmd" .AMA.   .AMMA..JMML.  .JMML. `"bmmd"'   
'''

API_URL = "http://ip-api.com/json/"

def locate(ip):
    if not ip:
        print("Please enter an IP address.")
        return

    try:
        response = requests.get(f"{API_URL}{ip}?fields=66842623")
        response.raise_for_status()
        data = response.json()

        if data.get("status") == "success":
            print(f"📍 Located: {data.get('query')}")
            print(f"🌍 Country: {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
            print(f"🏛 Region: {data.get('regionName', 'N/A')} ({data.get('region', 'N/A')})")
            print(f"🏙 City: {data.get('city', 'N/A')}")
            print(f"📮 ZIP Code: {data.get('zip', 'N/A')}")
            print(f"📡 ISP: {data.get('isp', 'N/A')}")
            print(f"🏢 Organization: {data.get('org', 'N/A')}")
            print(f"🔗 AS (Autonomous System): {data.get('as', 'N/A')}")
            print(f"🔄 Reverse DNS: {data.get('reverse', 'N/A')}")
            print(f"🌎 Latitude: {data.get('lat', 'N/A')}")
            print(f"🌍 Longitude: {data.get('lon', 'N/A')}")
            print(f"⏳ Timezone: {data.get('timezone', 'N/A')}")
            print(f"📶 Mobile Network: {'✅ Yes' if data.get('mobile') else '❌ No'}")
            print(f"🕵️ Proxy/VPN: {'✅ Yes' if data.get('proxy') else '❌ No'}")
            print(f"🏢 Hosting Provider: {'✅ Yes' if data.get('hosting') else '❌ No'}")
        else:
            print(f"❌ Error: {data.get('message', 'Invalid IP or Rate Limited!')}")

    except requests.exceptions.RequestException as e:
        print(f"🚨 Network Error: {e}")

def main():
    print(ascii_art)

    print("Saho is starting...")
    time.sleep(5)

    ip = input("Enter IP Address: ").strip()
    locate(ip)

if __name__ == "__main__":
    main()
