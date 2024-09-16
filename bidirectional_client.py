import grpc
import bidirectional_pb2_grpc
import bidirectional_pb2


class BidrectionalClient():
    def __init__(self):
        self.host = "localhost"
        self.server_port= 50051
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host,self.server_port))
        self.stub= bidirectional_pb2_grpc.BidirectionalStub(self.channel)
    
    def getServerMessage(self ):
        return self.stub.getServerMessage(self.generate_message())
                
    def generate_message(self):
        for i in range(5):
            yield bidirectional_pb2.RequestPayload(message=f"message no {i}")
if __name__=="__main__":
    client=BidrectionalClient()
    responses = client.getServerMessage()
    for re in responses:
        print(re.message)