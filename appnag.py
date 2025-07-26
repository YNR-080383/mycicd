import sys
import json

def get_file_path(branch):
    if branch == "dev":
        return "configs/dev_config.json"
    elif branch == "test":
        return "configs/test_config.json"
    elif branch == "main":
        return "configs/prod_config.json"
    else:
        return "configs/default_config.json"

def load_config(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] Config file not found: {path}")
        return {}
    except json.JSONDecodeError:
        print(f"[ERROR] Failed to parse JSON in: {path}")
        return {}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python appnag.py <branch-name>")
        sys.exit(1)

    branch = sys.argv[1]
    config_path = get_file_path(branch)

    print(f"[INFO] Branch: {branch}")
    print(f"[INFO] Config Path: {config_path}")

    config = load_config(config_path)
    print("[INFO] Loaded Config:", config)
