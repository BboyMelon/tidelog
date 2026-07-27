#!/usr/bin/env python3
import os

# ROOT 自動抓「這個腳本所在資料夾的上一層」= tidelog-site/ 專案根目錄
# 所以不管在誰的電腦上，只要資料夾結構不變，這個腳本都能正常執行
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)

# 浪況機器人後端（Render），/subscribe 表單送出目標
RENDER_API_URL = "https://surf-robot.onrender.com"

def head(prefix, title, desc=""):
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}｜浪誌 TIDELOG</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{prefix}css/styles.css">
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
    <li><a{cls("contact")} href="{prefix}contact.html">聯絡我們</a></li>
    <li><a{cls("subscribe")} href="{prefix}subscribe.html">訂閱最新浪況</a></li>
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
      <a href="#" aria-label="YouTube">
        <svg viewBox="0 0 24 24" fill="none"><rect x="1" y="5" width="22" height="14" rx="4" fill="#ff0000"/><path d="M10 9l6 3-6 3V9z" fill="#fff"/></svg>
      </a>
      <a href="#" aria-label="Instagram">
        <svg viewBox="0 0 24 24" fill="none"><rect x="2" y="2" width="20" height="20" rx="6" fill="#d6249f"/><circle cx="12" cy="12" r="4.2" stroke="#fff" stroke-width="1.8"/><circle cx="17.2" cy="6.8" r="1.3" fill="#fff"/></svg>
      </a>
      <a href="#" aria-label="Facebook">
        <svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="11" fill="#1877f2"/><path d="M13.6 21v-7.3h2.4l.4-2.8h-2.8v-1.8c0-.8.2-1.4 1.4-1.4h1.5V5.2c-.3 0-1.1-.1-2.1-.1-2.1 0-3.6 1.3-3.6 3.7v2.1H8.4v2.8H11V21h2.6z" fill="#fff"/></svg>
      </a>
    </div>
  </div>
  <ul class="footer-nav">
    <li><a href="{prefix}index.html">首頁</a></li>
    <li><a href="{prefix}articles.html">衝浪文章</a></li>
    <li><a href="{prefix}index.html#spots">浪點資料庫</a></li>
    <li><a href="{prefix}contact.html">聯絡我們</a></li>
    <li><a href="{prefix}subscribe.html">訂閱最新浪況</a></li>
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
         img=None, wave_cls="waves-b", read="5 分", stub=False),
    dict(id="current-conditions", tag="衝浪知識", region="安全教室", title="海流與海況：下水前該看的注意事項",
         desc="浪高只是海況的一部分，陸風／onshore、潮汐、離岸流一起看，才不會被表面的平靜騙了。",
         img=None, wave_cls="waves-c", read="6 分", stub=False),
    dict(id="rip-current", tag="衝浪知識", region="安全教室", title="離岸流不是鬼故事：三個辨識訣竅",
         desc="混濁的水色、沒有白沫的水面、垂直於岸的小波紋——學會看這三個徵兆，比什麼都重要。",
         img=None, wave_cls="waves-b", read="4 分", stub=True),
    dict(id="jinzun", tag="浪點介紹", region="東部・台東金樽", title="金樽：退潮時大石裸露，這樣安排下水時間",
         desc="礁岩型浪點，浪況佳但地形變化快，建議有經驗者優先，並抓緊滿潮前兩小時的空檔。",
         img=None, wave_cls="waves-c", read="7 分", stub=True),
    dict(id="wetsuit-guide", tag="裝備筆記", region="新手必看", title="台灣海溫怎麼選防寒衣？四季實測心得",
         desc="冬天東北季風浪點水溫直落 18 度，厚度怎麼挑、袖長要不要留，實際下水比較給你看。",
         img=None, wave_cls="waves-a", read="5 分", stub=True),
    dict(id="waimu", tag="浪點介紹", region="北部・宜蘭外澳", title="外澳：風浪都大，進階者的練習場",
         desc="示範文章，內容待補：外澳浪點特色、風向與離岸流位置整理。",
         img=None, wave_cls="waves-b", read="－", stub=True),
    dict(id="fin-setup", tag="裝備筆記", region="板具設定", title="尾鰭配置入門：單/三鰭差在哪？",
         desc="示範文章，內容待補：不同尾鰭配置對操控性與速度的影響。",
         img=None, wave_cls="waves-c", read="－", stub=True),
    dict(id="tide-reading", tag="衝浪知識", region="浪況判斷", title="怎麼看潮汐表決定下水時間？",
         desc="示範文章，內容待補：潮汐表基礎判讀與各浪點的黃金窗口對照。",
         img=None, wave_cls="waves-a", read="－", stub=True),
    dict(id="nanwan", tag="浪點介紹", region="南部・恆春南灣", title="南灣夏季衝浪：人潮與水母季注意事項",
         desc="示範文章，內容待補：南灣夏季浪況、人潮尖峰時段與水母出沒提醒。",
         img=None, wave_cls="waves-b", read="－", stub=True),
    dict(id="paddle-basics", tag="衝浪知識", region="新手基本功", title="划水效率差？三個常見姿勢錯誤",
         desc="示範文章，內容待補：划水常見錯誤姿勢與修正方式圖解。",
         img=None, wave_cls="waves-c", read="－", stub=True),
    dict(id="board-care", tag="裝備筆記", region="板具保養", title="衝浪板保養：曬痕、黃化、修補怎麼處理",
         desc="示範文章，內容待補：板具日常保養與簡易修補教學。",
         img=None, wave_cls="waves-a", read="－", stub=True),
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
  <div class="hero-tickets">
    <div class="ticket"><span class="dot green"></span>烏石港・浪高 1.4m</div>
    <div class="ticket"><span class="dot amber"></span>金樽・浪高 1.8m</div>
    <div class="ticket"><span class="dot red"></span>外澳・浪高 1.9m</div>
  </div>
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
    <p>烏石港衝浪教室聚集地，租板／換裝設施齊全，開車到國5頭城交流道下來 或搭火車到頭城站再轉乘計程車，都方便抵達。</p>'''

beginner_content = '''    <p>新手選浪點，比起「哪裡浪比較大」，更該問「哪裡出錯的代價比較低」。三個簡單原則：地形以沙灘為主、避開整片礁岩區；浪高最好落在機器人 GoOcean 分級的 🟢 初學區間（浪高 1.2m 以下、週期 7 秒以下）；離岸流少，或至少流的位置固定、看得出來。</p>

    <h2>北部：烏石港</h2>
    <p>沙灘與礁岩混合地形，衝浪教室聚集地，租板、換裝設施齊全。防波堤內側是主要練習區，退潮前後兩小時浪型比較有型。<strong>但防波堤北側礁岩區退流不小</strong>，新手不建議靠過去。</p>

    <h2>中部：外埔漁港</h2>
    <p>沙灘型浪點，浪通常偏小，很適合單純練習划水的階段。底質偏砂泥，跌倒摔板的代價比礁岩區低很多，但一樣要留意離岸流位置。</p>

    <h2>南部：台南漁光島</h2>
    <p>沙灘型浪點，浪小適合長板，是南部新手很常去的起點。要注意的是岸邊砂洲會隨潮汐變化，退潮時水深、流向都可能跟漲潮時不一樣。</p>

    <h2>下水前，先查一次即時浪況</h2>
    <p>上面三個是「平常表現」比較穩定的新手浪點，但沒有哪個浪點是「永遠安全」——同一個浪點，颱風前後或東北季風增強時，照樣可能超出新手能應付的範圍。加 LINE 浪況機器人好友，出發前打浪點名稱查一次即時浪高、風向、潮汐，比看這篇文章更準。</p>'''

current_conditions_content = '''    <p>很多人挑浪點只看「今天浪高幾公尺」，但同樣 0.8m 的浪，陸風配退潮跟onshore配滿潮，海況可以差很多。這篇整理下水前該一起看的幾件事。</p>

    <h2>離岸流：三個辨識徵兆</h2>
    <ul>
      <li>水色明顯比周圍混濁，像一條顏色不同的水道</li>
      <li>浪快要碎的區域，那條水道卻沒有白沫</li>
      <li>水面出現一排跟岸邊垂直（不是平行）的小波紋</li>
    </ul>
    <p>看到這三個徵兆同時出現，那多半就是離岸流的位置——不一定要完全避開（有經驗者甚至會利用離岸流快速划出去），但新手至少要知道它在哪，不要傻傻站在裡面對抗它。</p>

    <h2>陸風（offshore）跟 onshore 差在哪</h2>
    <p>陸風從岸上吹向海面，會把浪面「壓」得比較乾淨、浪型漂亮；onshore 風從海面吹向岸邊，會把浪面吹得破碎雜亂，看起來浪高差不多，實際上難抓好浪型很多。這也是為什麼機器人的浪點資料裡，每個點都會標記「陸風方向」——出發前風向對不對，比浪高數字更該優先看。</p>

    <h2>潮汐怎麼影響海況</h2>
    <p>同一個浪點，滿潮跟退潮的海況可能完全不同：礁岩型浪點退潮容易礁石裸露、水深變淺，危險度上升；沙灘型浪點則常是退潮前後兩小時浪型最乾淨。機器人查單一浪點時會附上今日潮汐時刻，出發前可以順便看一眼。</p>

    <h2>GoOcean 分級對照</h2>
    <p>機器人每則浪況推播都會附上分級燈號，判斷邏輯大致是：</p>
    <ul>
      <li>🟢 初學：浪高 0.8m 以下，或週期短的小浪</li>
      <li>🟡 中階：浪高 0.8～1.8m 左右</li>
      <li>🔴 進階：浪高 1.8m 以上，或浪不大但週期很長（長湧浪能量大）</li>
      <li>⛔ 危險封閉：浪高 3m 以上，或大浪配長週期</li>
    </ul>
    <p>加 LINE 好友、打浪點名稱查詢，就能同時看到浪高、風向、潮汐跟這個分級燈號，比單看一項數字更能判斷海況。</p>'''

CONTENT_MAP = {
    "wushi-gang": wushi_content,
    "beginner-spots": beginner_content,
    "current-conditions": current_conditions_content,
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

def article_detail(a):
    date = "2026.07.15" if a["id"]=="wushi-gang" else ("2026.07.24" if not a["stub"] else "草稿・尚未發布")
    stat_line = '<span class="stat">浪高 0.8–1.6m</span><span class="stat">週期 6–9s</span><span>適合｜初學～中階</span>' if a["id"]=="wushi-gang" else ('<span class="stat">衝浪知識</span>' if not a["stub"] else '<span class="stat">示範資料</span>')
    body_content = CONTENT_MAP.get(a["id"]) or stub_content(a)
    ph_label = "封面照片預留位置（之後換成烏石港實拍照）" if a["id"] == "wushi-gang" else "封面照片預留位置（之後可換成實拍照）"

    art_body = f'''{nav("../", "articles")}
