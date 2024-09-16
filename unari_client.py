import grpc
import unari_pb2_grpc
import unari_pb2


class UnariClient():
    def __init__(self):
        self.host = "localhost"
        self.server_port= 50051
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host,self.server_port))
        self.stub= unari_pb2_grpc.UnariStub(self.channel)
    
    def getServerMessage(self , message):
        request_payload = unari_pb2.RequestPayload(message=message)
        return self.stub.getServerMessage(request_payload)
                

if __name__=="__main__":
    client=UnariClient()
    response = client.getServerMessage(message="Hello World! from grpc!")
    print(response.message)