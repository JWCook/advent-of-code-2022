import logging
from pathlib import Path

INPUTS_DIR = Path(__file__).parent.parent / 'inputs'
logging.basicConfig(level='INFO')


def get_input_data(day: int) -> str:
    with open(INPUTS_DIR / f'input_{day}') as f:
        return f.read()
