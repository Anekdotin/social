from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
posts = Table('posts', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', TEXT),
    Column('timestamp', DATETIME),
    Column('author_id', INTEGER),
)

roles = Table('roles', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('default', BOOLEAN),
    Column('permissions', INTEGER),
)

users = Table('users', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=64)),
    Column('username', VARCHAR(length=64)),
    Column('role_id', INTEGER),
    Column('password_hash', VARCHAR(length=128)),
    Column('name', VARCHAR(length=64)),
    Column('location', VARCHAR(length=64)),
    Column('about_me', TEXT),
    Column('member_since', DATETIME),
    Column('last_seen', DATETIME),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['posts'].drop()
    pre_meta.tables['roles'].drop()
    pre_meta.tables['users'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['posts'].create()
    pre_meta.tables['roles'].create()
    pre_meta.tables['users'].create()
