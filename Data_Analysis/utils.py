import pandas as pd


def get_stats(group):
    stats= {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'sum': group.sum()}
    return stats

def get_min(group):
    return group.min()

def get_max(group):
    return group.max()

def get_count(group):
    return group.sum()

def get_sum(group):
    return group.sum()

def count_real(group):
    stats = {'count' :group.count()}
    return stats