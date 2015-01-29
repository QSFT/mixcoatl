from mixcoatl.admin.billing_code import BillingCode
from mixcoatl.geography.region import Region
from mixcoatl.admin.group import Group
from mixcoatl.admin.user import User


def get_servers(servers, **kwargs):
    """ Returns a list of servers

    Arguments:
    :param servers: a list of servers that needs to be filtered.

    Keyword arguments:
    :param account_user_id: owning user's account user ID.
    :param vm_login_id: owning user's VM login ID.
    :param email: owning user's email address.
    :param group_id: owning group's group ID.
    :param budget_id: budget ID.
    :returns: a list of filtered servers.
    :rtype: list
    """
    filtered_servers = servers

    if 'account_user_id' in kwargs and kwargs['account_user_id'] is not None:
        filtered_servers = [server for server in servers if hasattr(server, 'owning_user') and
                            'account_user_id' in server.owning_user and
                            server.owning_user['account_user_id'] == kwargs['account_user_id']]

    if 'vm_login_id' in kwargs and kwargs['vm_login_id'] is not None:
        if filtered_servers is not None:
            servers = filtered_servers
        filtered_servers = [server for server in servers if hasattr(server, 'owning_user') and
                            'vm_login_id' in server.owning_user and
                            server.owning_user['vm_login_id'] == kwargs['vm_login_id']]

    if 'email' in kwargs and kwargs['email'] is not None:
        if filtered_servers is not None:
            servers = filtered_servers

        filtered_servers = [server for server in servers if hasattr(server, 'owning_user') and
                            server.owning_user.has_key('email') and
                            server.owning_user['email'] == kwargs['email']]

    if 'group_id' in kwargs and kwargs['group_id'] is not None:
        if filtered_servers is not None:
            servers = filtered_servers

        filtered_servers = [server for server in servers if hasattr(server, 'owning_groups')
                            for group in server.owning_groups if group['group_id'] == int(kwargs['group_id'])]

    if 'budget_id' in kwargs and kwargs['budget_id'] is not None:
        if filtered_servers is not None:
            servers = filtered_servers

        filtered_servers = [server for server in servers if hasattr(server, 'budget') and
                            server.budget == int(kwargs['budget_id'])]

    return filtered_servers


def get_snapshots(snapshots, **kwargs):
    """ Returns a list of snapshots

    Arguments:
    :param snapshots: a list of snapshots that needs to be filtered.

    Keyword arguments:
    :param group_id: owning group's group ID.
    :param budget_id: budget ID.
    :returns: a list of filtered snapshots.
    :rtype: list
    """
    filtered_snapshots = snapshots

    if 'group_id' in kwargs and kwargs['group_id'] is not None:
        filtered_snapshots = [snapshot for snapshot in snapshots if hasattr(snapshot, 'owning_groups')
                              for g in snapshot.owning_groups if g['group_id'] == int(kwargs['group_id'])]
    if 'budget_id' in kwargs and kwargs['budget_id'] is not None:
        if filtered_snapshots is not None: snapshots = filtered_snapshots
        filtered_snapshots = [snapshot for snapshot in snapshots if hasattr(snapshot, 'budget') and
                              snapshot.budget == int(kwargs['budget_id'])]
    return filtered_snapshots


