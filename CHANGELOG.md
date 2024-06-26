# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### :warning: Changes for Developers/Package Distributors

> **Note**
> This change applies only to developers and package distributors

-   The 'bitmaps' directory has been removed from the git repository. You can now generate the PNG files using `yarn render` or download them from the release assets.

-   The `build.toml` file has been removed. Instead, the cursor build configurations are now distributed according to platforms within the `configs` directory:
    -   `configs/x.build.toml`: Used to build XCursor.
    -   `configs/win_rg.build.toml`: Used to build regular size Windows cursors.
    -   `configs/win_lg.build.toml`: Used to build large size Windows cursors.
    -   `configs/win_xxl.build.toml`: Used to build extra large size Windows cursors.

### What's New?

-   Fuchsia Amber #11
-   Support `256px` cursors
-   feat: Added `Person` and `Pin` cursors for Windows
-   Official Distributing `16` and `20` XCursors
-   Multi Resolution Windows Cursors
-   Attach version meta-data inside cursor packages
-   Using [cbmp v1.1.1](https://github.com/ful1e5/cbmp/tree/v1.1.1) for rendering cursor bitmaps.

### Changes

-   build script renamed (`release.sh` -> `build.sh`)
-   Use 'xz' for better compression in `build.sh` script
-   De-framed animated cursors to static SVG files

## [v2.0.0] - 21 October 2022

### Added

-   README.md: Human readable docs
-   uninstall docs added ful1e5/apple_cursor#79 ful1e5/apple_cursor#80
-   Add cursor top_left_arrow ful1e5/BreezeX_Cursor#10 ful1e5/BreezeX_Cursor#11
-   LICENSE: GNU General Public License v3

### Changed

-   refactor: build cursor with [clickgen v2](https://github.com/ful1e5/clickgen)
-   refactor: bitmapper moved to individual project [cbmp](https://github.com/ful1e5/cbmp)

## [v1.0.5] - 09 December 2021

### Added

-   Init Fuchsia-Red

### Changed

-   `build` workflow updated for `Fuchsia-Red` variant
-   Links updated inside all docs
-   Sponsorships updated

## [v1.0.4] - 14 November 2021

### Added

-   windows animated cursor's delay updated ( repatched #4 )
-   pling product's docs inside `pling` directory
-   distributed binaries inside `bin` directory
-   use `THEME_PREFIX` variable inside `make` commands

### Changed

-   bitmaps artifacts fixed in CI
-   minimal README.md (removed badges and emojis)
-   documented logs inside bitmapping
-   Typo fixed inside preview

## [v1.0.3] - 05 August 2021

### Changed

-   `busy` and `work` animation fixed on windows side #4

## [v1.0.2] - 07 July 2021

### Added

-   `make prepare` command for preparing Fuchsia binaries
-   [pyright](https://github.com/microsoft/pyright/blob/main/docs/configuration.md) configuration init
-   Fuchsia-Pop! (based on popOS color)

### Changed

-   `Makefile` and `builder/Makefile` build targets now supports `THEMES` variable
-   Import `src` module directly inside `build.py`
-   Builder code moved to `src`
-   Compact code inside `builder/*`
-   Removed **clean** target from `builder/Makefile`
-   Fuchsia cursor color changed to `#e11c79` from `#ff00ff`

## [v1.0.1] - 29 June 2021

### Added

-   compress binaries by `make release`

### Changed

-   `hand2` cursor dot size decreased
-   Figma file link updated

## [v1.0.0] - 27 June 2021

### Added

-   CI/CD Pipelines
-   Logo and badges
-   Initial release 🎊

[unreleased]: https://github.com/ful1e5/fuchsia-cursor/compare/v2.0.0...main
[v2.0.0]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.5...v2.0.0
[v1.0.5]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.4...v1.0.5
[v1.0.4]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.3...v1.0.4
[v1.0.3]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.2...v1.0.3
[v1.0.2]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.1...v1.0.2
[v1.0.1]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.0...v1.0.1
[v1.0.0]: https://github.com/ful1e5/fuchsia-cursor/tree/v1.0.0
