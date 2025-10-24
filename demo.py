# demo.py
import os
import sys
from helpers import clone_repo, list_files, read_readme, summarize_readme, extract_python_signatures, write_markdown_output

def run_demo(repo_url):
    dest = "temp_repo"
    repo_path = clone_repo(repo_url, dest=dest)
    files = list_files(repo_path)
    readme_text = read_readme(repo_path)
    summary = summarize_readme(readme_text, max_sentences=5)
    sigs = extract_python_signatures(repo_path)
    out = write_markdown_output(repo_url, summary, files, sigs)
    print("Documentation written to:", out)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python demo.py <public_github_repo_url>")
        print("Example: python demo.py https://github.com/pallets/flask")
        sys.exit(1)
    repo = sys.argv[1]
    run_demo(repo)
