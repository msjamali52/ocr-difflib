predefined_list=['gross pay']
predefined_dict={'a':'o','o':'a','g':'c','c':'g'}

for key, value in predefined_dict.items():
        for  word in predefined_list:
            for n in range(word.count(key)):
                final = word.replace(key,value,n+1)
                if final not in predefined_list:
                    predefined_list.append(final)
print(predefined_list)