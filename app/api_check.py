def api_check(ref: str, json: dict, config):
    # http://127.0.0.1:5000/tasks/1 {'answer': ''}
    url = ref.replace('http://127.0.0.1:5000/', '')
    if url.startswith('tasks'):
        """
        codes:
        400 - task id doesn't exist
        200 - answer correct
        300 - answer incorrect
        """

        task_id = url.replace('tasks/', '')
        print(task_id, 'task_id')

        # checking if task id exist
        if task_id not in config["tasks"].keys():
            return 400

        # is answer correct
        answer = json["answer"]
        if answer == config["tasks"][task_id]["answer"]:
            return 200
        return 300

