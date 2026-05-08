from git import Repo, InvalidGitRepositoryError, NoSuchPathError
from core import log
import os


def get_latest_tag(path: str):
    """
    Get the lastest tag from a repository
    """
    repo = Repo(path)
    if not repo.tags:
        return None
    return sorted(repo.tags, key= lambda t: t.commit.committed_datetime)[-1]


def clone_repo(url: str, path: str = None) -> (bool, Repo):
    """
    Clones a repository and stores into [*REPO_PATH*]/repo_name
    :param url: Git URL
    :return: (Status, Repository object) Status is true only if the repo exists and can be cloned
    """
    if path is None:
        name = get_repo_name(url)
        path = f'{os.environ["REPO_PATH"]}/{name}'

    try:
        r = Repo(path)
    except (InvalidGitRepositoryError, NoSuchPathError):
        try:
            log.debug(f"Clonning {url}...")
            r = Repo.clone_from(url, path)
        except Exception as e:
            log.error(f"Failed to clone {url}: {e}")
            return False, None
    except Exception as e:
        log.error(f"Error accessing {path}: {e}")
        return False, None
    else:
        try:
            log.debug(f"Fetching {path}...")
            r.remote().fetch()
        except Exception as e:
            log.error(f"Failed to fetch {url}: {e}")
            return False, r

    if not r.tags:
        try:
            log.debug(f"No tags found in {url}. Creating 'INIT' tag.")
            r.create_tag("INIT")
        except Exception as e:
            log.error(f"Failed to create 'INIT' tag in {path}: {e}")

    return True, r


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
