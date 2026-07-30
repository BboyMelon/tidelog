#!/usr/bin/env python3
import os
import json
import hashlib

# ROOT 自動抓「這個腳本所在資料夾的上一層」= tidelog-site/ 專案根目錄
# 所以不管在誰的電腦上，只要資料夾結構不變，這個腳本都能正常執行
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)

def _css_version() -> str:
    """styles.css 內容的短hash，當作cache-busting query參數。
    每次改CSS內容雜湊就會變，強迫瀏覽器（尤其手機Safari）抓新版，不用使用者自己清快取。"""
    with open(f"{ROOT}/css/styles.css", "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]

CSS_VERSION = _css_version()

CONTACT_EMAIL = "tidelog.surf@gmail.com"
# 聯絡表單寫入機器人共用的 Supabase（surf-robot Flask 後端 /api/contact 端點）
CONTACT_API_URL = "https://surf-robot.onrender.com/api/contact"

def head(prefix, title, desc=""):
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}｜浪誌 TIDELOG</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{prefix}css/styles.css?v={CSS_VERSION}">
</head>
<body>
'''

FOOT = '''
</body>
</html>
'''

def nav(prefix, active):
    def cls(key):
        return ' class="on"' if key == active else ''
    return f'''<nav class="site">
  <div class="brand">
    <svg class="mark" viewBox="0 0 28 22" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M1 16c3 0 4-10 8-10s5 10 8 10 4-10 8-10" stroke="#1477c9" stroke-width="2.6" stroke-linecap="round"/>
      <path d="M1 8c3 0 4 10 8 10s5-10 8-10 4 10 8 10" stroke="#ffc63a" stroke-width="2.6" stroke-linecap="round"/>
    </svg>
    <span class="zh">浪誌</span>
    <span class="en">TIDELOG</span>
  </div>
  <ul class="navlinks">
    <li><a{cls("home")} href="{prefix}index.html">首頁</a></li>
    <li><a{cls("articles")} href="{prefix}articles.html">衝浪文章</a></li>
    <li><a href="{prefix}index.html#spots">浪點資料庫</a></li>
    <li><a{cls("map")} href="{prefix}map.html">浪點地圖</a></li>
    <li><a{cls("contact")} href="{prefix}contact.html">聯絡我們</a></li>
    <li><a{cls("subscribe")} href="{prefix}subscribe.html">訂閱浪況機器人</a></li>
  </ul>
</nav>
'''

def footer(prefix):
    return f'''<footer class="site">
  <div class="footer-top">
    <div class="footer-brand">
      <svg class="mark" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M2 20c3-4 6-4 9 0s6 4 9 0 6-4 9 0" stroke="#1477c9" stroke-width="2.6" stroke-linecap="round"/>
        <path d="M2 26c3-4 6-4 9 0s6 4 9 0 6-4 9 0" stroke="#ffc63a" stroke-width="2.6" stroke-linecap="round"/>
      </svg>
      <span class="zh">浪誌</span>
      <span class="en">TIDELOG</span>
    </div>
    <div class="footer-social">
      <span class="label">Follow us</span>
      <a href="https://line.me/R/ti/p/%40457fdtbo" target="_blank" rel="noopener" aria-label="加入LINE浪況機器人好友">
        <svg viewBox="0 0 24 24" fill="none"><rect x="1" y="2" width="22" height="20" rx="6" fill="#06C755"/><path d="M12 6.2c-4.1 0-7.4 2.7-7.4 6 0 3 2.6 5.5 6.1 5.9-.24.9-.9 2-.9 2.3 0 .2.1.3.3.3.15 0 .3-.1.4-.2.5-.4 2-1.6 2.8-2.3 4.3-.3 6-2.9 6-5.9 0-3.4-3.3-6.1-7.3-6.1z" fill="#fff"/></svg>
      </a>
      <a href="https://youtube.com/@melonlin4032?si=wEVhNFv35biFvY-k" target="_blank" rel="noopener" aria-label="YouTube">
        <svg viewBox="0 0 24 24" fill="none"><rect x="1" y="5" width="22" height="14" rx="4" fill="#ff0000"/><path d="M10 9l6 3-6 3V9z" fill="#fff"/></svg>
      </a>
      <a href="https://www.instagram.com/bboymelonlin/" target="_blank" rel="noopener" aria-label="Instagram">
        <svg viewBox="0 0 24 24" fill="none"><rect x="2" y="2" width="20" height="20" rx="6" fill="#d6249f"/><circle cx="12" cy="12" r="4.2" stroke="#fff" stroke-width="1.8"/><circle cx="17.2" cy="6.8" r="1.3" fill="#fff"/></svg>
      </a>
      <a href="https://www.facebook.com/melon.lin.737148?locale=zh_TW" target="_blank" rel="noopener" aria-label="Facebook">
        <svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="11" fill="#1877f2"/><path d="M13.6 21v-7.3h2.4l.4-2.8h-2.8v-1.8c0-.8.2-1.4 1.4-1.4h1.5V5.2c-.3 0-1.1-.1-2.1-.1-2.1 0-3.6 1.3-3.6 3.7v2.1H8.4v2.8H11V21h2.6z" fill="#fff"/></svg>
      </a>
    </div>
  </div>
  <ul class="footer-nav">
    <li><a href="{prefix}index.html">首頁</a></li>
    <li><a href="{prefix}articles.html">衝浪文章</a></li>
    <li><a href="{prefix}index.html#spots">浪點資料庫</a></li>
    <li><a href="{prefix}map.html">浪點地圖</a></li>
    <li><a href="{prefix}contact.html">聯絡我們</a></li>
    <li><a href="{prefix}subscribe.html">訂閱浪況機器人</a></li>
  </ul>
  <div class="footer-bottom">Copyright © 浪誌 TIDELOG. All rights reserved.　草稿 v3・多頁版</div>
