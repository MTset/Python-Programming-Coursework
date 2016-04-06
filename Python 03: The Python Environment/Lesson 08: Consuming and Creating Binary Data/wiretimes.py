"""
wiretimes.py: demonstrate processing a Libpcap file.

Libpcap file format
    define guint32 unsigned int - 4 bytes
    define guint16 unsigned short - 2 bytes
    define guint8  unsigned char - 1 byte
    define gint32  int - 4 bytes

Global Header - total length: 24 bytes
    guint32 magic_number;   /* magic number */
    guint16 version_major;  /* major version number */
    guint16 version_minor;  /* minor version number */
    gint32  thiszone;       /* GMT to local correction */
    guint32 sigfigs;        /* accuracy of timestamps */
    guint32 snaplen;        /* max length of captured packets, in octets */
    guint32 network;        /* data link type */
    
Record (Packet) Header - total length: 16
    guint32 ts_sec;         /* timestamp seconds */
    guint32 ts_usec;        /* timestamp microseconds */
    guint32 incl_len;       /* number of octets of packet saved in file */
    guint32 orig_len;       /* actual length of packet */
"""
import struct
filename = r"v:\workspace\Python3_Homework08\src\wireshark.bin"
magic_number = 0xa1b2c3d4
endian = ""
f = open(filename, "rb")

# determine endianness and read global header
global_header = f.read(24)
if global_header[:4] == struct.pack(">I", magic_number):
    endian = b"big"
    unpacked_global_header = struct.unpack(">IhhIIII", global_header)
elif global_header[:4] == struct.pack("<I", magic_number):
    endian = b"little"
    unpacked_global_header = struct.unpack("<IhhIIII", global_header)
else:
    raise Exception("Couldn't determine Endianess")    

print("Packet timestamps for wireshark.bin\n{0}\n".format(35 * "-"))

i = 0
while True:
    # read packet header
    packet_header = f.read(16)
    if len(packet_header) == 16:
        if endian == "big":
            unpacked_packet_header = struct.unpack(">IIII", packet_header)
        else:
            unpacked_packet_header = struct.unpack("<IIII", packet_header)
        # skip over packet itself to the next packet header
        if unpacked_packet_header[2] <= unpacked_global_header[5]:
            packet = f.read(unpacked_packet_header[2])
        else:
            packet = f.read(unpacked_global_header[5])
        i += 1
    else:
        break
    print("packet: {0:3} - timestamp (sec.\u00B5sec): {1}.{2}".format(
                        i, unpacked_packet_header[0], unpacked_packet_header[1]))
    
