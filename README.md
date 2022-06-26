# Bus-Locator-App
Hi!
This is an python project done using Tkinter, CSV, Request modules.
This project has two screens.

# Sreen 1:
- It is the face of the project which contains project name, logo/image and some initial stuffs
- FROM place should be entered 
- TO place should be entered 
- If these strings are valid with the backend, then further process will be done by clicking search button
- Available busses based on these stops will be displayed 
- If no busses availbale for these stops or if the entered strings are not matching then an exceptional NOTE will be displaye
- User can navigate to next screen by clicking the bus no. BUTTON
- CLEAR button is given to search fresh

# Screen 2:
- In Screen 2 the available bus stops and bus timing of that stop is displayed
- At last a button is given to view the location of that bus using a device IP which will be placed inside the bus
- User can copy the Latitude and Longitude and paste it in Google maps to view the Location of that coordinates

# Requirements:
- python3
- "requests" module -- pip install requests ---> for requesting location details from the third-party website
- "pillow" module -- pip install pillow  ---> for using images in app
- "pyinstaller" module -- pip install pyinstaller ---> to convert .py file into .exe file

# Code Insights:
- main.py and main.pyw are same programs. It contains the main control flow and imported modules
- addBusStop.py contains a list variable "addBusStop_list" which extracts data from busStops.csv
- addStopsIn_busStopsCSV.py code is used to extract all bus stops from data.csv and writing it in busStops.csv
- data.csv contains arranged order of data such that (IP address, bus number plate, bus serial number, bus stop 1, bus stop 1 timing, bus stop 2, bus stop 2 timing, . . . . , bus stop N, bus stop N timing)
- busStops.csv contains every bus stop names in ascending order

# Note:
- .pyw extension is used for ignoring the command screen while working with .exe file
- It works as same as .py extension, and no affect to the code
- Since it's a complete working prototype, the future work includes the GPS tracker, web server, Google APIs and UI-UX
