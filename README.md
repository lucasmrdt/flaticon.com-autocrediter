# flaticon.com autocrediter

## Description
Avoid many cut/paste to credit author when your are downloading icons on flaticon.com.

## How does it works ?
+ CLIENT :
> Javascript sends a fetch request to **localhost** with author's information when user click on **DOWNLOAD**.

+ SERVER :
> Python runs web server to catch author's information and save it in **credited_authors.json** file.


## Prerequisites
+ [pip](https://pypi.org/project/pip/)

## Install
+ SERVER :
```
git clone https://github.com/lucasmrdt/flaticon.com-autocrediter.git
cd flaticon.com-autocrediter
pip install --user -r requirements.txt
```

+ CLIENT :
  * Install an Javascript injector [chrome](https://chrome.google.com/webstore/detail/custom-javascript-for-web/poakhlngfciodnhlhhgnaaelnpjljija?hl=en).
  * Go on [flaticon.com](https://www.flaticon.com/).
  * Open your Javascript Injector.
  * Enable **JQUERY**.
  * Cut and paste source code from **client/autocrediter-extension.js** on your Javascript Injector.
  * **Save it**.

## Run
+ SERVER :
```
python3 src/server/autocrediter-server.py
```

+ CLIENT :
  * Go on [flaticon.com](https://www.flaticon.com/).
  * Select any icon and click on **Download**.
