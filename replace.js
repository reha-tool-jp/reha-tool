const fs = require('fs');
const path = 'C:/Users/SHINSUKE/reha-tool/bi-tool.html';
let content = fs.readFileSync(path, 'utf8');

const o1 = "    @page { size: A4 portrait; margin: 12mm 12mm 12mm 12mm; }";
const n1 = "    @page { size: A4 portrait; margin: 8mm 8mm 8mm 8mm; }";
if (!content.includes(o1)) throw new Error("1");
content = content.replace(o1, n1);

const o2 = "    .info-section { display: none !important; }\r\n    .footer { display: none !important; }\r\n  }";
const n2 = "    .info-section { display: none !important; }\r\n    .footer { display: none !important; }\r\n    .no-print { display: none !important; }\r\n  }";
if (!content.includes(o2)) throw new Error("2");
content = content.replace(o2, n2);

const o3 = "<div class=\"breadcrumb\">\r\n  <a href=\"./index.html\">トップ</a>\r\n  <span>›</span>\r\n  <a href=\"./index.html#tools\">評価ツール</a>\r\n  <span>›</span>\r\n  BI(バーセルインデックス)\r\n</div>";
const n3 = "<div class=\"breadcrumb no-print\">\r\n  <a href=\"./index.html\">トップ</a>\r\n  <span>›</span>\r\n  <a href=\"./index.html#tools\">評価ツール</a>\r\n  <span>›</span>\r\n  BI(バーセルインデックス)\r\n</div>";
if (!content.includes(o3)) throw new Error("3");
content = content.replace(o3, n3);

const o4 = "  <div style=\"margin-top:40px;border-top:1px solid #e0ddd4;padding-top:32px;\">\r\n    <h2 style=\"font-size:15px;font-weight:700;color:#2a5c45;margin-bottom:10px;\">参考文献・出典</h2>";
const n4 = "  <div class=\"no-print\" style=\"margin-top:40px;border-top:1px solid #e0ddd4;padding-top:32px;\">\r\n    <h2 style=\"font-size:15px;font-weight:700;color:#2a5c45;margin-bottom:10px;\">参考文献・出典</h2>";
if (!content.includes(o4)) throw new Error("4");
content = content.replace(o4, n4);

const o51 = "  <div class=\"section-title\" style=\"margin-top: 40px;\">関連する解説記事</div>\r\n  <div class=\"article-list-home\">";
const n51 = "  <div class=\"no-print\">\r\n  <div class=\"section-title\" style=\"margin-top: 40px;\">関連する解説記事</div>\r\n  <div class=\"article-list-home\">";
if (!content.includes(o51)) throw new Error("5-1");
content = content.replace(o51, n51);

const o52 = "    <div style=\"text-align: right; margin-top: 12px; padding-right: 5px; margin-bottom: 24px;\">\r\n      <a href=\"articles/index.html\" style=\"font-size: 14px; color: var(--accent); text-decoration: none; font-weight: bold;\">すべての解説記事を見る →</a>\r\n    </div>\r\n  </div>\r\n\r\n  <div class=\"footer\" style=\"margin-top:32px;\">";
const n52 = "    <div style=\"text-align: right; margin-top: 12px; padding-right: 5px; margin-bottom: 24px;\">\r\n      <a href=\"articles/index.html\" style=\"font-size: 14px; color: var(--accent); text-decoration: none; font-weight: bold;\">すべての解説記事を見る →</a>\r\n    </div>\r\n  </div>\r\n  </div>\r\n\r\n  <div class=\"footer\" style=\"margin-top:32px;\">";
if (!content.includes(o52)) throw new Error("5-2");
content = content.replace(o52, n52);

fs.writeFileSync(path, content, 'utf8');
console.log('Success');
