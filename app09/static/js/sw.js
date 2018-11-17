importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.6.1/workbox-sw.js');

if (workbox) {
    console.log(`Yay! Workbox is loaded 🎉`);
} else {
    console.log(`Boo! Workbox didn't load 😬`);
}
workbox.navigationPreload.enable();

const strategy = workbox.strategies.networkFirst({
    cacheName: 'cached-navigations',
    plugins: [
      // Any plugins, like workbox.expiration, etc.
    ],
  });

// Precache entries from workbox-build or somewhere else
workbox.precaching.precache([
    {
        url: '/static/js/lazysizes.min.js',
        revision: 'abcd',
    }, {
        url: '/index.html',
        revision: 'abcd',
    }
]);

// Add Precache Route
workbox.precaching.addRoute();