"""TODO."""

import os

from rich import print as rprint

from gm.constants import SLUGS

# Files
SLUG_FILE = "slug.json"

# Directories
ROOT_DIR = os.path.expanduser("~")
STORAGE_DIR = ".el02gm"
BACKUP_DIR = ".gm/backup"

# Full Installation Paths
FULL_STORAGE_DIR = os.path.join(ROOT_DIR, STORAGE_DIR)
FULL_SLUG_FILE = os.path.join(FULL_STORAGE_DIR, SLUG_FILE)

# Full Backup Paths
FULL_BACKUP_DIR = os.path.join(ROOT_DIR, BACKUP_DIR)
BACKUP_SLUG_FILE = os.path.join(FULL_BACKUP_DIR, SLUG_FILE)

# Path map
PATH_MAP = {FULL_SLUG_FILE: BACKUP_SLUG_FILE}

for key, value in SLUGS.items():
    file = value.get("file")
    if not file:
        rprint("[bold red][ERROR][/bold red] Failed to process a slug. (-1)")
        continue

    full_file = os.path.join(FULL_STORAGE_DIR, file)
    full_backup_file = os.path.join(FULL_BACKUP_DIR, file)

    PATH_MAP[full_file] = full_backup_file
