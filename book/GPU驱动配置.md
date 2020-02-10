# 主要介绍GPU驱动安装配置，所用的操作系统为ubuntu18.04。为之后快速的训练大型模型作准备。

> ## 1:首先进入你电脑的BIOS关掉Secure BOOT，此时需要设置一个密码，之后GPU配置好了可以再disable。


> ## 2:禁用 Ubuntu18.04的nouveau驱动
```bash
# 查看是否有nouveau驱动
lsmod | grep nouveau
# 如果有输出表示没有禁用，需要禁用
sudo nano /etc/modprobe.d/blacklist.conf
# 在最后两行添加：
blacklist nouveau
options nouveau modeset=0
# 禁用nouveau的第三方驱动，之后也不需要改回来

# 执行刷新内核
sudo update-initramfs -u

sudo reboot

#重启后确认：lsmod | grep nouveau 如果没有输出表示成功
```

> ## 3:在终端输入以下命令，查看GPU型号
> ```bash
> lspci | grep -i nvidia
> ```
> ## 比如 GeForce MX150
> ## 去英伟达官网下相应驱动：
> https://www.geforce.cn/drivers

> ## 你可以找到GeForce MX150，64bit的驱动。然后下载它得到NVIDIA-Linux-x86_64-430.50.run安装文件。

> ## 同样在终端先安装一些工具，然后运行并安装它
```bash
sudo apt-get purge nvidia*
sudo apt-get --purge remove xserver-xorg-video-nouveau
sudo apt-cache search nvidia | grep -E "nvidia-[0-9]{3}"
sudo apt-get update
sudo apt-get install gcc make
# 安装驱动并重启
chmod +x NVIDIA-Linux-x86_64-430.50.run
sudo ./NVIDIA-Linux-x86_64-430.50.run
sudo  shutdown -r now

# 查看显卡信息
nvida-smi
```

> ## 4:遇到的问题

```bash 

NVIDIA-SMI has failed because it couldn’t communicate with the NVIDIA driver. Ma
ke sure that the latest NVIDIA driver is installed and running

# 遇到这个问题解决办法：
# 方法一：
# cd /usr/src 查看驱动版本号(我的是410.93)

# ls 查看你的驱动版本型号
  sudo apt-get install dkms
  sudo dkms install -m nvidia -v 410.93
  #无需重启即可成功看到输入nvidia-smi后熟悉的界面
```