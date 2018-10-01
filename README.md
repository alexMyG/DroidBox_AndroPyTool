# DroidBox-AndroPyTool

This is a fork of the [DroidBox](https://github.com/pjlantz/droidbox) tool to be used by [AndroPyTool](https://github.com/alexMyG/AndroPyTool). It includes new features:
  - Performance improved
  - Possibility of running in Non-GUI mode (ideal for servers)
  - Low level processes monitoring using **Strace**

### How to install

**0. Requirements**
- AndroPyTool has a series of dependencies. You can install all of them by executing:
    ```sh
    $ apt-get update
    $ apt-get install -y --no-install-recommends software-properties-common wget git lib32gcc1 lib32ncurses5 lib32stdc++6 lib32z1 libc6-i386 libgl1-mesa-dev python-pip python-dev gcc python-tk curl
    $ add-apt-repository ppa:webupd8team/java -y
    $ apt-get update
    $ echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
    $ apt-get install -y oracle-java8-installer
    $ apt-get install -y python-setuptools
    $ apt-get clean
    ```

**1. You need to install Android SDK** (go to next step if you already have it)
The next steps will allow you to install Android SDK in Non-GUI mode:
- Download and unzip Android SDK:
    ```sh
    $ cd
    $ wget http://dl.google.com/android/android-sdk_r24.2-linux.tgz
    $ tar -xvf android-sdk_r24.2-linux.tgz
    ```

- Add Android SDK to path (if you don't use Bash i.e. you prefer Zsh, remember to modify the correct file). To to that, add these two lines to your `~/.bashrc` file:
    ```
    export ANDROID_HOME=$HOME/android-sdk-linux/
    export PATH=$PATH:$ANDROID_HOME/tools
    export PATH=$PATH:$ANDROID_HOME/platform-tools
    ```
- Load the libraries in the current session with:

    ```sh
    $ source ~/.bashrc
    ```
**2. We have to install the Android 16 package**
- Let's install Android 16, which is the version supported by DroidBox (the platform and system image):

    ```sh
    $ echo y | android update sdk --filter tools --no-ui --force -a
    $ echo y | android update sdk --filter platform-tools --no-ui --force -a
    $ echo y | android update sdk --filter android-16 --no-ui --force -a
    $ echo y | /android update sdk --filter sys-img-armeabi-v7a-android-16 --no-ui -a
    ```
**3. Let's prepare DroidBox**
- Now we can start with DroidBox. First, you have to download this repo and the last release of the original DroidBox repo in order to copy the system and RAM images:
   ```sh
    $ cd
    $ git clone https://github.com/alexMyG/DroidBox-AndroPyTool
    $ wget https://github.com/pjlantz/droidbox/releases/download/v4.1.1/DroidBox411RC.tar.gz
    $ tar -zxvf DroidBox411RC.tar.gz
    $ cp -r DroidBox_4.1.1/images DroidBox_AndroPyTool/images
    ``` 
- We need to create the device (select **no** when asking if you wish a custom hardware profile):
    ```sh
    $ cd DroidBox-AndroPyTool/
    $ ./createDroidBoxDevice.sh
    ```
- Scripts need the correct permissions:
    ```
    $ chmod 744 *.sh
    ```
- This repo requires several Python libraries. We recommend you to use a Virtual Environment. If you do not want, go to next step:
    Install `virtualenv`:
    ```sh
    $ pip install virtualenv
    ```
    Create virtual environment and activate it:
    ```sh
    $ virtualenv droidbox_env
    $ source droidbox_env/bin/activate
    ```
- The following Python libraries are required:
    ```sh
    $ pip install -r requirements.txt
    ```
**4. Now we can run DroidBox**
- If everything was OK, we can now run DroidBox:
    ```sh
    python fork_droidbox.py <PATH_TO_FOLDER_WITH_APKS> <TIME_IN_SECONDS> <GUI_MODE:_False_or_True>
    ```
    For instance, this is the call to analyse all apks located in `/home/alex/my_apks/` during 300 seconds in the Non-GUI mode:
    ```sh
    python fork_droidbox.py /home/alex/my_apks/ 300 False
    ```
    

