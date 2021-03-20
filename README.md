# kv-grpc-python
Trabalho desenvolvido para a disciplina LABORATÓRIO DE DESENVOLVIMENTO DE APLICAÇÕES MÓVEIS E DISTRIBUÍDAS - Engenharia de Software - PUC Minas


### Pré-requisitos
- Python 3.5 or higher
- pip version 9.0.1 or higher

### Dependências   
- <code>python -m pip install grpcio</code>
- <code>python -m pip install grpcio-tools</code>

No prompt de comando, na pasta do projeto:
- Execute <code>python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. key_value.proto</code>
- Execute <code>python key_value_server.py</code>

Em 1 ou mais diferentes prompts de comando:
- Execute <code>python key_value_client.py</code>

Siga as instruções do menu.

Documentação referência: https://grpc.io/docs/languages/python/basics/
