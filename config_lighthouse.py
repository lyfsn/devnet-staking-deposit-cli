import json
import os
import sys

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def ensure_0x_prefix(pubkey):
    return pubkey if pubkey.startswith('0x') else f'0x{pubkey}'

def create_secret_file(pubkey, secret, secrets_dir):
    secret_file_name = ensure_0x_prefix(pubkey)
    file_path = os.path.join(secrets_dir, secret_file_name)
    with open(file_path, 'w') as file:
        file.write(secret)

def process_directory(directory, secret):
    keys_dir = os.path.join(directory, 'validator_keys')
    secrets_dir = os.path.join(directory, 'validator_keys_secrets')
    
    if not os.path.exists(secrets_dir):
        os.makedirs(secrets_dir)
    
    for filename in os.listdir(keys_dir):
        if filename.startswith('keystore-m_') and filename.endswith('.json'):
            file_path = os.path.join(keys_dir, filename)
            data = read_json_file(file_path)
            pubkey = data.get('pubkey')
            if pubkey:
                create_secret_file(pubkey, secret, secrets_dir)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <SECRET_CONSTANT>")
        sys.exit(1)

    SECRET_CONSTANT = sys.argv[1]
    directories = [
        'validator_keys_config/geth-lighthouse',
        'validator_keys_config/nethermind-lighthouse-1',
        'validator_keys_config/nethermind-lighthouse-2',
        'validator_keys_config/besu-lighthouse-1',
        'validator_keys_config/besu-lighthouse-2',
    ]

    for directory in directories:
        process_directory(directory, SECRET_CONSTANT)

    print("Secret files have been created.")
