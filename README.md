## Texas Advanced Computing Center
# Django CMS App: "Image Gallery"

This app creates an image gallery using images via child plugins, thrid-party scripts, and https://github.com/TACC/Core-Styles.

- __`__dist-name__`__: `djangocms-tacc-image-gallery`
- __`__package_name__`__: `djangocms_tacc_image_gallery`
- __`__ClassName__`__: `TaccsiteImageGallery`
- __"App Name"__: "Image Gallery"

## Quick Start

1. Follow https://github.com/wesleyboar/Core-CMS-App/wiki/Core-CMS-App-Usage-Quick-Start.
2. If you do not already have `django-sekizai` configured, follow just "Configuration" section of https://django-sekizai.readthedocs.io/en/latest/#configuration.

## Usage

1. Add instance of plugin to a page.
2. Within it, to supply images, add instances of Image/Picture plugins.
3. Verify plugin:
    - renders images added
    - wraps those images in links
    - the image links load an image gallery / carousel
