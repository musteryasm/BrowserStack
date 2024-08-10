## BrowserStack Interview
The folder contains files for the BrowserStack assessment which took place on aug 10 2024 
By - Shivam Musterya, DJSCE - CSE_DS 

## Problem Statment
The problem requires you to implement a log watching solution (similar to the tail -f command in UNIX). However, in this case, the log file is hosted on a remote machine (same machine as your server code).

## Description
The above problem is solved here
 test.log --> log file created for testing purposes
 index.html --> ui for the clients where they can see the visible output
 server.py --> websocket code which has the main functioning
 requirements.txt --> requirements to install
 try.py --> testing purpose file to run changes without interfering with the og code

## How to Run
1. Install the required packages by running `pip install -r requirements.txt`
2. Run the server by executing `python server.py`
3. Use the index.html to become a client and see the ouput (you can also see the output on the terminal)
4. Using touch command, make changes in the test.log file
5. See the visible changes on terminal as well the browser clients
 