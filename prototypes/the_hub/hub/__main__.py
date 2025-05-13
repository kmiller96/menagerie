import click

from hub import utils
from hub.sleep import sleep
from hub.goals import goals
from hub.tasks import tasks
from hub.projects import projects
from hub.quotes import inspire 


@click.group()
def main():
    pass


main.add_command(sleep, name="sleep")
main.add_command(goals)
main.add_command(tasks)
main.add_command(projects)
main.add_command(inspire)
