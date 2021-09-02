class TestRes():
    def __init__(self,test_name, resault, msg):
        self.test_name = test_name
        self.result = resault
        self.msg = msg

    def writeToJson(self):
        pass