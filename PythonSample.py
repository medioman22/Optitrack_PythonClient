#Copyright © 2018 Naturalpoint
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


# OptiTrack NatNet direct depacketization sample for Python 3.x
#
# Uses the Python NatNetClient.py library to establish a connection (by creating a NatNetClient),
# and receive data via a NatNet connection and decode it using the NatNetClient library.


"""IMPORTANT : SET SERVER AND CLIENT IP BEFORE RUNNING!"""


from NatNetClient import NatNetClient
import time

import numpy as np
import socket
import struct
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 9000

time_prev = time.clock()

skel = None

# This is a callback function that gets connected to the NatNet client and called once per mocap frame.
def receiveNewFrame( frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount,
                    labeledMarkerCount, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged ):
    print( "Received frame", frameNumber )
    pass

# This is a callback function that gets connected to the NatNet client. It is called once per rigid body per frame
def receiveRigidBodyFrame( id, position, rotation ):
    # print( "Received frame for rigid body", id )
    pass

def skelListener(data):
    # print(data)
    global time_prev
    print('new skeleton')

    MESSAGE = [item for sublist in data for item in sublist]

    # for i in range(0,100):

    strs = 'ifffffff'*13

    data_packed = struct.pack(strs, *MESSAGE)

    sock = socket.socket(socket.AF_INET,  # Internet
                        socket.SOCK_DGRAM)  # UDP
    sock.sendto(data_packed, (UDP_IP, UDP_PORT))

    time_curr = time.clock()
    print('f = {}s'.format(1/(time_curr-time_prev)))
    time_prev = time_curr

# This will create a new NatNet client
streamingClient = NatNetClient()

# Configure the streaming client to call our rigid body handler on the emulator to send data out.
streamingClient.newFrameListener = receiveNewFrame
streamingClient.rigidBodyListener = receiveRigidBodyFrame
streamingClient.skelListener = skelListener

# Start up the streaming client now that the callbacks are set up.
# This will run perpetually, and operate on a separate thread.
streamingClient.run()

time.sleep(1)

#skel = streamingClient.skel
