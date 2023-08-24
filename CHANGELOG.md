# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased][unreleased]

...

## [0.1.4]: Django 4 Compatibility Update

### Fixed

- Update cms_plugins.py for Django 4 compatibility (#1)

## [0.1.3]: Support Link Plugins and Image Link Attributes, Fix Link Title

### Added

- feat: render link attributes (84bcd50, 9bcb527)
- feat: support link plugins (a63db81, 7d83490)

### Fixed

- fix: tacc-wbomar and wesleyboar to TACC (0b3d4b7)
- fix: remove space from title tag (73c50f5)
- fix: target _blank if no target (883ca90)
- fix: render image alt as link title (5bbf811)

## [0.1.2]: Do Not Expect TACC/Core-Styles to be a Source of Extra CSS

### Fixed

- fix: do not expect nor use Core-Styles (94db635)
- fix: do not expect nor use s-image-grid (73cfcc9)

## [0.1.1]: Support Django 2 (for TACC/Core-CMS >3.10)

### Fixed

- fix: support Django 2.2.27 (186f7bf)

## [0.1.0]: Working Prototype

v0.1.0 Initial test release

[unreleased]: https://github.com/TACC/Core-CMS-Plugin-Image-Gallery/compare/v0.1.4...HEAD
[0.1.4]: https://github.com/TACC/Core-CMS-Plugin-Image-Gallery/releases/tag/v0.1.4
[0.1.3]: https://github.com/TACC/Core-CMS-Plugin-Image-Gallery/releases/tag/v0.1.3
[0.1.2]: https://github.com/TACC/Core-CMS-Plugin-Image-Gallery/releases/tag/v0.1.2
[0.1.1]: https://github.com/TACC/Core-CMS-Plugin-Image-Gallery/releases/tag/v0.1.1
[0.1.0]: https://github.com/TACC/Core-CMS-Plugin-Image-Gallery/releases/tag/v0.1.0
