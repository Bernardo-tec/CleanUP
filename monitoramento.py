import hashlib
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Banco de dados simples de hashes conhecidos de arquivos maliciosos
known_hashes = {
    'e99a18c428cb38d5f260853678922e03': 'Exemplo de vírus 1',
    'd41d8cd98f00b204e9800998ecf8427e': 'Exemplo de vírus 2'
}

# Função para calcular o hash de um arquivo
def get_file_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Função para verificar se o arquivo é suspeito
def check_file(file_path):
    file_hash = get_file_hash(file_path)
    if file_hash in known_hashes:
        print(f"Alerta! Arquivo suspeito detectado: {known_hashes[file_hash]}")
    else:
        print(f"Arquivo seguro: {file_path}")

# Monitorando diretórios em tempo real
class Watcher:
    def __init__(self, directory):
        self.directory = directory
        self.observer = Observer()

    def run(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_created = self.on_created
        self.observer.schedule(event_handler, self.directory, recursive=False)
        self.observer.start()

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"Novo arquivo detectado: {event.src_path}")
        check_file(event.src_path)

# Executando o monitoramento
directory_to_watch = '/path/to/your/directory'
watcher = Watcher(directory_to_watch)
watcher.run()