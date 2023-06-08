import lightGallery from 'https://cdnjs.cloudflare.com/ajax/libs/lightgallery/2.7.1/lightgallery.es5.min.js';

/**
* Elements that contain images for gallery
* @type {NodeList}
*/
const galleryContainers = document.getElementsByClassName('lightgallery');

/**
* To wrap images in links to full size image
* @param [HTMLElement] gallery - The gallery container
*/
function wrapImagesInLinks ( gallery ) {
    const unlinkedImages = gallery.querySelectorAll('img:not(a > img)');
    const fragment = document.createDocumentFragment();

    unlinkedImages.forEach( image => {
        const anchor = document.createElement('a');
        const href = image.currentSrc;

        console.log({ image, anchor, href });

        /* To build anchor */
        anchor.href = href;
        anchor.target = '_blank';
        fragment.appendChild( anchor );

        /* To wrap image */
        image.parentNode.replaceChild( anchor, image );
        anchor.appendChild( image );
    });
}

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

[ ...galleryContainers ].forEach( container => {
    wrapImagesInLinks( container );
    initGallery( container );
});