<div class="article-divider" style="margin-top:1.5rem;"><span>{a["tag"]}</span><div class="line"></div></div>
<article class="article">
  <div class="art-hero">
    <div class="ph"></div>
    <span class="ph-label">{ph_label}</span>
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
    <span>📧 hello@tidelog.example</span>
    <span>📍 台灣</span>
  </div>

  <form class="contact-form" action="mailto:hello@tidelog.example" method="post" enctype="text/plain">
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
  </form>

  <p class="form-note">目前用的是最簡單的 mailto 表單（點送出會開啟你自己的信箱軟體寄信，不是即時送到後台），
  之後想要「填完直接送到資料庫/信箱」的正式表單，可以接 Formspree、Google 表單，或串一個小後端，我可以幫你接。</p>
</div>

{footer("./")}'''

with open(f"{ROOT}/contact.html", "w") as f:
    f.write(head("./", "聯絡我們", "聯絡浪誌 TIDELOG") + contact_body + FOOT)

# ─────────────────────────────────────────────────────────
# subscribe.html
subscribe_body = f'''{nav("./", "subscribe")}
<div class="simple-page">
  <h1>訂閱最新浪況</h1>
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
  <p class="lead">加好友後，還要完成這一步，才會真的收到每天 05:00 的浪況早報。</p>

  <form id="subscribe-form" class="contact-form">
    <div class="form-field">
      <label for="s-email">Email（選填）</label>
      <input id="s-email" name="email" type="email" placeholder="your@email.com">
    </div>
    <div class="form-field">
      <label for="s-line-id">LINE User ID <span class="req">＊必填</span></label>
      <input id="s-line-id" name="line_id" type="text" placeholder="Uxxxxxxxxxxx" required>
    </div>
    <p class="form-hint">💡 還不知道自己的 LINE ID？傳「我的ID」給浪況機器人，它會回覆給你。</p>
    <button class="btn primary form-submit" type="submit">🏄 開通推播</button>
    <p id="subscribe-result" class="form-result" role="status" aria-live="polite"></p>
  </form>
