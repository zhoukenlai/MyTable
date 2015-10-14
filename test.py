from MyTable import MyTable

tt=MyTable()
tt.createtable("aa,bb,cc,dd")
tt.insert("aa,dd","13|zhou")
tt.insert("dd,aa,bb","1|2|3")
tt.insert("aa,dd,cc","11|zhou11|xxx")
tt.insert("aa,dd,cc","11|zhou|xxx")

tt.Print()
print ''

where = tt.updatewhere("cc","11111","dd,aa","1|2")
tt.Print()
print ''

tt.Sort()
tt.Print()
print ''

where = tt.updatewhere("cc","11111","aa","11")
tt.Print()
print ''

#tt.updatewhere("aa,cc","1111|2222","dd,aa","1|2")
#tt.Print()
#print ''

#i=tt.halffind(['aa','bb'],['2','3'])
#print i

#tt.deletewhere("dd,cc","zhou|")
#tt.Print()
