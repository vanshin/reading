"""add somethings

Revision ID: 22db450c605
Revises: 304621c29b32
Create Date: 2016-11-27 16:47:17.734865

"""

# revision identifiers, used by Alembic.
revision = '22db450c605'
down_revision = '304621c29b32'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=32), nullable=True),
    sa.Column('Chinese', sa.String(length=64), nullable=True),
    sa.Column('Phonogram', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phrase', sa.Text(), nullable=True),
    sa.Column('grammar', sa.Text(), nullable=True),
    sa.Column('translation', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'readings', sa.Column('editors', sa.String(length=64), nullable=True))
    op.drop_column(u'sentences', 'grammar_c')
    op.drop_column(u'sentences', 'grammar_j')
    op.drop_column(u'sentences', 'translation')
    op.drop_column(u'sentences', 'phrase')
    op.add_column(u'users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_column(u'users', 'password')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'users', sa.Column('password', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column(u'users', 'password_hash')
    op.add_column(u'sentences', sa.Column('phrase', mysql.TEXT(), nullable=True))
    op.add_column(u'sentences', sa.Column('translation', mysql.TEXT(), nullable=True))
    op.add_column(u'sentences', sa.Column('grammar_j', mysql.TEXT(), nullable=True))
    op.add_column(u'sentences', sa.Column('grammar_c', mysql.TEXT(), nullable=True))
    op.drop_column(u'readings', 'editors')
    op.drop_table('notes')
    op.drop_table('words')
    ### end Alembic commands ###
