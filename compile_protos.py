import os
import grpc_tools

cmd1 = "python -m grpc_tools.protoc --python_out=. --proto_path=./protos {}"
cmd2 = "python -m grpc_tools.protoc --grpc_python_out=. --proto_path=./protos {}"

for subdir, dirs, files in os.walk(r''.join(['.', os.sep, 'protos', os.sep])):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith('.proto'):
            print(filepath)
            # grpc_tools.command
            print(cmd1.format(filepath))
            os.system(cmd1.format(filepath))
            os.system(cmd2.format(filepath))