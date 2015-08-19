from fabric.api import *

#ec2-52-27-53-114.us-west-2.compute.amazonaws.com
#ec2-54-148-179-185.us-west-2.compute.amazonaws.com
def ec2():
    filename= ""
    hosts = []
    print "You will now enter the pubic DNS of your nodes, type STOP to execute"
    while(True):
        filename= raw_input("Please enter the public DNS of your node:  ")
        if(url_is_valid(filename)):
            print filename
            env.hosts.append(filename)
        else:
            break
    print env.hosts
    env.user= 'centos'
    env.key_filename= 'gem.pem'

def hello():
    run("echo hi from")
    run("python mypy.py")

def send_files():
    put('Pivotal_GemFire_810_b50625_Linux.tar.gz')
    # put('configure_nodes.gf')

def install_files():
    # run('sudo apt-get update')
    # run('sudo apt-get install default-jre')
    run('sudo yum install java-1.7.0-openjdk.x86_64')
    run('tar -xzvf Pivotal_GemFire_810_b50625_Linux.tar.gz')
    run('sudo mkdir /opt/pivotal')
    run('sudo mv Pivotal_GemFire_810_b50625_Linux /opt/pivotal')


def setup_env():
    run("echo 'export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64' >> .bash_rc")
    run("echo 'export PATH=$PATH:$JAVA_HOME/bin:/opt/pivotal/Pivotal_GemFire_810_b50625_Linux/bin' >> .bash_rc")
    run("echo 'export GEMFIRE=/opt/pivotal/Pivotal_Gemfire_810' >> .bash_rc")
    run("echo 'export GF_JAVA=$JAVA_HOME/bin/java' >> .bash_rc")
    run("echo 'export ip=$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)'")
    run(". .bash_rc")
    # run("gfsh start locator --name=locator1 --port=8001")
    # run("gfsh start server --name=server1 --locators=$ip[8001] --server-port=0")

def setup_gemfire():
    # run("/opt/pivotal/Pivotal_GemFire_810_b50625_Linux/bin/gfsh run --file=serverStart.gf")
    run("/opt/pivotal/Pivotal_GemFire_810_b50625_Linux/bin/gfsh start locator --name=locator1 --port=8001")
    # run("/opt/pivotal/Pivotal_GemFire_810_b50625_Linux/bin/gfsh start server --name=server1 --locators=52.25.81.63[8001] --server-port=0")

def setup_node_with_gf():
    send_files()
    install_files()
    setup_env()

def url_is_valid(filename):
    #make this a little more robust :-)
    if(filename != "STOP"):
        return True
    else:
        return False
