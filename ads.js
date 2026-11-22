/* 広告タグの共通ファイル（2026-11-22）
 * 使い方：ページの広告枠に <script>rehaAd(PC用の広告会社, スマホ用の広告会社, 位置);</script> と書く。
 *   広告会社：'admax'（忍者AdMax）／'adstir'／'imobile'／null（何も出さない）
 *   位置：'mid'（記事中）／'end'（記事末尾）
 *   幅900px以上はPC用、それ未満はスマホ用のタグを使う。
 * 広告の入れ替え方針：スマホは3つの位置（記事中・末尾の上・末尾の下）に3社を、PCはAdMaxとAdStirの2社を、
 *   ページごとに入れ替えて置く。i-mobileのPC枠は、課金対象が出ない間は使わない（pc側にnullを指定）。
 * このファイルは、広告を置くページより前で、同期的に読み込む（defer・asyncは付けない）。
 */
(function () {
  // 印刷時は広告を隠す（広告ブロックには class="ad-no-print" を付ける）
  try {
    var st = document.createElement('style');
    st.textContent = '@media print{.ad-no-print{display:none!important}}';
    document.head.appendChild(st);
  } catch (e) {}

  var isPc = !!(window.matchMedia && window.matchMedia('(min-width: 900px)').matches);

  var ADMAX = {
    pcMid: 'a744071ba10526f6f08808ab8d2c6db5',
    spMid: '512dfa58e797dd0773a44f74567a7f2c',
    pcEnd: '7979f3abb149cdd6510d2ff42a1c26f1',
    spEnd: '2b8fba0e703f3e0e28eab6a340b4324b'
  };
  var ADSTIR = {
    pcMid: { app: 'MEDIA-b9c2b2b4', spot: 3 },
    pcEnd: { app: 'MEDIA-b9c2b2b4', spot: 2 },
    spMid: { app: 'MEDIA-af55c103', spot: 2 },
    spEnd: { app: 'MEDIA-af55c103', spot: 1 }
  };
  var IMOBILE = {
    pcMid: { id: 'im-7f13897f93704ba99d40b648e9fd4103', mid: 597415, asid: 1951724 },
    spMid: { id: 'im-ac148f21d5d248f08ebcfd468cea00dc', mid: 597416, asid: 1951725 },
    pcEnd: { id: 'im-33da1cebb763412a9befcaff69d7e630', mid: 597415, asid: 1951720 },
    spEnd: { id: 'im-cc6a8c3d983f4df2b0e9ee6bc576cb10', mid: 597416, asid: 1949900 }
  };

  window.rehaAd = function (pcVendor, spVendor, pos) {
    var vendor = isPc ? pcVendor : spVendor;
    if (!vendor) return;
    var key = (isPc ? 'pc' : 'sp') + (pos === 'end' ? 'End' : 'Mid');
    var html = '';
    if (vendor === 'admax') {
      html = '<scr' + 'ipt src="https://adm.shinobi.jp/s/' + ADMAX[key] + '"></scr' + 'ipt>';
    } else if (vendor === 'adstir') {
      var a = ADSTIR[key];
      html = '<scr' + 'ipt type="text/javascript">var adstir_vars = { ver: "4.0", app_id: "' + a.app + '", ad_spot: ' + a.spot + ', center: false };</scr' + 'ipt>'
        + '<scr' + 'ipt type="text/javascript" src="https://js.ad-stir.com/js/adstir.js"></scr' + 'ipt>';
    } else if (vendor === 'imobile') {
      var m = IMOBILE[key];
      html = '<div id="' + m.id + '">'
        + '<scr' + 'ipt async src="https://imp-adedge.i-mobile.co.jp/script/v1/spot.js?20220104"></scr' + 'ipt>'
        + '<scr' + 'ipt>(window.adsbyimobile=window.adsbyimobile||[]).push({pid:85604,mid:' + m.mid + ',asid:' + m.asid + ',type:"banner",display:"inline",elementid:"' + m.id + '"})</scr' + 'ipt>'
        + '</div>';
    } else {
      return;
    }
    document.write('<div style="min-width:300px;min-height:250px;">' + html + '</div>');
  };
})();
