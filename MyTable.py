#coding=gbk

class MyTable:
  columnname = []
  columnvalue = []
  indexcolumn = []
  index = []

  def __init__(self):
    self.columnname = []


  # ��ʼ����ṹ
  def createtable(self,colname):
    if len(self.columnname) == 0: 
      self.columnname = colname.split('|')
      self.columnsize = len(self.columnname)
    else:
      print "createtable error:table not null"


  # �����ṹ�Լ�����
  def droptable(self):
    self.columnname = []
    self.columnvalue = []


  # ����һ����¼
  def insert(self,colvalue):
    col_li = colvalue.split('|')
    self.columnvalue.append(col_li)

    
  # ɾ��һ����¼
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


  # ɾ��һ����¼
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
        

  # ��ӡ��
  def Print(self):
    for n in self.columnname:
      print n,
    print ''
    for x in self.columnvalue:
      for y in x:
        print y,
      print ''
      
        
    
  
