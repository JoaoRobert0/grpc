const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

// Carregar o arquivo .proto
const packageDefinition = protoLoader.loadSync('../proto/greeter_service.proto');
const greeterProto = grpc.loadPackageDefinition(packageDefinition).Greeter;

// Conectar ao servidor gRPC (Python)
const client = new greeterProto('localhost:50051', grpc.credentials.createInsecure());

// Enviar uma solicitação de saudação
const request = { name: 'Fabiiii' };

client.SayHello(request, (error, response) => {
  if (!error) {
    console.log('Mensagem recebida do servidor:', response.message);
  } else {
    console.error('Erro:', error);
  }
});
