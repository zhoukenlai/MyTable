#coding=gbk

class MyTable:
  columnname = []
  columnvalue = []
  indexcolumn = []
  index = []

  # 初始化表结构
  def createtable(self,colname):
    if len(self.columnname) == 0: 
      self.columnname = colname.split('|')
      self.columnsize = len(self.columnname)
    else:
      print "createtable error : table is not null"


  # 清除表结构以及数据
  def droptable(self):
    self.columnname = []
    self.columnvalue = []

  # 获取列序号
  def getColPos(self,colname):
    colpos = -1;
    try:
      colpos = self.columnname.index(colname)
    except Exception:
      pass;
    return colpos

  # 指定列名与值的合法性校验
  def checkCol(self,coln_li,colv_li):
    # 列名不为空，且个数与值的个数相同
    if len(coln_li)!=len(colv_li) or len(coln_li)==0:
      return False
    # 列名必须在表中存在
    for n in range(len(coln_li)):
      colpos = self.getColPos(coln_li[n])
      if colpos==-1:
        return False
    return True


  # 插入一条记录
  def insert(self,colname,colvalue):
    coln_li = colname.split('|')
    colv_li = colvalue.split('|')

    # 指定列名与值的合法性校验
    if not self.checkCol(coln_li,colv_li):
      print "insert error"
      return

    li = []
    for n in self.columnname:
      try:
        colpos = coln_li.index(n)
        li.append(colv_li[colpos])
      except Exception:
        li.append('')
        
    self.columnvalue.append(li)

    
  # 查找记录
  def selectwhere(self,colname,colvalue):
    coln_li = colname.split('|')
    colv_li = colvalue.split('|')
    
    # 指定列名与值的合法性校验
    if not self.checkCol(coln_li,colv_li):
      print "select error"
      return

    lili = []
    for i in range(len(self.columnvalue)):
      iFind = 0;
      for idx in range(len(colv_li)):
        colpos = self.getColPos(coln_li[idx])
        if self.columnvalue[i][colpos]==colv_li[idx]:
          iFind = iFind+1
        else:
          break;
      if iFind == len(colv_li):
        lili.append(self.columnvalue[i])
    return lili


  # 删除一条记录
  def deletewhere(self,colname,colvalue):
    coln_li = colname.split('|')
    colv_li = colvalue.split('|')

    # 指定列名与值的合法性校验
    if not self.checkCol(coln_li,colv_li):
      print "delete error"
      return
    
    for i in range(len(self.columnvalue)-1,-1,-1):
      iFind = 0;
      for idx in range(len(colv_li)):
        colpos = self.getColPos(coln_li[idx])
        if self.columnvalue[i][colpos]==colv_li[idx]:
          iFind = iFind+1
        else:
          break;
        
      if iFind == len(colv_li):
        del self.columnvalue[i]


  # 打印表
  def Print(self):
    for n in self.columnname:
      print n,
    print ''
    for x in self.columnvalue:
      for y in x:
        print y,
      print ''
      
        
    
  
