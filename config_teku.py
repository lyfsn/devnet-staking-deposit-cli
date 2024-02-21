import json
import os
import glob
import sys

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def create_secrets_directory(base_dir):
    secrets_dir = os.path.join(base_dir, 'validator_keys_secrets')
    if not os.path.exists(secrets_dir):
        os.makedirs(secrets_dir)
    return secrets_dir

def create_secret_file(file_path, secrets_dir, secret_password):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    secret_file_path = os.path.join(secrets_dir, f'{base_name}.txt')
    with open(secret_file_path, 'w') as file:
        file.write(secret_password)

def process_directory(base_dir, secret_password):
    keys_dir = os.path.join(base_dir, 'validator_keys')
    search_pattern = os.path.join(keys_dir, 'keystore-*.json')
    file_paths = glob.glob(search_pattern)

    secrets_dir = create_secrets_directory(base_dir)
    
    for file_path in file_paths:
        create_secret_file(file_path, secrets_dir, secret_password)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <SECRET_CONSTANT>")
        sys.exit(1)

    SECRET_CONSTANT = sys.argv[1]
    directories = [
        'validator_config/geth-teku',
        'validator_config/nethermind-teku',
        'validator_config/besu-teku',
    ]

    for directory in directories:
        process_directory(directory, SECRET_CONSTANT)

    print("Secret files have been created.")
