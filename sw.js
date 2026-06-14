const CACHE_NAME = 'ester-app-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/login.html',
  '/rotina.html',
  '/resumo.html',
  '/portage.html',
  '/spm.html',
  '/icon-512.png',
  '/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        // Usar addAll é mais simples, mas se falhar em 1, falha tudo.
        // Como todos os arquivos existem, deve funcionar.
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  // Estratégia "Stale-While-Revalidate" para assets e "Network First" para APIs (se houver, mas a API é do Supabase)
  // Como o Supabase usa POST/GET com params na url, vamos ignorar requisições para supabase.co
  if (event.request.url.includes('supabase.co')) {
      return; // Deixa passar pra rede normalmente
  }

  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Cache hit - return response
        if (response) {
            // Pode fazer o fetch em background para atualizar o cache
            fetch(event.request).then(res => {
                if(!res || res.status !== 200 || res.type !== 'basic') return;
                const responseToCache = res.clone();
                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, responseToCache);
                });
            }).catch(e => console.log("Offline, usando cache stale."));

            return response;
        }

        // Não tem no cache, busca na rede
        return fetch(event.request).then(
          function(response) {
            // Verifica se a requisição foi bem sucedida
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            // Clona a requisição porque é um stream que só pode ser consumido uma vez
            var responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });

            return response;
          }
        );
      })
  );
});

self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
