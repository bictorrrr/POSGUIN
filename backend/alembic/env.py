# alembic/env.py
from __future__ import annotations
from logging.config import fileConfig
import sys
from pathlib import Path

from alembic import context
from sqlalchemy import engine_from_config, pool

# === Ajusta el PYTHONPATH para que pueda importar "database" y "app.***" ===
BASE_DIR = Path(__file__).resolve().parents[1]  # carpeta "backend"
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# === Importa settings y metadata de tu app ===
from app.core.config import settings            # <- tu Settings (DATABASE_URL)
from database import Base                       # <- tu Base declarative_base

# IMPORTA TUS MODELOS para que Alembic los detecte (autogenerate)
# importa módulos, no clases sueltas:
import app.models.user          # noqa
import app.models.product       # noqa
# si tienes más, impórtalos aquí (catalogs, etc.)
# import app.models.catalogs    # noqa

# Alembic config
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Pasa la URL a Alembic (ignora la de alembic.ini si quieres)
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# ¡Clave! para autogenerate:
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,        # detecta cambios de tipo
        compare_server_default=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
