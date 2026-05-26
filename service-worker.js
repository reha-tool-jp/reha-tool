const CACHE_NAME = 'reha-tool-v2';
const ASSETS = [
  '/reha-tool/',
  '/reha-tool/index.html',
  '/reha-tool/fim-tool.html',
  '/reha-tool/bi-tool.html',
  '/reha-tool/walk-tool.html',
  '/reha-tool/hdsr-tool.html',
  '/reha-tool/santei-tool.html',
  '/reha-tool/balance-tool.html',
  '/reha-tool/privacy.html',
  '/reha-tool/manifest.json',
];

// インストール時にキャッシュ
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

// 古いキャッシュを削除
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// ネットワーク優先・失敗時はキャッシュから返す
self.addEventListener('fetch', event => {
  // articlesディレクトリ以下はキャッシュに保存せず、常にネットワークから取得する
  if (event.request.url.includes('/articles/')) {
    event.respondWith(fetch(event.request));
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then(response => {
        // レスポンスが正常な場合のみキャッシュを更新
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() => caches.match(event.request))
  );
});
