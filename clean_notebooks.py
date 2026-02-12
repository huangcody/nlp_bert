#!/usr/bin/env python3
"""清理 Jupyter Notebook 的输出和 metadata，避免 git 冲突"""

import json
import sys
from pathlib import Path


def clean_notebook(notebook_path):
    """清理 notebook 的输出和 metadata"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # 清理每个 cell
    for cell in notebook.get('cells', []):
        # 清空输出
        if 'outputs' in cell:
            cell['outputs'] = []

        # 清空执行计数
        if 'execution_count' in cell:
            cell['execution_count'] = None

        # 清理 cell metadata 中的 widgets 相关内容
        if 'metadata' in cell:
            # 移除可能导致冲突的 metadata
            cell['metadata'].pop('collapsed', None)
            cell['metadata'].pop('scrolled', None)
            cell['metadata'].pop('execution', None)

            # 清理 widgets metadata
            if 'widgets' in cell['metadata']:
                cell['metadata'].pop('widgets')

    # 清理 notebook 级别的 metadata
    if 'metadata' in notebook:
        # 保留必要的 metadata，移除 widgets
        if 'widgets' in notebook['metadata']:
            notebook['metadata'].pop('widgets')

        # 清理可能的其他动态 metadata
        if 'colab' in notebook['metadata']:
            # 保留 colab metadata，但移除动态内容
            colab_meta = notebook['metadata']['colab']
            colab_meta.pop('last_runtime', None)
            colab_meta.pop('provenance', None)

    # 写回文件，使用一致的格式
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)
        f.write('\n')  # 添加末尾换行符

    print(f"✓ 已清理: {notebook_path}")


def main():
    # 清理指定的 notebook 文件
    notebooks = [
        'finetune.ipynb',
        'predict.ipynb'
    ]

    script_dir = Path(__file__).parent

    for notebook_name in notebooks:
        notebook_path = script_dir / notebook_name
        if notebook_path.exists():
            clean_notebook(notebook_path)
        else:
            print(f"✗ 找不到文件: {notebook_path}")


if __name__ == '__main__':
    main()
