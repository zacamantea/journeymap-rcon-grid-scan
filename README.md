# journeymap rcon grid scan
Automate world mapping for JourneyMap by teleporting one or more players across a grid using RCON. Built for self hosted servers.

**Important Notice:**
This project was created using AI assisted coding. The implementation is the result of AI, debugging, and experimentation rather than fully manual development.
The goal is to share a practical working solution for automated JourneyMap scanning. Always review and test code before using it in production or public servers.

What this does
- Teleports players on a grid to force chunk loading and fill JourneyMap quickly
- Supports many players at once
- Saves progress so you can stop and resume
- Prints progress like 25/1681 and percent complete
- Includes a spiral scan mode that starts at 0,0 and works outward

Requirements
- Java server with RCON enabled (Spigot, Paper, Purpur)
- Python 3.10+
- mcrcon Python package
- JourneyMap on the client

1) Server setup (RCON)
Edit server.properties in your server instance folder
enable-rcon=true
rcon.port=25575
rcon.password="yourpassword"

2) Restart the server

3) Confirm from your PC
Inside PowerShell test your connection to the server
"Test-NetConnection YOUR_SERVER_IP -Port 25575"

4) install dependency
- Install Python
- pip install mcrcon

5) Edit the script settings
- RCON_HOST
- RCON_PASSWORD
- PLAYERS
- STEP
- RADIUS
- DELAY

6) Run command in Powershell where your file is stored.
- python rcon_scan.py

To stop/pause 
Ctrl + C

To Resume
Run it again. It continues where it left off using progress.txt

Restart from the beginning
Delete progress.txt

Recommended settings
Fast and safe mapping on a LAN
- STEP 350
- DELAY 17 seconds
- Client render distance 8 to 12

#The best DELAY I found was 17 second for the full render to finish

Dense coverage
- STEP 250
- DELAY 17 seconds

Notes
- This does not bypass server limits. It only loads chunks the server can generate and send.
- If you change STEP, RADIUS, or scan mode, delete progress.txt once.
- Journeymap loads in about 250ish circle around you at a time.
