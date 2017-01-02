import socket
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
from urllib import urlopen
# import pyaudio
import mad
# from scipy.io.wavfile import write
import wave
import time
import struct
from pymp3decoder import Decoder

CHUNK_SIZE = 4096

import io

# pyaud = pyaudio.PyAudio()

# fs = 44100

# stream = pyaud.open(format = pyaud.get_format_from_width(1),
#                     channels = 2,
                    # rate = fs,
                    # output=True)

url = "http://dradio_mp3_dlf_m.akacast.akamaistream.net/7/249/142684/v1/gnl.akacast.akamaistream.net/dradio_mp3_dlf_m"

# u = urlopen(url)

# data = u.read(8192)

def printurl(url):
    import requests
    dec = Decoder(CHUNK_SIZE)

    remote_mp3 = requests.get(url, stream=True)

    for chunk in dec.decode(remote_mp3):
        print(chunk)

def streamurl(url):
    scheme, netloc, path, params, query, fragment = urlparse(url)
    try:
        host, port = netloc.split(':')
    except ValueError:
        host, port = netloc, 80
    if not path:
        path = '/'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, int(port)))
    message = 'GET %s HTTP/1.0\r\n\r\n' % path
    sock.send(message.encode(('ascii')))
    reply = sock.recv(1<<16)

    print(reply)
    file = sock.makefile("rb", bufsize=1024*16)

    dec = Decoder(20*CHUNK_SIZE)


    if False:
        mf = mad.MadFile(file)
    else:
        u = urlopen(url)
        u.read(1<<16)
        mf = mad.MadFile(u)


    # while mf.bitrate() == 0:
    #     time.sleep(1)

    print(('bitrate %lu bps' % mf.bitrate()))
    print(('samplerate %d Hz' % mf.samplerate()))

    # open the wave writer
    ww = wave.open("tempout.wav", 'wb')
    ww.setnchannels(2)
    ww.setframerate(44100)
    ww.setsampwidth(2)

    f = open('testout.mp3', 'wb')

    # print(file.readline())
    last = bytearray([])
    while True:
        n = u.read(CHUNK_SIZE)
        # buffy = mf.read(CHUNK_SIZE)#.decode('utf-8')
        # buffy = file.read()

        buffy= dec.decode(n, last)



        if buffy is None:
            break



        # print('new')
        # print(buffy)
        # print('dec')
        # print(struct.unpack('h', buffy))
        # print(struct.unpack_from('!h', buffy, 100))
        # write("tempout.wav", fs=mf.samplerate(), )
        # ww.writeframes(buffy)

        # f.write(n)

    ww.close()
    f.close()
# while data:
#     print(data)
#     data = u.read(8192)

if __name__ == "__main__":
    url = "http://dradio_mp3_dlf_m.akacast.akamaistream.net/7/249/142684/v1/gnl.akacast.akamaistream.net/dradio_mp3_dlf_m"
    # url = "http://www.maninblack.org/demos/WhereDoAllTheJunkiesComeFrom.mp3"
    # url = "http://ndr-ndrinfo-nds-mp3.akacast.akamaistream.net/7/250/273753/v1/gnl.akacast.akamaistream.net/ndr_ndrinfo_nds_mp3"
    streamurl(url)