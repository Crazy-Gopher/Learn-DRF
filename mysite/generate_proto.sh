#!/bin/bash
echo "generating proto"
python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. user.proto