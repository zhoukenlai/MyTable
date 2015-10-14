#coding=gbk

class MyTable:
  columnname = []
  columnvalue = []
  sortflag = False;

  # 初始化表结构
  def createtable(self,colname):
    if len(self.columnname) == 0: 
      self.columnname = colname.split(',')
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


  # 比较函数
  def Cmp(self,i,coln_li,colv_li):
    for idx in range(len(colv_li)):
      colpos = self.getColPos(coln_li[idx])
      if self.columnvalue[i][colpos]<colv_li[idx]:
        return 1
      elif self.columnvalue[i][colpos]>colv_li[idx]:
        return -1
      else:
        pass
    return 0


  # 插入一条记录
  def insert(self,colname,colvalue):
    coln_li = colname.split(',')
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
    self.sortflag = False;


  # 查找记录
  def selectwhere(self,colname,colvalue):
    if self.sortflag:
      lili = self.selectwhere2(colname,colvalue)
    else:
      lili = self.selectwhere1(colname,colvalue)
    return lili
      
    
  # 遍历查找记录
  def selectwhere1(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    
    # 指定列名与值的合法性校验
    if not self.checkCol(coln_li,colv_li):
      print "select error"
      return

    lili = []
    for i in range(len(self.columnvalue)):
      if self.Cmp(i,coln_li,colv_li)==0:
        lili.append(self.columnvalue[i])
    return lili
        

  # 二分查找记录
  def selectwhere2(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    
    # 指定列名与值的合法性校验
    if not self.checkCol(coln_li,colv_li):
      print "select error"
      return

    lili = []
    i = self.halffind(coln_li,colv_li)
    if len(i)==2 or (len(i)==1 and i[0]!=-1):
      for x in i:
        lili.append(self.columnvalue[x])
    return lili
  

  # 删除记录
  def updatewhere(self,ucolname,ucolvalue,colname,colvalue):
    if self.sortflag:
      print "upd 2"
      self.updatewhere2(ucolname,ucolvalue,colname,colvalue)
    else:
      print "upd 1"
      self.updatewhere1(ucolname,ucolvalue,colname,colvalue)

      
  # 更新记录
  def updatewhere1(self,ucolname,ucolvalue,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    ucoln_li = ucolname.split(',')
    ucolv_li = ucolvalue.split('|')
    
    # 指定列名与值的合法性校验
    if not self.checkCol(coln_li,colv_li) or not self.checkCol(ucoln_li,ucolv_li):
      print "update error"
      return

    for i in range(len(self.columnvalue)):
      # 找到  
      if self.Cmp(i,coln_li,colv_li)==0:
        for idx in range(len(ucolv_li)):
          colpos = self.getColPos(ucoln_li[idx])
          self.columnvalue[i][colpos]=ucolv_li[idx]
        self.sortflag = False;


  # 更新记录
  def updatewhere2(self,ucolname,ucolvalue,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    ucoln_li = ucolname.split(',')
    ucolv_li = ucolvalue.split('|')
    
    # 指定列名与值的合法性校验
    if not self.checkCol(coln_li,colv_li) or not self.checkCol(ucoln_li,ucolv_li):
      print "update error"
      return

    i = self.halffind(coln_li,colv_li)
    if len(i)==2 or (len(i)==1 and i[0]!=-1):
      for x in range(len(i)-1,-1,-1):
        for idx in range(len(ucolv_li)):
          colpos = self.getColPos(ucoln_li[idx])
          self.columnvalue[x][colpos]=ucolv_li[idx]
    self.sortflag = False;
        

  # 删除记录
  def deletewhere(self,colname,colvalue):
    if self.sortflag:
      self.deletewhere2(colname,colvalue)
    else:
      self.deletewhere1(colname,colvalue)
  

  # 遍历删除记录
  def deletewhere1(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # 指定列名与值的合法性校验
    if not self.checkCol(coln_li,colv_li):
      print "delete error"
      return
    
    for i in range(len(self.columnvalue)-1,-1,-1):
      if self.Cmp(i,coln_li,colv_li)==0:
        del self.columnvalue[i]


  # 二分查到删除记录
  def deletewhere2(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # 指定列名与值的合法性校验
    if not self.checkCol(coln_li,colv_li):
      print "delete error"
      return
    
    i = self.halffind(coln_li,colv_li)
    if len(i)==2 or (len(i)==1 and i[0]!=-1):
      for x in range(len(i)-1,-1,-1):
        del self.columnvalue[i[x]]


  # 二分查找
  def halffind(self,coln_li,colv_li):
    l=0
    h=len(self.columnvalue)-1
    while l<=h:
      m=(l+h)//2
      ii = self.Cmp(m,coln_li,colv_li)
      if ii==0:
        bb=m
        ee=m
        while bb>0:
          if self.Cmp(bb-1,coln_li,colv_li)==0:
            bb=bb-1
          else:
            break
        while ee<len(self.columnvalue)-1:
          if self.Cmp(ee+1,coln_li,colv_li)==0:
            ee=ee+1
          else:
            break
        if bb==ee:
          return [bb]
        else:
          return [bb,ee]
      else:
        if ii==-1:
          h=m-1
        else:
          l=m+1
    if l>h:
      return [-1]
  

  # 排序
  def Sort(self):
    self.columnvalue.sort()
    self.sortflag = True;
    
  
  # 打印表
  def Print(self):
    for n in self.columnname:
      print n,
    print ''
    for x in self.columnvalue:
      for y in x:
        print y,
      print ''
      
        
    
  
