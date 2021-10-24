"""aimater_surface_reactions

Revision ID: de603b4a1175
Revises: f31c7d486f1f
Create Date: 2021-10-24 11:08:31.155048

"""
from alembic import op
from sqlalchemy.dialects import postgresql as pgsql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de603b4a1175'
down_revision = 'f31c7d486f1f'
branch_labels = ('aimater_surface_reactions',)
depends_on = None


def upgrade():
    op.create_table(
        "aimater_surface_layer",
        sa.Column("aimater_surface_layer_id", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("created_on", sa.DateTime, nullable=False),
        sa.Column("updated_on", sa.DateTime, nullable=False),
        sa.Column("substrate", sa.String(10), nullable=False),
        sa.Column("system_structure", sa.String(10), nullable=False),
        sa.Column("surface_layer", sa.String(10), nullable=False),
        sa.Column("surface_miller_index", sa.Integer, nullable=False),
        sa.Column("number_of_layers", sa.Integer, nullable=False),
        sa.Column("surface_repetition", sa.String(10), nullable=False),
        sa.Column("number_of_adsorbate1", sa.Integer),
        sa.Column("adsorbate1", sa.String(10)),
        sa.Column("number_of_adsorbate2", sa.Integer),
        sa.Column("adsorbate2", sa.String(10)),
        sa.Column("adsorption_site", sa.String(20)),
        sa.Column("adsorbate_coordinates", sa.String(50)),
        sa.Column("coverage_in_ml", sa.Float),
        sa.Column("number_of_atoms", sa.Integer),
        sa.Column("neb_step", sa.Integer),
        sa.Column("adsorption_energy", sa.Float),
        schema="public",
    )


def downgrade():
    op.drop_table('aimater_surface_layer')
