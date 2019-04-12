# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""App Engine app to serve as an endpoint for App Engine queue samples."""
import os
# [START cloud_tasks_appengine_quickstart]
from flask import Flask, request

app = Flask(__name__)


@app.route('/example_task_handler', methods=['POST'])
def example_task_handler():
    """Log the request payload."""
    payload = request.get_data(as_text=True) or '(empty payload)'
    print('Received task with payload: {}'.format(payload))
    return 'Printed task payload: {}'.format(payload)
# [END cloud_tasks_appengine_quickstart]


@app.route('/')
def hello():
    """Basic index to verify app is serving."""
    return 'Hello World!'


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    port = os.environ.get('PORT', 8080)
    app.run(debug=True, host='0.0.0.0', port=int(port))