</footer>
'''

# ─────────────────────────────────────────────────────────
# 文章資料（之後新增文章，就是在這裡加一筆 + 建一個對應的 articles/xxx.html）
articles = [
    dict(id="wushi-gang", tag="浪點介紹", region="北部・烏石港", title="烏石港完整攻略：從防波堤內側練起",
         desc="沙灘與礁岩混合地形，適合初學者練習，但防波堤北側礁岩區要特別留意退流時機。",
         img="./images/wushi_surfbackground.png", wave_cls="waves-a", read="6 分", stub=False),
    dict(id="beginner-spots", tag="衝浪知識", region="新手起步", title="新手衝浪去哪邊好？北中南推薦浪點",
         desc="沙灘地形、浪高別超過 1.2m、離岸流少——三個挑浪點原則，附北中南各一個新手友善浪點。",
         img="./images/新手衝浪＿封面.jpg", wave_cls="waves-b", read="5 分", stub=False),
    dict(id="first-timer-safety", tag="衝浪知識", region="新手起步", title="不會游泳可以衝浪嗎？第一次下水前該知道的 3 件事",
         desc="不會游泳不是問題，問題是海況複雜、離岸流，還有沒學會讀浪跟划水——這篇整理下水前的checklist。",
         img="./images/Noswming＿封面.png", wave_cls="waves-c", read="6 分", stub=False),
]

# ─────────────────────────────────────────────────────────
# 浪點資料庫（同步自機器人 config.py 的 SURF_SPOTS_CONFIG，
# 陸風方向／安全提醒文字是機器人原始資料；「難度」是機器人本身沒有存的
# 靜態欄位（機器人是每天用即時浪高動態算 GoOcean 分級，不是固定值），
# 這裡依安全提醒的地形描述人工給一個概略難度，方便新手瀏覽選點）
spots = [
    dict(name="金山沙珠灣", region="北部", wind="南／西南", level="中階",
         pill="浪況適中", dot="#f4b13a", safety="注意水母與左側礁石區"),
    dict(name="翡翠灣", region="北部", wind="南／東南", level="中階",
         pill="私人海灣", dot="#f4b13a", safety="私人海灣，西側礁岩勿靠近"),
    dict(name="中角灣", region="北部", wind="南／西南／西", level="中階",
         pill="浪型多變", dot="#f4b13a", safety="礁岩地形，浪型多變，注意退流"),
    dict(name="烏石港", region="北部", wind="西／西南／南", level="初～中階",
         pill="適合初學", dot="#3fce8a", safety="防波堤北側礁岩區，注意退流"),
    dict(name="宜蘭外澳", region="北部", wind="西／西南／南", level="進階",
         pill="浪大刺激", dot="#ff5b5b", safety="注意防波堤旁離岸流"),
    dict(name="松柏港福德里", region="中部", wind="東／東南／東北", level="中階",
         pill="冬季浪佳", dot="#f4b13a", safety="冬季東北季風浪較佳，注意強流"),
    dict(name="外埔漁港", region="中部", wind="東／東南", level="初～中階",
         pill="適合練習", dot="#3fce8a", safety="沙灘型浪點，注意離岸流與砂泥底質"),
    dict(name="花蓮北濱公園", region="東部", wind="西／西北／西南", level="中～進階",
         pill="暗礁注意", dot="#ff5b5b", safety="礫石灘，退潮暗礁多，注意強離岸流"),
    dict(name="花蓮環保公園", region="東部", wind="西／西北／西南", level="中～進階",
         pill="浪崩快", dot="#ff5b5b", safety="礫石底質，浪崩快，注意下浪時機"),
    dict(name="台東金樽", region="東部", wind="西／西北／西南", level="進階",
         pill="經驗者優先", dot="#ff5b5b", safety="礁岩型，退潮大石裸露，建議有經驗者入水"),
    dict(name="台東東河", region="東部", wind="西／西北／西南", level="中階",
         pill="人潮注意", dot="#f4b13a", safety="沙礫混合底質，注意人潮與流向"),
    dict(name="台南漁光島", region="南部", wind="東／東南／東北", level="初學",
         pill="適合長板", dot="#3fce8a", safety="沙灘型浪點，浪小適合長板，注意岸邊砂洲與潮汐變化"),
    dict(name="恆春南灣", region="南部・恆春", wind="北／東北／西北", level="初～中階",
         pill="夏季熱門", dot="#f4b13a", safety="熱門觀光沙灘，人潮多，夏季水母頻繁，注意衝浪區域劃分"),
    dict(name="恆春九鵬", region="南部・恆春", wind="西／西北／西南", level="進階",
         pill="強流注意", dot="#ff5b5b", safety="半島東側礁岩地形，浪型多變，注意強流與離岸流"),
    dict(name="恆春佳樂水", region="南部・恆春", wind="西／西北", level="中～進階",
         pill="河口地形", dot="#f4b13a", safety="河口地形，退潮時注意暗礁"),
]

def spot_card(s):
    return f'''    <div class="spot-card">
      <div class="row1"><h3>{s['name']}</h3><span class="region">{s['region']}</span></div>
      <div class="stats-row">
        <div class="stat-block"><div class="label">陸風</div><div class="val">{s['wind']}</div></div>
        <div class="stat-block"><div class="label">難度</div><div class="val">{s['level']}</div></div>
      </div>
      <div class="level-pill"><span class="dot" style="background:{s['dot']}"></span>{s['pill']}</div>
      <p class="safety">{s['safety']}</p>
    </div>'''


def feat_card(a, linked=True, in_articles_page=False):
    href = f'articles/{a["id"]}.html' if not in_articles_page else f'{a["id"]}.html'
    href_prefix = './' if in_articles_page else './'
    media_inner = ''
    if a["img"]:
        media_inner = f'<img src="{a["img"]}" alt="封面圖" style="width:100%; height:100%; object-fit:cover;">'
    stub_cls = ' is-stub' if a.get('stub') else ''
    body = f'''      <article class="feat-card{stub_cls}" data-tag="{a['tag']}">
        <div class="feat-media {a['wave_cls']}">
          {media_inner}
          <span class="tag">{a['tag']}</span>
          <span class="len">閱讀 {a['read']}</span>
        </div>
        <div class="feat-body">
          <span class="eyebrow">{a['region']}</span>
          <h3><a href="{href_prefix}{href}" style="color:inherit; text-decoration:none;">{a['title']}</a></h3>
          <p>{a['desc']}</p>
        </div>
      </article>'''
    return body

os.makedirs(f"{ROOT}/articles", exist_ok=True)
print("helpers ready")

# ─────────────────────────────────────────────────────────
# index.html
featured_cards = "\n".join(feat_card(a) for a in articles[:4])

index_body = f'''{nav("./", "home")}
<header class="hero">
  <video class="hero-media" autoplay muted loop playsinline aria-hidden="true">
    <source src="./videos/hero-surf.mp4" type="video/mp4">
  </video>
  <div class="hero-scrim" aria-hidden="true"></div>
  <div class="hero-inner">
    <span class="eyebrow">台灣衝浪筆記</span>
    <h1>讀懂台灣的<em>每一道浪</em></h1>
    <p>從北海岸到南灣，紀錄每個浪點的浪況、地形與注意事項。</p>
    <div class="cta-row">
      <a class="btn primary" href="#spots">瀏覽浪點資料庫</a>
      <a class="btn ghost" href="./articles.html">看最新文章</a>
    </div>
  </div>
