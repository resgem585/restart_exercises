import json

def readJsonFile(fileName="insulin.json"):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data

# Call the function without providing a file name, it will use the default ("insuline.json")
result = readJsonFile()

# Print or use the result as needed
print(result)