import grpc
import bidirectional_pb2
import bidirectional_pb2_grpc
from concurrent import futures

class BidirectionalService(bidirectional_pb2_grpc.BidirectionalServicer):


    def __init__(self):
        pass

    def getServerMessage(self, request_iterator, context):
        for request in request_iterator:
            print(f"Request Param: {request.message}")
            yield bidirectional_pb2.ResponsePayload(message="Received the message!")


if __name__ == "__main__" :
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    bidirectional_pb2_grpc.add_BidirectionalServicer_to_server(BidirectionalService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    