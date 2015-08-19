# Centos Config for Gemfire

So you want to setup a Gemfire cluster on AWS using CENTOS?
Follow these easy steps and you'll be running heavy transactional workloads before you can say throughput

### Installation

```sh
$ git clone https://github.com/mross-pivotal/CentosGemfireConfig.git
$ cd CentosGemfireConfig
$ sudo pip install fabric
```

Almost too easy...here's how fabric works, so if you look in the fabfile.py, you'll see a bunch of different funcitons.  You'll specificy which one's you want to run from the command line and then Fabric will ssh onto each of the nodes and do whatever you please with them.  

So for our Gemfire endeavors we want something like this.  

```sh
$ fab ec2 send_files install_files setup_env
```

When you run the script, it'll ask you for the public dns of the nodes you want to run the scripts on, just write STOP to execute on those nodes once you've entered the addresses.  
