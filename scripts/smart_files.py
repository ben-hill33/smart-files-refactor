import click
from automation import main


@click.group()
def smart_files():
    pass


@smart_files.command()
def run():
    """Run the Smart-files program on an ad hoc basis"""
    print("\nRunning Smart-files...\n\n")
    print("\nMoving Files Now... \n")
    main()
    print("\n\nSmart-files run complete!\n\n")