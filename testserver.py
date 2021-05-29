import pynetwork as pn

host = "192.168.1.76" # Test server
port = 9090

# Create a server
server = pn.Server(host, port)
# Start it
server.start()
# Get a reply after sending "Hi!""
reply = server.send_to_client("Hi!")
# Print the reply.
print(reply)

# Comment this is if you want to keep connection with the client.
server.close_client_connection()

# Keep the window open so you can read what the client sent.
while True:
    None
