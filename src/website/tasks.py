from houseChecker.celery import app


@app.tasks(name='test_task')
def test_task():
    print('BATAAAAAAAAAAAAAAAAAAAAAAAATAS')