from collections import deque

def printMax(arr, n, k):
	Q = deque()
	for i in range(k):
		while Q and arr[i] >= arr[Q[-1]]:
			Q.pop()
		Q.append(i)

	for i in range(k,n):
		print(str(arr[Q[0]]) + " ", end = "")

		while Q and Q[0] <= i-k:
			Q.popleft()

		while Q and arr[i] >= arr[Q[-1]]:	#last ele
			Q.pop()
		Q.append(i)
	print(str(arr[Q[0]]))

if __name__=="__main__":
	arr = [12, 1, 78, 90, 57, 89, 56]
	k = 0
	printMax(arr, len(arr), k)