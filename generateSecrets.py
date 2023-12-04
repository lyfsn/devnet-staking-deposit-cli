import json
import os
from glob import glob

SECRET_CONSTANT = "12345678"

def read_json_files(directory):
    file_paths = glob(os.path.join(directory, 'deposit_data-*.json'))
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            yield json.load(file)

def create_secrets_directory(directory):
    secrets_dir = os.path.join(directory, 'secrets')
    if not os.path.exists(secrets_dir):
        os.makedirs(secrets_dir)
    return secrets_dir

def create_secret_files(pubkeys, secrets_dir):
    for pubkey in pubkeys:
        file_path = os.path.join(secrets_dir, f'0x{pubkey}')
        with open(file_path, 'w') as file:
            file.write(SECRET_CONSTANT)

def main():
    directory = './validator_keys'
    secrets_dir = create_secrets_directory(directory)

    pubkeys = []
    for data in read_json_files(directory):
        pubkeys.extend([item['pubkey'] for item in data])

    create_secret_files(pubkeys, secrets_dir)

if __name__ == "__main__":
    main()
