from buildbot.plugins import worker

class KubeCustomWorker(worker.KubeLatentWorker):
    def createEnvironment(self, props):
        return super().createEnvironment(props)

    def get_build_container_volume_mounts(self, props):
        return [
            {
                "name": "docker-socket",
                "mountPath": "/var/run"
            }
        ]

    def get_volumes(self, props):
        return [
            {
                "name": "docker-socket",
                "emptyDir": {}
            }
        ]

    def getServicesContainers(self, props):
        return [
            {
                "name": "docker-dind",
                "image": "docker:28.1-dind",
                "args": ["--ip6tables=false"],
                "volumeMounts": (yield self.get_build_container_volume_mounts(props)),
                "securityContext": {"privileged": True}
            }
        ]
