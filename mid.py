with open('成绩.txt',encoding = 'utf-8') as file1:
        list1 = file1.readlines()
list2 = []
#计算总分和平均分插入最后两列
for a in list1[1:]:
    a = a.split()
    a[1:] = [int(i) for i in a[1:]]
    score_sum = sum(a[1:])
    score_ave = int(score_sum/len(a[1:]))
    a.append(score_sum)
    a.append(score_ave)
    list2.append(a)
b = list1[0].split()
b.insert(0,'名次')
b.append('总分')
b.append('平均分')
list2.insert(0,b)
list2[1:] = sorted(list2[1:],key = lambda x:x[-1],reverse = True)#按平均分排序
#插入名次
for j in range(1,len(list2[1:])+1):
    list2[j].insert(0,j)
#计算所有项目平均分，并替换60分为不及格
c = []
for L in range(2,len(list2[1])):
    sum1 = 0
    for m in list2[1:]:
        sum1 += int(m[L])
        if int(m[L]) < 60:
            m[L] = '不及格'
    ave1 = int(sum1/len(list2[1:]))
    c.append(ave1)
c.insert(0,0)
c.insert(1,'平均')
list2.insert(1,c)
#将元素转为字符
for e in range(len(list2)):
    for f in range(len(list2[1])):
        list2[e][f] = str(list2[e][f])
list3 = ''
for g in list2:
    list3 += ' '.join(g)
    list3 += '\n'
#写入文件
with open('结果.xls','w',encoding = 'utf-8') as jg:
    jg.writelines(list3)