def get_volumes(volumes, **kwargs):
    """ Returns a list of volumes

    Arguments:
    :param volumes: a list of volumes that needs to be filtered.

    Keyword arguments:
    :param vm_login_id: owning user's VM login ID.
    :param email: owning user's email address.
    :param group_id: owning group's group ID.
    :param budget_id: budget ID.
    :param size: minimum size of the volume.
    :returns: a list of filtered volumes.
    :rtype: list
    """
    filtered_volumes = volumes

    if 'vm_login_id' in kwargs and kwargs['vm_login_id'] is not None:
        filtered_volumes = [volume for volume in volumes if hasattr(volume, 'owning_user') and
                            'vm_login_id' in volume.owning_user and
                            volume.owning_user['vm_login_id'] == kwargs['vm_login_id']]
    if 'email' in kwargs and kwargs['email'] is not None:
        if filtered_volumes is not None:
            volumes = filtered_volumes
        filtered_volumes = [volume for volume in volumes if hasattr(volume, 'owning_user') and
                            'email' in volume.owning_user and
                            volume.owning_user['email'] == kwargs['email']]
    if 'group_id' in kwargs and kwargs['group_id'] is not None:
        if filtered_volumes is not None:
            volumes = filtered_volumes
        filtered_volumes = [volume for volume in volumes if hasattr(volume, 'owning_groups')
                            for group in volume.owning_groups if group['group_id'] == int(kwargs['group_id'])]
    if 'budget_id' in kwargs and kwargs['budget_id'] is not None:
        if filtered_volumes is not None:
            volumes = filtered_volumes
        filtered_volumes = [volume for volume in volumes if hasattr(volume, 'budget') and
                            volume.budget == int(kwargs['budget_id'])]
    if 'size' in kwargs and kwargs['size'] is not None:
        if filtered_volumes is not None:
            volumes = filtered_volumes
        filtered_volumes = [volume for volume in volumes if volume.size_in_gb >= int(kwargs['size'])]

    return filtered_volumes


def get_user(users, **kwargs):
    """ Returns a user that matches with arguments.

    Arguments:
    :param users: a list of users that needs to be filtered.

    Keyword arguments:
    :param vm_login_id: owning user's VM login ID.
    :param email: owning user's email address.
    :returns: a list of filtered users.
    :rtype: list
    """
    selected_user = users

    if 'vm_login_id' in kwargs and kwargs['vm_login_id'] is not None:
        for user in users:
            if hasattr(user, 'vm_login_id') and user.vm_login_id == kwargs['vm_login_id']:
                selected_user = user
    elif 'email' in kwargs and kwargs['email'] is not None:
        for user in users:
            if hasattr(user, 'email') and user.email == kwargs['email']:
                selected_user = user

    return selected_user


def get_account_user_id(**kwargs):
    """ Returns account_user_id from arguments

    Keyword arguments:
    :param vm_login_id: user's VM login ID like p100
    :param email: user's E-Mail address
    :returns: account_user_id
    :rtype: int
    """
    if 'vm_login_id' in kwargs:
        users = User.all()
        selected_user = get_user(users, vm_login_id=kwargs['vm_login_id'])
    elif 'email' in kwargs:
        users = User.all()
        selected_user = get_user(users, email=kwargs['email'])

    return selected_user.account_user_id


def get_vm_login_id(**kwargs):
    """ Returns vm_login_id from arguments

    Keyword arguments:
    :param email: user's E-Mail address
    :returns: vm_login_id
    :rtype: str
    """
    if 'email' in kwargs:
        users = User.all()
        selected_user = get_user(users, email=kwargs['email'])

    return selected_user.vm_login_id


def get_budget_id(budget_name):
    """ Returns budget_id from arguments

    Arguments:
    :param budget_name: budget name
    :returns: budget_id
    :rtype: int
    """
    budgets = BillingCode.all(detail='basic')

    for budget in budgets:
        if hasattr(budget, 'name') and budget.name == budget_name:
            selected_budget = budget
            return selected_budget.billing_code_id


def get_group_id(group_name):
    """ Returns a group ID from group name

    Arguments:
    :param group_name: name of the group
    :returns: group_id
    :rtype: int
    """
    groups = Group.all(detail='basic')

    for group in groups:
        if hasattr(group, 'name') and group.name == group_name:
            selected_group = group
            return selected_group.group_id


def get_region_id(region_pid):
    """ Returns a region ID from provider_id such as us-east-1.

    Arguments:
    :param region_pid: provider ID of the region such as us-east-1
    :returns: region_id such as 19343
    :rtype: int
    """
    regions = Region.all(detail='basic')

    for region in regions:
        if hasattr(region, 'provider_id') and region.provider_id == region_pid:
            selected_region = region
            return selected_region.region_id
