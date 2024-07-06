import json

data = {"key1" : "value1", "key2" : "value2"}

jsonData = json.dumps(data)
print(jsonData)

# data = {"key1" : "value1", "key2" : "value2"}

sampleJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
prettyPrintedJson  = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(prettyPrintedJson)

# {
#   "key1" = "value2",
#   "key2" = "value2",
#   "key3" = "value3"
# }