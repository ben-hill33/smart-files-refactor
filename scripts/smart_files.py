import click
from crontab import CronTab
from automation import main, cron_min, get_files, user, root_dir


@click.group()
@click.version_option()
def smart_files():
    pass


@smart_files.command()
def show_files():
    """Will show you files currently in downloads file"""
    files = get_files(root_dir)
    print("\nFiles not yet sorted:\n")

    for item in files:
        click.secho(item, fg="magenta")

    print("\n")


@smart_files.command()
def show_cronjob():
    """Shows active cron job"""
    print("Strech goal")


@smart_files.command()
def run():
    """Run the Smart-files program on an ad hoc basis"""
    print("\nRunning Smart-files...\n\n")
    print("\nMoving Files Now... \n")
    main()
    print("\n\nSmart-files run complete!\n\n")


@smart_files.command()
@click.option(
    "--minute",
    "-m",
    is_flag=True,
    default=True,
    help="Will create a cron job for Smart-files to run every minute",
)
@click.option(
    "--hour",
    "-h",
    is_flag=True,
    help="Will create a cron job for Smart-files to run every hour",
)
@click.option(
    "--day",
    "-d",
    is_flag=True,
    help="Will create a cron job for Smart-files to run once every day",
)
@click.option(
    "--month",
    "-o",
    is_flag=True,
    help="Will create a cron job for Smart-files to run once a month",
)
def cron(minute, hour, day, month):
    """Adds a job to the time scheduler called cron"""

    if hour:
        print("Hour picked")
    elif day:
        print("Day Picked")
    elif month:
        print("Month Picked")
    else:
        cron_min()
