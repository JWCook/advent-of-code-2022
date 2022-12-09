import pandas as pd
import seaborn as sns

from . import SOLUTIONS_DIR, read_input
from .problem_9 import find_visited

sns.set_theme(style="darkgrid")


def plot_visited(data: str, n_segments: int):
    df = _get_visited_df(data, n_segments)
    plot = sns.scatterplot(data=df, x='x', y='y')
    plot.get_figure().savefig(SOLUTIONS_DIR / 'problem_9.png')


def plot_visited_line(data: str, n_segments: int):
    df = _get_visited_df(data, n_segments)
    # plot = sns.relplot(data=df, x='x', y='y', hue='i', kind="line")
    plot = sns.lineplot(x=df.x, y=df.y, sort=False)
    plot.figure.savefig(SOLUTIONS_DIR / 'problem_9b.png')


def _get_visited_df(*args):
    visited = [(x, y, i) for i, (x, y) in enumerate(find_visited(*args))]
    return pd.DataFrame.from_records(list(visited), columns=['x', 'y', 'i'])


if __name__ == '__main__':
    data = read_input(9)
    # plot_visited(data, 2)
    # plot_visited(data, 10)
    plot_visited_line(data, 10)
