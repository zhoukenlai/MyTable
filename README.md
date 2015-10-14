# MyTable
Python实现的内存表，提供类似的数据库表操作，提高相关场景的开发效率，可能的应用场景如下：</p>
1、程序运行时，加载参数表，运行时需要多次读取参数内容的</p>
2、与数据库操作关联，从数据库查询时保存到该表，进行一定的内存操作后，再更新到数据库</p>
3、其他业务逻辑中需要做类似二位表操作的</p>

已实现如下API：</p>
createtable;
droptable;
insert;
selectwhere;
updatewhere;
deletewhere;
Sort;
getRows;
getCols
print;

更新说明 2015-10-14：</p>
1、insert支持缺列名插入</p>
2、select delete支持多个字段为条件</p>
3、select delete可以根据排序情况自动确定是遍历还是二分方式查找</p>


其他说明：</p>
排序是对全表字段进行排序，排序后才能用上二分查找；二分查找有局限性（不支持指定列创建索引），必须为全表字段的前缀，否则会按遍历方式查找</p>
