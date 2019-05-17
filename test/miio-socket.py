import codecs
import socket
import datetime
from miio.protocol import Message

helobytes = bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(helobytes, ('192.168.31.201', 54321))  # 插座ip，端口54321
data, addr = s.recvfrom(1024)
print("data信息")
print(data)
m = Message.parse(data)
tok = codecs.encode(m.checksum, 'hex')

print(m)
print(tok)

# 控制脚本
ts = m.header.value.ts + datetime.timedelta(seconds=1)
device_id = m.header.value.device_id

cmd = {'id': 1, 'method': 'set_power', 'params': ['off']}
header = {'length': 0, 'unknown': 0x00000000, 'device_id': device_id, 'ts': ts}
msg = {'data': {'value': cmd}, 'header': {'value': header}, 'checksum': 0}

m0 = Message.build(msg, token=m.checksum)
print("m0的信息")
print(m0)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2.sendto(m0, ('192.168.31.201', 54321))
data2, addr2 = s2.recvfrom(1024)
print("data的信息")
print(data2)
m1 = Message.parse(data2, token=tok)
print("显示回传控制信息")
print(m1)

print("end")