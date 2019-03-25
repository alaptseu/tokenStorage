import click
from ts.cli import pass_context
from urllib import parse
from ts.core import DataError
from ts.core.dbhandler import DBHandler


@click.command('add', short_help='Add auth token url request.')
@click.option('--url', '-u', prompt=True)
@pass_context
def cli(ctx, url):
    data = parse.parse_qs(parse.urlparse(url).query)
    data.update({'url': url})
    db_handler = DBHandler()
    try:
        db_handler.add_token_data(data, 'client_id', 'username')
        ctx.log('Added new endpoint %s', url)
    except DataError as error:
        ctx.log(error)

