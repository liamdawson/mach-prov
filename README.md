# Machine Provisioning

License: [CC0-1.0](LICENSE)

Liam Dawson's personal machine provisioning scripts.

## Instructions

### Arch Dell XPS 15

#### New Install

```shell
# enable network, then...

mkdir ~/b
cd ~/b
curl -sSL https://github.com/liamdawson/mach-prov/archive/master.tar.gz | tar xz --strip-components=1
./prepare dell/xps15
arch-chroot /mnt
cd /mach-prov
./install dell/xps15 fhtagn liamdawson
```

#### Update
