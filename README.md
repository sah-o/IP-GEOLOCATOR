# Saho IP Locator

Saho is a simple Python script that locates an IP address and provides information about its geographical location, including country, region, city, ISP, and more.

## Features:
- Displays an ASCII art on startup.
- Takes an IP address as input and returns detailed location information.
- Includes a 5-second delay at startup to simulate loading.

## How to Use:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/sah-o/IP-GEOLOCATOR.git
   cd IP-GEOLOCATOR
   ```

2. Make sure you have Python installed (Python 3.6+ recommended).

3. Install the necessary dependencies:
   ```bash
   pip install requests
   ```

4. Run the script:
   ```bash
   python main.py
   ```

5. The program will display an ASCII art, followed by a 5-second loading delay, and then ask you to input an IP address.

6. After entering the IP address, the program will provide information about its location, such as:
   - Country
   - Region
   - City
   - ISP
   - and more.

## Example Output:
```
 .M"""bgd      db      `7MMF'  `7MMF' .g8""8q.   
,MI    "Y     ;MM:       MM      MM .dP'    `YM. 
`MMb.        ,V^MM.      MM      MM dM'      `MM 
  `YMMNq.   ,M  `MM      MMmmmmmmMM MM        MM 
.     `MM   AbmmmqMA     MM      MM MM.      ,MP 
Mb     dM  A'     VML    MM      MM `Mb.    ,dP' 
P"Ybmmd" .AMA.   .AMMA..JMML.  .JMML. `"bmmd"'   

Saho is starting...

Enter IP Address: 8.8.8.8
📍 Located: 8.8.8.8
🌍 Country: United States (US)
🏛 Region: California (CA)
🏙 City: Mountain View
📮 ZIP Code: 94043
📡 ISP: Google LLC
🏢 Organization: Google LLC
🔗 AS (Autonomous System): AS15169
🔄 Reverse DNS: dns.google
🌎 Latitude: 37.4056
🌍 Longitude: -122.0775
⏳ Timezone: America/Los_Angeles
📶 Mobile Network: ❌ No
🕵️ Proxy/VPN: ❌ No
🏢 Hosting Provider: ✅ Yes
```

## Notes:
- The script uses the `requests` library to query the IP location API (http://ip-api.com) for retrieving geographical details.
- The script has a 5-second delay before asking for the IP address to simulate loading.
  
## License:
This project is licensed under the MIT License.
