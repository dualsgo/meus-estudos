import os
import json
import base64
import html
import shutil

VIEWERS_DIR = ".viewers"

def b64_encode(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

def generate_viewer_html(title, content_html, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    {extra_head}
    <style>
        :root {{
            --bg-color: #0f172a;
            --glass-bg: rgba(30, 41, 59, 0.7);
            --glass-border: rgba(255, 255, 255, 0.08);
            --primary: #38bdf8;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Outfit', sans-serif; }}
        body {{
            background-color: var(--bg-color);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        header {{
            padding: 1rem 2rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            border-bottom: 1px solid var(--glass-border);
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        .back-btn {{
            color: var(--text-main);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            background: rgba(255,255,255,0.05);
            transition: 0.3s;
        }}
        .back-btn:hover {{
            background: rgba(56, 189, 248, 0.2);
            color: var(--primary);
        }}
        .file-title {{
            font-size: 1.2rem;
            font-weight: 500;
        }}
        main {{
            flex: 1;
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
        }}
        .container {{
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid var(--glass-border);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            overflow-x: auto;
        }}
    </style>
</head>
<body>
    <header>
        <a href="../index.html" class="back-btn"><i class="fa-solid fa-arrow-left"></i> Voltar</a>
        <div class="file-title">{title}</div>
    </header>
    <main>
        {content_html}
    </main>
</body>
</html>"""

def make_py_viewer(file_path, rel_path, viewer_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    escaped_code = html.escape(code)
    
    extra_head = """
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css">
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
    <style>
        .sandbox-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
        .sandbox-header h2 { font-size: 1.2rem; color: var(--primary); display: flex; align-items: center; gap: 0.5rem; }
        .py-repl-container { border-radius: 8px; overflow: hidden; border: 1px solid var(--glass-border); background: #1e293b; }
    </style>
    """
    
    content_html = f"""
    <div class="container">
        <div class="sandbox-header">
            <h2><i class="fa-brands fa-python"></i> Sandbox PyScript</h2>
            <span>Edite e execute (Shift + Enter) ou no botão verde ▶</span>
        </div>
        <div class="py-repl-container">
            <script type="py" id="main-script"></script>
            <py-repl auto-generate="true">
{escaped_code}
            </py-repl>
        </div>
    </div>
    """
    
    os.makedirs(os.path.dirname(viewer_path), exist_ok=True)
    with open(viewer_path, 'w', encoding='utf-8') as f:
        f.write(generate_viewer_html(os.path.basename(file_path), content_html, extra_head))

def make_ipynb_viewer(file_path, rel_path, viewer_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            notebook = json.load(f)
        except:
            notebook = {"cells": []}
            
    extra_head = """
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/monokai-sublime.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/python.min.js"></script>
    
    <style>
        .cell { margin-bottom: 1.5rem; }
        .cell-markdown { font-size: 1.05rem; line-height: 1.6; color: #cbd5e1; }
        .cell-markdown h1, .cell-markdown h2, .cell-markdown h3 { color: #f1f5f9; margin-top: 1rem; margin-bottom: 0.5rem; }
        .cell-markdown code { background: rgba(0,0,0,0.3); padding: 0.2rem 0.4rem; border-radius: 4px; color: #eab308; }
        .cell-markdown pre { background: rgba(0,0,0,0.3); padding: 1rem; border-radius: 8px; overflow-x: auto; border: 1px solid var(--glass-border); margin: 1rem 0; }
        .cell-code { background: #23241f; border-radius: 8px; padding: 1rem; overflow-x: auto; position: relative; border: 1px solid #333; }
        .cell-output { background: #000; color: #a3e635; padding: 1rem; border-radius: 8px; margin-top: 0.5rem; font-family: monospace; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;}
        .prompt { position: absolute; top: 0.5rem; right: 0.5rem; color: #64748b; font-size: 0.8rem; user-select: none; }
    </style>
    """
    
    cells_html = ""
    for idx, cell in enumerate(notebook.get("cells", [])):
        cell_type = cell.get("cell_type")
        source = "".join(cell.get("source", []))
        
        if cell_type == "markdown":
            b64_source = b64_encode(source)
            cells_html += f"""
            <div class="cell cell-markdown" id="md-{idx}"></div>
            <script>
                (function(){{
                    const b64 = "{b64_source}";
                    const decoded = decodeURIComponent(escape(window.atob(b64)));
                    document.getElementById('md-{idx}').innerHTML = marked.parse(decoded);
                }})();
            </script>
            """
        elif cell_type == "code":
            escaped_code = html.escape(source)
            cells_html += f"""
            <div class="cell cell-code">
                <div class="prompt">In [{cell.get("execution_count") or " "}]</div>
                <pre><code class="language-python">{escaped_code}</code></pre>
            </div>
            """
            
            outputs = cell.get("outputs", [])
            if outputs:
                output_text = ""
                for out in outputs:
                    if out.get("output_type") == "stream":
                        output_text += html.escape("".join(out.get("text", [])))
                    elif out.get("output_type") == "execute_result":
                        data = out.get("data", {})
                        if "text/plain" in data:
                            output_text += html.escape("".join(data["text/plain"]))
                if output_text.strip():
                    cells_html += f'<div class="cell-output">{output_text}</div>'
            
    content_html = f'<div class="container">{cells_html}</div><script>hljs.highlightAll();</script>'
    os.makedirs(os.path.dirname(viewer_path), exist_ok=True)
    with open(viewer_path, 'w', encoding='utf-8') as f:
        f.write(generate_viewer_html(os.path.basename(file_path), content_html, extra_head))

def make_md_viewer(file_path, rel_path, viewer_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()
        
    extra_head = """
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        .markdown-body { font-size: 1.1rem; line-height: 1.7; color: #cbd5e1; }
        .markdown-body h1, .markdown-body h2 { border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem; margin-bottom: 1rem; color: var(--text-main); }
        .markdown-body a { color: var(--primary); text-decoration: none; }
        .markdown-body a:hover { text-decoration: underline; }
        .markdown-body pre { background: rgba(0,0,0,0.3); padding: 1rem; border-radius: 8px; overflow-x: auto; border: 1px solid var(--glass-border); margin: 1rem 0; }
        .markdown-body code { font-family: monospace; color: #eab308; background: rgba(0,0,0,0.3); padding: 0.2rem 0.4rem; border-radius: 4px; }
        .markdown-body pre code { padding: 0; background: transparent; color: inherit; }
        .markdown-body img { max-width: 100%; border-radius: 8px; }
        table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
        th, td { border: 1px solid var(--glass-border); padding: 0.5rem; text-align: left; }
        th { background: rgba(255,255,255,0.05); }
    </style>
    """
    
    b64_source = b64_encode(source)
    
    content_html = f"""
    <div class="container markdown-body" id="md-content"></div>
    <script>
        const b64 = "{b64_source}";
        const decoded = decodeURIComponent(escape(window.atob(b64)));
        document.getElementById('md-content').innerHTML = marked.parse(decoded);
    </script>
    """
    os.makedirs(os.path.dirname(viewer_path), exist_ok=True)
    with open(viewer_path, 'w', encoding='utf-8') as f:
        f.write(generate_viewer_html(os.path.basename(file_path), content_html, extra_head))

def make_pdf_viewer(file_path, rel_path, viewer_path):
    target_pdf = f"../{rel_path.replace(os.path.sep, '/')}"
    
    extra_head = """
    <style>
        main { padding: 0 !important; max-width: 100% !important; display: flex; flex-direction: column; }
        .pdf-container { flex: 1; width: 100%; height: calc(100vh - 75px); }
        iframe { width: 100%; height: 100%; border: none; display: block; }
    </style>
    """
    
    content_html = f"""
    <div class="pdf-container">
        <iframe src="{target_pdf}"></iframe>
    </div>
    """
    os.makedirs(os.path.dirname(viewer_path), exist_ok=True)
    with open(viewer_path, 'w', encoding='utf-8') as f:
        f.write(generate_viewer_html(os.path.basename(file_path), content_html, extra_head))


def build_tree(startpath, exclude_dirs):
    viewers_dir_path = os.path.join(startpath, VIEWERS_DIR)
    if os.path.exists(viewers_dir_path):
        shutil.rmtree(viewers_dir_path)
    os.makedirs(viewers_dir_path, exist_ok=True)
    
    tree = {
        "name": os.path.basename(startpath),
        "type": "folder",
        "children": []
    }
    for root, dirs, files in os.walk(startpath):
        if VIEWERS_DIR in dirs:
            dirs.remove(VIEWERS_DIR)
            
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
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
            if f in ["build_dashboard.py", ".gitignore", "index.html"]:
                continue
                
            abs_file_path = os.path.join(root, f)
            file_rel_path = os.path.relpath(abs_file_path, startpath)
            ext = os.path.splitext(f)[1].lower()
            
            target_url = file_rel_path.replace("\\", "/")
            
            try:
                viewer_name = file_rel_path.replace(os.path.sep, "_") + ".html"
                viewer_path = os.path.join(viewers_dir_path, viewer_name)
                viewer_url = f"{VIEWERS_DIR}/{viewer_name}"
                
                if ext == '.py':
                    make_py_viewer(abs_file_path, file_rel_path, viewer_path)
                    target_url = viewer_url
                elif ext == '.ipynb':
                    make_ipynb_viewer(abs_file_path, file_rel_path, viewer_path)
                    target_url = viewer_url
                elif ext == '.md':
                    make_md_viewer(abs_file_path, file_rel_path, viewer_path)
                    target_url = viewer_url
                elif ext == '.pdf':
                    make_pdf_viewer(abs_file_path, file_rel_path, viewer_path)
                    target_url = viewer_url
            except Exception as e:
                print(f"Erro ao processar viewer para {file_rel_path}: {e}")
            
            current_node["children"].append({
                "name": f,
                "type": "file",
                "ext": ext,
                "path": target_url
            })
            
    return tree

def generate_html(tree_json):
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meus Estudos - Dashboard Interativo</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --bg-color: #0f172a;
            --glass-bg: rgba(30, 41, 59, 0.7);
            --glass-border: rgba(255, 255, 255, 0.08);
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.5);
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --hover-bg: rgba(56, 189, 248, 0.1);
            --icon-folder: #eab308;
            --icon-python: #3b82f6;
            --icon-html: #ef4444;
            --icon-pdf: #ec4899;
            --icon-file: #cbd5e1;
            --card-radius: 20px;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Outfit', sans-serif;
        }}
        
        body {{
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(circle at 15% 50%, rgba(56, 189, 248, 0.15), transparent 25%),
                radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.15), transparent 25%);
            background-attachment: fixed;
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }}
        
        header {{
            padding: 2rem 4rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--glass-border);
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            z-index: 10;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        }}
        
        .logo-container {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}
        
        .logo-icon {{
            font-size: 2rem;
            color: var(--primary);
            filter: drop-shadow(0 0 10px var(--primary-glow));
            animation: float 3s ease-in-out infinite;
        }}
        
        h1 {{
            font-size: 1.8rem;
            font-weight: 700;
            letter-spacing: -0.5px;
            background: linear-gradient(135deg, #38bdf8, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .search-container {{
            position: relative;
            width: 350px;
        }}
        
        .search-input {{
            width: 100%;
            padding: 0.8rem 1.2rem;
            padding-left: 2.8rem;
            border-radius: 30px;
            border: 1px solid var(--glass-border);
            background: rgba(15, 23, 42, 0.6);
            color: var(--text-main);
            font-size: 1rem;
            outline: none;
            transition: all 0.3s ease;
            box-shadow: inset 0 2px 5px rgba(0,0,0,0.2);
        }}
        
        .search-input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 15px var(--primary-glow), inset 0 2px 5px rgba(0,0,0,0.2);
        }}
        
        .search-icon {{
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            transition: color 0.3s;
        }}
        
        .search-input:focus + .search-icon {{
            color: var(--primary);
        }}
        
        main {{
            display: flex;
            flex: 1;
            padding: 2rem;
            gap: 2rem;
            height: calc(100vh - 90px);
        }}
        
        /* Sidebar Styles */
        aside {{
            width: 300px;
            background: var(--glass-bg);
            border-radius: var(--card-radius);
            border: 1px solid var(--glass-border);
            padding: 1.5rem;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }}
        
        .sidebar-title {{
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-muted);
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        
        .nav-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}
        
        .nav-item {{
            padding: 0.8rem 1rem;
            border-radius: 12px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 1rem;
            transition: all 0.2s ease;
            color: var(--text-main);
            border: 1px solid transparent;
        }}
        
        .nav-item:hover, .nav-item.active {{
            background: var(--hover-bg);
            border-color: rgba(56, 189, 248, 0.2);
            transform: translateX(5px);
        }}
        
        .nav-item i {{
            font-size: 1.2rem;
            color: var(--icon-folder);
        }}
        
        /* Content Area */
        .content-area {{
            flex: 1;
            background: var(--glass-bg);
            border-radius: var(--card-radius);
            border: 1px solid var(--glass-border);
            padding: 2rem;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            display: flex;
            flex-direction: column;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }}
        
        .breadcrumb {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 2rem;
            font-size: 1.1rem;
            color: var(--text-muted);
            flex-wrap: wrap;
        }}
        
        .breadcrumb span {{
            cursor: pointer;
            transition: color 0.2s;
        }}
        
        .breadcrumb span:hover {{
            color: var(--primary);
        }}
        
        .breadcrumb i {{
            font-size: 0.8rem;
        }}
        
        .breadcrumb .current {{
            color: var(--text-main);
            font-weight: 600;
        }}
        
        .grid-view {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 1.5rem;
            overflow-y: auto;
            padding-right: 0.5rem;
        }}
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: transparent;
        }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(255, 255, 255, 0.2);
        }}
        
        .file-card {{
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid var(--glass-border);
            border-radius: 15px;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            gap: 1rem;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            text-decoration: none;
            color: var(--text-main);
            position: relative;
            overflow: hidden;
        }}
        
        .file-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(135deg, transparent, rgba(255,255,255,0.03));
            opacity: 0;
            transition: opacity 0.3s;
        }}
        
        .file-card:hover {{
            transform: translateY(-5px);
            border-color: rgba(56, 189, 248, 0.4);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3), 0 0 15px rgba(56, 189, 248, 0.1);
        }}
        
        .file-card:hover::before {{
            opacity: 1;
        }}
        
        .file-card.folder:hover i {{
            transform: scale(1.1);
        }}
        
        .file-icon {{
            font-size: 3.5rem;
            transition: transform 0.3s;
        }}
        
        .file-name {{
            font-size: 1rem;
            font-weight: 500;
            word-break: break-word;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        
        .file-meta {{
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: -0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        /* Icon Colors based on EXT */
        .icon-py {{ color: var(--icon-python); }}
        .icon-html {{ color: var(--icon-html); }}
        .icon-pdf {{ color: var(--icon-pdf); }}
        .icon-ipynb {{ color: #e38a22; }}
        .icon-ts, .icon-tsx {{ color: #3178c6; }}
        .icon-css {{ color: #264de4; }}
        .icon-json {{ color: #cbd5e1; }}
        .icon-md {{ color: #f8fafc; }}
        
        .empty-state {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: var(--text-muted);
            gap: 1rem;
        }}
        
        .empty-state i {{
            font-size: 4rem;
            opacity: 0.5;
        }}
        
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-5px); }}
            100% {{ transform: translateY(0px); }}
        }}
        
        /* Responsive */
        @media (max-width: 900px) {{
            main {{ flex-direction: column; }}
            aside {{ width: 100%; height: auto; max-height: 250px; }}
            header {{ flex-direction: column; gap: 1rem; padding: 1.5rem; }}
            .search-container {{ width: 100%; }}
        }}
    </style>
</head>
<body>

    <header>
        <div class="logo-container">
            <i class="fa-solid fa-graduation-cap logo-icon"></i>
            <h1>Meus Estudos</h1>
        </div>
        <div class="search-container">
            <input type="text" id="searchInput" class="search-input" placeholder="Buscar cursos, arquivos, resumos...">
            <i class="fa-solid fa-search search-icon"></i>
        </div>
    </header>

    <main>
        <aside>
            <div class="sidebar-title"><i class="fa-solid fa-layer-group"></i> Cursos & Trilhas</div>
            <ul class="nav-list" id="sidebarList">
                <!-- Injected via JS -->
            </ul>
        </aside>

        <section class="content-area">
            <div class="breadcrumb" id="breadcrumb">
                <!-- Injected via JS -->
            </div>
            <div class="grid-view" id="gridView">
                <!-- Injected via JS -->
            </div>
        </section>
    </main>

    <script>
        const fileTree = {json.dumps(tree_json)};
        
        let currentPathNodes = [fileTree];
        
        const gridView = document.getElementById('gridView');
        const breadcrumb = document.getElementById('breadcrumb');
        const sidebarList = document.getElementById('sidebarList');
        const searchInput = document.getElementById('searchInput');

        function getIconForFile(ext) {{
            switch(ext) {{
                case '.py': return '<i class="fa-brands fa-python file-icon icon-py"></i>';
                case '.html': return '<i class="fa-brands fa-html5 file-icon icon-html"></i>';
                case '.css': return '<i class="fa-brands fa-css3-alt file-icon icon-css"></i>';
                case '.js': return '<i class="fa-brands fa-js file-icon" style="color:#f7df1e"></i>';
                case '.ts': case '.tsx': return '<i class="fa-brands fa-react file-icon icon-tsx"></i>';
                case '.pdf': return '<i class="fa-solid fa-file-pdf file-icon icon-pdf"></i>';
                case '.ipynb': return '<i class="fa-solid fa-book-open file-icon icon-ipynb"></i>';
                case '.json': return '<i class="fa-solid fa-file-code file-icon icon-json"></i>';
                case '.md': return '<i class="fa-brands fa-markdown file-icon icon-md"></i>';
                case '.png': case '.jpg': case '.jpeg': return '<i class="fa-solid fa-image file-icon" style="color:#a855f7"></i>';
                default: return '<i class="fa-solid fa-file file-icon icon-file"></i>';
            }}
        }}
        
        function formatExt(ext) {{
            return ext ? ext.replace('.', '').toUpperCase() : 'FILE';
        }}

        function renderSidebar() {{
            sidebarList.innerHTML = '';
            // Render top level folders
            const topFolders = fileTree.children.filter(c => c.type === 'folder');
            
            const homeLi = document.createElement('li');
            homeLi.className = 'nav-item ' + (currentPathNodes.length === 1 ? 'active' : '');
            homeLi.innerHTML = `<i class="fa-solid fa-house"></i> Início`;
            homeLi.onclick = () => navigateToHome();
            sidebarList.appendChild(homeLi);
            
            topFolders.forEach(folder => {{
                const li = document.createElement('li');
                // Check if active
                const isActive = currentPathNodes.length > 1 && currentPathNodes[1].name === folder.name;
                li.className = 'nav-item ' + (isActive ? 'active' : '');
                li.innerHTML = `<i class="fa-solid fa-folder-open"></i> ${{folder.name.replace(/_/g, ' ')}}`;
                li.onclick = () => navigateToNode([fileTree, folder]);
                sidebarList.appendChild(li);
            }});
        }}

        function renderBreadcrumb() {{
            breadcrumb.innerHTML = '';
            currentPathNodes.forEach((node, index) => {{
                const span = document.createElement('span');
                if(index === currentPathNodes.length - 1) {{
                    span.className = 'current';
                    span.textContent = node.name === fileTree.name ? 'Meus Estudos' : node.name;
                }} else {{
                    span.textContent = node.name === fileTree.name ? 'Meus Estudos' : node.name;
                    span.onclick = () => {{
                        currentPathNodes = currentPathNodes.slice(0, index + 1);
                        renderView();
                    }};
                }}
                
                breadcrumb.appendChild(span);
                
                if (index < currentPathNodes.length - 1) {{
                    const icon = document.createElement('i');
                    icon.className = 'fa-solid fa-chevron-right';
                    breadcrumb.appendChild(icon);
                }}
            }});
        }}

        function renderGrid(nodes) {{
            gridView.innerHTML = '';
            if (!nodes || nodes.length === 0) {{
                gridView.innerHTML = `
                    <div class="empty-state" style="grid-column: 1 / -1;">
                        <i class="fa-solid fa-folder-open"></i>
                        <h2>Pasta Vazia</h2>
                        <p>Não há arquivos ou pastas aqui.</p>
                    </div>`;
                return;
            }}
            
            // Sort: folders first, then files
            const sortedNodes = [...nodes].sort((a, b) => {{
                if (a.type === b.type) return a.name.localeCompare(b.name);
                return a.type === 'folder' ? -1 : 1;
            }});

            sortedNodes.forEach(node => {{
                const el = document.createElement(node.type === 'folder' ? 'div' : 'a');
                el.className = `file-card ${{node.type}}`;
                
                if (node.type === 'folder') {{
                    el.onclick = () => {{
                        currentPathNodes.push(node);
                        searchInput.value = '';
                        renderView();
                    }};
                    el.innerHTML = `
                        <i class="fa-solid fa-folder file-icon" style="color: var(--icon-folder)"></i>
                        <div class="file-name">${{node.name}}</div>
                        <div class="file-meta">Pasta</div>
                    `;
                }} else {{
                    el.href = node.path;
                    el.target = '_blank';
                    el.innerHTML = `
                        ${{getIconForFile(node.ext)}}
                        <div class="file-name">${{node.name}}</div>
                        <div class="file-meta">${{formatExt(node.ext)}}</div>
                    `;
                }}
                gridView.appendChild(el);
            }});
        }}

        function renderView() {{
            renderSidebar();
            renderBreadcrumb();
            const currentNode = currentPathNodes[currentPathNodes.length - 1];
            renderGrid(currentNode.children);
        }}

        function navigateToHome() {{
            currentPathNodes = [fileTree];
            searchInput.value = '';
            renderView();
        }}

        function navigateToNode(pathArray) {{
            currentPathNodes = pathArray;
            searchInput.value = '';
            renderView();
        }}

        // Search Implementation
        function searchTree(node, query, results) {{
            if (node.name.toLowerCase().includes(query) && node !== fileTree) {{
                results.push(node);
            }}
            if (node.children) {{
                node.children.forEach(child => searchTree(child, query, results));
            }}
        }}

        searchInput.addEventListener('input', (e) => {{
            const query = e.target.value.toLowerCase();
            if (!query) {{
                renderView();
                return;
            }}
            
            const results = [];
            searchTree(fileTree, query, results);
            
            // Update breadcrumb for search
            breadcrumb.innerHTML = `<span class="current">Resultados de busca para: "${{query}}"</span>`;
            
            // Remove active states from sidebar
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            
            renderGrid(results);
        }});

        // Initial render
        renderView();
    </script>
</body>
</html>"""
    return html_content

if __name__ == "__main__":
    repo_dir = r"C:\Users\md\Desktop\meus-estudos"
    exclude_dirs = [".git", "node_modules", ".idea", ".vscode", "__pycache__", "build", "dist"]
    
    print("Escaneando o diretório e gerando viewers...")
    tree = build_tree(repo_dir, exclude_dirs)
    
    html_output = generate_html(tree)
    
    output_path = os.path.join(repo_dir, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)
        
    print(f"✅ Dashboard atualizado com sucesso em: {output_path}")
    print("Abra o arquivo index.html no navegador para visualizar.")
