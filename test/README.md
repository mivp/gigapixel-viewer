**Simulating a CAVE2 environment on a Linux desktop system**

Edit your default.cfg to point cave2-emu.cfg (or copy to default.cfg in the script directory)

Put this in your /etc/hosts so we can ssh to our simulated nodes

#CAVE2 test aliases
127.0.0.1	n01
127.0.0.1	n02
127.0.0.1	n03
127.0.0.1	n04
127.0.0.1	n05
127.0.0.1	n06
127.0.0.1	n07
127.0.0.1	n08
127.0.0.1	n09
127.0.0.1	n10
127.0.0.1	n11
127.0.0.1	n12
127.0.0.1	n13
127.0.0.1	n14
127.0.0.1	n15
127.0.0.1	n16
127.0.0.1	n17
127.0.0.1	n18
127.0.0.1	n19
127.0.0.1	n20

Ensure passwordless ssh is configured (your public key is in .ssh/authorized_keys)
Add this to your ~/.ssh/config file to avoid the 20 prompts the first time you connect

StrictHostKeyChecking no


