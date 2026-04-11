from git import Repo, InvalidGitRepositoryError, repo
from core import log
import os


def get_latest_tag(path: str):
    """
    Get the lastest tag from a repository
    """
    repo = Repo(path)
    return sorted(repo.tags, key= lambda t: t.commit.committed_datetime)[-1]


def clone_repo(url: str, path: str = None) -> Repo:
    """
    Clones a repository and stores into [*REPO_PATH*]/repo_name
    :param url: Git URL
    :return: Repository object
    """
    if path is None:
        name = get_repo_name(url)
        path = f'{os.environ["REPO_PATH"]}/{name}'

    try:
        r = Repo(path)
    except InvalidGitRepositoryError:
        log.debug(f"Clonning {repo}...")
        r = Repo.clone_from(url, path)
    else:
        log.debug(f"Fetching {path}...")
        r.remote().fetch()

    return r


def get_repo_name(url: str) -> str:
    """
    Returns the name of the repository from a url
    :param url: Git URL
    :return: name of the repository
    """
    return url.split("/")[-1]


def remove_project(id: int):
    #TODO: Implement after Persistence is implemented
    pass
