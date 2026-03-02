"""
Data preprocessing utilities for the Intrusion Detection (CIC-IDS2017) project.
"""

import numpy as np


def remove_duplicates(data):
    """Remove duplicate rows from a list of records."""
    seen = set()
    result = []
    for row in data:
        key = tuple(row)
        if key not in seen:
            seen.add(key)
            result.append(row)
    return result


def _replace_missing(value, fill_value):
    """Return fill_value if value is None or NaN, otherwise return value."""
    if value is None:
        return fill_value
    if isinstance(value, float) and np.isnan(value):
        return fill_value
    return value


def handle_missing_values(data, fill_value=0):
    """Replace None/NaN values with fill_value."""
    return [
        [_replace_missing(v, fill_value) for v in row]
        for row in data
    ]


def normalize(values):
    """Min-max normalize a list of numeric values to [0, 1]."""
    arr = np.array(values, dtype=float)
    min_val = arr.min()
    max_val = arr.max()
    if max_val == min_val:
        return [0.0] * len(values)
    return list((arr - min_val) / (max_val - min_val))


def encode_labels(labels):
    """Encode string labels to integer indices."""
    unique = sorted(set(labels))
    mapping = {label: idx for idx, label in enumerate(unique)}
    return [mapping[label] for label in labels], mapping
