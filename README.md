# Fuchsia Cursor

First OpenSource port of [FuchsiaOS](https://fuchsia.dev/)'s cursors for **Linux** and **Windows**.

[![build](https://github.com/ful1e5/fuchsia-cursor/actions/workflows/build.yml/badge.svg)](https://github.com/ful1e5/fuchsia-cursor/actions)
[![CodeFactor](https://www.codefactor.io/repository/github/ful1e5/fuchsia-cursor/badge)](https://www.codefactor.io/repository/github/ful1e5/fuchsia-cursor)
[![Twitter](https://img.shields.io/badge/twitter-ful1e5-blue)](https://twitter.com/ful1e5)

#### Cursor Sizes

<kbd>22</kbd>
<kbd>24</kbd>
<kbd>28</kbd>
<kbd>32</kbd>
<kbd>40</kbd>
<kbd>48</kbd>
<kbd>56</kbd>
<kbd>64</kbd>
<kbd>72</kbd>
<kbd>80</kbd>
<kbd>88</kbd>
<kbd>96</kbd>

#### Quick install

- Fuchsia:[https://www.pling.com/p/1544830](https://www.pling.com/p/1544830)
- Fuchsia-Pop!:[https://www.pling.com/p/1641968](https://www.pling.com/p/1641968)
- Fuchsia-Red:[https://www.pling.com/p/1660999](https://www.pling.com/p/1660999)

### Manual Install

#### Linux/X11

```bash
# extract `Fuchsia.tar.gz`
tar -xvf Fuchsia.tar.gz

# For local users
mv Fuchsia ~/.icons/

# For all users
sudo mv Fuchsia /usr/share/icons/
```

#### Windows

1. unzip `.zip` file
2. Open `unziped` directory in Explorer, and **right click** on `install.inf`.
3. Click 'Install' from the context menu, and authorize the modifications to your system.
4. Open _Control Panel > Personalization and Appearance > Change mouse pointers_, and select **Fuchsia Cursors**.
5. Click '**Apply**'.

#### Preview:

> Check Figma file [here](https://www.figma.com/file/jPmS71GFhBN4NUTZx4VHbg/Fuchsia-Cursor?node-id=0%3A1)

<p align="center">
  <img title="Fuchsia" src="https://imgur.com/2MwCf35.png">
  </br>
  <sub>Fuchsia Cursors</sub>
</p>

<p align="center">
  <img title="Fuchsia Pop!" src="https://imgur.com/h9UYn37.png">
  </br>
  <sub>Fuchsia Pop! Cursors</sub>
</p>

<p align="center">
  <img title="Fuchsia Red" src="https://imgur.com/oheg7Wl.png">
  </br>
  <sub>Fuchsia Red Cursors</sub>
</p>

# Dependencies

## External Libraries

- libxcursor
- libx11
- libpng (<=1.6)

#### Install External Libraries

##### macOS

```bash
brew install --cask xquartz
brew install libpng
```

##### Debain/ubuntu

```bash
sudo apt install libx11-dev libxcursor-dev libpng-dev
```

##### ArchLinux/Manjaro

```bash
sudo pacman -S libx11 libxcursor libpng
```

##### Fedora/Fedora Silverblue/CentOS/RHEL

```bash
sudo dnf install libX11-devel libXcursor-devel libpng-devel
```

## Build Dependencies

- [gcc](https://gcc.gnu.org/install/)
- [make](https://www.gnu.org/software/make/)
- [nodejs](https://nodejs.org/en/) (<=12.x.x)
- [yarn](https://classic.yarnpkg.com/en/docs/install/)
- [python](https://www.python.org/downloads/) (<=3.8)
- [pip3](https://pip.pypa.io/en/stable/installing/)

### Node Packages

- [puppeteer](https://www.npmjs.com/package/puppeteer)
- [pngjs](https://www.npmjs.com/package/pngjs)
- [pixelmatch](https://www.npmjs.com/package/pixelmatch)

### PyPi Packages

- [clickgen](https://pypi.org/project/clickgen/s)

## Build From Scratch

### Auto Build (using GitHub Actions)

GitHub Actions is automatically runs on every `push`(on **main** and **dev** branches) and `pull request`(on **main** branch), You found theme resources in `artifact` section of **build**.GitHub **Actions** source is available inside [.github/workflows](https://github.com/ful1e5/fuchsia-cursor/tree/main/.github/workflows) directory.

### Manual Build

```bash
make
```

#### Build `XCursor` theme

```bash
make unix
```

#### Customize `XCursor` size

```bash
make unix X_SIZES=22            # Only built '22px' pixel-size.
make unix X_SIZES=22 24 32      # Multiple sizes are provided with  ' '(Space)
```

#### Install `XCursor` theme

```bash
make install            # install as user
  # OR
sudo make install       # install as root
```

#### Build `Windows` theme

```bash
make windows
```

#### Customize `Windows Cursor` size

```bash
make windows WIN_SIZE=96            # Provide only one pixel-size
```

> For installation follow [these](#windows) steps.

# Bugs

Bugs should be reported [here](https://github.com/ful1e5/fuchsia-cursor/issues) on the Github issues page.

# Getting Help

You can create a **issue**, I will help you. 🙂

# Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md), any suggestions for features and contributions to the continuing code masterelopment can be made via the issue tracker or code contributions via a `Fork` & `Pull requests`.
