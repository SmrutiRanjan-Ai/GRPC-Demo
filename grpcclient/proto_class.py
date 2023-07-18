import os

import grpc

import comm_pb2 as pb2
import comm_pb2_grpc as pb2_grpc

class Client():
    def __init__(self):
        self.host=os.getenv("GRPC_HOST", "localhost")
        self.port=50051
        self.channel=grpc.insecure_channel('{}:{}'.format(self.host,self.port))
        self.stub=pb2_grpc.CommStub(self.channel)

    def get_response(self,message):
        message=pb2.Request(name=message)
        print(f"Message is {message}")
        return self.stub.GetSerialNumber(message)