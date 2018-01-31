import logging
import os

import paramiko
from scotty.utils import WorkloadUtils

logger = logging.getLogger(__name__)


class HiBenchWorkload(object):
    def __init__(self, context):
        self.workload = context.v1.workload
        self.workload_utils = WorkloadUtils(context)

    def run(self):
        logger.info('Run workload')
        hibench_cluster = self.workload_utils.resources['hibench']
        #my_param = self.workload.params['my_param']
        #hibench_cluster.endpoint

    def _run_on(self, endpoint, params):
        pass
        #command = self._create_command(xxx)
        #self._exec_remote_command(command, endpoint)

    def _exec_remote_command(self, command, endpoint):
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                endpoint['ip'], 
                username=endpoint['user'], 
                key_filename=self._key_path(endpoint['key_name'])
            )
            stdin, stdout, stderr = ssh.exec_command(command)
            out = stdout.read()
            logger.info("Hibench {}:\r\n{}".format(endpoint['ip'], out))

    def _key_path(self, private_key_name):
        experiment_workspace_path = self.workload_utils.experiment_workspace.path
        key_path = os.path.join(experiment_workspace_path, private_key_name)
        return key_path
