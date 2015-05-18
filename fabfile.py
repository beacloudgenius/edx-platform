# Fabfile to:
#    - run ansible on remote machines(s)
#    - run ls

# Import Fabric's API module
from fabric.api import *

env.hosts = [
    'edxa.ec2.cloudgeni.us',
    #'edxb.ec2.cloudgeni.us',
    #'edxc.ec2.cloudgeni.us'
    # 'ip.add.rr.ess',
    # 'server2.domain.tld'
]

# Set the username
env.user   = "ubuntu"

# Set the password [NOT RECOMMENDED]
# env.password = "passwd"

def run_ansible():
    """
        Connect to remote
        Activate venv
        Change to the correct folder and
        Run ansible-playbook there
                                            """
    run("source /var/tmp/venv/configuration/bin/activate ; cd /var/tmp/configuration/playbooks/cloudgenius/ ; ansible-playbook ./edx_sandbox.yml \
        -c local -i 'localhost,' \
        -e edx_platform_version=named-release/birch \
        -e ora2_version=named-release/birch \
        -e certs_version=named-release/birch \
        -e forum_version=named-release/birch \
        -e xqueue_version=named-release/birch \
        -e@online.mongo.yml \
        -e@online.mysql.yml \
        -e@18010.yml")

def install_something():
    """ Download and install something. """
    run("ls")

def do_both():

    # Update
    run_ansible()

    # Install
    install_something()
