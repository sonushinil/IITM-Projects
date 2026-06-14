#!/usr/bin/env python3
"""starter_eda.py - load dataset and perform initial EDA
"""

import argparse
import os
import pandas as pd


def main(path):
    print(f"Loading dataset from: {path}")
    df = pd.read_csv(path)
    print("\nShape:", df.shape)
    print("\nAttrition distribution:\n", df['Attrition'].value_counts())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nData types:\n", df.dtypes)

    outdir = os.path.join(os.path.dirname(__file__), 'outputs')
    os.makedirs(outdir, exist_ok=True)
    df.head().to_csv(os.path.join(outdir, 'head.csv'), index=False)
    df.describe(include='all').to_csv(os.path.join(outdir, 'describe.csv'))

    print(f"\nSample outputs written to: {outdir}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Starter EDA for HR Attrition dataset')
    default_path = r"C:\\Shinil\\IITM Pravartak\\Professional Certificate Programme in Generative AI and Machine Learning\\Python\\Projects\\Assignments\\WA_Fn-UseC_-HR-Employee-Attrition.csv"
    parser.add_argument('--path', default=default_path, help='Path to dataset CSV')
    args = parser.parse_args()
    main(args.path)
