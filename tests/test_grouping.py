import pytest

pytest.importorskip('pandas')
import pandas as pd

from utils.grouping import group_data


def test_numeric_grouping_quintiles():
    df = pd.DataFrame({'value': list(range(1, 101))})
    groups = group_data(df, 'value')
    assert len(groups) == 5
    expected = {f'value Quintile {i}' for i in range(1, 6)}
    assert set(groups.keys()) == expected
    for i in range(1, 6):
        grp = groups[f'value Quintile {i}']
        assert len(grp) == 20


def test_categorical_grouping():
    df = pd.DataFrame({'color': ['red', 'blue', 'red', 'green', 'blue', 'green']})
    groups = group_data(df, 'color')
    expected = {f'color: {c}' for c in ['red', 'blue', 'green']}
    assert set(groups.keys()) == expected
    for c in ['red', 'blue', 'green']:
        grp = groups[f'color: {c}']
        assert all(grp['color'] == c)
