/* サイト内リンクのクリック計測（GA4イベント internal_link_click）
   - 同じサイト内の別ページへのリンクを押した回数を測る。記事からツールへ、のような流れを見るため
   - 送る値：link_url（行き先のパス）、from_page（今のページのパス）、area（ナビ／フッター／本文）、link_text（先頭40字）
   - 個人情報は送らない。入力欄の中身や、ページ内アンカー（#）のみのリンクは対象外 */
(function () {
  function track(params) {
    try { if (typeof gtag === 'function') gtag('event', 'internal_link_click', params); } catch (e) {}
  }
  document.addEventListener('click', function (ev) {
    try {
      var a = ev.target && ev.target.closest ? ev.target.closest('a[href]') : null;
      if (!a) return;
      var u = new URL(a.href, location.href);
      if (u.origin !== location.origin) return;
      if (u.pathname === location.pathname) return;
      var area = a.closest('nav') ? 'nav' : a.closest('footer') ? 'footer' : a.closest('header') ? 'header' : 'body';
      var text = (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40);
      track({ link_url: u.pathname, from_page: location.pathname, area: area, link_text: text });
    } catch (e) {}
  }, true);
})();