</header>

<section class="rail-wrap" id="feature">
  <div class="section">
    <div class="section-head">
      <h2>本週精選</h2>
      <a href="./articles.html">看全部 →</a>
    </div>
    <div class="rail">
{featured_cards}
    </div>
  </div>
</section>

<section class="grid-wrap section" id="spots">
  <div class="section-head">
    <h2>浪點資料庫</h2>
    <span class="eyebrow">全台 {len(spots)} 個浪點</span>
  </div>
  <div class="spot-grid">
{chr(10).join(spot_card(s) for s in spots)}
  </div>
</section>

{footer("./")}'''

with open(f"{ROOT}/index.html", "w") as f:
    f.write(head("./", "首頁", "台灣衝浪浪點與知識筆記") + index_body + FOOT)

print("index.html written")

# ─────────────────────────────────────────────────────────
# articles.html (文章列表 + 標籤篩選 + 數字分頁)
PER_PAGE = 4
cards_html = "\n".join(feat_card(a) for a in articles)
unique_tags = list(dict.fromkeys(a['tag'] for a in articles))
tag_buttons = " ".join(f'<button data-tag="{t}">{t}</button>' for t in unique_tags)

pagination_js = '''
<script>
(function(){
  var perPage = ''' + str(PER_PAGE) + ''';
  var grid = document.querySelector('.article-grid');
  var cards = Array.prototype.slice.call(grid.querySelectorAll('.feat-card'));
  var pagBar = document.getElementById('pagination');
  var filterBar = document.getElementById('tag-filter');
  var state = { tag: 'all', page: 1 };

  function filteredCards(){
    if(state.tag === 'all') return cards;
    return cards.filter(function(c){ return c.dataset.tag === state.tag; });
  }

  function pageTokens(totalPages, current){
    var tokens = [];
    for(var p=1; p<=totalPages; p++){
      if(p===1 || p===totalPages || (p>=current-1 && p<=current+1)){
        tokens.push(p);
      } else if(tokens[tokens.length-1] !== '...'){
        tokens.push('...');
      }
    }
    return tokens;
  }

  function scrollToTop(){
    window.scrollTo({top: document.querySelector('.page-head').offsetTop - 90, behavior:'smooth'});
  }

  function render(){
    var list = filteredCards();
    var totalPages = Math.max(1, Math.ceil(list.length / perPage));
    if(state.page > totalPages) state.page = totalPages;

    cards.forEach(function(c){ c.classList.add('is-hidden'); });
    list.forEach(function(c, i){
      var p = Math.floor(i/perPage) + 1;
      c.classList.toggle('is-hidden', p !== state.page);
    });

    var tokens = pageTokens(totalPages, state.page);
    var html = '<button data-nav="prev"' + (state.page===1 ? ' disabled' : '') + '>\u2039 \u4e0a\u4e00\u9801</button>';
    tokens.forEach(function(t){
      if(t === '...'){
        html += '<span class="pg-ellipsis">\u2026</span>';
      } else {
        html += '<button data-page="' + t + '"' + (t===state.page ? ' class="active"' : '') + '>' + t + '</button>';
      }
    });
    html += '<button data-nav="next"' + (state.page===totalPages ? ' disabled' : '') + '>\u4e0b\u4e00\u9801 \u203a</button>';
    pagBar.innerHTML = html;
  }

  filterBar.addEventListener('click', function(e){
    var t = e.target.closest('button');
    if(!t) return;
    filterBar.querySelectorAll('button').forEach(function(b){ b.classList.remove('active'); });
    t.classList.add('active');
    state.tag = t.dataset.tag;
    state.page = 1;
    render();
  });

  pagBar.addEventListener('click', function(e){
    var t = e.target.closest('button');
    if(!t || t.disabled) return;
    var list = filteredCards();
    var totalPages = Math.max(1, Math.ceil(list.length/perPage));
    if(t.dataset.nav === 'prev'){ if(state.page>1){ state.page--; render(); scrollToTop(); } return; }
    if(t.dataset.nav === 'next'){ if(state.page<totalPages){ state.page++; render(); scrollToTop(); } return; }
    if(t.dataset.page){ state.page = parseInt(t.dataset.page,10); render(); scrollToTop(); }
  });

  render();
})();
</script>
'''

articles_body = f'''{nav("./", "articles")}
<div class="page-head">
  <h1>衝浪文章</h1>
  <p>浪點介紹、安全知識、裝備筆記，之後新增文章就是在這頁加卡片。</p>
