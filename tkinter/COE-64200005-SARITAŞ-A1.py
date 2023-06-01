###############################################################################
#  Name:         Melisa Sarıtaş
#  Student ID:   64200005
#  Department:   Computer Engineering
#  
#  Assignment ID: A1
###############################################################################

###############################################################################
#  QUESTION I
#  Description:
#  It can be done several things with tkinter. Such as doing login, online 
#  order or online payment interfaces. In the example code, it is done a pizza
#  interface which includes a button for seeing the order summary and a button 
#  to reset what is chosen. Also there are a place to write the name of the 
#  customer, radiobuutons to choose the size of the pizza, combobox to choose
#  the crust type of the pizza, a listbox for choosing the toppings, 
#  checkbuttons to choose extras and a place to write comments. All of them are
#  placed to seem symmetrical.
#  
#  Sources:
#  www.geeksforgeeks.org
#  www.codegrepper.com
#  stackoverflow.com
###############################################################################

from tkinter import ttk
import tkinter as tk 

window = tk.Tk()
window.title("Pizza Place")

window.geometry("500x650")
window.resizable(False, False)

#Custumer Name
label1 = ttk.Label(window, text = "Costumer Name: ")
label1.pack()
label1.place(x = 40, y = 10)
entry1 = ttk.Entry(window)
entry1.pack()
entry1.place(x = 140, y = 10, width = 300)

#Pizza Size
label2 = ttk.Label(window, text = "Pizza Size: ")
label2.pack()
label2.place(x = 78, y = 50)

a = tk.StringVar()

small = ttk.Radiobutton(window, text = "Small", value = "Small", variable = a)
small.pack()
small.place(x = 146, y = 50)

medium = ttk.Radiobutton(window, text = "Medium", value = "Medium", variable = a)
medium.pack()
medium.place(x = 206, y = 50)

large = ttk.Radiobutton(window, text = "Large", value = "Large", variable = a)
large.pack()
large.place(x = 280, y = 50)

#Crust Type
label3 = ttk.Label(window, text = "Crust Type: ")
label3.pack()
label3.place(x = 72, y = 90)

n = tk.StringVar()

crustchoosen = ttk.Combobox(window, width = 46, textvariable = n)
  

crustchoosen['values'] = (' Stuffed',
                          ' Cracker',
                          ' Flat Bread',
                          ' Thin',
                          ' Cheese',
                          ' Thick',
                          ' Wrapping It Up', 
                          )
crustchoosen.pack()
crustchoosen.place(x = 140, y = 90)
crustchoosen.current()

#Toppings
label4 = ttk.Label(window, text = "Toppings: ")
label4.pack()
label4.place(x = 77, y = 130)

toppings = tk.Listbox(window, height = 6, width = 20, selectmode = "multiple")
  
toppings.insert(1, "Pepperoni")
toppings.insert(2, "Sausage")
toppings.insert(3, "Green Peppers")
toppings.insert(4, "Onions")
toppings.insert(5, "Tomatoes")
toppings.insert(6, "Anchovies")

toppings.pack()
toppings.place(x = 140, y = 130)

#Extras
label5= ttk.Label(window, text ='Extras: ') 
label5.pack()
label5.place(x = 95, y = 250)

var1= tk.IntVar()
var2= tk.IntVar()
var3= tk.IntVar()

Button1 = tk.Checkbutton(window, text = "BreadSticks", variable = var1, 
                         onvalue = 1, offvalue = 0, height = 1, width = 8) 
Button2 = tk.Checkbutton(window, text = "Salad", variable = var2,
                         onvalue = 1, offvalue = 0, height = 1, width = 8)
Button3 = tk.Checkbutton(window, text = "Soda", variable = var3, 
                         onvalue = 1, offvalue = 0, height = 1, width = 8)

Button1.pack()
Button1.place(x = 145, y = 250)
Button2.pack() 
Button2.place(x = 235, y = 250)
Button3.pack() 
Button3.place(x = 325, y = 250)

#Order Comments
label6 = ttk.Label(window, text = "Order Comments: ")
label6.pack()
label6.place(x = 32, y = 290)

inputtxt = tk.Text(window, height = 10, width = 37)
inputtxt.pack()
inputtxt.place(x = 140, y = 290)

