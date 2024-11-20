import redis

# string 就是普通的键值对
# r = redis.Redis(host='192.168.245.129', port=6379, db=0)
#
# # 设置键值对
# r.set('mykey', 'Hello Redis!')
#
# # 获取键值对
# value = r.get('mykey')
# print('mykey:', value.decode('utf-8'))  # 输出: Hello Redis!
#
# # 删除键值对
# r.delete('mykey')
#
# # 检查键是否存在
# exists = r.exists('mykey')
# print('mykey exists:', exists)  # 输出: 0 (表示键不存在)
#
# # 列出所有的键
# keys = r.keys('*')
# print('All keys:', keys)  # 输出: [] (如果数据库为空)
#
# # 关闭连接
# r.close()

# hash
# r = redis.Redis(host='192.168.245.129', port=6379, db=0)
#
# r.hset('type:fe', 'name', 'Alice')
#
# val = r.hget('type:fe',"name")
#
# print(val)
# # 关闭连接
# r.hdel('type:fe',"name")
# r.close()

#list
r = redis.Redis(host='192.168.245.129', port=6379, db=0)
# 在列表左侧插入元素
r.set("name","1")



# 获取列表中指定索引的元素
index_element = r.dump('name')
r.restore('name', 0, index_element)
# print(f"Element at index 0: {index_element.decode('utf-8')}")
# r.delete('mylist')

# 检查列表是否已被删除
if not r.exists('name'):
    print("The list has been successfully deleted.")
else:
    print("The list still exists.")
print(f"Element at index 0: {r.get("name1")}")
r.close()

# alter table name rename as name1;

# alter table name1 add name1 varchar(1024) not null default '1';

# ALTER TABLE name1 MODIFY name1 VARCHAR(11);

# ALTER TABLE name1 CHANGE name1 age1 VARCHAR(11);


# CREATE TABLE Employees (
#     EmployeeID INT PRIMARY KEY,
#     Email VARCHAR(100) UNIQUE,
#     Name VARCHAR(100)
# );
/*
	1. 定义外键key
	2. 给外键添加约束（执行引用）references 引用
*/
-- 创建年级表
# CREATE TABLE `grade`(
# 	`gradeid` INT(10) NOT NULL COMMENT '年级id',
# 	`gradename` VARCHAR(50) NOT NULL COMMENT '年纪名称',
# 	PRIMARY KEY (`gradeid`)
# )ENGINE=INNODB DEFAULT CHARSET=utf8;
#
# CREATE TABLE IF NOT EXISTS `student`(
# 	`id` INT(4) NOT NULL AUTO_INCREMENT COMMENT '学号',
# 	`name` VARCHAR(30) NOT NULL DEFAULT '匿名' COMMENT '姓名',
# 	`pwd` VARCHAR(20) NOT NULL DEFAULT '123456' COMMENT '密码',
# 	`sex` VARCHAR(2)	NOT NULL DEFAULT '女' COMMENT '性别',
# 	`birthday` DATETIME DEFAULT NULL COMMENT '出生日期',
# 	`address` VARCHAR(100) DEFAULT NULL COMMENT '家庭住址',
# 	`email` VARCHAR(50) DEFAULT NULL COMMENT '邮箱',
# 	`gradeid` INT(10) NOT NULL COMMENT '学生的年级',
# 	PRIMARY KEY (`id`),
# 	KEY `FK1_gradeid` (`gradeid`),
# 	CONSTRAINT `FK1_gradeid` FOREIGN KEY (`gradeid`) REFERENCES `grade`(`gradeid`)
# )ENGINE=INNODB DEFAULT CHARSET=utf8;

# insert into grade (gradeid,gradename) value (1,'一年');
# insert into grade (gradeid,gradename) value (2,'四年'),(3,'二年'),(4,'三年');

update grade set gradename = 'bai' where gradeid = 1;

select
    Sname,
    s1.*
from
    Student s2,
    (select
        s.SId,
        avg(s.score) avg1
    from
        SC s
    group by
        s.SId
    having avg1>=60) s1
where
    s2.SId = s1.SId


select st.*
from (select s.SId, max(if(s.CId = '01', s.CId, null)) 01c, max(if(s.CId = '02', s.CId, null)) 02c
      from SC s
      group by s.SId) t , Student st
where t.SId = st.SId
and t.01c is not null
and t.02c is not null

select s.*, t.CId c1
      from Student s,
           (select * from SC s where s.SId = '01') t