#JSON module

import json
'''convert json string into python object'''
# json_str='{"name":"simran", "isTeacher":true, "city": null}'

# py_obj=json.loads(json_str)

# print(py_obj)
# print(type(py_obj)) 


'''convert python object into json string'''
# py_obj={
#   "name":"simran",
#   "company":"HCLTech",
#   "isEngineer": True
# }

# json_str=json.dumps(py_obj)

# print(type(json_str), json_str)



'''read json string from file'''
# with open("File_Input_output/data.json","r") as f:
#   py_obj=json.load(f)

# print(type(py_obj), py_obj)


'''write data into json string'''
py_obj={
  "name":"simran",
  "company":"HCLTech",
  "isEngineer": True
}

with open("File_Input_output/data.json", "w") as f:
  json.dump(py_obj, f, indent=4, sort_keys=True)