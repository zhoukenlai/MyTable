# MyTable
Python实现的内存表，提供类似的数据库表操作，提高相关场景的开发效率

已实现如下API：</p>
1、createtable</p>
2、insert</p>
3、selectwhere</p>
4、updatewhere</p>
5、deletewhere</p>
6、Sort</p>
7、print</p>

更新说明 2015-10-14：</p>
1、insert支持缺列名插入</p>
2、select delete支持多个字段为条件</p>
3、select delete可以根据排序情况自动确定是遍历还是二分方式查找</p>


其他说明：</p>
排序是对全表字段进行排序，排序后才能用上二分查找；二分查找有局限性（不支持指定列创建索引），必须为全表字段的前缀，否则会按遍历方式查找</p>
