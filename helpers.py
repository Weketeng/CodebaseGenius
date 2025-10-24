import os
import shutil
import git
import ast

def clone_repo(repo_url: str, dest='temp_repo'):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    print(f"Cloning {repo_url} ...")
    git.Repo.clone_from(repo_url, dest)
    print("Clone complete.")
    return os.path.abspath(dest)

def list_files(root_path: str):
    files = []
    for r, _, f in os.walk(root_path):
        if any(ig in r for ig in ['.git', 'node_modules', '__pycache__']):
            continue
        for file in f:
            files.append(os.path.relpath(os.path.join(r, file), root_path))
    return sorted(files)

def read_readme(repo_path: str):
    for name in ["README.md", "README.txt", "readme.md"]:
        path = os.path.join(repo_path, name)
        if os.path.exists(path):
            with open(path, encoding='utf-8', errors='ignore') as f:
                return f.read()
    return ""

def summarize_readme(text: str):
    if not text:
        return "No README found."
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return " ".join(lines[:5])[:800] + "..."

def extract_python_signatures(repo_path: str, max_files=100):
    results = {}
    count = 0
    for r, _, f in os.walk(repo_path):
        if any(ig in r for ig in ['.git', 'node_modules', '__pycache__']):
            continue
        for file in f:
            if not file.endswith(".py"):
                continue
            rel = os.path.relpath(os.path.join(r, file), repo_path)
            try:
                with open(os.path.join(r, file), encoding='utf-8', errors='ignore') as fh:
                    src = fh.read()
                tree = ast.parse(src)
                functions, classes = [], []
                for node in tree.body:
                    if isinstance(node, ast.FunctionDef):
                        args = [a.arg for a in node.args.args]
                        functions.append((node.name, args))
                    elif isinstance(node, ast.ClassDef):
                        methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                        classes.append((node.name, methods))
                results[rel] = {"functions": functions, "classes": classes}
            except Exception as e:
                results[rel] = {"error": str(e)}
            count += 1
            if count >= max_files:
                break
    return results

def write_markdown_output(repo_url, summary, files, sigs, out_dir="outputs"):
    os.makedirs(out_dir, exist_ok=True)
    repo_slug = repo_url.replace("https://", "").replace("/", "_").replace(":", "_")
    out_path = os.path.join(out_dir, f"{repo_slug}_docs.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Documentation for {repo_url}\n\n")
        f.write("## Summary\n" + summary + "\n\n")
        f.write("## File List\n")
        for fl in files[:50]:
            f.write(f"- `{fl}`\n")
        f.write("\n## Extracted Signatures\n")
        for path, info in sigs.items():
            f.write(f"\n### {path}\n")
            if "error" in info:
                f.write(f"❌ Parse error: {info['error']}\n")
                continue
            for c, m in info["classes"]:
                f.write(f"- Class `{c}` → methods: {m}\n")
            for fn, args in info["functions"]:
                f.write(f"- Function `{fn}({', '.join(args)})`\n")
    print(f"✅ Documentation written to: {out_path}")
    return out_path
