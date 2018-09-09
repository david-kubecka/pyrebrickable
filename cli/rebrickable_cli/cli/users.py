from getpass import getpass

import click

from rebrickable_api import UsersApi, Badge
from rebrickable_api.rest import ApiException
from rebrickable_cli.cli.common import object_print, add_typed_subcommands, \
    get_or_push_context_obj, pass_state
from rebrickable_cli.utils import get_data, write_data, DATA_PATH


@click.group(help='login a certain user or get global badges information')
@pass_state
def users(ctx):
    ctx.api = UsersApi(ctx.client)


@users.command(name='badges')
@pass_state
@object_print
def users_badges_list(ctx):
    return ctx.api.users_badges_list()


@add_typed_subcommands(Badge)
@users.group('badge')
@pass_state
@get_or_push_context_obj(click.argument('id', type=int))
def users_badge(ctx, id):
    return ctx.api.users_badges_read(id=id)


def create_auth(ctx, username=None):
    if username is None:
        username = input('Username: ')
    password = getpass()
    return ctx.api.users_token_create(username, password)


@users.command(name='login', help='login a certain user (store its user token)')
@pass_state
@click.option('--other',
              help='login another user and not the default (which will be used by default in "rebrickable user [...]")',
              is_flag=True,
              default=False)
@click.argument('username', required=False)
def users_login(ctx, other, username=None):
    try:
        users_token = create_auth(ctx, username)
        data = get_data()
        if not other:
            data.setdefault('users', {}).setdefault('%%default%%', {})['token'] = users_token
        data.setdefault('users', {}).setdefault(username, {})['token'] = users_token
        write_data(data)

        print('OK, saved users token into %s' % DATA_PATH)
    except ApiException as e:
        print('Login failed, response was %s' % e.body)
        raise click.Abort()