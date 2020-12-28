import requests


def get_latest_jobs(limit=5, text=''):
    try:
        response = requests.get(
            'https://remotelist.ru/api/jobs',
            params={'limit': limit, 'text': text},
            timeout=5
        )
    except Exception:
        return []
    else:
        return response.json()