#summary order function and button
def summaryoforder():
    window1 = tk.Tk()
    window1.title("Message")
    window1.geometry("400x550")
    
    label1 = tk.Label(window1 ,text = "Customer Name: ")
    label1.pack()
    label1.place(x = 40, y = 10)
    
    label2 = tk.Label(window1 ,text = entry1.get())
    label2.pack()
    label2.place(x = 140, y = 10)
    
    label3 = tk.Label(window1, text = "Pizza Size: ")
    label3.pack()
    label3.place(x = 78, y = 50)
    
    label4 = tk.Label(window1 ,text = a.get())
    label4.pack()
    label4.place(x = 140, y = 50)
    
    label5 = tk.Label(window1, text = "Crust Type: ")
    label5.pack()
    label5.place(x = 72, y = 90)
    
    label6 = tk.Label(window1, text = n.get())
    label6.pack()
    label6.place(x = 140, y = 90)
    
    label7 = tk.Label(window1, text = "Toppings: ")
    label7.pack()
    label7.place(x = 77, y = 130)
    
    r = 0
    
    for i in toppings.curselection():
        b = [toppings.get(i)]
        for t in range(len(b)):
            r += 1
            label8 = tk.Label(window1, text = toppings.get(i))
            if r == 1:
                label8.pack()
                label8.place(x = 140, y = 130)
            if r == 2:
                label8.pack()
                label8.place(x = 140, y = 150)
            if r == 3:
                label8.pack()
                label8.place(x = 140, y = 170)
            if r == 4:
                label8.pack()
                label8.place(x = 140, y = 190)
            if r == 5:
                label8.pack()
                label8.place(x = 140, y = 210)
            if r == 6:
                label8.pack()
                label8.place(x = 140, y = 230)
            
    label9= tk.Label(window1, text ='Extras: ') 
    label9.pack()
    label9.place(x = 95, y = 250)
    
    if var1.get() == 1:
        label10= tk.Label(window1, text = Button1.cget("text")) 
        label10.pack()
        label10.place(x = 140, y = 250)
    
    if var2.get() == 1:
        label11= tk.Label(window1, text = Button2.cget("text")) 
        label11.pack()
        label11.place(x = 140, y = 270)
    
    if var3.get() == 1:
        label12= tk.Label(window1, text = Button3.cget("text")) 
        label12.pack()
        label12.place(x = 140, y = 290)
        
    label13 = tk.Label(window1, text = "Order Comments: ")
    label13.pack()
    label13.place(x = 32, y = 310)
    
    label14 = tk.Label(window1, text = inputtxt.get("1.0", "end"))
    label14.pack( padx= 23, pady= 23)
    label14.place(x = 140, y = 310)
  
button1 = ttk.Button(window, text = "Place Order", command = summaryoforder)
button1.pack()
button1.place(x = 140, y = 470)

#reset function and button
def reset():
    try:
        entry1.delete(0, "end")
        a.set(None)
        crustchoosen.set('')
        toppings.selection_clear(0, "end")
        Button1.deselect()
        Button2.deselect()
        Button3.deselect()
        inputtxt.delete("1.0", "end")
    except:
        pass
    
button2 = ttk.Button(window, text = "Reset Values",command =reset)
button2.pack()
button2.place(x = 220, y = 470)

window.mainloop()

###############################################################################
#  QUESTION II
#  Description:
#  In the example, it is done generating and reading files, and it is written  
#  random number into the files. Recorded the time for determining execution 
#  time of functions which are fillFile and readFile. After that it is noted 
#  the execution times in a text file named fileStats.
#
#  Sources:
#  www.geeksforgeeks.org
###############################################################################

import random
import time

def fillFile(fileSize, fileName):
    print(fileName)
    #open a file
    file = open(fileName,"w")
    for i in range(fileSize):
        a = random.randint(0,fileSize+1000)
        file.write(str(a))
    file.close()
        
def readFile(fileName):
    file2 = open(fileName, "r")
    b = [file2.read()]
    print(b)
    file2.close()
    
fileSizes = [1000, 5000, 10000, 25000, 50000, 75000, 100000]
c = []
d = []
for f in fileSizes: 
    start  = time.time()
    fillFile(f, "file" + str(f))
    finish = time.time()
    runTime = finish - start
    c.append(runTime)
    start2 = time.time()
    readFile("file" + str(f))
    finish2 = time.time()
    runTime2 = finish2 - start2
    d.append(runTime2)
