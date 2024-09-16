import grpc
import unari_pb2_grpc
import unari_pb2
from concurrent import futures

class UnariService(unari_pb2_grpc.UnariServicer):


    def __init__(self):
        pass

    def getServerMessage(self,request,context):
        print(f"Request Param: {request.message}")
        return unari_pb2.ResponsePayload(message="Received the message!")


if __name__ == "__main__" :
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    unari_pb2_grpc.add_UnariServicer_to_server(UnariService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    