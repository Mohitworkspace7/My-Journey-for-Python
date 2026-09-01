Seconds = int(input("Seconds = "))
second = Seconds % 60 #Module liya hai mtlb whole min complete ke baad jo bacha vo seconds
Minute = int(Seconds / 60) #int type liye h ki whole divide hi dikhayega
print((Minute,"min",second,"secs"))