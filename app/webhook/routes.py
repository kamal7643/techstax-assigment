from flask import Blueprint, json, request
from app.extensions import add_document
webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


def extract_event_data(payload):
    if 'action' in payload:
        # pull_request open or close
        if payload['action'] == 'opened':
            # pull_request
            author = payload['pull_request']['user']['login']
            from_branch = payload['pull_request']['head']['ref']
            to_branch = payload['pull_request']['base']['ref']
            timestamp = payload['pull_request']['updated_at']
            return {'event_type': 'pull_request', 'author': author, 'from_branch': from_branch, 'to_branch': to_branch, 'timestamp': timestamp}
        else:
            # pull_request merged
            author = payload['pull_request']['user']['login']
            from_branch = payload['pull_request']['head']['ref']
            to_branch = payload['pull_request']['base']['ref']
            timestamp = payload['pull_request']['merged_at']
            return {'event_type':'merge', 'author': author, 'from_branch': from_branch, 'to_branch': to_branch, 'timestamp': timestamp}
    else:
        # push request 
        author = payload['head_commit']['author']['name']
        to_branch = payload['ref'].split("/")[-1]
        timestamp = payload['head_commit']['timestamp']
        return {'event_type': 'push', 'author': author, 'to_branch': to_branch, 'timestamp': timestamp}

@webhook.route('/receiver', methods=["POST"])
def receiver():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        data = extract_event_data(data)
        add_document(data)

    return {'status':'success'}, 200

@webhook.route('/test', methods=['GET'])
def test():
    add_document({'test':'test'})
    return {'message': 'Hello World!'}, 200
