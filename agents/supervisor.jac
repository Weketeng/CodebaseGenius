walker Supervisor {
    has repo_url;

    can run entry;

    entry {
        print("🚀 Supervisor: starting Codebase Genius pipeline");

        spawn RepoMapper(repo_url=repo_url);
        spawn CodeAnalyzer(repo_path="temp_repo");
        spawn DocGenie(repo_url=repo_url, repo_path="temp_repo");

        print("✅ Pipeline complete! Check outputs/ for your docs.md file");
    }
}
