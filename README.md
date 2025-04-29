# SocketDDS
SocketDDS

A DDS like socket tool.

# Requirements
No requirements with CPython.
Json/Socket/Threading/Time was imported. Some functions might won't work on micropython.
Trying to adapt asap...

# How 2 Use

## DDS Client
To broardcast the messages. Init the DDS Client with a name a list of topic and the port(default to 9999)
Use `DDS_Client.broad_cast(topic,message)` to broardcast message.

## DDS Receiver
To receive messages. Init the DDS Receiver with the target topic and port(default to 9999).
Use `start_listening()` to start. Read the message at `DDS_Receiver.data`.
Use `stop_listening()` to stop.

