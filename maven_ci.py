from buildbot.plugins import util, steps

class MavenCI:
    MAVEN_TOOLCHAINS_PATH = "/opt/toolchains/toolchains.xml"

    def __init__(self, repo_url: str):
        self.repo_url = repo_url
    
    def get_factory(self):
        factory = util.BuildFactory()

        # check out the source
        factory.addStep(steps.Git(name="Git Init", repourl=self.repo_url, mode='incremental'))

        # run maven clean compile
        factory.addStep(
            steps.Compile(
                name="Maven Clean Compile",
                command=["mvn", "clean", "compile", "-t", self.MAVEN_TOOLCHAINS_PATH]
            )
        )

        # run maven test
        factory.addStep(
            steps.Compile(
                name="Maven Unit Tests",
                command=["mvn", "test", "-t", self.MAVEN_TOOLCHAINS_PATH]
            )
        )

        # run maven package
        factory.addStep(
            steps.Compile(
                name="Maven Generate Artifact",
                command=["mvn", "package", "-t", self.MAVEN_TOOLCHAINS_PATH]
            )
        )

        return factory
