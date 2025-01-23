import grpc
from concurrent import futures
import greeter_service_pb2
import greeter_service_pb2_grpc

# Implementando a classe que contém a lógica do serviço
class Greeter(greeter_service_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        # Processa a requisição recebida e retorna a resposta
        message = f"Hello, {request.name}!"
        return greeter_service_pb2.HelloReply(message=message)

# Função para rodar o servidor
def serve():
    # Cria o servidor
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Registra o serviço Greeter no servidor
    greeter_service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    
    # Define a porta onde o servidor irá escutar (por exemplo, 50051)
    server.add_insecure_port('[::]:50051')
    
    # Inicia o servidor
    print("Servidor gRPC rodando na porta 50051...")
    server.start()
    
    # Aguarda indefinidamente (mantém o servidor rodando)
    server.wait_for_termination()

# Rodar o servidor
if __name__ == '__main__':
    serve()
