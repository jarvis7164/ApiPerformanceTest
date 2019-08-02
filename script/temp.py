# header = {'userinfo': {'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}, 'content-type': 'application/octet-stream'}
#
# def dictvalue2str(dictionary):
# 	di = {}
# 	for key,value in dictionary.items():
# 		if isinstance(value,dict):
# 			value = str(value)
# 		di[key]=value
# 	return di
#
# print(dictvalue2str(header))


# l = ['a', 'b', 'c','c','c']
#
# def rename_duplicates( old ):
#     seen = {}
#     for x in old:
#         if x in seen:
#             seen[x] += 1
#             yield "%s_%d" % (x, seen[x])
#         else:
#             seen[x] = 0
#             yield x
#     # return seen
# # print(rename_duplicates(l))
# print(list(rename_duplicates(l)))

from script.pytest_run_bak import main

main(20)
