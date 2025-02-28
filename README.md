<h1 align="center">Photo Gallery for Numworks Calculator</h1>
<p align="center">
    <img alt="Version" src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge&color=blue">
    <img alt="Stars" src="https://img.shields.io/github/stars/SaltyMold/Photo-Gallery-for-Numworks?style=for-the-badge&color=magenta">
    <img alt="Forks" src="https://img.shields.io/github/forks/SaltyMold/Photo-Gallery-for-Numworks?color=cyan&style=for-the-badge&color=purple">
    <img alt="License" src="https://img.shields.io/github/license/SaltyMold/Photo-Gallery-for-Numworks?style=for-the-badge&color=blue">
    <br>
    <a href="https://github.com/SaltyMold"><img title="Developer" src="https://img.shields.io/badge/Developer-SaltyMold-red?style=flat-square"></a>
    <img alt="Maintained" src="https://img.shields.io/badge/Maintained-Yes-blue?style=flat-square">
    <img alt="Written In" src="https://img.shields.io/badge/Written%20In-C-yellow?style=flat-square">
</p>

_This app is a **[Photo Gallery](https://en.wikipedia.org/wiki/Art_gallery)** reader that runs on the **[NumWorks calculator](https://www.numworks.com)**, allowing users to view and navigate through images directly on their device. It can store up to **64 images at a 320×240 resolution with 52 colors** and provides a simple interface for browsing them.  The app comes preinstalled with a collection of **funny pictures** to make classes more entertaining._


## Install the app

To install this app, you'll need to:
1. Download the latest **`Gallery.nwa`** file from the **[Releases](https://github.com/SaltyMold/Photo-Gallery-for-Numworks/releases)** page
3. Connect your **NumWorks calculator** to your computer using a USB cable.  
4. Head to **[my.numworks.com/apps](https://my.numworks.com/apps)** to send the **`nwa`** file on your **calculator**.

## How to use the app

<table>
  <tr>
    <td>
      <table>
        <tr>
          <th>Touche</th>
          <th>Action</th>
        </tr>
        <tr>
          <td>Home</td>
          <td>Quit</td>
        </tr>
        <tr>
          <td>Arrow Down</td>
          <td>Down</td>
        </tr>
        <tr>
          <td>Arrow Up</td>
          <td>Up</td>
        </tr>
        <tr>
          <td>OK</td>
          <td>Select the photo</td>
        </tr>
        <tr>
          <td>1</td>
          <td>Go to page 1</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Go to page 2</td>
        </tr>
        <tr>
          <td>3</td>
          <td>Go to page 3</td>
        </tr>
        <tr>
          <td>4</td>
          <td>Go to page 4</td>
        </tr>
        <tr>
          <td>5</td>
          <td>Go to page 5</td>
        </tr>
        <tr>
          <td>6</td>
          <td>Go to page 6</td>
        </tr>
        <tr>
          <td>7</td>
          <td>Go to page 7</td>
        </tr>
      </table>
    </td>
    <td style="padding-left: 20px;">
      <img src="https://cdn-icons-png.flaticon.com/512/1375/1375106.png" width="350" title="icon">
    </td>
  </tr>
</table>


## Build the app

To build this sample app, you will need to install the **[embedded ARM toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain)** and **[Node.js](https://nodejs.org/en/) 18**. The C SDK for Epsilon apps is shipped as an **npm module called [nwlink](https://www.npmjs.com/package/nwlink) v0.0.16**.

### Debian

```sh
sudo apt install -y build-essential git gcc-arm-none-eabi binutils-arm-none-eabi nodejs npm && npm install -g n && sudo n 18 && npm install -g nwlink@0.0.16
git clone https://github.com/SaltyMold/Photo-Gallery-for-Numworks.git
cd Photo-Gallery-for-Numworks
make clean && make build
```

### Windows

Install msys2 from [the MSYS2 Github](https://github.com/msys2/msys2-installer/releases/download/2025-02-21/msys2-x86_64-20250221.exe) and open the msys2.exe file.
Download the .zip from [the Node Github](https://github.com/actions/node-versions/releases/download/18.20.7-13438827950/node-18.20.7-win32-x64.7z), and extract it.

```sh
#MSYS2

pacman -Syu

#Replace with the reel node path
echo 'export PATH="/c/Users/UserName/AppData/Local/Programs/node-18.20.7-win32-x64:$PATH"' >> ~/.bashrc
source ~/.bashrc

npm install -g nwlink@0.0.16
nwlink --version
```

```ps
#PowerShell

#You can chose a diferent path
$env:ChocolateyInstall = "$env:LOCALAPPDATA\Programs\choco"
[System.Environment]::SetEnvironmentVariable("ChocolateyInstall", $env:ChocolateyInstall, "User")

Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

$env:Path += ";$env:ChocolateyInstall\bin"
[System.Environment]::SetEnvironmentVariable("Path", $env:Path, "User")
choco --version

choco install make --version=4.3 -y --force
make --version
```

```sh
#MSYS2

#Replace with the reel make path
echo 'export PATH="/c/Users/UserName/AppData/Local/Programs/choco/make/bin:$PATH"' >> ~/.bashrc 
source ~/.bashrc

pacman -S --noconfirm mingw-w64-x86_64-arm-none-eabi-gcc
arm-none-eabi-gcc --version

pacman -S --noconfirm git
git --version
git clone https://github.com/SaltyMold/Photo-Gallery-for-Numworks.git

cd Photo-Gallery-for-Numworks
make clean && make build
```

You should now have a **`output/app.nwa` file** that you can distribute! Anyone can now install it on their calculator from the **[NumWorks online uploader](https://my.numworks.com/apps)**.

## How I created this application

I use **GIMP** to convert **images into text** (the GIMP Python code is available in the repository). The process works by **resizing the image to 320×240 pixels using a 52-color palette**. Each letter **represents a color from the palette**. The images are encoded like **"A5B3d7k2"**, which means 5 pixels of color A, 3 pixels of color B, 7 pixels of color d, and 2 pixels of color k. Then, the **C code** reconstructs and displays the image.

## Build your own app

To build your own app, start by cloning the repository:

```sh
git clone https://github.com/SaltyMold/Photo-Gallery-for-Numworks.git
```
Inside the project, you'll find `eadk.h`, which provides **essential functions** for interacting with the **[calculator](https://en.wikipedia.org/wiki/NumWorks)**. Modify `main.c` to implement your own code.
Additionally, make sure to include an `icon.png` with dimensions **55×56 pixels** to serve as your **app’s icon**. Once your modifications are done, link the app with **[nwlink](https://www.npmjs.com/package/nwlink)** and enjoy your app!

## Special thanks 

I followed the guide from [epsilon-sample-app-c](https://github.com/numworks/epsilon-sample-app-c) to build this app.
