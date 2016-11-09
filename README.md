# Scirocco Pyclient
[![Build Status](https://travis-ci.org/eloylp/scirocco-pyclient.svg?branch=master)](https://travis-ci.org/eloylp/scirocco-pyclient)

*Advice: This project is at BETA phase.*

This is a handy library to interact with the [scirocco-server](https://github.com/eloylp/scirocco-server) project. If you dont know about it , please read firts that project docs.

## Installation

This client library has two main install methods.

#### With source:
```bash
 git clone https://github.com/eloylp/scirocco-pyclient.git
 python3 setup.py install
```

#### With pip3:
```bash
 pip3 install scirocco-pyclient
```

## Using the library

#### The response object

Every operation in this client will return the same [response object](https://github.com/eloylp/scirocco-pyclient/blob/docs/sciroccoclient/responses.py#L10)
, representing the state of the operation in system_data as well the resultant message representation in
message_data.

#### Instantiating the client

For use the library you must instantiate the HTTPClient by passing three params. 
Respectively they are scirocco-server endpoint (take care about http/https schema), 
your pre-stablished by convention node_id and a the auth token for gain access to that
scirocco-server instance.

```python

from sciroccoclient.httpclient import HTTPClient

scirocco_client = HTTPClient('http://localhost', 'af123', 'DEFAULT_TOKEN')
```

#### Pushing messages
Pushing messages is simple as this:

```python

scirocco_client.message_queue_push('af123', {"type": "message"})

scirocco_client.message_queue_push('af123', 'message')

binfile = open('file.bin', 'rb').read()
scirocco_client.message_queue_push('af123', binfile)
```
"af123" will become detination node_id as first parameter. At second we 
need to send the message itself. It can be a string , object or binary type.
When yous push a message , it can be in schedule or pending (default) status.
If the message is being scheduled, it only will be accesible in a 'pull' operation 
when schedule_time is reached.

#### Receiving messages

You will receive messages in the same data type as you send it, except for binary
type. You will push binary , and the item is stored as binary , but you will receive 
it in base64 representation.

```python
response_object = scirocco_client.message_queue_pull()

# print system headers
print(response_object.system_data.__dict__)

# print the message itself.
print(response_object.message_data.__dict__)
```

If no pending messages the client will return None else, it will return
a response object which contains system_data and message_data. The message
will change its status to 'processing', so it cannot be accesible by other
'pull' operation.

#### Confirming messages

When you deal with ipcs, or interdependant operations in different processes,
you need to mark the message as "done" or processed for further operations
in other processes.

You only need to save the previous response in pull operation to confirm
the message by id. For example if we want to confirm '5823a70203c123003de4229b' 
message id , the code will be :

```python
scirocco_client.message_queue_ack('5823a70203c123003de4229b')
```
