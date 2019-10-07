import pdb
import sys
import click
import multiprocessing as mp
from pathlib import Path

@click.group()
def project_group():
    pass

def job(id):
    print(f'job {id}')


def start_job():
    pool = mp.Pool(4)
    for i in range(100):
        pool.apply_async(job, (i,))
    pool.close()
    pool.join()

@project_group.command()
@click.argument('name')
def func(name):
    print(f'fuck {name}')
    # __name__='__main__'
    print(__name__)
    # pdb.set_trace()
    # start_job()
    sys.path.append(Path(__file__).parent.as_posix())
    import project
    print(project.__name__)
    project.start_job()
