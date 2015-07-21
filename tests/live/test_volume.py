import uuid

from mixcoatl.resource import Endpoint
from mixcoatl.infrastructure.volume import Volume
from mixcoatl.admin.job import Job


class TestVolumeLive:
    def setup(self):
        # load an endpoint that this file must be hosted outside of git
        # because it contains credentials
        self.endpoint = Endpoint.multiple_from_file("../../../secret-test-data/endpoints.json")['vagrant']

    def test_volume_creation(self):
        """Test the creating of a dummy volume against a live endpoint"""

        # This command would create a volume similar to below
        # dcm-create-volume --budgetid 1512 --datacenter 1273 --size 1 --name mixcoatl-qa --description junk

        self.volume = Volume(endpoint=self.endpoint)
        self.volume.set_from_file("../../../secret-test-data/vagrant-volume.json")
        self.volume.name = "mixcoatl-qa-%s" % str(uuid.uuid4())[:8]
        self.job = self.volume.create()
        Job.wait_for(self.job.job_id, endpoint=self.endpoint)

        # force reload of job attributed from DCM API
        self.job.load()
        self.live_volume = Volume(volume_id=self.job.message, endpoint=self.endpoint)

        assert self.volume.data_center == self.live_volume.data_center
        assert self.volume.budget == self.live_volume.budget
        assert self.volume.size_in_gb == self.live_volume.size_in_gb
        assert self.volume.description == self.live_volume.description
        assert self.volume.name == self.live_volume.name

    def teardown(self):
        if hasattr(self, 'live_volume'):
            if self.live_volume:
                try:
                    assert self.live_volume.destroy(reason="Mixcoatl QA test finished")
                except AssertionError:
                    raise AssertionError("Failed to destroy volume_id: %s with name: %s" %
                                         (self.live_volume.volume_id, self.live_volume.name))
