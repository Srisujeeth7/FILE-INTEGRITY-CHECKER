import os
import hashlib
import json

# Directory to monitor
MONITOR_DIR = "./monitor_folder"
HASH_FILE = "hashes.json"

def calculate_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def scan_directory(directory):
    """Scan directory and return a dictionary of file hashes."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, directory)
            file_hashes[rel_path] = calculate_hash(full_path)
    return file_hashes

def save_hashes(hashes, file_path):
    with open(file_path, 'w') as f:
        json.dump(hashes, f, indent=4)

def load_hashes(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def check_integrity():
    print("🔍 Scanning files...")
    current_hashes = scan_directory(MONITOR_DIR)
    saved_hashes = load_hashes(HASH_FILE)

    changed = []
    added = []
    deleted = []

    for file, hash_val in current_hashes.items():
        if file not in saved_hashes:
            added.append(file)
        elif saved_hashes[file] != hash_val:
            changed.append(file)

    for file in saved_hashes:
        if file not in current_hashes:
            deleted.append(file)

    if not changed and not added and not deleted:
        print("✅ No changes detected. Files are intact.")
    else:
        if changed:
            print("⚠️ Changed files:")
            for file in changed:
                print("  -", file)
        if added:
            print("➕ Added files:")
            for file in added:
                print("  -", file)
        if deleted:
            print("❌ Deleted files:")
            for file in deleted:
                print("  -", file)

    # Update the stored hashes
    save_hashes(current_hashes, HASH_FILE)

if __name__ == "__main__":
    os.makedirs(MONITOR_DIR, exist_ok=True)
    check_integrity()
