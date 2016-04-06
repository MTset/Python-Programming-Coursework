import os, struct, time
f = open("wireshark.bin", "rb")
c = 1
skip = f.read(24)
while True:
    try:
        header = f.read(16)
        rtime, microseconds, incl, orig = struct.unpack("=IIII", header)
#        print(time, microseconds, incl, orig)
        stime = time.ctime(rtime)
        print("packet: {0}  | timestamp: {1} | microseconds: {2}".format(c, stime, microseconds))
        c += 1
        f.read(incl)
    except:
        break