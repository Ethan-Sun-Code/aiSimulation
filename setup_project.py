import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

def create_file(path, content=""):
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created file: {path}")
    else:
        print(f"File already exists: {path}")

# 定义目录结构
directories = [
    "src/micro_models",
    "src/meso_structure",
    "src/simulation",
    "src/agent",
    "data/raw",
    "data/processed",
    "notebooks",
    "config",
    "tests"
]

# 定义文件
files = {
    "src/__init__.py": "",
    "src/micro_models/__init__.py": "",
    "src/meso_structure/__init__.py": "",
    "src/simulation/__init__.py": "",
    "src/agent/__init__.py": "",
    "config/material_props.yaml": "# Material properties configuration\n",
}

def main():
    base_dir = os.getcwd()
    print(f"Setting up project in: {base_dir}")

    for directory in directories:
        create_directory(os.path.join(base_dir, directory))

    for file_path, content in files.items():
        create_file(os.path.join(base_dir, file_path), content)

    print("\nProject structure setup complete!")

if __name__ == "__main__":
    main()