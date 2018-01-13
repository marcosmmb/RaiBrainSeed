ASCIICHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

def asciiparser(string):
	for c in string:
		if c not in list(ASCIICHARS):
			return False
	return True

def asciilist(string):
	s = string.replace(" ", "")
	l = list(set(s))
	l.sort()
	return l

def makehexdic(l):
	d = {}
	for i in range(len(l)):
		d[l[i]] = (hex(i%16)[2]).upper()
	return d

def makeseed(s, d):
	s = s.replace(" ", "")
	l = list(s)
	seed = []
	for c in l:
		seed.append(d[c])
	seed = "".join(seed)
	while(len(seed) < 64):
		seed = seed + seed
	return seed[:64]


def mainflow(s):
	if not asciiparser(s):
		return False
	l = asciilist(s)
	d = makehexdic(l)
	seed = makeseed(s, d)
	return seed

