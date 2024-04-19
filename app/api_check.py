def api_check(ref: str, json: dict, config):
    # http://127.0.0.1:5000/tasks/1 {'answer': ''}
    url = ref.replace('http://127.0.0.1:5000/', '')
    if url.startswith('tasks'):
        task_id = url.replace('tasks/', '')
        print(task_id, 'task_id')

        if task_id not in config["tasks"].keys():
            print('task id not in tasks')
            return 444

        answer = json["answer"]
        if answer == config["tasks"][task_id]["answer"]:
            print('yahooooo')
            return 200

