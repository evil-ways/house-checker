from houseChecker.celery import app


@app.task(name='test_task')
def test_task():
    print('BATAAAAAAAAAAAAAAAAAAAAAAAATAS')