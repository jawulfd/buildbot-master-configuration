TRIVY_SRC_ANALYSIS = ["trivy", "fs", "--scanners", "vuln,secrets,misconfig,license"]

TRIVY_IMAGE_ANALYSIS = ["trivy", "image", "--image-config-scanners", "vuln,secrets,license"]

SYFT_SRC_SBOM = []

SYFT_IMAGE_SBOM = []
