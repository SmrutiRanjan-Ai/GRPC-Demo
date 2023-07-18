FROM python

RUN mkdir /service
COPY grpcclient/ /service/grpcclient/
WORKDIR /service/grpcclient
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc --proto_path=. ./comm.proto --python_out=. --grpc_python_out=.

EXPOSE 5000
ENTRYPOINT [ "python", "main.py" ]