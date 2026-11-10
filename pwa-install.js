/* ホーム画面に追加する案内（FIM・総合実施計画書で使用）
   - ページを開いただけでは出さない。ツールを使ったあとに window.pwaInstallOffer(直前に置く要素) を呼ぶと、その要素の下に1行で出す
   - 起動済み（アプリとして開いている）ときは案内を出さず、利用だけ計測する
   - Android/PCのChrome：「追加」ボタン／iPhone・iPad：手順の文章
   - ×で閉じると30日間は出さない */
(function () {
  function track(name, params) {
    try { if (typeof gtag === 'function') gtag('event', name, Object.assign({ page: location.pathname }, params || {})); } catch (e) {}
  }
  var DAYS = 30, KEY = 'pwaBannerClosedAt';
  var standalone = (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || window.navigator.standalone === true;

  if (standalone) {
    try {
      if (!sessionStorage.getItem('pwaOpenTracked')) { sessionStorage.setItem('pwaOpenTracked', '1'); track('pwa_standalone_open'); }
    } catch (e) { track('pwa_standalone_open'); }
    return;
  }

  function closedRecently() {
    try { var t = +localStorage.getItem(KEY); return t && (Date.now() - t) < DAYS * 86400000; } catch (e) { return false; }
  }
  if (closedRecently()) return;

  var ua = navigator.userAgent || '';
  var isIOS = /iPhone|iPad|iPod/.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1);
  var deferred = null, shown = false, wantAnchor = null;

  function render() {
    if (shown || !wantAnchor || !document.body) return;
    if (!deferred && !isIOS) return;
    shown = true;

    var st = document.createElement('style');
    st.textContent =
      '.pwa-banner{display:flex;align-items:center;gap:8px;margin:12px 0 0;padding:8px 12px;background:var(--surface,#fff);border:1px solid var(--border,#d8d5ce);border-left:4px solid var(--primary,#1F5C55);border-radius:10px;font-size:13px;line-height:1.6;color:var(--text,#1c1c1e)}' +
      '.pwa-banner .pwa-text{flex:1 1 auto;min-width:0}.pwa-banner .pwa-add,.pwa-banner .pwa-close{flex:0 0 auto}.pwa-banner .pwa-add{white-space:nowrap}' +
      '.pwa-banner button{font:inherit;cursor:pointer}' +
      '.pwa-banner .pwa-add{background:var(--primary,#1F5C55);color:#fff;border:none;border-radius:8px;padding:6px 14px;font-weight:700}' +
      '.pwa-banner .pwa-close{background:none;border:none;color:var(--muted,#6e6e73);font-size:18px;line-height:1;padding:2px 6px}' +
      '@media print{.pwa-banner{display:none!important}}';
    document.head.appendChild(st);

    var el = document.createElement('div');
    el.className = 'pwa-banner no-print';
    el.setAttribute('role', 'region');
    el.setAttribute('aria-label', 'ホーム画面に追加');
    var msg = deferred
      ? '<span class="pwa-text">📱 次も使うなら、ホーム画面に追加すると、すぐ開けます。</span><button type="button" class="pwa-add">追加する</button>'
      : '<span class="pwa-text">📱 次も使うなら、Safariの共有ボタン（□↑）→「ホーム画面に追加」で、すぐ開けます。</span>';
    el.innerHTML = msg + '<button type="button" class="pwa-close" aria-label="閉じる">×</button>';
    wantAnchor.parentNode.insertBefore(el, wantAnchor.nextSibling);
    track('pwa_banner_show', { platform: deferred ? 'chrome' : 'ios' });

    var add = el.querySelector('.pwa-add');
    if (add) add.addEventListener('click', function () {
      track('pwa_install_click');
      if (!deferred) return;
      deferred.prompt();
      deferred.userChoice.then(function (c) {
        track(c && c.outcome === 'accepted' ? 'pwa_install_accepted' : 'pwa_install_dismissed');
        deferred = null; el.remove();
      }).catch(function () {});
    });
    el.querySelector('.pwa-close').addEventListener('click', function () {
      track('pwa_banner_close');
      try { localStorage.setItem(KEY, String(Date.now())); } catch (e) {}
      el.remove();
    });
  }

  window.addEventListener('beforeinstallprompt', function (e) {
    e.preventDefault(); deferred = e;
    render();
  });
  window.addEventListener('appinstalled', function () { track('pwa_installed'); });
  // ツールを使ったあとにページ側から呼ぶ（何度呼んでも、出すのは1回だけ）
  window.pwaInstallOffer = function (anchor) {
    if (shown || !anchor) return;
    wantAnchor = anchor;
    render();
  };
})();
