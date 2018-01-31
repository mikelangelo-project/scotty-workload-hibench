from hibench.workload import HiBenchWorkload

def run(context):
    hibench_workload = HiBenchWorkload(context)
    hibench_workload.run()

def collect(context):
    pass

def clean(context):
    pass
