# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Added

- Init Fuchsia-Red

### Changed

- sponsorships updated

## [v1.0.4] - 14 Nov 2021

### Added

- use `THEME_PREFIX` variable inside `make` commands
- distributed binaries inside `bin` directory
- pling product's docs inside `pling` directory
- windows animated cursor's delay updated ( repatched #4 )

### Changed

- Typo fixed inside preview
- documented logs inside bitmapping
- minimal README.md (removed badges and emojis)
- bitmaps artifacts fixed in CI

## [v1.0.3] - 05 Aug 2021

### Changed

- `busy` and `work` animation fixed on windows side #4

## [v1.0.2] - 07 Jul 2021

### Added

- Fuchsia-Pop! (based on popOS color)
- [pyright](https://github.com/microsoft/pyright/blob/main/docs/configuration.md) configuration init
- `make prepare` command for preparing Fuchsia binaries

### Changed

- Fuchsia cursor color changed to `#e11c79` from `#ff00ff`
- Removed **clean** target from `builder/Makefile`
- Compact code inside `builder/*`
- Builder code moved to `src`
- Import `src` module directly inside `build.py`
- `Makefile` and `builder/Makefile` build targets now supports `THEMES` variable

## [v1.0.1] - 29 Jun 2021

### Added

- compress binaries by `make release`

### Changed

- Figma file link updated
- `hand2` cursor dot size decreased

## [v1.0.0] - 27 Jun 2021

### Added

- Initial release 🎊
- Logo and badges
- CI/CD Pipelines

[unreleased]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.4...main
[v1.0.4]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.3...v1.0.4
[v1.0.3]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.2...v1.0.3
[v1.0.2]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.1...v1.0.2
[v1.0.1]: https://github.com/ful1e5/fuchsia-cursor/compare/v1.0.0...v1.0.1
[v1.0.0]: https://github.com/ful1e5/fuchsia-cursor/tree/v1.0.0
