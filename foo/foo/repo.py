from dagster import RunRequest, pipeline, repository, schedule, sensor, solid, op


@op()
def foo_op():
    pass


@op()
def foo_op_2():
    pass


@pipeline
def foo_pipeline():
    foo_op()
    foo_op_2()


@pipeline
def other_foo_pipeline():
    foo_op()


@repository
def foo_repo():
    return [foo_pipeline]


@repository
def other_foo_repo():
    return [other_foo_pipeline]
