1) We’re going to do this in a virtual environment, so we don’t pollute the main `Python` installation:

- Change to a suitable clean directory that you can work in
- **YOU NEED TO MAKE SURE THAT THE PATH TO THIS DIRECTORY CONTAINS NO SPACES!** If the path contains spaces, `sip` will fail
- Create a new `Python` virtual environment:

```bash
virtualenv venv-test-ete3 -p python3
```

- Activate the virtual environment

```bash
source venv-test-ete3/bin/activate
```

- Install packages

```bash
pip install scipy lxml
```

2) Install Qt4 with Homebrew

- [homebrew Qt4](https://github.com/cartr/homebrew-qt4)

```bash
brew tap cartr/qt4
brew tap-pin cartr/qt4
brew install qt@4
```

3) Download and install `SIP`

- `SIP` is the set of C/C++ bindings in `Python` used by `PyQt4`.
- download the source code from [`https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.1/sip-4.19.1.tar.gz`](https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.1/sip-4.19.1.tar.gz) to the current directory

```bash
wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.1/sip-4.19.1.tar.gz
```

- extract and compile the source

```bash
tar -zxvf sip-4.19.1.tar.gz 
cd sip-4.19.1
python configure.py
make
make install
cd ..
```

4) Download and install `PyQt4`

- download the source code from [`http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12/PyQt4_gpl_mac-4.12.tar.gz`](http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12/PyQt4_gpl_mac-4.12.tar.gz) into your current directory

```bash
wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12/PyQt4_gpl_mac-4.12.tar.gz
```

- extract and compile the source (**THIS WILL FAIL WITH A SIP ERROR IF THE PATH CONTAINS SPACES**)

```bash
tar -zxvf PyQt4_gpl_mac-4.12.tar.gz
cd PyQt4_gpl_mac-4.12
python configure.py -q /usr/local/Cellar/qt/4.8.7_3/bin/qmake
make
make install
cd ..
```

5) Install `ete3`

```bash
pip install ete3
```

6) Test the installation

```bash
$ python
Python 3.6.0 (default, Dec 24 2016, 08:01:42) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from ete3 import TreeStyle
>>> 
```

If no error is thrown at this point, then `ete3` should be correctly installed.
