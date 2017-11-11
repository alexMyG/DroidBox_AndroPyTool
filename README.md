
Instalar SDK
######################################################
https://gist.github.com/rikyperdana/61b1a5008b757da35a745185bfed7374

# download android sdk
wget http://dl.google.com/android/android-sdk_r24.2-linux.tgz
tar -xvf android-sdk_r24.2-linux.tgz

# install all sdk packages
cd android-sdk-linux/tools
./android update sdk --no-ui


# set android-sdk path
nano ~/.bashrc
nano ~/.zshrc

# add these lines on top, save, and exit
export PATH=${PATH}:~/android-sdk-linux/tools
export PATH=${PATH}:~/android-sdk-linux/platform-tools


######################################################

Vincular con export... (ver droidbox github)
export PATH=$PATH:/home/shared-ciberdine/android-sdk-linux/tools/
export PATH=$PATH:/home/shared-ciberdine/android-sdk-linux/platform-tools
to zshrc or to bashrc

requirements, virtualenv

# Linea no necesaria, sirve para buscar lo de abajo
android list sdk --extended --no-ui --all |grep android-16

echo "y" | android update sdk -a --no-ui --filter sys-img-armeabi-v7a-android-16

./createDroidBoxDevice.sh


kill:
https://stackoverflow.com/questions/20155376/android-stop-emulator-from-command-line
# DroidBox-AndroPyTool
