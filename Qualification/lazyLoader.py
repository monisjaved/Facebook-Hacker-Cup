# https://www.facebook.com/hackercup/problem/169401886867367/
__author__ = "Moonis Javed"
__email__ = "monis.javed@gmail.com"

def numberOfDays(arr):
	arr = sorted(arr)
	n = 0
	while len(arr) > 0:
		k = arr[-1]
		w = k
		del arr[-1]
		while w <= 50:
			try:
				del arr[0]
				w += k
			except:
				break
		if w > 50:
			n += 1
	return n

if __name__ == "__main__":
	f = open("input2.txt").read().split("\n")
	writeF = open("output2.txt","w")
	n = int(f[0])
	del f[0]
	for i in range(1,n+1):
		t = int(f[0])
		del f[0]
		arr =[None]*t
		for j in xrange(t):
			arr[j] = int(f[0])
			del f[0]
		writeF.write("Case #%d: %d\n" % (i,numberOfDays(arr)))
		# print i
