from concurrent import futures
import logging
import grpc
import key_value_pb2
import key_value_pb2_grpc

KEYS = {}

class KeyValue(key_value_pb2_grpc.KeyValueServicer):

    def Put(self, request, context):
        if request.key and request.value:
            if not request.key in KEYS:
                KEYS[request.key] = request.value
                print(KEYS)
                return key_value_pb2.Response(message='Chave adicionada.')
            else:
                return key_value_pb2.Response(message=f"Não foi encontrada a chave: {request.key}.")
        return key_value_pb2.Response(message=f"Chave e/ou valor vazio(s).")     

    def Get(self, request, context):
        if request.key in KEYS:
            return key_value_pb2.Response(message=(KEYS[request.key]))
        else:
            return key_value_pb2.Response(message=f"Não foi encontrada a chave: {request.key}.")

    def GetAll(self, request, context):
        return key_value_pb2.ResponseAll(message=list(KEYS.keys()))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    key_value_pb2_grpc.add_KeyValueServicer_to_server(KeyValue(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()