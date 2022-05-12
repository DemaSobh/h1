import json
name = input("Enter your name: ")
correct = 0
all = 0
with open('data.json') as json_file:
    data = json.load(json_file)
    for d in data:
        print(d)
        ans = input()
        if ans == data[d]:
            correct += 1
        all += 1

resultFile = open("result.txt", "w")
resultFile.write("your name is: "+name+"\n")
resultFile.write("and your result is: " + str(correct)+"/" + str(all))
