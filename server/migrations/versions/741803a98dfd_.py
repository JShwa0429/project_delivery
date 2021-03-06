"""empty message

Revision ID: 741803a98dfd
Revises: a4280757e07e
Create Date: 2021-12-29 20:54:10.862131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '741803a98dfd'
down_revision = 'a4280757e07e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rabbitWeather',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('weather_name', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rabbitWeatherRanking',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('kinds_id', sa.Integer(), nullable=False),
    sa.Column('weather_id', sa.Integer(), nullable=False),
    sa.Column('weather_rank', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['kinds_id'], ['rabbitKinds.id'], ),
    sa.ForeignKeyConstraint(['weather_id'], ['rabbitWeather.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rabbitWeatherRanking')
    op.drop_table('rabbitWeather')
    # ### end Alembic commands ###
