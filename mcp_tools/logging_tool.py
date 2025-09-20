import json
import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), '..', 'logs', 'activity.log')

def log_action(user: str, action: str, details: dict):
    """Logs an action to the activity log."""
    log_entry = {
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'user': user,
        'action': action,
        'details': details
    }

    log_dir = os.path.dirname(LOG_FILE)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')
