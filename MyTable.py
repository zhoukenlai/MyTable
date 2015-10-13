#coding=gbk

class MyTable:
  columnname = []
  columnvalue = []
  indexcolumn = []
  index = []

  # ��ʼ����ṹ
  def createtable(self,colname):
    if len(self.columnname) == 0: 
      self.columnname = colname.split('|')
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
    coln_li = colname.split('|')
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
    coln_li = colname.split('|')
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


  # ɾ��һ����¼
  def deletewhere(self,colname,colvalue):
    coln_li = colname.split('|')
    colv_li = colvalue.split('|')

    # ָ��������ֵ�ĺϷ���У��
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


  # ��ӡ��
  def Print(self):
    for n in self.columnname:
      print n,
    print ''
    for x in self.columnvalue:
      for y in x:
        print y,
      print ''
      
        
    
  
