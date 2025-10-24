walker DocGenie {
    has repo_url;
    has repo_path;
    has out_path;

    can run entry;

    entry {
        print("🪄 DocGenie: generating Markdown docs...");
        py_import("helpers");
        summary = helpers.summarize_readme(helpers.read_readme(repo_path));
        files = helpers.list_files(repo_path);
        sigs = helpers.extract_python_signatures(repo_path);
        out_path = helpers.write_markdown_output(repo_url, summary, files, sigs);
        report out_path;
    }
}
