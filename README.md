# MyTable
Python实现的内存表，提供类似的数据库表操作，提高相关场景的开发效率

已实现如下API：</p>
1、createtable</p>
2、insert</p>
3、selectwhere</p>
4、deletewhere</p>
5、print</p>

更新说明 2015-10-13：</p>
1、insert支持缺列名插入</p>
2、select delete支持多个字段为条件</p>

其他说明：
目前select delete都是遍历是查找的，后续将改为索引方式实现</p>

还需补充API：</p>
1、updatewhere</p>
2、createindex</p>
3、orderby</p>