</div>
<div class="tag-filter" id="tag-filter">
  <button data-tag="all" class="active">全部</button>
  {tag_buttons}
</div>
<div class="article-grid">
{cards_html}
</div>
<div class="pagination" id="pagination" data-current="1"></div>

{footer("./")}
{pagination_js}'''

with open(f"{ROOT}/articles.html", "w") as f:
    f.write(head("./", "衝浪文章", "所有浪點介紹、衝浪知識與裝備筆記文章列表") + articles_body + FOOT)

print("articles.html written")

# ─────────────────────────────────────────────────────────
# 文章內頁

wushi_content = '''    <p>烏石港是北部最容易入門的浪點之一，主要是沙灘地形，適合新手練習划水與站板的好地方。但別被「好上手」騙了——退潮時防波堤北側的消坡塊區暗流不小，這篇會把安全範圍講清楚。</p>

    <h2>浪況特性</h2>
    <p>屬於沙灘浪與地形浪的混合型態，西南到南風時最乾淨。退潮前後兩小時是黃金窗口，浪型會比滿潮時更有型、更好抓。</p>
    <ul>
      <li>適合浪高：0.5～1.5m，超過 2m 建議進階者再下水</li>
      <li>最佳風向：西南、南（離岸風）</li>
      <li>底質：沙地為主，靠近防波堤轉礁岩</li>
    </ul>

<div class="inline-figs">
  <figure>
    <img src="../images/wushi_surfbackground.png" alt="烏石港防波堤內側" loading="lazy">
    <figcaption>防波堤內側練習區</figcaption>
  </figure>
  <figure>
    <img src="../images/wushi_surfrock.jpg" alt="烏石港退潮礁岩" loading="lazy">
    <figcaption>退潮時的礁岩區</figcaption>
  </figure>
</div>

    <p class="pullquote">「防波堤北側消波區，注意退潮」——這句話我一開始也覺得是罐頭警語，直到有次退潮貪玩多划了兩趟，才知道那股流有多扎實。</p>

    <h2>注意事項</h2>
    <p>人潮集中在防波堤內側，外側浪型較大也較亂，新手不建議貿然移動過去。退潮後段消坡塊會裸露，務必留意腳踩位置。</p>

    <h2>周邊資訊</h2>
    <p>烏石港衝浪教室聚集地，租板／換裝設施齊全，開車到國5頭城交流道下來 或搭火車到頭城站再轉乘計程車，都方便抵達。</p>
    
<div class="yt-embed">
  <iframe src="https://www.youtube.com/embed/VnCYsQAK2XI?si=jpKUzB7nHe9n8OZy"
    title="烏石港空拍" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen loading="lazy"></iframe>
</div>'''

beginner_content = '''    <p>新手選浪點，比起「哪裡浪比較大」，更該問「哪裡出錯的代價比較低」。三個簡單原則：地形以沙灘為主、避開整片礁岩區；浪高最好落在機器人 GoOcean 分級的 🟢 初學區間（浪高 1.2m 以下、週期 7 秒以下）；離岸流少，或至少流的位置固定、看得出來。</p>

    <h2>北部：烏石港</h2>
    <p>沙灘與礁岩混合地形，衝浪教室聚集地，租板、換裝設施齊全。防波堤內側是主要練習區，退潮前後兩小時浪型比較有型。<strong>但防波堤北側礁岩區退流不小</strong>，新手不建議靠過去。</p>

<div class="inline-figs solo">
  <figure>
    <img src="../images/烏石港_新手.jpg" alt="烏石港新手練習區" loading="lazy">
    <figcaption>烏石港防波堤內側練習區</figcaption>
  </figure>
