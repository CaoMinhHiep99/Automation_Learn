str_exp = 'newspapers'

list_exp =  list(str_exp)
dup_list = []
for i in list_exp:
    if list_exp.count(i) > 1 and i not in dup_list:
        dup_list.append(i)
dup_list = ' '.join(dup_list)
print(dup_list)
