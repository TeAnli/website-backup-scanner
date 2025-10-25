import requests
import argparse

from rich.console import Console

# setting common backup filename and suffix
DEFAULT_NAME = ['web', 'website', 'backup', 'back', 'www', 'wwwroot', 'temp']
DEFAULT_SUFFIX = ['tar', 'tar.gz', 'zip', 'rar', '7-zip', '7z']

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
    return parser


def main():
    parser = initialize_argument_parser()
    console = Console()

    # get the arguments
    arguments = parser.parse_args()
    url = arguments.url
    with console.status("[bold green]WEBSITE-BACKUP-SCANNER scanning...") as status:
        # foreach the filename is composed of a prefix and a suffix
        for name in DEFAULT_NAME:
            for suffix in DEFAULT_SUFFIX:
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