</div>

    <h2>中部：台中松柏港</h2>
    <p>正式站名是「松柏港福德里」，位在台中大安溪出口北岸，冬季東北季風時浪況較穩定。沙灘型浪點，浪通常偏小，很適合單純練習划水的階段，跌倒摔板的代價也比礁岩區低很多，但一樣要留意強流與離岸流位置。</p>

<div class="inline-figs solo">
  <figure>
    <img src="../images/松柏港_新手.jpg" alt="台中松柏港新手浪點" loading="lazy">
    <figcaption>台中松柏港（松柏港福德里）</figcaption>
  </figure>
</div>

    <h2>南部：台南漁光島</h2>
    <p>沙灘型浪點，浪小適合長板，是南部新手很常去的起點。要注意的是岸邊砂洲會隨潮汐變化，退潮時水深、流向都可能跟漲潮時不一樣。</p>

<div class="inline-figs solo">
  <figure>
    <img src="../images/漁光島_新手.JPG" alt="台南漁光島新手浪點" loading="lazy">
    <figcaption>台南漁光島</figcaption>
  </figure>
</div>

    <h2>下水前，先查一次即時浪況</h2>
    <p>上面三個是「平常表現」比較穩定的新手浪點，但沒有哪個浪點是「永遠安全」——同一個浪點，颱風前後或東北季風增強時，照樣可能超出新手能應付的範圍。加 LINE 浪況機器人好友，出發前打浪點名稱查一次即時浪高、風向、潮汐，比看這篇文章更準。</p>'''

first_timer_safety_content = '''    <p>常有人問：不會游泳可以學衝浪嗎？答案是可以——新手課大多在踩得到底的淺灘上課，重點從來不是「會不會游泳」，而是腳繩有沒有綁好、教練有沒有在旁邊顧、今天的海況適不適合新手下水。真正該留意的，是接下來這三件事。</p>

    <h2>海況比你想的複雜</h2>
    <p>能不能下水，不是看「今天有沒有出太陽」就能判斷。夏天離台灣很遠的颱風，照樣可能把大浪送過來；新手常常想「颱風那麼遠應該還好吧」，結果海況早就超出能應付的範圍。找教練或有經驗的浪友問清楚今天適不適合新手，比自己憑感覺猜準得多——出發前也可以先打浪點名稱問問機器人，浪高、週期跟分級燈號一次看到。</p>

<div class="inline-figs solo">
  <figure>
    <img src="../images/平靜海域_Noswming.jpg" alt="表面看似平靜的海域" loading="lazy">
    <figcaption>看起來平靜，不代表適合新手下水</figcaption>
  </figure>
</div>

    <h2>離岸流才是真正的敵人</h2>
    <p>離岸流是海浪拍上岸後，海水匯聚成一股往外海流回去的力量。沒有浮具又不知道怎麼脫離的話，很容易被帶到外海，一慌就更容易溺水。辨識訣竅：水色比周圍混濁、浪快碎的區域卻沒有白沫、水面出現一排垂直於岸邊的小波紋——這三個徵兆同時出現，那多半就是離岸流的位置。第一次到不熟的浪點，務必先問教練今天的地形怎麼看。</p>

<div class="inline-figs solo">
  <figure>
    <img src="../images/離岸流_Noswming.jpg" alt="離岸流示意" loading="lazy">
    <figcaption>離岸流：水色混濁、快碎卻沒有白沫的區域要留意</figcaption>
  </figure>
</div>

    <h2>沒學會讀浪跟划水，永遠站不起來</h2>
    <p>體驗課能站起來，很多時候是教練幫忙挑浪、推板的功勞。之後自己租板練習才會發現「怎麼突然站不起來了」——這不是退步，是進入真正要學「讀浪」跟「划水」的階段，本來就會經歷這段卡關期，撐過去就是自己的功力。</p>

    <h2>下水前 checklist</h2>
    <ul>
      <li>先上正式體驗課，不要只租板子附贈的教學，落差真的很大</li>
      <li>問清楚今天適不適合新手，教練回答含糊就換一家</li>
      <li>裝備到位：腳繩、合身防磨衣，帥不帥不重要，能不能平安回家比較重要</li>
      <li>把離岸流的三個徵兆記起來，哪怕只記得「顏色不同、沒有白沫的水道要小心」也好</li>
    </ul>

<div class="inline-figs solo">
  <figure>
    <img src="../images/衝浪腳繩＿Noswiming.png" alt="衝浪腳繩" loading="lazy">
    <figcaption>下水前先確認腳繩有沒有綁好</figcaption>
  </figure>
