# DockerHub Mirror

DockerHub Mirror on Github powered by Github Actions and [Crane](https://github.com/google/go-containerregistry/tree/main/cmd/crane)

GitHub Actions scheduled to run daily at Midnight UTC to mirror DockerHub images
used by the Rust projects to [GHCR.io](https://ghcr.io).

The workflow can also be triggered manually.

## TODO

- [ ] Decide license. Can we use the same license as the original project?

## Why

DockerHub has rate limits to pull images, while GHCR.io does not.

## Credits

Codebase forked from [rblaine95/dockerhub-mirror](https://github.com/rblaine95/dockerhub-mirror).
