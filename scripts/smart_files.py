import click
from automation import main, cron_min


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


@smart_files.command()
# @smart_files.option(
#     "--minute", "-m", help="Will create a cron job for Smart-files to run every minute"
# )
# @smart_files.option(
#     "--hour", "-h", help="Will create a cron job for Smart-files to run every hour"
# )
# @smart_files.option(
#     "--day", "-d", help="Will create a cron job for Smart-files to run once every day"
# )
# @smart_files.option(
#     "--month", "-o", help="Will create a cron job for Smart-files to run once a month"
# )
def cron():
    """Adds a job to the time scheduler called cron"""
    cron_min()