</div>
    <p>不會游泳真的不等於不能學衝浪，但值得信任的教練跟合適的海況，才是能不能安心下水的關鍵。出發前加 LINE 好友、打浪點名稱查一次即時浪況，比憑印象猜安不安全準確。</p>'''

CONTENT_MAP = {
    "wushi-gang": wushi_content,
    "beginner-spots": beginner_content,
    "first-timer-safety": first_timer_safety_content,
}

def stub_content(a):
    return f'''    <p>這是示範用的佔位文章，用來測試「衝浪文章」列表頁的分頁功能是否正常運作。之後把這段換成 <strong>{a["title"]}</strong> 的實際內容即可，段落結構（h2 / p / ul / figure）都可以照抄 {"../images/" }下的圖片路徑寫法。</p>

    <h2>之後要補的內容</h2>
    <p>{a["desc"]}</p>
    <ul>
      <li>浪況特性</li>
      <li>最佳風向／潮汐時機</li>
      <li>注意事項與安全提醒</li>
    </ul>'''

# 已有實拍封面圖的文章：art-hero 直接放圖，不再顯示灰底佔位
COVER_IMAGES = {
    "beginner-spots": "../images/新手衝浪＿封面.jpg",
    "first-timer-safety": "../images/Noswming＿封面.png",
}

def article_detail(a):
    date = {"wushi-gang": "2026.07.15", "beginner-spots": "2026.07.24", "first-timer-safety": "2026.07.27"}.get(a["id"], "草稿・尚未發布")
    stat_line = '<span class="stat">浪高 0.8–1.6m</span><span class="stat">週期 6–9s</span><span>適合｜初學～中階</span>' if a["id"]=="wushi-gang" else ('<span class="stat">衝浪知識</span>' if not a["stub"] else '<span class="stat">示範資料</span>')
    body_content = CONTENT_MAP.get(a["id"]) or stub_content(a)
    ph_label = "封面照片預留位置（之後換成烏石港實拍照）" if a["id"] == "wushi-gang" else "封面照片預留位置（之後可換成實拍照）"

    cover_img = COVER_IMAGES.get(a["id"])
    if cover_img:
        hero_inner = f'<img src="{cover_img}" alt="{a["title"]}" style="width:100%; height:100%; object-fit:cover;">'
    else:
        hero_inner = f'<div class="ph"></div>\n    <span class="ph-label">{ph_label}</span>'

    art_body = f'''{nav("../", "articles")}
<div class="article-divider" style="margin-top:1.5rem;"><span>{a["tag"]}</span><div class="line"></div></div>
<article class="article">
  <div class="art-hero">
    {hero_inner}
  </div>
  <div class="art-wrap">
    <span class="eyebrow">{a["tag"]}・{a["region"]}</span>
    <h1>{a["title"]}</h1>
    <div class="art-meta">
      <span>{date}</span>
      {stat_line}
    </div>

{body_content}
  </div>
</article>

{footer("../")}'''
    return head("../", a["title"], a["desc"]) + art_body + FOOT

for a in articles:
    with open(f"{ROOT}/articles/{a['id']}.html", "w") as f:
        f.write(article_detail(a))

print(f"{len(articles)} article pages written")

# ─────────────────────────────────────────────────────────
# contact.html
contact_body = f'''{nav("./", "contact")}
<div class="simple-page">
  <h1>聯絡我們</h1>
  <p class="lead">浪點資訊有誤、想投稿文章，或單純想聊衝浪，都歡迎寫信給我們。</p>

  <div class="contact-info">
    <span>📧 {CONTACT_EMAIL}</span>
    <span>📍 台灣</span>
  </div>

  <form class="contact-form" id="contact-form">
    <div class="form-field">
      <label for="c-name">姓名</label>
      <input id="c-name" name="姓名" type="text" required>
    </div>
    <div class="form-field">
      <label for="c-email">Email</label>
      <input id="c-email" name="Email" type="email" required>
    </div>
    <div class="form-field">
      <label for="c-msg">訊息</label>
      <textarea id="c-msg" name="訊息" required></textarea>
    </div>
    <button class="btn primary form-submit" type="submit">送出</button>
    <p class="form-note" id="contact-status" hidden></p>
  </form>

  <p class="form-note">填寫後會直接寫進後台資料庫，我們看到會盡快回覆；若表單暫時無法送出，也歡迎直接寫信到 {CONTACT_EMAIL}。</p>
</div>

<script>
document.getElementById('contact-form').addEventListener('submit', function (e) {{
  e.preventDefault();
  var form = e.target;
  var status = document.getElementById('contact-status');
  var payload = {{
    name: document.getElementById('c-name').value,
    email: document.getElementById('c-email').value,
    message: document.getElementById('c-msg').value,
  }};
  fetch({json.dumps(CONTACT_API_URL)}, {{
    method: 'POST',
    headers: {{ 'Content-Type': 'application/json' }},
    body: JSON.stringify(payload),
  }})
    .then(function (r) {{ return r.json(); }})
    .then(function (data) {{
      status.hidden = false;
      status.textContent = data.ok ? '✅ ' + data.message : '❌ ' + data.message;
      if (data.ok) form.reset();
    }})
    .catch(function () {{
      status.hidden = false;
      status.textContent = '送出失敗，請直接寫信到 {CONTACT_EMAIL}';
    }});
}});
</script>

