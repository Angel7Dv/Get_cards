
https://cloudbytes.dev/snippets/run-selenium-and-chrome-on-wsl2

```
$ sudo apt update && sudo apt upgrade -y
```


Step 2: Install latest Chrome for Linux
Chrome is not available in Ubuntu's official APT repository, so we will download the .deb directly from Google and install it.

a) Download the latest chrome .deb file

```
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

b) Install the .deb file

```
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
```


c) And finally, force install all the dependencies by running

sudo apt --fix-broken install


This feels a hackish way of installing the latest version of Chrome, but if someone figures out a better way, do let me know please.

d) Get the latest version of Chrome

google-chrome-stable --version