import lightGallery from 'https://cdnjs.cloudflare.com/ajax/libs/lightgallery/2.7.1/lightgallery.es5.min.js';

/**
 * Elements that contain images for gallery
 * @type {NodeList}
 */
const galleryContainers = document.getElementsByClassName('lightgallery');

/**
 * To initialize a single gallery
 * @param [HTMLElement] gallery - The gallery container
 */
function initGallery ( gallery ) {
    lightGallery( gallery, {
        // plugins: [ lgZoom, lgThumbnail ],
        speed: 500,
        licenseKey: '0000-0000-000-0000'
        // ... other settings
    });
}

[ ...galleryContainers ].forEach( initGallery );
