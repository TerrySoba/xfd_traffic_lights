import requests


def travisCiBuildWasSuccessfull(userName, repositoryName, branchName):
    """
    This function checks if the latest Travis CI build was successfull.

    :param userName: The github username of the repository
    :param repositoryName: The name of the repository
    :param branchName: The branch to check.
    :return: True if build was successfull, False otherwise.
    """

    headers = {'user-agent': 'MyTravisCiClient/0.0.1',
               'Accept': 'application/vnd.travis-ci.2+json'}

    uri = 'https://api.travis-ci.org/repos/{}/{}/branches/{}'.format(userName, repositoryName, branchName)
    r = requests.get(uri, headers=headers)

    json_object = r.json()

    job_state = json_object["branch"]["state"]

    success = (job_state == "passed")

    return success


if __name__ == "__main__":
    # execute only if run as a script
    if (travisCiBuildWasSuccessfull("TerrySoba", "retro-game", "master")):
        print("Build was successfull.")
    else:
        print("Build failed.")

