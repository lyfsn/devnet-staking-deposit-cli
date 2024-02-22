import os
import subprocess
import sys
import shutil

def create_password_file(secret_constant, file_path):
    """Create or overwrite password.txt file with the SECRET_CONSTANT."""
    with open(file_path, 'w') as file:
        file.write(secret_constant)

def run_docker_commands(directory, docker_image, password_file_path):
    """Run the specified Docker commands in the given directory with the specified Docker image."""
    commands = [
        f"docker run --rm -it --user=root -v {directory}/validator_keys:/validator_keys -v {password_file_path}:/password.txt {docker_image} wallet create --wallet-dir=/validator_keys --wallet-password-file=/password.txt",
        f"docker run --rm -it --user=root -v {directory}/validator_keys:/validator_keys -v {password_file_path}:/password.txt {docker_image} accounts import --wallet-dir=/validator_keys --wallet-password-file=/password.txt --keys-dir=/validator_keys"
    ]

    for command in commands:
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <SECRET_CONSTANT>")
        sys.exit(1)

    SECRET_CONSTANT = sys.argv[1]
    docker_image = "gcr.io/prysmaticlabs/prysm/validator:v4.2.1-rc.1"  # Docker image variable
    password_file_path = os.path.abspath('password.txt')  # Get the absolute path of the password file

    print("Create password.txt file in the current directory: ", password_file_path)
    create_password_file(SECRET_CONSTANT, password_file_path)  # Create password.txt file with the absolute path

    directories = [
        'validator_keys_config/geth-prysm',
        'validator_keys_config/nethermind-prysm',
        'validator_keys_config/besu-prysm',
    ]

    for directory in directories:
        full_directory_path = os.path.abspath(directory)
        run_docker_commands(full_directory_path, docker_image, password_file_path)
        shutil.copy(password_file_path, full_directory_path)

    print("Docker commands have been executed.")
