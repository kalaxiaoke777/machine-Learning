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
r.close();
