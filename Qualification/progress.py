# https://www.facebook.com/hackercup/problem/1254819954559001/
__author__ = "Moonis Javed"
__email__ = "monis.javed@gmail.com"

import math

def checkPoint(progress, pointX, pointY):
	dist = math.sqrt((pointY - 50)**2 + (pointX-50)**2)
	startX = 50
	startY = 100
	if dist > 50:
		return False
	else:
		firstLine = math.sqrt((startY - 50)**2 + (startX - 50)**2)
		secondLine = math.sqrt((startX - pointX)**2 + (startY - pointY)**2)
		arc = math.acos((firstLine**2 + dist**2 - secondLine**2) / (2 * firstLine * dist))
		return math.degrees(arc)/3.6 <= progress

if __name__ == "__main__":
	f = open("input.txt").read().split("\n")
	writeF = open("output.txt","w")
	n = int(f[0])
	for i in range(1,n+1):
		progress,pointX,pointY = [int(j) for j in f[i].split()]
		writeF.write("Case #%s: "%i)
		flag = checkPoint(progress,pointX,pointY)
		if flag is True:
			flag = "black"
		else:
			flag = "white"
		writeF.write("%s\n"%flag)
		