{footer("./")}'''

with open(f"{ROOT}/contact.html", "w") as f:
    f.write(head("./", "聯絡我們", "聯絡浪誌 TIDELOG") + contact_body + FOOT)

# ─────────────────────────────────────────────────────────
# subscribe.html
subscribe_body = f'''{nav("./", "subscribe")}
<div class="simple-page">
  <div class="subscribe-heading">
    <img class="bot-avatar" src="./images/bot-avatar.png" alt="浪況機器人大頭貼" width="72" height="72" loading="lazy">
    <h1>WaveForecast浪況機器人</h1>
  </div>
  <p class="lead">加入「浪誌 TIDELOG」的 LINE 浪況機器人好友，每天 05:00 收到專屬浪況早報，隨時打浪點名稱查即時浪高、風向、潮汐。</p>

  <div class="line-cta">
    <img class="line-qr" src="./images/Line＿QRcode.png" alt="加入LINE浪況機器人好友 QRCode" width="180" height="180" loading="lazy">
    <div class="line-cta-body">
      <a class="btn primary" href="https://line.me/R/ti/p/%40457fdtbo" target="_blank" rel="noopener">加入 LINE 好友</a>
      <p class="line-id">LINE ID：@457fdtbo</p>
      <p>手機掃描左側 QRCode，或點選按鈕直接加入。</p>
    </div>
  </div>

  <ul class="subscribe-perks">
    <li>每天 05:00 專屬浪況早報，依你的浪齡個人化推薦浪點</li>
    <li>長浪／颱風警戒即時推播，不用自己盯氣象</li>
    <li>打浪點名稱（如「烏石港」）隨時查即時浪高、風向、潮汐時刻</li>
  </ul>

  <h2 class="form-heading">開通每日推播</h2>
  <p class="lead">加好友後，還要多一個步驟才會真的收到每天 05:00 的浪況早報：在 LINE 對話裡傳「<strong>Surfer 檔案建立</strong>」（或點選單同名按鈕），依格式填寫性別／浪齡／板型／常衝浪點並回傳，送出後就會自動開通，而且每天還會依你的程度收到個人化浪點推薦。</p>

  <div class="howto-shot">
    <img src="./images/subscribe-howto.jpg" alt="LINE對話操作示範：傳「Surfer 檔案建立」或點選單按鈕" loading="lazy">
    <p class="howto-caption">📱 在 LINE 對話裡傳「Surfer 檔案建立」，或點下方選單同名按鈕</p>
  </div>
</div>

{footer("./")}'''

with open(f"{ROOT}/subscribe.html", "w") as f:
    f.write(head("./", "WaveForecast浪況機器人", "訂閱浪誌 TIDELOG 最新浪況與文章通知") + subscribe_body + FOOT)

print("contact.html + subscribe.html written")

# ─────────────────────────────────────────────────────────
# map.html — 互動式浪點地圖
# 座標是浪點實際地理位置（真實經緯度，非機器人 STATION_COORDS 那種共用浮標外海座標），
# 用於在真實台灣地圖上準確標記。松柏港福德里／外埔漁港兩筆座標為查證後修正：
# 機器人 TIDE_STATION_MAP 原本對應到雲林縣的潮汐站，但實際地點分別在台中大安溪口、
# 苗栗後龍——這是機器人那邊潮汐站選錯地區的既有問題，跟這裡的地圖座標無關，
# 已另外記錄提醒使用者。
MAP_SPOTS = [
    dict(name="金山中角灣（沙珠灣）", category="北部", lat=25.222, lon=121.636,
         safety="礁岩地形，浪型多變，注意退流、水母與左側礁石區"),
    dict(name="翡翠灣", category="北部", lat=25.199, lon=121.687,
         safety="私人海灣，西側礁岩勿靠近"),
    dict(name="烏石港", category="北部", lat=24.860, lon=121.831,
         safety="防波堤北側礁岩區，注意退流"),
    dict(name="宜蘭外澳", category="北部", lat=24.870, lon=121.834,
         safety="注意防波堤旁離岸流"),
    dict(name="福隆", category="北部", lat=25.017, lon=121.945,
         safety="雙溪出海口地形，注意河口離岸流"),
    dict(name="松柏港福德里", category="中部", lat=24.4015, lon=120.5809,
         safety="冬季東北季風浪較佳，注意強流"),
    dict(name="外埔漁港", category="中部", lat=24.6499, lon=120.7717,
         safety="沙灘型浪點，注意離岸流與砂泥底質"),
    dict(name="花蓮北濱公園", category="東部", lat=23.980, lon=121.618,
         safety="礫石灘，退潮暗礁多，注意強離岸流"),
    dict(name="花蓮環保公園", category="東部", lat=23.985, lon=121.615,
         safety="礫石底質，浪崩快，注意下浪時機"),
    dict(name="台東金樽", category="東部", lat=23.152, lon=121.397,
         safety="礁岩型，退潮大石裸露，建議有經驗者入水"),
    dict(name="台東東河", category="東部", lat=23.128, lon=121.371,
         safety="沙礫混合底質，注意人潮與流向"),
    dict(name="台南漁光島", category="南部", lat=22.984, lon=120.146,
         safety="沙灘型浪點，浪小適合長板，注意岸邊砂洲與潮汐變化"),
    dict(name="恆春南灣", category="南部・恆春", lat=21.939, lon=120.751,
         safety="熱門觀光沙灘，人潮多，夏季水母頻繁，注意衝浪區域劃分"),
    dict(name="恆春九鵬", category="南部・恆春", lat=22.011, lon=120.845,
         safety="半島東側礁岩地形，浪型多變，注意強流與離岸流"),
    dict(name="恆春佳樂水", category="南部・恆春", lat=22.021, lon=120.856,
         safety="河口地形，退潮時注意暗礁"),
]

LIVE_API_URL = "https://surf-robot.onrender.com/api/live-conditions"

map_body = f'''{nav("./", "map")}
<div class="map-page">
  <h1>浪點地圖</h1>
  <p class="lead">點圖釘查看該浪點的即時浪況（浪高、週期、風向、GoOcean分級）。資料來源跟 LINE 機器人相同，每次開啟頁面即時抓取。</p>

  <div id="map-banner" class="map-banner" hidden>
    <span id="map-banner-text"></span>
    <button id="map-retry" class="btn" type="button">重新查詢</button>
  </div>

  <div id="spot-map" class="spot-map"></div>

  <div class="map-legend">
    <span><i style="background:#3fce8a"></i>初學 🟢</span>
    <span><i style="background:#f4b13a"></i>中階 🟡</span>
    <span><i style="background:#ff5b5b"></i>進階 🔴</span>
    <span><i style="background:#6b1414"></i>危險封閉 ⛔</span>
    <span><i style="background:#9aa7b2"></i>暫無資料</span>
  </div>
  <p class="map-note">即時浪況每次開啟頁面向機器人伺服器抓取一次；伺服器若剛從休眠喚醒，第一次查詢可能要等 30-60 秒。</p>