file3 = open("C://Users//Dell//OneDrive - medipol.edu.tr//Masaüstü//fileStats.txt","w")    
file3.write("fillFile: " + str(c[0])+" "+ str(c[1])+" "+ str(c[2])+" "+ str(c[3])+" "+
            str(c[4])+" "+ str(c[5])+" "+ str(c[6])+" "+ "\n")
file3.write("readFile: " + str(d[0])+" "+ str(d[1])+" "+ str(d[2])+" "+ str(d[3])+" "+
            str(d[4])+" "+ str(d[5])+" "+ str(d[6]))
file3.close()

###############################################################################
#  QUESTION III
#  Description:
#  In the example, it is read the files that created in the previous example 
#  and then it is sorted the files by using the sorting functions that are 
#  bubbleSort, selectionSort, insertionSort, shellSort, mergeSort, quickSort 
#  and heapSort. After that it is recorded the execution times of functions by
#  using time library for each file and noted in a text file which is sortStats.
#  Main aim of the example is doing a benchmark analysis. 
#
#  Sources:
#  runestone.academy
#  www.geeksforgeeks.org
#  stackoverflow.com
###############################################################################

import time
def readFile(fileName):
    file2 = open(fileName, "r")
    alist = [n for n in file2.read()]
    return alist
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

def shellSort(alist):
    n = len(alist)
    gap = n/2
    while gap > 0:
        for i in range(int(gap),n):
            temp = alist[i]
            j = i
            while j >= int(gap) and alist[j-int(gap)] >temp:
                alist[j] = alist[j-int(gap)]
                j -= int(gap)
            alist[j] = temp
        gap /= 2

