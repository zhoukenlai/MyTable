#coding=gbk

class MyTable:
  columnname = []
  columnvalue = []
  indexcolumn = []
  index = []

  # ��ʼ����ṹ
  def createtable(self,colname):
    if len(self.columnname) == 0: 
      self.columnname = colname.split(',')
      self.columnsize = len(self.columnname)
    else:
      print "createtable error : table is not null"


  # �����ṹ�Լ�����
  def droptable(self):
    self.columnname = []
    self.columnvalue = []

  # ��ȡ�����
  def getColPos(self,colname):
    colpos = -1;
    try:
      colpos = self.columnname.index(colname)
    except Exception:
      pass;
    return colpos

  # ָ��������ֵ�ĺϷ���У��
  def checkCol(self,coln_li,colv_li):
    # ������Ϊ�գ��Ҹ�����ֵ�ĸ�����ͬ
    if len(coln_li)!=len(colv_li) or len(coln_li)==0:
      return False
    # ���������ڱ��д���
    for n in range(len(coln_li)):
      colpos = self.getColPos(coln_li[n])
      if colpos==-1:
        return False
    return True


  # ����һ����¼
  def insert(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # ָ��������ֵ�ĺϷ���У��
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

    
  # ���Ҽ�¼
  def selectwhere(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    
    # ָ��������ֵ�ĺϷ���У��
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


  # ������Ҽ�¼
  def Cmp(self,i,coln_li,colv_li):
    for idx in range(len(colv_li)):
      colpos = self.getColPos(coln_li[idx])
      if self.columnvalue[i][colpos]>colv_li[idx]:
        return 1
      elif self.columnvalue[i][colpos]<colv_li[idx]:
        return -1
      else:
        pass
    return 0
        
  def selectwherex(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    
    # ָ��������ֵ�ĺϷ���У��
    if not self.checkCol(coln_li,colv_li):
      print "select error"
      return

    lili = []
    for i in range(len(self.columnvalue)):
      if self.Cmp(i,coln_li,colv_li)==0:
        lili.append(self.columnvalue[i])
    return lili
  

  # ���¼�¼
  def updatewhere(self,ucolname,ucolvalue,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    ucoln_li = ucolname.split(',')
    ucolv_li = ucolvalue.split('|')
    
    # ָ��������ֵ�ĺϷ���У��
    if not self.checkCol(coln_li,colv_li) or not self.checkCol(ucoln_li,ucolv_li):
      print "update error"
      return

    for i in range(len(self.columnvalue)):
      # �ҵ�  
      if self.Cmp(i,coln_li,colv_li)==0:
        for idx in range(len(ucolv_li)):
          colpos = self.getColPos(ucoln_li[idx])
          self.columnvalue[i][colpos]=ucolv_li[idx]


  # ɾ��һ����¼
  def deletewhere(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # ָ��������ֵ�ĺϷ���У��
    if not self.checkCol(coln_li,colv_li):
      print "delete error"
      return
    
    for i in range(len(self.columnvalue)-1,-1,-1):
      if self.Cmp(i,coln_li,colv_li)==0:
        del self.columnvalue[i]


  # ����
  def Sort(self):
    self.columnvalue.sort()
  
  # ��ӡ��
  def Print(self):
    for n in self.columnname:
      print n,
    print ''
    for x in self.columnvalue:
      for y in x:
        print y,
      print ''
      
        
    
  
