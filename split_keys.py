import os
import shutil

directories_to_delete = ['validator_keys_all', 'validator_config']

for directory in directories_to_delete:
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Deleted: {directory}")
    else:
        print(f"Directory does not exist: {directory}")

# Step 1: Split and copy files to validator_keys_all
source_dir = 'validator_keys/validator_keys'
target_root_dir = 'validator_keys_all'
os.makedirs(target_root_dir, exist_ok=True)

index_ranges = [(i * 3000, (i + 1) * 3000 - 1) for i in range(11)]
for start_index, end_index in index_ranges:
    target_dir = os.path.join(target_root_dir, f'validator_keys_{start_index // 3000 + 1}')
    os.makedirs(target_dir, exist_ok=True)
    
    for filename in os.listdir(source_dir):
        parts = filename.split('_')
        if len(parts) >= 5:
            try:
                index = int(parts[3])
                print('Processing: ', index)
                if start_index <= index <= end_index:
                    source_file = os.path.join(source_dir, filename)
                    target_file = os.path.join(target_dir, filename)
                    shutil.copy2(source_file, target_file)
            except ValueError:
                continue

# Step 2: Create target directories with subdirectories
target_directories = [
    'validator_config/geth-lighthouse',
    'validator_config/geth-prysm',
    'validator_config/geth-teku',
    'validator_config/nethermind-lighthouse-1',
    'validator_config/nethermind-lighthouse-2',
    'validator_config/nethermind-prysm',
    'validator_config/nethermind-teku',
    'validator_config/besu-lighthouse-1',
    'validator_config/besu-lighthouse-2',
    'validator_config/besu-prysm',
    'validator_config/besu-teku',
]

for target in target_directories:
    os.makedirs(os.path.join(target, 'validator_keys'), exist_ok=True)
    os.makedirs(os.path.join(target, 'validator_keys_secrets'), exist_ok=True)

# Step 3: Copy files from validator_keys_all to corresponding validator_config directory
source_base = 'validator_keys_all/validator_keys_'
for i, target_dir_base in enumerate(target_directories, start=1):
    source_dir = f'{source_base}{i}'
    target_dir = os.path.join(target_dir_base, 'validator_keys')
    
    if os.path.exists(source_dir):
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)
            shutil.copy2(source_file, target_file)
    else:
        print(f"Source directory {source_dir} does not exist.")

print("Copy completed!")
