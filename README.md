# PyNetwork
(PyNetwork v1.40.0)


# Intro
----------
Have you ever been super confused and had to use a tutorial for socket?
### Well, fear *not*!
PyNetwork comes to the rescue! We make socket programming SOO much easier to read.
To get a server up and running, it only takes 5 lines! I know, right?
*(extra features will be more than 5 lines ofc lol)*

# Usage
---------
- Import
1: Download PyNetwork
2: Move it to the same folder
3: Import PyNetwork

***( REPLACE HOST WITH THE SERVER HOST )***
### Making a server
1: After the import, add: `server = pynetwork.Server("yourhost", "port")`.
2: You can the start it! `server.start()`.

### Connecting to a server
1: After the import, add: `client = pynetwork.ClientConnection("host", "port")`.
2: Connect to the server. `client.connect()`.


# FEATURES
### Server
1: `send_to_client(str, data="ascii")`
2: `recieve_from_client(bytes)`
3: `close_client_connection`

### Client
1: `send_to_server(str, data="ascii")`
2: `recieve_from_server(bytes)`


# I will see what all of you can make using this!
------------
Bye!
