# Auto-generated Python classes from archetype
# Loads dummy data from CSV file for testing

import csv
import os
from typing import Any, Dict, List, Optional


def create_dataset(csv_file=None):
    """Create a dataset from CSV dummy data"""
    if csv_file is None:
        # Default to dummy CSV file
        csv_file = 'generated/data.csv'
    
    if not os.path.exists(csv_file):
        print(f'CSV file not found: {csv_file}')
        print('Run "epsilon archetypes <dataset_id>" to generate dummy data')
        return DatasetWrapper([])
    
    # Load CSV data
    records = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    
    print(f'Loaded {len(records)} dummy records from CSV')
    return DatasetWrapper(records)


class DatasetWrapper:
    """Wrapper for dataset records with easy access"""
    def __init__(self, records):
        self.records = records if isinstance(records, list) else [records]
    
    def __len__(self):
        return len(self.records)
    
    def __iter__(self):
        for record in self.records:
            yield Root(record)
    
    def __getitem__(self, index):
        return Root(self.records[index])
    
    @property
    def first(self):
        return Root(self.records[0]) if self.records else None


class Diagnoses:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def icd_code(self):
        # Try direct access first (JSON format)
        if 'icd_code' in self._data:
            return self._data['icd_code']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.icd_code'):
                return v
        return None

    @property
    def icd_version(self):
        # Try direct access first (JSON format)
        if 'icd_version' in self._data:
            return self._data['icd_version']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.icd_version'):
                return v
        return None


class Admissions:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def time(self):
        # Try direct access first (JSON format)
        if 'time' in self._data:
            return self._data['time']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.time'):
                return v
        return None

    @property
    def type(self):
        # Try direct access first (JSON format)
        if 'type' in self._data:
            return self._data['type']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.type'):
                return v
        return None


class Patient:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def gender(self):
        # Try direct access first (JSON format)
        if 'gender' in self._data:
            return self._data['gender']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.gender'):
                return v
        return None

    @property
    def age(self):
        # Try direct access first (JSON format)
        if 'age' in self._data:
            return self._data['age']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.age'):
                return v
        return None


class Medications:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def drug(self):
        # Try direct access first (JSON format)
        if 'drug' in self._data:
            return self._data['drug']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.drug'):
                return v
        return None


class Root:
    def __init__(self, data):
        self._data = data if data else {}


class Root:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def diagnoses(self):
        # Handle nested field access with dot notation
        if 'diagnoses' in self._data and isinstance(self._data['diagnoses'], dict):
            return Diagnoses(self._data['diagnoses'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'diagnoses.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Diagnoses(flattened)

    @property
    def admissions(self):
        # Handle nested field access with dot notation
        if 'admissions' in self._data and isinstance(self._data['admissions'], dict):
            return Admissions(self._data['admissions'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'admissions.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Admissions(flattened)

    @property
    def patient(self):
        # Handle nested field access with dot notation
        if 'patient' in self._data and isinstance(self._data['patient'], dict):
            return Patient(self._data['patient'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'patient.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Patient(flattened)

    @property
    def medications(self):
        # Handle nested field access with dot notation
        if 'medications' in self._data and isinstance(self._data['medications'], dict):
            return Medications(self._data['medications'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'medications.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Medications(flattened)

    @property
    def root(self):
        # Handle nested field access with dot notation
        if 'root' in self._data and isinstance(self._data['root'], dict):
            return Root(self._data['root'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'root.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Root(flattened)
