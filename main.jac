import agents/repo_mapper.jac;
import agents/code_analyzer.jac;
import agents/doc_genie.jac;
import agents/supervisor.jac;

walker main {
    has repo_url;

    can run entry;

    entry {
        if (repo_url == None) {
            repo_url = "https://github.com/pallets/flask";
        }

        print("🌐 Starting Codebase Genius...");
        spawn Supervisor(repo_url=repo_url);
    }
}
