import json
import sys

class auditEntry:
    """Parsing Audit Logs can be Fun and Easy"""
    def __init__(self, line):
        self.line = line
        self.jo = json.loads(self.line)
        self.kind = self.jo["kind"]
        self.apiVersion = self.jo["apiVersion"]
        self.level = self.jo["level"]
        self.auditID = self.jo["auditID"]
        self.stage = self.jo["stage"]
        self.requestURI = self.jo["requestURI"]
        self.verb = self.jo["verb"]
        self.user = self.jo["user"]
        self.username = self.user["username"]
        self.groups = self.user["groups"]
        self.sourceIPs = self.jo["sourceIPs"]
        self.userAgent = self.jo["userAgent"]
        self.objectRef = self.jo["objectRef"]
        self.resource = self.objectRef["resource"]
        #self.namespace = self.objectRef["namespace"]
        #self.name = self.objectRef["name"]
        #self.apiGroup = self.objectRef["apiGroup"]
        #self.apiVersion = self.objectRef["apiVersion"]
        self.responseStatus = self.jo["responseStatus"]
        self.metadata = self.responseStatus["metadata"]
        self.code = self.responseStatus["code"]
        self.requestReceivedTimestamp = self.jo["requestReceivedTimestamp"]
        self.stageTimestamp = self.jo["stageTimestamp"]
        self.annotations = self.jo["annotations"]
    
    def getAll(self):
        print("*" * 10)
        print("Kind:  " + self.kind)
        print("apiVersion:  " + self.apiVersion)
        print("level:  " + self.level)
        print("auditID:  " + self.auditID)
        print("stage:  " + self.stage)
        print("requestURI:  " + self.requestURI)
        print("verb: " + self.verb)
        print("User:")
        print("   " + self.username)
        print("Groups:")
        for i in self.groups:
            print("   " + i)
        print("Source IPs:")
        for i in self.sourceIPs:
            print("   " + i)
        print("UserAgent:  " + self.userAgent)
        print("ObjectRef:")
        print("   " + "Resource:  " + self.resource)
        #print("   " + "Namespace:  " + self.namespace)
        #print("   " + "Name:  " + self.name)
        #print("   " + "apiGroup:  " + self.apiGroup)
        #print("   " + "apiVersion" + self.apiVersion)
        print("responseStatus: ")
        print("   " + str(self.metadata))
        print("   " + str(self.code))
        print("RequestReceived:  " + self.requestReceivedTimestamp)
        print("Stage:  " + self.stageTimestamp)
        print("Annotations")
        print(self.annotations)
        print(("*" * 10) + "\n\n\n")




arg = sys.argv[1]

with open(arg) as f:
    for line in f:
        try:       
            s = auditEntry(line)
            s.getAll()
        except:
            pass
