
With this package you can add projects to your buildout for cross-compiling android packages

You will need a copy of the android sdk and ndks for your project environments

These can be installed using bit.recipe.android_sdk and bit.recipe.android_ndk

A complete buildout example might be:

[buildout]
parts = my_android_sdk
      my_android_ndk
      my_kivy

[my_android_sdk]
recipe = bit.recipe.android_sdk
apis = 8
sdk = http://dl.google.com/android/android-sdk_r14-linux.tgz

[my_android_ndk]
recipe = bit.recipe.android_ndk
version = r7
ndk = http://dl.google.com/android/ndk/android-ndk-r7-linux-x86.tar.bz2

[my_kivy]
recipe = bit.recipe.python_for_android
package = org.bitfoundation.my_kivy
src = git@github.com:kivy/python-for-android
sdk = parts/android_sdk
ndk = parts/android_ndk
ndk_version = r7
api = 8
recipes = kivy
version = 0.0.1
public = var/my_kivy/public
private = var/my_kivy/private
orientation = portrait
permissions = INTERNET


This could then be installed as follows

./bin/buildout
./bin/my_android_sdk install
./bin/my_android_ndk install
./bin/my_kivy install


Once you have done this you can create your distribution

./bin/my_kivy dist


And build and install your android package

./bin/my_kivy build debug installd

