#coding=gbk

class MyTable:
  __columnname = []
  __columnvalue = []
  __sortflag = False;

  # ��ʼ����ṹ��colname�԰�ǵĶ���(,)�ָ�
  def createtable(self,colname):
    if len(self.__columnname) == 0: 
      self.__columnname = colname.split(',')
    else:
      print "createtable error : table is not null"


  # �����ṹ�Լ�����
  def droptable(self):
    self.__columnname = []
    self.__columnvalue = []
    

  # ��ȡ����ţ�colnameֻ����һ����
  def __getColPos(self,colname):
    colpos = -1;
    try:
      colpos = self.__columnname.index(colname)
    except Exception:
      pass;
    return colpos
  

  # ָ��������ֵ�ĺϷ���У��
  def __checkCol(self,coln_li,colv_li):
    # ������Ϊ�գ��Ҹ�����ֵ�ĸ�����ͬ
    if len(coln_li)!=len(colv_li) or len(coln_li)==0:
      return False
    # ���������ڱ��д���
    for n in range(len(coln_li)):
      colpos = self.__getColPos(coln_li[n])
      if colpos==-1:
        return False
    return True


  # �ȽϺ������˴���У���ʽ�ĺϷ��ԣ��Ƚ϶���е�ֵ
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


  # ����һ����¼������ȱʡһЩ������ͬʱ������һ��������ʱ��˳��
  def insert(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # ָ��������ֵ�ĺϷ���У��
    if not self.__checkCol(coln_li,colv_li):
      print "insert error"
      return

    # ����˳�򣬲���ȱʡ��
    li = []
    for n in self.__columnname:
      try:
        colpos = coln_li.index(n)
        li.append(colv_li[colpos])
      except Exception:
        li.append('')
        
    self.__columnvalue.append(li)
    self.__sortflag = False;


  # ���Ҽ�¼
  def selectwhere(self,colname,colvalue):
    if self.__sortflag:
      result = self.__selectwhere2(colname,colvalue)
    else:
      result = self.__selectwhere1(colname,colvalue)
    return result
      
    
  # �������Ҽ�¼
  def __selectwhere1(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    
    # ָ��������ֵ�ĺϷ���У��
    if not self.__checkCol(coln_li,colv_li):
      print "select error"
      return

    result = []
    for i in range(len(self.__columnvalue)):
      if self.__Cmp(i,coln_li,colv_li)==0:
        result.append(self.__columnvalue[i])
    return result
        

  # ���ֲ��Ҽ�¼���ɷ��ض���
  def __selectwhere2(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    
    # ָ��������ֵ�ĺϷ���У��
    if not self.__checkCol(coln_li,colv_li):
      print "select error"
      return

    result = []
    i = self.__halffind(coln_li,colv_li)
    if len(i)==2 or (len(i)==1 and i[0]!=-1):
      for x in i:
        result.append(self.__columnvalue[x])
    return result
  

  # ���¼�¼
  def updatewhere(self,ucolname,ucolvalue,colname,colvalue):
    if self.__sortflag:
      self.__updatewhere2(ucolname,ucolvalue,colname,colvalue)
    else:
      self.__updatewhere1(ucolname,ucolvalue,colname,colvalue)

      
  # �������¼�¼���ɸ��¶���
  def __updatewhere1(self,ucolname,ucolvalue,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    ucoln_li = ucolname.split(',')
    ucolv_li = ucolvalue.split('|')
    
    # ָ��������ֵ�ĺϷ���У��
    if not self.__checkCol(coln_li,colv_li) or not self.__checkCol(ucoln_li,ucolv_li):
      print "update error"
      return

    for i in range(len(self.__columnvalue)):
      # �ҵ�  
      if self.__Cmp(i,coln_li,colv_li)==0:
        for idx in range(len(ucolv_li)):
          colpos = self.__getColPos(ucoln_li[idx])
          self.__columnvalue[i][colpos]=ucolv_li[idx]
        self.__sortflag = False;


  # ���ֲ��Ҹ��¼�¼���ɸ��¶���
  def __updatewhere2(self,ucolname,ucolvalue,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')
    ucoln_li = ucolname.split(',')
    ucolv_li = ucolvalue.split('|')
    
    # ָ��������ֵ�ĺϷ���У��
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
        

  # ɾ����¼
  def deletewhere(self,colname,colvalue):
    if self.__sortflag:
      self.__deletewhere2(colname,colvalue)
    else:
      self.__deletewhere1(colname,colvalue)
  

  # ����ɾ����¼����ɾ������
  def __deletewhere1(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # ָ��������ֵ�ĺϷ���У��
    if not self.__checkCol(coln_li,colv_li):
      print "delete error"
      return

    # ֻ�ܴӺ�����ǰ��ɾ��
    for i in range(len(self.__columnvalue)-1,-1,-1):
      if self.__Cmp(i,coln_li,colv_li)==0:
        del self.__columnvalue[i]


  # ���ֲ鵽ɾ����¼����ɾ������
  def __deletewhere2(self,colname,colvalue):
    coln_li = colname.split(',')
    colv_li = colvalue.split('|')

    # ָ��������ֵ�ĺϷ���У��
    if not self.__checkCol(coln_li,colv_li):
      print "delete error"
      return

    # ֻ�ܴӺ�����ǰ��ɾ��
    i = self.__halffind(coln_li,colv_li)
    if len(i)==2 or (len(i)==1 and i[0]!=-1):
      for x in range(len(i)-1,-1,-1):
        del self.__columnvalue[i[x]]


  # ���ֲ��ң��ɷ���һ����������
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
  

  # ����
  def Sort(self):
    self.__columnvalue.sort()
    self.__sortflag = True;
    
  
  # ȡ������
  def getRows(self):
    return len(self.__columnvalue)


  # ȡ������
  def getCols(self):
    return len(self.__columnname)
  
  
  # ��ӡ�����ֻ��ӡ100��
  def Print(self):
    print self.__columnname
    i=0
    for x in self.__columnvalue:
      i=i+1
      if i>100:
        break
      print x
      
        
    
  
