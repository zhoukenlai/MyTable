from MyTable import MyTable

tt=MyTable()
tt.createtable("aa,bb,cc,dd")

print "begin insert"
for i in range(1000000,-1,-1):
  tt.insert("aa,bb,cc,dd",str(i)+"|11|22|zhou")
print "end insert"

print "begin sort"
tt.Sort()
print "end sort"

print "begin select"
for i in range(100):
  tt.selectwhere("aa","3456")
print "end select"


#tt.updatewhere("aa,cc","1111|2222","dd,aa","1|2")
#tt.Print()
#print ''

#i=tt.halffind(['aa','bb'],['2','3'])
#print i

#tt.deletewhere("dd,cc","zhou|")
#tt.Print()