def mergeSort(alist):
	if len(alist) > 1:
		mid = len(alist)//2
		L = alist[:mid]
		R = alist[mid:]
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				alist[k] = L[i]
				i += 1
			else:
				alist[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			alist[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			alist[k] = R[j]
			j += 1
			k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

def heapify(alist, n, i):
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	

	if l < n and alist[largest] < alist[l]:
		largest = l

	if r < n and alist[largest] < alist[r]:
		largest = r

	if largest != i:
		alist[i], alist[largest] = alist[largest], alist[i]
		heapify(alist, n, largest)

def heapSort(alist):
    n = len(alist)
    for i in range(n//2 - 1, -1, -1):
        heapify(alist, n, i)
    for i in range(n-1, 0, -1):
        alist[i], alist[0] = alist[0], alist[i] 
        heapify(alist, i, 0)

fileSizes = [1000, 5000, 10000, 25000, 50000, 75000, 100000]
c = []
d = []
e = []
s = []
g = []
h = []
k = []
 
print("Benchmark analysis is started.")

for f in fileSizes:
    # 1st
    start1  = time.time()
    bubbleSort(readFile("file" + str(f)))
    finish1 = time.time()
    runTime1 = finish1 - start1
    c.append(runTime1)
    #2nd
    start2  = time.time()
    selectionSort(readFile("file" + str(f)))
    finish2 = time.time()
    runTime2 = finish2 - start2
    d.append(runTime2)
    #3rd
    start3  = time.time()
    insertionSort(readFile("file" + str(f)))
    finish3 = time.time()
    runTime3 = finish3 - start3
    e.append(runTime3)
    #4th
    start4 = time.time()
    shellSort(readFile("file" + str(f)))
    finish4 = time.time()
    runTime4 = finish4 - start4
    s.append(runTime4)
    #5th
    start5  = time.time()
    mergeSort(readFile("file" + str(f)))
    finish5 = time.time()
    runTime5 = finish5 - start5
    g.append(runTime5)
    #7th
    start7  = time.time()
    heapSort(readFile("file" + str(f)))
    finish7 = time.time()
    runTime7 = finish7 - start7
    k.append(runTime7)
    
print("Benchmark analysis is finished.")   
 
file3 = open("C://Users//Dell//OneDrive - medipol.edu.tr//Masaüstü//sortStats.txt","w")    
file3.write("Bubble_Sort: " + str(c[0])+" "+ str(c[1])+" "+ str(c[2])+" "+ str(c[3])+" "+
            str(c[4])+" "+ str(c[5])+" "+ str(c[6])+" "+ "\n")
file3.write("Selection_Sort: " + str(d[0])+" "+ str(d[1])+" "+ str(d[2])+" "+ str(d[3])+" "+
            str(d[4])+" "+ str(d[5])+" "+ str(d[6])+ "\n")
file3.write("Insertion_Sort: " + str(e[0])+" "+ str(e[1])+" "+ str(e[2])+" "+ str(e[3])+" "+
            str(e[4])+" "+ str(e[5])+" "+ str(e[6])+ "\n")
file3.write("Shell_Sort: " + str(s[0])+" "+ str(s[1])+" "+ str(s[2])+" "+ str(s[3])+" "+
            str(s[4])+" "+ str(s[5])+" "+ str(s[6])+ "\n")
file3.write("Merge_Sort: " + str(g[0])+" "+ str(g[1])+" "+ str(g[2])+" "+ str(g[3])+" "+
            str(g[4])+" "+ str(g[5])+" "+ str(g[6])+ "\n")
file3.write("Heap_Sort: " + str(k[0])+" "+ str(k[1])+" "+ str(k[2])+" "+ str(k[3])+" "+
            str(k[4])+" "+ str(k[5])+" "+ str(k[6]))

for f in fileSizes:
    #6th
    start6  = time.time()
    quickSort(readFile("file" + str(f)))
    finish6 = time.time()
    runTime6 = finish6 - start6
    h.append(runTime6)
file3.write("Quick_Sort: " + str(h[0])+" "+ str(h[1])+" "+ str(h[2])+" "+ str(h[3])+" "+
            str(h[4])+" "+ str(h[5])+" "+ str(h[6])+ "\n")
file3.close()

###############################################################################
#  QUESTION IV
#  Description:
#  In the example, the main aim is to do a benchmark analysis. At that time, 
#  the analysis is about searching. There are 3 functions that are bubbleSort 
#  which is for sorting the list of the integers that the file includes, 
#  orderedSequentialSearch and binarySearch, and 1 class which is Hashtable. It
#  is sorted the file and had a hash for each integer. Then it is done a list 
#  which includes 1000 random numbers and searched 500 of them with the search 
#  functions. Also, it is chosen 500 elements of the hash table and searched 
#  with hashing. After that it is recorded the execution times and noted into a
#  text file that is searchStats.
#
#  Sources:
#  runestone.academy
#  www.geeksforgeeks.org
#  stackoverflow.com
###############################################################################

import random
import time

def heapify(alist, n, i):
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	

	if l < n and alist[largest] < alist[l]:
		largest = l

	if r < n and alist[largest] < alist[r]:
		largest = r

	if largest != i:
		alist[i], alist[largest] = alist[largest], alist[i]
		heapify(alist, n, largest)

def heapSort(alist):
    n = len(alist)
    for i in range(n//2 - 1, -1, -1):
        heapify(alist, n, i)
    for i in range(n-1, 0, -1):
        alist[i], alist[0] = alist[0], alist[i] 
        heapify(alist, i, 0)

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1
    return found

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

file = open("C://Users//Dell//OneDrive - medipol.edu.tr//Masaüstü//file100000","r")
list = [int(n) for n in file.read()]
heapSort(list)

H = HashTable()

for s in list:
    t = HashTable.put(H,s,"data" + str(s))
    H.size = 11007

list1 = [random.randint(0,100000) for t in range(1000)]
list2 = []
list3 = []

for r in range(500):
    list2.append(list1[r+5])
for r in range(10):
    list3.append(r)

print("Benchmark analysis is started.")

start1  = time.time()
for n in range(500):
    orderedSequentialSearch(list1,list2[n])
finish1 = time.time()
runTime1 = finish1 - start1
print(runTime1)

start2  = time.time()
for d in range(500):
    binarySearch(list1,list2[d])
finish2 = time.time()
runTime2 = finish2 - start2
print(runTime2)

start3  = time.time()
for m in list3:
    H.get(list3,m)
finish3 = time.time()
runTime3 = finish3 - start3
print(runTime3)

print("Benchmark analysis is finished.")
file = open("C://Users//Dell//OneDrive - medipol.edu.tr//Masaüstü//searchStats.txt","w")    
file.write("Linear_Search: " + str(runTime1)+"\n")
file.write("Binary_Search: " + str(runTime2)+"\n")
file.write("Hashing: " + str(runTime3)+"\n")
file.close()