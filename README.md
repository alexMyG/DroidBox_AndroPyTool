# DroidBox-AndroPyTool

This is a fork of the [DroidBox](https://github.com/pjlantz/droidbox) tool to be used in the [AndroPyTool](https://github.com/AIDA-UAM/AndroPyTool) (coming soon!). It includes new features:
  - Performance improved
  - Possibility of running in Non-GUI mode (ideal for servers)
  - Low level processes monitoring using **Strace**

### How to install

**0. Requirements**
- Python 2.7.*, python-tk and python-dev
- Java 8

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
 
- Let's install Android 16, which is the version supported by DroidBox (the platform and system image):

    ```sh
    $ echo "y" | android update sdk -a --no-ui --filter android-16
    $ echo "y" | android update sdk -a --no-ui --filter sys-img-armeabi-v7a-android-16
    $ echo "y" | android update sdk -a --no-ui --filter platform-tools,tools
    ```

- Now we can start with DroidBox. First, you have to download this repo:
   ```sh
    $ cd
    $ git clone https://github.com/alexMyG/DroidBox-AndroPyTool
    ``` 
 
- We need to create the device (select **no** when asking if you wish a custom hardware profile):
    ```sh
    $ cd DroidBox-AndroPyTool/
    $ ./createDroidBoxDevice.sh
    ```
- Scripts need the correct permissions:
    ````
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

- If everything was OK, we can now run DroidBox:
    ```sh
    python fork_droidbox.py <PATH_TO_FOLDER_WITH_APKS> <TIME_IN_SECONDS> <GUI_MODE:_False_or_True>
    ```
    For instance, this is the call to analyse all apks located in `/home/alex/my_apks/` during 300 seconds in the Non-GUI mode:
    ```sh
    python fork_droidbox.py /home/alex/my_apks/ 300 False
    ```
    