</div>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
  const FALLBACK_SPOTS = {json.dumps(MAP_SPOTS, ensure_ascii=False)};
  const LIVE_API_URL = "{LIVE_API_URL}";
  const LEVEL_COLOR = {{
    "🟢": "#3fce8a", "🟡": "#f4b13a", "🔴": "#ff5b5b", "⛔": "#6b1414"
  }};
  const NO_DATA_COLOR = "#9aa7b2";

  const map = L.map("spot-map", {{ scrollWheelZoom:false }}).setView([23.6, 120.9], 7.4);
  L.tileLayer("https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png", {{
    attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
    maxZoom: 18
  }}).addTo(map);

  function dotIcon(color){{
    return L.divIcon({{
      className: "",
      html: `<span style="display:block;width:16px;height:16px;border-radius:50%;background:${{color}};border:2px solid #fff;box-shadow:0 1px 4px rgba(11,39,64,.4);"></span>`,
      iconSize: [16,16], iconAnchor: [8,8], popupAnchor: [0,-10]
    }});
  }}

  function popupHTML(spot, live){{
    let body = `<div class="spot-popup"><h3>${{spot.name}}</h3><div class="region">${{spot.category}}</div>`;
    if (live && live.has_data){{
      const windText = live.wind_dir ? `${{live.wind_dir}}（${{live.wind_beaufort}}級）` : "—";
      body += `
        <div class="row"><span>浪高</span><span>${{live.wave_height.toFixed(1)}} m</span></div>
        <div class="row"><span>週期</span><span>${{live.wave_period.toFixed(0)}} s</span></div>
        <div class="row"><span>風向</span><span>${{windText}}</span></div>
        <div class="row"><span>分級</span><span>${{live.stars || ""}} ${{live.level_emoji || ""}}</span></div>`;
    }} else if (live){{
      body += `<div class="row"><span>浪況</span><span>暫無觀測資料</span></div>`;
    }} else {{
      body += `<div class="row"><span>浪況</span><span>載入中…</span></div>`;
    }}
    body += `<div class="safety">⚠️ ${{spot.safety}}</div></div>`;
    return body;
  }}

  const markers = {{}};
  FALLBACK_SPOTS.forEach(spot => {{
    const m = L.marker([spot.lat, spot.lon], {{ icon: dotIcon(NO_DATA_COLOR) }}).addTo(map);
    m.bindPopup(popupHTML(spot, null));
    markers[spot.name] = m;
  }});

  function showBanner(text, showRetry){{
    const banner = document.getElementById("map-banner");
    document.getElementById("map-banner-text").textContent = text;
    document.getElementById("map-retry").style.display = showRetry ? "inline-block" : "none";
    banner.hidden = false;
  }}
  function hideBanner(){{ document.getElementById("map-banner").hidden = true; }}

  function loadLiveConditions(){{
    showBanner("正在抓取即時浪況…", false);
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 25000);
    fetch(LIVE_API_URL, {{ signal: controller.signal }})
      .then(r => {{ if(!r.ok) throw new Error("HTTP " + r.status); return r.json(); }})
      .then(data => {{
        clearTimeout(timeout);
        hideBanner();
        const byName = {{}};
        (data.spots || []).forEach(s => byName[s.name] = s);
        FALLBACK_SPOTS.forEach(spot => {{
          const live = byName[spot.name];
          const marker = markers[spot.name];
          if (!marker) return;
          const color = live && live.has_data ? (LEVEL_COLOR[live.level_emoji] || NO_DATA_COLOR) : NO_DATA_COLOR;
          marker.setIcon(dotIcon(color));
          marker.setPopupContent(popupHTML(spot, live || {{ has_data:false }}));
        }});
      }})
      .catch(err => {{
        clearTimeout(timeout);
        showBanner("目前無法取得即時浪況，伺服器可能剛從休眠中喚醒，稍後再試一次。", true);
        console.error("[live-conditions]", err);
      }});
  }}

  document.getElementById("map-retry").addEventListener("click", loadLiveConditions);
  loadLiveConditions();
</script>

{footer("./")}'''

with open(f"{ROOT}/map.html", "w") as f:
    f.write(head("./", "浪點地圖", "互動式台灣浪點地圖，點圖釘查看即時浪況") + map_body + FOOT)

print("map.html written")
