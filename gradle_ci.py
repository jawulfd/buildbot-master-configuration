from buildbot.plugins import util, steps

class GradleCI:
    def __init__(self, repo_url: str):
        self.repo_url = repo_url
    
    def get_factory(self):
        factory = util.BuildFactory()

        # check out the source
        factory.addStep(steps.Git(name="Git Init", repourl=self.repo_url, mode='incremental'))

        # run gradle build without tests
        factory.addStep(
            steps.Compile(
                name="Gradle Clean Build",
                command=["gradle", "clean", "build", "-x", "test"]
            )
        )

        # run gradle test
        factory.addStep(
            steps.Compile(
                name="Gradle Tests",
                command=["gradle", "test"]
            )
        )

        return factory
