# zzl

罗安887（[luoan887](https://github.com/luoan887)）的个人仓库起点。

## 简介

这是一个使用 **src-layout** 的最小 Python 项目脚手架（包名 `zzl`，Python >= 3.11）。后续可在此迭代实际功能。

## 快速开始

```bash
git clone https://github.com/luoan887/zzl.git
cd zzl
```

### 安装

建议使用虚拟环境后以可编辑模式安装：

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

仅安装运行时依赖可用 `pip install -e .`。

### 运行

安装后可通过模块或控制台脚本启动（会打印 hello / 版本）：

```bash
python -m zzl
zzl
```

### 测试

```bash
pytest
```

## 目录结构

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── docs/
│   └── notes.md
├── src/
│   └── zzl/
│       ├── __init__.py
│       ├── __main__.py
│       └── cli.py
└── tests/
    └── test_smoke.py
```

## 开发

欢迎开 Issue / PR。贡献约定见 `docs/notes.md`。

## License

MIT — 见 [LICENSE](./LICENSE)。
