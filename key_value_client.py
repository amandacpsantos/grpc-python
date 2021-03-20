from __future__ import print_function
import logging

import grpc

import key_value_pb2
import key_value_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = key_value_pb2_grpc.KeyValueStub(channel)

        while True:

            print("\n0)Sair;\n1)Adicionar chave;\n2)Pegar Chave;\n3)Ver todas as chaves.")
            op = input("Opção:")
            if op == "0":
                break
            elif op == "1":
                key = input("Chave: ")
                value = input("Valor: ")
                response = stub.Put(key_value_pb2.PutRequest(key=key, value=value))
                print(response.message)
            elif op == "2":
                key = input("Digite a chave: ")
                response = stub.Get(key_value_pb2.PutRequest(key=key))
                print(response.message)
            elif op == "3":
                response = stub.GetAll(key_value_pb2.PutRequest())
                print(response.message)
               

if __name__ == '__main__':
    logging.basicConfig()
    run()