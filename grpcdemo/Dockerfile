FROM python

RUN mkdir /service
COPY grpcdemo/ /service/grpcdemo/
WORKDIR /service/grpcdemo
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc --proto_path=. ./comm.proto --python_out=. --grpc_python_out=.

EXPOSE 50051
ENTRYPOINT [ "python", "server.py"]