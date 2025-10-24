walker CodeAnalyzer {
    has repo_path;
    has signatures;

    can run entry;

    entry {
        print("🔍 CodeAnalyzer: analyzing Python files...");
        py_import("helpers");
        signatures = helpers.extract_python_signatures(repo_path);
        report signatures;
    }
}
