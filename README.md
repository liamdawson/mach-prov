# Machine Provisioning

License: [CC0-1.0](LICENSE)

Liam Dawson's personal machine provisioning scripts.

## Instructions

### Ubuntu Dell XPS 15

#### After new install

```shell
# enable network, then...

sudo apt-get install -y curl
mkdir ~/b
cd ~/b
curl -sSL https://github.com/liamdawson/mach-prov/archive/new.tar.gz | tar xz --strip-components=1
sudo python3 provision.py ubuntu xps15
```
