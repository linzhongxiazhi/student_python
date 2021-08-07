# passwordfile =open("password.txt","a")
# sequence ="平台："+"腾讯"+","+\
#           "账号："+"123456"+","+\
#           "密码："+"123456"+"\n"
#
# passwordfile.write(sequence)
# passwordfile.close()
# aa =[]
# def search_password():
#
#     for i in aa:
#         for j in i:
#             if "腾讯" in j:
#                 print(j)
#     else:
#         print("没有查询到!")
#
# with open("password.txt", "r") as f:
#     for line in f.readlines():
#         data = line.split('\n\t')
#         for str in data:
#             sub_str = str.split(' ')
#         if sub_str:
#             aa.append(sub_str)
# search_password()