from git import Repo
import os


"""
Get the lastest tag from a repository
"""
def get_latest_tag(path: str):
    repo = Repo(path)
    return sorted(repo.tags, key= lambda t: t.commit.committed_datetime)


def clone_repo(url: str) -> Repo:
    """
    Clones a repository and stores into [*REPO_PATH*]/repo_name
    :param url: Git URL
    :return: Repository object
    """
    name = url.split("/")[-1]
    path = f'{os.environ["REPO_PATH"]}/{name}'

    try:
        r = Repo(path)
    except InvalidGitRepositoryError:
        log.debug(f"Clonning {repo}...")
        r = Repo.clone_from(url, path)
    else:
        log.debug(f"Fetching {path}...")
        r.remote().fetch()

    r = Repo()
    r.clone(url, path)
    r = Repo(path)
    return r


def remove_project(id: int):
    #TODO: Implement after Persistence is implemented
    pass
