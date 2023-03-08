import click

@click.command()
def test():
    """Example Sub-command"""
    click.echo('Hello World!')



# from cadet.cli.entry import cadet

# @click.command()
# def test():
#     """Example Sub-command"""
#     click.echo('Hello World!')
    
# cadet.add_command(test)