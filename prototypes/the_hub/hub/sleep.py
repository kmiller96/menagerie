import subprocess

import click


@click.command()
@click.option("--no-clear", is_flag=True, help="Doesn't wipe the screen after awaking.")
def sleep(no_clear):
    """Runs the screensaver animation."""
    subprocess.check_call("cmatrix -as -C cyan".split())
    if no_clear:
        pass  # Don't wipe the screen - keep command history
    else:
        subprocess.check_call("clear")
    return
