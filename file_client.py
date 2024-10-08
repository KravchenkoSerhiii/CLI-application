import click
import requests


@click.command()
@click.option('--backend', default='rest', help='Set a backend to be used, choices are grpc and rest.')
@click.option('--base-url', default='http://localhost/', help='Set a base URL for a REST server.')
@click.option('--output', default='-', help='Set the file where to store the output. Default is -, i.e. the stdout.')
@click.argument('command')
@click.argument('uuid')
def file_client(backend, base_url, output, command, uuid):
    if backend == 'rest':
        url = f"{base_url}file/{uuid}/{command}/"
        if command == 'stat':
            response = requests.get(url)
            if response.status_code == 200:
                print(response.json())
            else:
                print("File not found.")
        elif command == 'read':
            response = requests.get(url)
            if response.status_code == 200:
                with open(output, 'wb') as f:
                    f.write(response.content)
                print(f"File saved as {output}")
            else:
                print("File not found.")
    else:
        print("gRPC support not implemented.")


if __name__ == '__main__':
    file_client()
