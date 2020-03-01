import json
#read file

StateCount = {}
CanadaStates = []

StateKeyData = {}
with open('/Users/yiqunliu/Desktop/IE7275Project1/business.json', 'r') as f:
    for line in f:
        # if json.loads(line)["state"] == 'AL' and any(c.isalpha() for c in json.loads(line)["postal_code"]):
        #     print(json.loads(line)["postal_code"])
        # else: continue
        dataState = json.loads(line)["state"]

        if any(c.isalpha() for c in json.loads(line)["postal_code"]) and json.loads(line)["state"] not in CanadaStates: 
            CanadaStates.append(json.loads(line)["state"])
            continue
        elif (json.loads(line)["state"] in CanadaStates):
            continue
        
        if dataState in StateCount:
            StateCount[dataState] += 1
        else:
            StateCount[dataState] = 1
        
        businessId = json.loads(line)["business_id"]
        if (dataState in StateKeyData.keys()):
            StateKeyData[dataState][businessId] = json.loads(line)
        else:
            StateKeyData[dataState] = {}
            StateKeyData[dataState][businessId] = json.loads(line)
    f.flush()

#print(CanadaStates)
#print(StateCount)
#print(StateKeyData)
# StateCount
topCount = [""]*5
def getTopCount(topCountStore, dic, ind):
    if (ind >= 5):
        return topCountStore
    data = dic.values()
    currentMax = max(data)
    for key in dic.keys():
        if dic[key] == currentMax:
            topCountStore[ind] = key
            del dic[key]
            break
    
    topCountStore = getTopCount(topCountStore, dic, ind+1)
    return topCountStore


topCount = getTopCount(topCount, StateCount, 0)
print (topCount)
print (StateCount)

for key in StateCount.keys():
    del StateKeyData[key]

businessIdBusinessData = {}

for state in topCount:
    stateData = StateKeyData[state]
    for key in stateData.keys():
        businessIdBusinessData[key] = stateData[key]

trimmedData = businessIdBusinessData.values()

with open('/Users/yiqunliu/Desktop/IE7275Project1/business.json', 'r') as f:
    with open('trimmedData2.json', 'w') as outfile:
        for line in f:
            state = json.loads(line)["state"]
            if state in topCount:
                outfile.write(line)
# with open('trimmedData.json', 'w') as outfile:
#     json.dump(trimmedData, outfile)

'''
print(StateKeyData.keys())

trimmedReviewData = []
with open('/Users/yiqunliu/Desktop/IE7275Project1/reviewcopy.json', 'r') as f:
    with open('trimmedReviewData.json', 'w') as outfile:
        for line in f:
            businessId = json.loads(line)["business_id"]
            if businessId in businessIdBusinessData:
                outfile.write(line)
            
            # merge = {}
            # merge.update(json.loads(line))
            # merge.update(businessIdBusinessData[businessId])
            # trimmedReviewData.append(json.loads(line))
        # businessIdReviewData[businessId] = json.loads(line)
# print(businessIdReviewData.keys())

# with open('trimmedReviewData.json', 'w') as outfile:
#     json.dump(trimmedReviewData, outfile)

'''
