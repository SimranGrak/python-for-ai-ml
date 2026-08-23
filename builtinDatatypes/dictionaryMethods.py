#dictionary methods

info={
  "name":"simran",
  "cgpa":9.2,
  "subjects":["hindi", "english","maths"],
  3.14:"PI"
}


'''access all keys'''
# dict_keys=list(info.keys())
# print(dict_keys)
# print(type(dict_keys))


'''access all value'''
# print(info.values())


'''access key value pairs'''
# print(info.items())


'''access value according to key'''
# print(info.get("name"))

# print("end of code") 



'''add new item to dictionary'''
info.update({
  "city":"karnal"
})

print(info)