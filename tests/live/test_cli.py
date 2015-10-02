import subprocess
import json
import xml.dom.minidom


class TestCli:
    def setup(self):

        self.full_permissions = [
            "dcm-list-accounts",
            "dcm-list-cm",  # may be a real problem with CM commands below
            "dcm-list-cm-environments",
            "dcm-list-cm-personalities",
            "dcm-list-cm-scripts",
            "dcm-list-cm-systems",
        ]

        self.user_only = [
            "dcm-list-api-keys",
            "dcm-list-billing-codes",  # bug associated
            "dcm-list-customers",
            "dcm-list-groups",
            "dcm-list-role-assignments",
            "dcm-list-roles",
        ]

        self.needs_flag = [
            "dcm-list-datacenters",  # requires --regionid
            "dcm-list-firewall-rules",  # requires --firewall
            "dcm-list-machine-images",  # one of the arguments --image/-i --regionid/-r --regionpid/-R is required
            "dcm-list-networks",  # You must specify either a dataCenterId, regionId, or accountId
            "dcm-list-rdbms-products",  # argument --region/-r is required
            "dcm-list-server-analytics",  # --server SERVER (also no shown as required)
            "dcm-list-server-terminate",  # required flag --all (change de default)
            "dcm-list-storage-objects",  # --regionid/-r is required
        ]

        self.broken = [
            "dcm-list-snapshots",
        ]

        self.all_list = [
            "dcm-list-accounts",
            "dcm-list-api-keys",
            "dcm-list-api-versions",
            "dcm-list-billing-codes",
            "dcm-list-clouds",
            "dcm-list-cm",
            "dcm-list-cm-environments",
            "dcm-list-cm-personalities",
            "dcm-list-cm-scripts",
            "dcm-list-cm-systems",
            "dcm-list-customers",
            "dcm-list-datacenters",
            "dcm-list-firewall-rules",
            "dcm-list-firewalls",
            "dcm-list-groups",
            "dcm-list-jobs",
            "dcm-list-loadbalancers",
            "dcm-list-machine-images",
            "dcm-list-networks",
            "dcm-list-rdbms",
            "dcm-list-rdbms-products",
            "dcm-list-regions",
            "dcm-list-role-assignments",
            "dcm-list-roles",
            "dcm-list-server-analytics",
            "dcm-list-server-products",
            "dcm-list-server-terminate",
            "dcm-list-servers",
            "dcm-list-snapshots",
            "dcm-list-storage-objects",
            "dcm-list-subscriptions",
            "dcm-list-users",
            "dcm-list-volumes"]

    def test_list_cli_simple(self):
        """run dcm-list-* commands that require no flags and work with account keys"""
        failed_commands = []

        simple_list_commands = [x for x in self.all_list
                                if x not in (set(self.broken)
                                             | set(self.needs_flag)
                                             | set(self.full_permissions)
                                             | set(self.user_only))]

        for command in simple_list_commands:
            try:
                assert 0 == subprocess.call(command)
            except AssertionError:
                failed_commands.append(command)

        for command in simple_list_commands:
            for flag in ["--json", "--xml"]:
                p = subprocess.Popen([command, flag], stdout=subprocess.PIPE)
                print "testing %s %s" % (command, flag)
                stdoutput, stderror = p.communicate()
                try:
                    assert 0 == p.returncode
                except AssertionError:
                    failed_commands.append("%s %s" % (command, flag))
                try:
                    if flag == "--json":
                        json.loads(stdoutput)
                    if flag == "--xml":
                        xml.dom.minidom.parseString(stdoutput)
                except ValueError:
                    failed_commands.append("%s %s did not parse" % (command, flag))
                except xml.parsers.expat.ExpatError:
                    failed_commands.append("%s %s did not parse" % (command, flag))

        if failed_commands:
            fail_message = "These commands failed"
            for command in failed_commands:
                fail_message = "%s\n%s" % (fail_message, command)
            raise AssertionError(fail_message)
