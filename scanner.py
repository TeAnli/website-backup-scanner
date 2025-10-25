import requests
import argparse
import yaml

from rich.console import Console

def get_file_size(url):
    response = requests.head(url)
    if 'Content-Length' in response.headers:
        file_size = int(response.headers['Content-Length'])
        return file_size
    else:
        return None

def initialize_argument_parser():
    parser = argparse.ArgumentParser(description='website-backup-scanner')
    parser.add_argument('url', help='the target website url path')
    parser.add_argument('-d', '--delay', help='this argument recive a milliseconds to delay your custom time')
    return parser

def get_configuration():
    # 获取当前目录下的config.yaml文件
    config_path = 'config.yaml'
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

def main():
    console = Console()
    # get the arguments
    parser = initialize_argument_parser()
    arguments = parser.parse_args()
    url = arguments.url
    delay = arguments.delay
    # get the configuration
    config = get_configuration()
    default_name = config.get('default_name', [])
    default_suffix = config.get('default_suffix', [])

    with console.status("[bold green]`WEBSITE-BACKUP-SCANNER scanning...") as status:
        # foreach the filename is composed of a prefix and a suffix
        for name in default_name:
            for suffix in default_suffix:
                # splice suffix and name to a filename
                backup_filename = f'{name}.{suffix}'
                final_url = f'{url}/{backup_filename}'
                response = requests.get(final_url)
                # output the information of the request result
                match response.status_code:
                    case 200:
                        console.log(f'[bold green][{response.status_code}] -  {get_file_size(url)}B -  /{backup_filename}[/bold green]')
                    case 403:
                        console.log(f'[bold blue][{response.status_code}] -  {get_file_size(url)}B -  /{backup_filename}[/bold blue]')
                    case _:
                        console.log(f'[bold red][{response.status_code}][/bold red] -  {get_file_size(url)}B -  /{backup_filename}')

if __name__ == "__main__":
    main()


