import uuid

from mixcoatl.resource import Endpoint
from mixcoatl.infrastructure.server import Server
from mixcoatl.admin.job import Job


class TestServerLive:
    def setup(self):
        # load an endpoint that this file must be hosted outside of git
        # because it contains credentials
        self.endpoint = Endpoint.multiple_from_file("../../secret-test-data/endpoints.json")['saas']

    def test_saas_server_create(self):
        """Test if we can create a VM using an live endpoint object and shut it down"""

        # This cli command would make a server similar to below
        # dcm-create-server --machineimage 29710 --datacenter 1273 \
        #     --name igable-terminateme --productid t1.micro --budgetid 1512 --description longstring

        self.server = Server(endpoint=self.endpoint)
        self.server.set_from_file("../../secret-test-data/ubuntu-trusty-14.04-amd64-server-20150629.json")

        # override the server name loaded from the json
        self.server.name = "mixcoatl-qa-%s" % str(uuid.uuid4())[:8]
        self.job_id = self.server.launch()

        Job.wait_for(self.job_id, endpoint=self.endpoint)
        self.job = Job(job_id=str(self.job_id), endpoint=self.endpoint)

        self.running_server = Server(self.job.message, endpoint=self.endpoint)
        self.running_server.wait_for(status='RUNNING')

        assert self.server.provider_product_id == self.running_server.provider_product_id
        assert self.server.machine_image['machine_image_id'] == self.running_server.machine_image['machine_image_id']
        assert self.server.data_center == self.running_server.data_center
        assert self.server.description == self.running_server.description
        assert self.server.name == self.running_server.name
        assert self.server.budget == self.running_server.budget

    def teardown(self):
        if hasattr(self, 'running_server'):
            if self.running_server:
                try:
                    assert self.running_server.destroy(reason="Mixcoatl QA test finished")
                except AssertionError:
                    raise AssertionError("Failed to destroy server id: %s with name: %s" %
                                         (self.running_server.server_id, self.running_server.name))
