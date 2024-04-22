from app.core import queries


def api_login(ref: str, json: dict, config):
    url = ref.replace('http://127.0.0.1:5000/', '')
    if url.startswith('api/login'):
        """
        codes:
        400 - task id doesn't exist
        200 - answer correct
        300 - answer incorrect
        """

        # if all correct
        return 200

    else:
        return 400
