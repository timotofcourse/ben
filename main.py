#!/usr/bin/env python

import requests
import os
import argparse
from rich.console import Console
from rich.progress import track

console = Console()

# Arguments for ben

parser = argparse.ArgumentParser(prog="Ben", description="Command line tool to download files. Made to be used in Timot's software", epilog="For more detailed help look at github. :)")
parser.add_argument('-l', '--link', help='Download links', required=True)
parser.add_argument('-o', '--output', help='Download Output', required=True)

# Download function

def download_file(url, output_path):

    try:
        console.print(f'[bold blue]Downloading file from:[/bold blue] {url}')
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            
            total_size = int(response.headers.get('content-length', 0))

            if total_size == 0:
                console.print(f'[bold yellow]Warning: Content length not available, download progress may not be accurate.[/bold yellow]')


            total_size = int(response.headers.get('content-length', 0))

            with open(output_path, 'wb') as file:
                
                for chunk in track(
                    response.iter_content(chunk_size=1024),
                    description=f'[green]Saving to {output_path}[/green]',
                    total=total_size // 1024 if total_size != 0 else None,
                ):
                    file.write(chunk)

            console.print(f'[bold green]Download completed sucessfully![/bold green] File saved to {output_path}')

        else:

            console.print(f'[bold red]Failed to download file! Status code: {response.status_code}[/bold red]')

    except Exception as e:

        console.print(f'[bold red]An error occured: {e}[/bold red]')


# Check if the output exists

def output_checker(output_path):

    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        make_dir(output_dir)

# make the output dir

def make_dir(output_path):

    os.makedirs(output_path)


# Main function to handle the arguments and call the download function 


def main_function():

    args = parser.parse_args()
    url = args.link
    output_path = args.output

    output_checker(output_path)

    download_file(url, output_path)



if __name__ == '__main__':

    main_function()