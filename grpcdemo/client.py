import grpc
import comm_pb2 as pb2
import comm_pb2_grpc as pb2_grpc

class Client():
    def __init__(self):
        self.host = 'localhost'
        self.port = 50051
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host,self.port))
        self.stub = pb2_grpc.CommStub(self.channel)

    def get_response(self,message):
        message=pb2.Request(name=message)
        print(f'{message}')
        return self.stub.GetSerialNumber(message)

if __name__=="__main__":
    client=Client()
    name="ADB012.C"
    response=client.get_response(message=name)
    if response.status is False:
        print("serial number doesn't exist")
    else:
        print(f"Serial Number for {name} is {response.serial}")
    print(response)
