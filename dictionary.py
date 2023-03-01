testdict = {
    "a" : [1,2,3],
    "b" : True,
    "c" : "cee"
    }

##print(testdict ["a"][2]) ##prints value of key a at index 2.

list = [{
        "a" : [1,2,3],
        "b" : [3,4,5],
        "c" : [6,7,8]
        },

        {
         "a" : True,
         "b" : True,
         "c" : False
         }]

print(list[0]["a"][1], end = " is ")
print(list[1]["a"], end = '\n')

print(testdict.get("a"))

