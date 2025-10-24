walker RepoMapper {
    has repo_url;
    has repo_path;

    can run entry;

    entry {
        print("🧭 RepoMapper: cloning ", repo_url);
        py_import("helpers");
        repo_path = helpers.clone_repo(repo_url, dest="temp_repo");
        report repo_path;
    }
}
