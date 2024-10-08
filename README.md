# CLI File Client

This is a simple command-line interface (CLI) application designed to retrieve and print file metadata and contents from specified backends. The application supports  REST API protocols, allowing users to interact with file services easily.
## Features

- Retrieve file metadata, including:
  - Creation date and time
  - File size in bytes
  - MIME type
  - Display name of the file
- Read file contents directly from the backend.
- Support for  **REST API**.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate
   pip install -r requirements.txt

## Usage
Run the application with the following commands:

1. To get file metadata:
    ```bash
    python file_client.py --backend <backend_type> stat <UUID>

2. To read the file content:
    ```bash
    python file_client.py --backend <backend_type> read <UUID>

## Options
    --backend: Specify the backend to be used (grpc or rest). Default is grpc.
    --grpc-server: Set the host and port for the gRPC server. Default is localhost:50051.
    --base-url: Set the base URL for the REST server. Default is http://localhost/.
    --output: Set the file where to store the output. Default is - (stdout).

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.

Feel free to customize this template to fit your project's specific needs and add any additional sections that might be relevant, such as examples of responses from the API, troubleshooting tips.