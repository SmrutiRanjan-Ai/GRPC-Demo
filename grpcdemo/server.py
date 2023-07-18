import grpc
from concurrent import futures
import comm_pb2 as pb2
import comm_pb2_grpc as pb2_grpc




class CommServer(pb2_grpc.CommServicer):
    def __init__(self,*args,**kwargs):
        pass


    def GetSerialNumber(self, request, context):

        print(f'message received is {request.name}')
        serialnum= "SKE-500.0333-00"
        message = {'serial': serialnum, 'status': True}

        return pb2.Response(**message)

if __name__=='__main__':
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CommServicer_to_server(CommServer(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()











