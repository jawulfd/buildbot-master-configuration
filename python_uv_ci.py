from buildbot.plugins import util, steps

class PythonUVCI:
    VENV_PATH = "{{ buildbot_venv_path }}/bin"

    def __init__(self, repo_url: str):
        self.repo_url = repo_url
    
    def get_factory(self):
        factory = util.BuildFactory()

        # check out the source
        factory.addStep(steps.Git(name="Git Init", repourl=self.repo_url, mode='incremental'))

        # run uv sync
        factory.addStep(
            steps.Compile(
                name="UV Sync",
                command=[f"{VENV_PATH}/uv", "sync"]
            )
        )

        # run uv run ruff check
        factory.addStep(
            steps.Compile(
                name="UV Ruff Lint",
                command=[f"{VENV_PATH}/uv", "run", "ruff", "check"]
            )
        )

        # run uv build
        factory.addStep(
            steps.Compile(
                name="UV Build",
                command=[f"{VENV_PATH}/uv", "build"]
            )
        )

        return factory
