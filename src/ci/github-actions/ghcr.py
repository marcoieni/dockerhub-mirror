import os
import requests
import tarfile
import shutil
from io import BytesIO
from tempfile import TemporaryDirectory

def crane_gh_release_url() -> str:
    version = "v0.20.2"
    os_name = "Linux"
    arch = "x86_64"

    return f"https://github.com/google/go-containerregistry/releases/download/{version}/go-containerregistry_{os_name}_{arch}.tar.gz"


def download_crane():
    """Download the crane executable from the GitHub releases in the current directory.
    """

    try:
        # Download the GitHub release tar.gz file
        response = requests.get(crane_gh_release_url(), stream=True)
        response.raise_for_status()

        with TemporaryDirectory() as tmp_dir:
            # Extract the tar.gz file to temp dir
            with tarfile.open(fileobj=BytesIO(response.content), mode="r:gz") as tar:
                tar.extractall(path=tmp_dir)

            # The tar.gz file contains multiple files.
            # Copy crane executable to current directory.
            # We don't need the other files.
            crane_path = os.path.join(tmp_dir, "crane")
            shutil.copy2(crane_path, "./crane")

        print("Successfully downloaded and extracted crane")

    except requests.RequestException as e:
        print(f"Error downloading crane: {e}")
    except (tarfile.TarError, OSError) as e:
        print(f"Error handling files: {e}")


def mirror_dockerhub():
    # Images from DockerHub that we want to mirror
    images = ["ubuntu:25.04"]
    for img in images:
        # Mirror images from DockerHub to GHCR
        command = (
            f"./crane copy docker.io/{img} ghcr.io/${{ github.repository_owner }}/{img}"
        )
        os.system(command)


if __name__ == "__main__":
    download_crane()
    mirror_dockerhub()
