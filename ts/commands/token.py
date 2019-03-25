import requests
import click
from ts.cli import pass_context
from ts.core.dbhandler import DBHandler


@click.command('token', short_help='fetch token by account id.')
@click.option('--account', '-a', prompt=True)
@pass_context
def cli(ctx, account):
    db_handler = DBHandler()
    result =  db_handler.search_token_endpoint('client_id', account.split())
    if len(result) == 0:
        ctx.log('No data found for %s', account)
    else:
        url = result[0]['url'].strip('\'"')
        ctx.log('Url is %s', url)
        token = get_token(url)
        ctx.log(token)

def get_token(url):
    response = requests.post(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Couldn't get auth token {}".format(response.status_code))
    return response.json()