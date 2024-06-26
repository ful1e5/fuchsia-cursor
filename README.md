![Fuchsia](https://github.com/ful1e5/fuchsia-cursor/assets/24286590/68223b08-7020-4cb6-8d97-090bacef62d6)

First open source port of [FuchsiaOS](https://fuchsia.dev/)'s cursors for **Linux** and **Windows**.

[![build](https://github.com/ful1e5/fuchsia-cursor/actions/workflows/build.yml/badge.svg)](https://github.com/ful1e5/fuchsia-cursor/actions)

## Notes

-   All cursor's SVG files are found in [svg](./svg) directory or you can also find them on [Figma](https://www.figma.com/design/jPmS71GFhBN4NUTZx4VHbg/Fuchsia-Cursor?node-id=0-1&t=QIgHaHw4N75yeUkU-1).

<!-- If you're interested, you can learn more about "sponsor-spotlight" on
 https://dev.to/ful1e5/lets-give-recognition-to-those-supporting-our-work-on-github-sponsors-b00 -->

![shoutout-sponsors](https://sponsor-spotlight.vercel.app/sponsor?login=ful1e5)

-   **2024-04-26**: [f3ca511](https://github.com/ful1e5/fuchsia-cursor/commit/f3ca5116adc9c428e56e248758d11d8d8cfaf682) Partitioned cursor build configuration into multiple files according to platform:
    `build.toml` -> `configs/win_lg.build.toml`, `configs/win_rg.build.toml`, `configs/win_xl.build.toml`, `configs/x.build.toml`.

---

![Fuchsia](https://github.com/ful1e5/fuchsia-cursor/assets/24286590/11dc68d3-fc78-4481-a829-2d05add9833a)
![Fuchsia-Amber](https://github.com/ful1e5/fuchsia-cursor/assets/24286590/49213cb0-be9d-4159-8929-0fd5fcd8aee4)
![Fuchsia-Red](https://github.com/ful1e5/fuchsia-cursor/assets/24286590/9d0b8668-6a0d-4176-a64c-1f7982926425)
![Fuchsia-Pop!](https://github.com/ful1e5/fuchsia-cursor/assets/24286590/f53f5edd-67f3-4d56-97f3-bb80677a277a)

## Cursor Sizes

### Xcursor Sizes:

<kbd>16</kbd>
<kbd>20</kbd>
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

### Windows Cursor Size:

| size | Regular (× ²⁄₃) | Large (× ⁴⁄₅) | Extra-Large (× 1) |
| ---: | --------------: | ------------: | ----------------: |
|   32 |     21.333 → 22 |     25.6 → 26 |                32 |
|   48 |              32 |     38.4 → 39 |                48 |
|   64 |     42.666 → 43 |     51.2 → 52 |                64 |
|   96 |              64 |     76.8 → 77 |                96 |
|  128 |     85.333 → 86 |   102.4 → 103 |               128 |

## Colors

### Fuchsia

-   Outline Color - `#FFFFFF` (White)
-   Base Color - `#E11C79` (Fuchsia)

### Fuchsia Amber

-   Outline Color - `#FFFFFF` (White)
-   Base Color - `#FFA400` (Amber)

### Fuchsia Red

-   Outline Color - `#FFFFFF` (White)
-   Base Color - `#FF0000` (Red)

### Fuchsia Pop!

-   Outline Color - `#FFFFFF` (White)
-   Base Color - `#F8B572` (PopOS Orange)

## How to get it

### Easiest Way

You can download latest `stable` & `development` releases from
[Release Page](https://github.com/ful1e5/fuchsia-cursor/releases).

## Installing Fuchsia Cursor

#### Linux/X11

**Installation:**

```bash
tar -xvf Fuchsia.tar.gz                   # extract `Fuchsia.tar.gz`
mv Fuchsia ~/.icons/                      # Install to local users
sudo mv Fuchsia /usr/share/icons/         # Install to all users
```

**Uninstallation:**

```bash
rm ~/.icons/Fuchsia                       # Remove from local users
sudo rm /usr/share/icons/Fuchsia          # Remove from all users
```

#### Windows

**Installation:**

1. Unzip `.zip` file
2. Open unziped directory in Explorer, and **right click** on `install.inf`.
3. Click 'Install' from the context menu, and authorize the modifications to your system.
4. Open Control Panel > Personalization and Appearance > Change mouse pointers,
   and select **Fuchsia Cursors**.
5. Click '**Apply**'.

**Uninstallation:**

Run the `uninstall.bat` script packed with the `.zip` archive

**OR** follow these steps:

1. Go to **Registry Editor** by typing the same in the _start search box_.
2. Expand `HKEY_CURRENT_USER` folder and expand `Control Panel` folder.
3. Go to `Cursors` folder and click on `Schemes` folder - all the available custom cursors that are
   installed will be listed here.
4. **Right Click** on the name of cursor file you want to uninstall; for eg.: _Fuchsia Cursors_ and
   click `Delete`.
5. Click '**yes**' when prompted.

## Build From Source

### Prerequisites

-   Python version 3.7 or higher
-   [clickgen](https://github.com/ful1e5/clickgen)>=2.2.5 (`pip install clickgen`)
-   [yarn](https://github.com/yarnpkg/yarn)

### Quick start

1. Install [build prerequisites](#prerequisites) on your system
2. `git clone https://github.com/ful1e5/fuchsia-cursor`
3. `cd fuchsia-cursor`
4. `yarn install`
5. `yarn generate`
6. See [Installing Fuchsia Cursor](#installing-fuchsia-cursor).

### Getting Started

Once you have the [build prerequisites](#prerequisites) installed, You can personalize colors,
customize sizes, change target platforms, and more. This process involves using external tools,
as this repository only contains SVG files and configuration for these tools:

-   [cbmp](https://github.com/ful1e5/cbmp): Used for customizing colors and generating PNG files.
-   [ctgen](https://github.com/ful1e5/clickgen): Used for customizing sizes and building XCursor and Windows Cursors.

You can refer to the README of each tool for more information on their command-line options.

#### Crafting Your Fuchsia Cursor

The process of creating custom cursor themes involves two main steps:

1. Rendering SVG files to PNG files.
2. Building cursor themes from PNG files.

#### Customize Colors

`cbmp` provides three options for changing colors:

1. `-bc`: Base color, which replaces the `#00FF00` color in the SVG.
2. `-oc`: Outlined color, which replaces the `#0000FF` color in the SVG.
3. `-wc` (optional): Watch Background color, which replaces the `#FF0000` color in the SVG.

```bash
npx cbmp [...] -bc '<hex>' -oc '<hex>' -wc '<hex>'
```

Alternatively, you can provide a JSON configuration file to render SVG files, which contains a sequence of `cbmp` commands:

```bash
npx cbmp render.json
```

#### Customize Sizes

##### Customize Windows Cursor size

To build Windows cursor with size `16`:

```bash
ctgen build.toml -s 16 -p windows -d 'bitmaps/Fuchsia' -n 'Fuchsia' -c 'First OpenSource port of FuchsiaOS Cursors with size 16'
```

You can also customize output directory with `-o` option:

```bash
ctgen build.toml -s 16 -p windows -d 'bitmaps/Fuchsia' -o 'out' -n 'Fuchsia' -c 'First OpenSource port of FuchsiaOS Cursors with size 16'
```

##### Customize XCursor size

To build XCursor with size `16`:

```bash
ctgen build.toml -s 16 -p x11 -d 'bitmaps/Fuchsia' -n 'Fuchsia' -c 'FuchsiaOS Cursors with size 16'
```

You can also assign multiple sizes to `ctgen` for XCursors build:

```bash
ctgen build.toml -s 16 18 24 32 -p x11 -d 'bitmaps/Fuchsia' -n 'Fuchsia' -c 'FuchsiaOS Cursors with size 16'
```

#### Examples

Lets generate Fuchsia Cursor with green and black colors:

```bash
npx cbmp -d 'svg' -o 'bitmaps/Fuchsia-Hacker' -bc '#00FE00' -oc '#000000'
```

After rendering custom color you have to build cursor through `ctgen`:

```bash
ctgen build.toml -d 'bitmaps/Fuchsia-Hacker' -n 'Fuchsia-Hacker' -c 'Green and Black FuchsiaOS cursors.'
```

Afterwards, Generated theme can be found in the `themes` directory.

###### Fuchsia Gruvbox

```bash
npx cbmp -d 'svg/original' -o 'bitmaps/Fuchsia-Gruvbox' -bc '#282828' -oc '#EBDBB2'
ctgen build.toml -d 'bitmaps/Fuchsia-Gruvbox' -n 'Fuchsia-Gruvbox' -c 'Groovy FuchsiaOS cursors.'
```

###### Fuchsia Solarized Dark

```bash
npx cbmp -d 'svg/original' -o 'bitmaps/Fuchsia-Solarized-Dark' -bc '#002b36' -oc '#839496'
ctgen build.toml -d 'bitmaps/Fuchsia-Solarized-Dark' -n 'Fuchsia-Solarized-Dark' -c 'Solarized Dark FuchsiaOS cursors.'
```

###### Fuchsia Solarized Light

```bash
npx cbmp -d 'svg/original' -o 'bitmaps/Fuchsia-Solarized-Light' -bc '#839496' -oc '#002b36'
ctgen build.toml -d 'bitmaps/Fuchsia-Solarized-Light' -n 'Fuchsia-Solarized-Light' -c 'Solarized Light FuchsiaOS cursors.'
```

###### Fuchsia Dracula

```bash
npx cbmp -d 'svg/original' -o 'bitmaas/Fuchsia-Dracula' -bc '#282a36' -oc '#f8f8f2'
ctgen build.toml -d 'bitmaps/Fuchsia-Dracula' -n 'Fuchsia-Dracula' -c 'Dracula FuchsiaOS cursors.'
```

## Testing Cursor

There are several websites that allow you to test your cursor states by hovering over buttons. This can be very useful when developing or verifying the behavior of a cursor. The following websites cover many of the most commonly used cursors, although they may not include all available options.

-   [Cursor-Test](https://vibhorjaiswal.github.io/Cursor-Test/)
-   [Mozilla CSS Cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor)

For a blueprint for creating XCursors, you may also want to refer to [Cursor-demo](https://wiki.tcl-lang.org/page/Cursor+demo).

## Bugs

Bugs should be reported [here](https://github.com/ful1e5/Fuchsia/issues) on the Github issues page.

## Getting Help

You can create a **issue**, I will help you.

## Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md), any suggestions for features and contributions to the continuing code masterelopment can be made via the issue tracker or code contributions via a `Fork` & `Pull requests`.
