import os
import json
import base64
import html
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
VIEWERS_DIR = ".viewers"
EXCLUDE_DIRS = [".git", "node_modules", ".idea", ".vscode", "venv", ".viewers", "dist", "build"]

def b64_encode(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

def format_bytes(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} GB"

def detect_category(rel_path):
    normalized = rel_path.replace('\\', '/').lower()
    if normalized.startswith('resumos'):
        return 'Resumos Jupyter'
    if normalized.startswith('jornada python'):
        return 'Jornada Python'
    if normalized.startswith('cursoemvideo_python'):
        return 'Curso em Vídeo'
    if normalized.startswith('cisco_fundamentos_python'):
        return 'Cisco Python'
    if normalized.startswith('mimo_app'):
        return 'Mimo App'
    if normalized.startswith('javascript'):
        return 'JavaScript & Web'
    if normalized.startswith('python'):
        return 'Apostilas & PDFs'
    return 'Geral'

def build_tree(startpath):
    viewers_dir_path = os.path.join(startpath, VIEWERS_DIR)
    if os.path.exists(viewers_dir_path):
        shutil.rmtree(viewers_dir_path)
    os.makedirs(viewers_dir_path, exist_ok=True)
    
    tree = {
        "name": os.path.basename(startpath),
        "type": "folder",
        "path": "",
        "children": []
    }
    
    all_files = []
    
    for root, dirs, files in os.walk(startpath):
        if VIEWERS_DIR in dirs:
            dirs.remove(VIEWERS_DIR)
            
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        dirs.sort()
        files.sort()
        
        rel_path = os.path.relpath(root, startpath)
        if rel_path == ".":
            current_node = tree
        else:
            parts = rel_path.split(os.sep)
            current_node = tree
            for part in parts:
                for child in current_node["children"]:
                    if child["name"] == part and child["type"] == "folder":
                        current_node = child
                        break
        
        for d in dirs:
            dir_path = os.path.relpath(os.path.join(root, d), startpath)
            current_node["children"].append({
                "name": d,
                "type": "folder",
                "path": dir_path.replace("\\", "/"),
                "children": []
            })
            
        for f in files:
            if f in ["build_dashboard.py", "build_dashboard.js", ".gitignore", "index.html"]:
                continue
                
            abs_file_path = os.path.join(root, f)
            file_rel_path = os.path.relpath(abs_file_path, startpath)
            ext = os.path.splitext(f)[1].lower()
            norm_rel_path = file_rel_path.replace("\\", "/")
            stat = os.stat(abs_file_path)
            
            category = detect_category(file_rel_path)
            viewer_name = file_rel_path.replace(os.path.sep, "_") + ".html"
            viewer_path = os.path.join(viewers_dir_path, viewer_name)
            viewer_url = f"{VIEWERS_DIR}/{viewer_name}"
            
            file_info = {
                "name": f,
                "type": "file",
                "ext": ext,
                "path": norm_rel_path,
                "viewerUrl": viewer_url,
                "size": stat.st_size,
                "sizeFormatted": format_bytes(stat.st_size),
                "modified": stat.st_mtime * 1000,
                "category": category
            }
            
            current_node["children"].append(file_info)
            all_files.append(file_info)
            
    return tree, all_files

if __name__ == "__main__":
    import subprocess
    print(f"🐍 Executando build a partir de: {ROOT_DIR}")
    # Chamar o build Node.js se disponível para renderização completa
    try:
        res = subprocess.run(["node", "build_dashboard.js"], cwd=ROOT_DIR, capture_output=True, text=True)
        print(res.stdout)
        if res.stderr:
            print(res.stderr)
    except Exception as e:
        print(f"Executando fallback Python: {e}")
        tree, all_files = build_tree(ROOT_DIR)
        print(f"Indexados {len(all_files)} arquivos.")