</div>

<script>
(function () {{
  const API_URL = "{RENDER_API_URL}/subscribe";
  const form   = document.getElementById("subscribe-form");
  const result = document.getElementById("subscribe-result");
  const submit = form.querySelector(".form-submit");

  form.addEventListener("submit", async function (e) {{
    e.preventDefault();
    result.className = "form-result";
    result.textContent = "傳送中，若機器人剛好在休眠可能要等 30-60 秒⋯⋯";

    const email  = document.getElementById("s-email").value.trim();
    const lineId = document.getElementById("s-line-id").value.trim();

    submit.disabled = true;
    try {{
      const resp = await fetch(API_URL, {{
        method: "POST",
        headers: {{ "Content-Type": "application/json" }},
        body: JSON.stringify({{ email: email, line_id: lineId }}),
      }});
      const data = await resp.json();
      result.textContent = data.message || (resp.ok ? "訂閱成功！" : "發生錯誤，請稍後再試");
      result.className = "form-result " + (resp.ok ? "ok" : "err");
    }} catch (err) {{
      result.textContent = "連線失敗，請確認網路後再試一次";
      result.className = "form-result err";
    }} finally {{
      submit.disabled = false;
    }}
  }});
}})();
</script>

{footer("./")}'''

with open(f"{ROOT}/subscribe.html", "w") as f:
    f.write(head("./", "訂閱最新浪況", "訂閱浪誌 TIDELOG 最新浪況與文章通知") + subscribe_body + FOOT)

print("contact.html + subscribe.html written")
