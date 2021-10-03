mem = [0] * 65536
ptr = 0
cinst = 0
prg = input()

def runcode(char):
	global mem, ptr, cinst
	if char == "[":
		ptr += 1
	elif char == "]":
		ptr -= 1
	elif char == "J":
		cinst = mem[ptr]
	elif char == "R":
		runcode(chr(mem[ptr]))
	elif char == "+":
		mem[ptr] += 1
	elif char == "-":
		mem[ptr] -= 1
	elif char == "C":
		cinst += 1
		if mem[ptr]:
			runcode(prg[cinst])
	cinst += 1

while cinst in range(0, len(prg)):
	runcode(prg[cinst])

print("".join([chr(x) for x in mem]))
