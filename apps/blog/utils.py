import requests


def get_latest_jobs(limit=5):
    try:
        response = requests.get('https://remotelist.ru/api/jobs', params={'limit': limit}, timeout=5)
    except Exception:
        return []
    else:
        return response.json()
