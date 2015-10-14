#coding=gbk

class MyTable:
  __columnname = []
  __columnvalue = []
  __sortflag = False;

  # 初始化表结构，colname以半角的逗号(,)分隔
  def createtable(self,colname):
    if len(self.__columnname) == 0: 
      self.__columnname = colname.split(',')
    else:
      print "createtable error : table is not null"


  # 清除表结构以及数据
  def droptable(self):
    self.__columnname = []
    self.__columnvalue = []
    

  # 获取列序号，colname只能是一个列
  def __getColPos(self,colname):
    colpos = -1;
    try:
      colpos = self.__columnname.index(colname)
    except Exception:
      pass;
    return colpos
  

  # 指定列名与值的合法性校验
  def __checkCol(self,coln_li,colv_li):
    # 列名不为空，且个数与值的个数相同
    if len(coln_li)!=len(colv_li) or len(coln_li)==0:
      return False
    # 列名必须在表中存在
    for n in range(len(coln_li)):
      colpos = self.__getColPos(coln_li[n])
      if colpos==-1:
        return False
    return True


  # 比较函数，此处不校验格式的合法性，比较多个列的值
  def __Cmp(self,i,coln_li,colv_li):
    for idx in range(len(colv_li)):
      colpos = self.__getColPos(coln_li[idx])
      if self.__columnvalue[i][colpos]<colv_li[idx]:
        return 1
      elif self.__columnvalue[i][colpos]>colv_li[idx]:
        return -1
      else:
        pass
    return 0


  # 插入一条记录，可以缺省一些列名，同时列名不一定按建表时的顺序
  def insert(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # 指定列名与值的合法性校验
    if not self.__checkCol(coln_li,colv_li):
      print "insert error"
      return

    # 矫正顺序，补充缺省的
    li = []
    for n in self.__columnname:
      try:
        colpos = coln_li.index(n)
        li.append(colv_li[colpos])
      except Exception:
        li.append('')
        
    self.__columnvalue.append(li)
    self.__sortflag = False;


  # 查找记录
  def selectwhere(self,colname,colvalue):
    if self.__sortflag:
      result = self.__selectwhere2(colname,colvalue)
    else:
      result = self.__selectwhere1(colname,colvalue)
    return result
      
    
  # 遍历查找记录
  def __selectwhere1(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    
    # 指定列名与值的合法性校验
    if not self.__checkCol(coln_li,colv_li):
      print "select error"
      return

    result = []
    for i in range(len(self.__columnvalue)):
      if self.__Cmp(i,coln_li,colv_li)==0:
        result.append(self.__columnvalue[i])
    return result
        

  # 二分查找记录，可返回多行
  def __selectwhere2(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    
    # 指定列名与值的合法性校验
    if not self.__checkCol(coln_li,colv_li):
      print "select error"
      return

    result = []
    i = self.__halffind(coln_li,colv_li)
    if len(i)==2 or (len(i)==1 and i[0]!=-1):
      for x in i:
        result.append(self.__columnvalue[x])
    return result
  

  # 更新记录
  def updatewhere(self,ucolname,ucolvalue,colname,colvalue):
    if self.__sortflag:
      self.__updatewhere2(ucolname,ucolvalue,colname,colvalue)
    else:
      self.__updatewhere1(ucolname,ucolvalue,colname,colvalue)

      
  # 遍历更新记录，可更新多行
  def __updatewhere1(self,ucolname,ucolvalue,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    ucoln_li = ucolname.split(',')
    ucolv_li = ucolvalue.split('|')
    
    # 指定列名与值的合法性校验
    if not self.__checkCol(coln_li,colv_li) or not self.__checkCol(ucoln_li,ucolv_li):
      print "update error"
      return

    for i in range(len(self.__columnvalue)):
      # 找到  
      if self.__Cmp(i,coln_li,colv_li)==0:
        for idx in range(len(ucolv_li)):
          colpos = self.__getColPos(ucoln_li[idx])
          self.__columnvalue[i][colpos]=ucolv_li[idx]
        self.__sortflag = False;


  # 二分查找更新记录，可更新多行
  def __updatewhere2(self,ucolname,ucolvalue,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    ucoln_li = ucolname.split(',')
    ucolv_li = ucolvalue.split('|')
    
    # 指定列名与值的合法性校验
    if not self.__checkCol(coln_li,colv_li) or not self.__checkCol(ucoln_li,ucolv_li):
      print "update error"
      return

    i = self.__halffind(coln_li,colv_li)
    if len(i)==2 or (len(i)==1 and i[0]!=-1):
      for x in range(len(i)):
        for idx in range(len(ucolv_li)):
          colpos = self.__getColPos(ucoln_li[idx])
          self.__columnvalue[x][colpos]=ucolv_li[idx]
    self.__sortflag = False;
        

  # 删除记录
  def deletewhere(self,colname,colvalue):
    if self.__sortflag:
      self.__deletewhere2(colname,colvalue)
    else:
      self.__deletewhere1(colname,colvalue)
  

  # 遍历删除记录，可删除多行
  def __deletewhere1(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # 指定列名与值的合法性校验
    if not self.__checkCol(coln_li,colv_li):
      print "delete error"
      return

    # 只能从后面往前面删除
    for i in range(len(self.__columnvalue)-1,-1,-1):
      if self.__Cmp(i,coln_li,colv_li)==0:
        del self.__columnvalue[i]


  # 二分查到删除记录，可删除多行
  def __deletewhere2(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # 指定列名与值的合法性校验
    if not self.__checkCol(coln_li,colv_li):
      print "delete error"
      return

    # 只能从后面往前面删除
    i = self.__halffind(coln_li,colv_li)
    if len(i)==2 or (len(i)==1 and i[0]!=-1):
      for x in range(len(i)-1,-1,-1):
        del self.__columnvalue[i[x]]


  # 二分查找，可返回一个序列区间
  def __halffind(self,coln_li,colv_li):
    l=0
    h=len(self.__columnvalue)-1
    while l<=h:
      m=(l+h)//2
      ii = self.__Cmp(m,coln_li,colv_li)
      if ii==0:
        bb=m
        ee=m
        while bb>0:
          if self.__Cmp(bb-1,coln_li,colv_li)==0:
            bb=bb-1
          else:
            break
        while ee<len(self.__columnvalue)-1:
          if self.__Cmp(ee+1,coln_li,colv_li)==0:
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
    self.__columnvalue.sort()
    self.__sortflag = True;
    
  
  # 取表行数
  def getRows(self):
    return len(self.__columnvalue)


  # 取表列数
  def getCols(self):
    return len(self.__columnname)
  
  
  # 打印表，最多只打印100行
  def Print(self):
    print self.__columnname
    i=0
    for x in self.__columnvalue:
      i=i+1
      if i>100:
        break
      print x
      
        
    
  
