from dagster import RunRequest, pipeline, op, repository, schedule, sensor


@op
def bar_op(_):
    pass


@pipeline
def bar_pipeline():
    bar_op()


@pipeline
def other_bar_pipeline():
    bar_op()


@repository
def bar_repo():
    return [bar_pipeline]
