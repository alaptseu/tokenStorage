import click
from ts.cli import pass_context

from ts.core.dbhandler import DBHandler
from ts.core.printutils import print_list_data


@click.command('all', short_help='Prints all data from the table passed as parameter')
@click.option('--table', '-t', prompt=True)
@pass_context
def cli(ctx, table):
    db_handler = DBHandler()
    all = db_handler.get_all_auth_endpooints()
    if len(all) == 0:
        ctx.log('No data in table %s', table)
    else:
        print_list_data(all, 'client_id')
