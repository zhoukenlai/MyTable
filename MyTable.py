#coding=gbk

class MyTable:
  columnname = []
  columnvalue = []
  indexcolumn = []
  index = []

  def __init__(self):
    self.columnname = []


  # 初始化表结构
  def createtable(self,colname):
    if len(self.columnname) == 0: 
      self.columnname = colname.split('|')
      self.columnsize = len(self.columnname)
    else:
      print "createtable error:table not null"


  # 清除表结构以及数据
  def droptable(self):
    self.columnname = []
    self.columnvalue = []


  # 插入一条记录
  def insert(self,colvalue):
    col_li = colvalue.split('|')
    self.columnvalue.append(col_li)

    
  # 删除一条记录
  def selectwhere(self,colname,colvalue):
    colpos = -1;
    try:
      colpos = self.columnname.index(colname)
    except Exception:
      print "column error"
      return

    irow = -1
    for x in self.columnvalue:
      irow = irow+1
      if x[colpos]==colvalue:
        return x


  # 删除一条记录
  def deletewhere(self,colname,colvalue):
    colpos = -1;
    try:
      colpos = self.columnname.index(colname)
    except Exception:
      print "column error"
      return

    irow = -1
    for x in self.columnvalue:
      irow = irow+1
      if x[colpos]==colvalue:
        del self.columnvalue[irow]
        irow = irow-1
        

  # 打印表
  def Print(self):
    for n in self.columnname:
      print n,
    print ''
    for x in self.columnvalue:
      for y in x:
        print y,
      print ''
      
        
    
  
