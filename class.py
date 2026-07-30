class data:
    def __init__(self,tone,language,token_length,tempK,tempN):
        self.tone=tone
        self.language=language
        self.token_length=token_length
        self.tempK=tempK
        self.tempN=tempN




class request(data):
    def __init__(self,request_id,tone,language,token_length,tempK,tempN):
        super().__init__(tone,language,token_length,tempK,tempN)
        self.request_id=request_id
    

r1=request(1122,"fun and humorous","english","short",0.2,0.2)

print(r1.token_length)
print(r1.request_id)



class response(data):
    def __init__(self,response_id,tone,language,token_length,tempK,tempN):
        super().__init__(tone,language,token_length,tempK,tempN)
        self.response_id=response_id






