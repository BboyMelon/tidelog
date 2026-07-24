#!/usr/bin/env python3
import os

# ROOT 自動抓「這個腳本所在資料夾的上一層」= tidelog-site/ 專案根目錄
# 所以不管在誰的電腦上，只要資料夾結構不變，這個腳本都能正常執行
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)

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
    <a href="#">依地區篩選 →</a>
  </div>
  <div class="spot-grid">
    <div class="spot-card">
      <div class="row1"><h3>烏石港</h3><span class="region">北部</span></div>
      <div class="stats-row">
        <div class="stat-block"><div class="label">陸風</div><div class="val">西南</div></div>
        <div class="stat-block"><div class="label">難度</div><div class="val">初～中階</div></div>
      </div>
      <div class="level-pill"><span class="dot" style="background:#3fce8a"></span>適合初學</div>
      <p class="safety">防波堤北側礁岩區，注意退流</p>
    </div>
    <div class="spot-card">
      <div class="row1"><h3>宜蘭外澳</h3><span class="region">北部</span></div>
      <div class="stats-row">
        <div class="stat-block"><div class="label">陸風</div><div class="val">西南</div></div>
        <div class="stat-block"><div class="label">難度</div><div class="val">進階</div></div>
      </div>
      <div class="level-pill"><span class="dot" style="background:#ff5b5b"></span>浪大刺激</div>
      <p class="safety">注意防波堤旁離岸流</p>
    </div>
    <div class="spot-card">
      <div class="row1"><h3>台南漁光島</h3><span class="region">南部</span></div>
      <div class="stats-row">
        <div class="stat-block"><div class="label">陸風</div><div class="val">東北</div></div>
        <div class="stat-block"><div class="label">難度</div><div class="val">初學</div></div>
      </div>
      <div class="level-pill"><span class="dot" style="background:#3fce8a"></span>適合長板</div>
      <p class="safety">注意岸邊砂洲與潮汐變化</p>
    </div>
    <div class="spot-card">
      <div class="row1"><h3>恆春南灣</h3><span class="region">南部・恆春</span></div>
      <div class="stats-row">
        <div class="stat-block"><div class="label">陸風</div><div class="val">東北</div></div>
        <div class="stat-block"><div class="label">難度</div><div class="val">初～中階</div></div>
      </div>
      <div class="level-pill"><span class="dot" style="background:#f4b13a"></span>夏季熱門</div>
      <p class="safety">人潮多，夏季水母頻繁</p>
    </div>
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
    date = "2026.07.15" if a["id"]=="wushi-gang" else "草稿・尚未發布"
    stat_line = '<span class="stat">浪高 0.8–1.6m</span><span class="stat">週期 6–9s</span><span>適合｜初學～中階</span>' if a["id"]=="wushi-gang" else '<span class="stat">示範資料</span>'
    body_content = wushi_content if a["id"]=="wushi-gang" else stub_content(a)
    ph_label = "封面照片預留位置（之後換成實拍照）" if a["id"] != "wushi-gang" else "封面照片預留位置（之後換成烏石港實拍照）"

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
contact_body = f'''{nav("./", "")}
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
subscribe_body = f'''{nav("./", "")}
<div class="simple-page">
  <h1>訂閱最新浪況</h1>
  <p class="lead">留下 Email，新文章、浪點更新、突發好浪通知，第一時間收到。</p>

  <form class="subscribe-form" onsubmit="return false;">
    <div class="subscribe-row">
      <input type="email" placeholder="你的 email" required>
      <button class="btn primary" type="submit">訂閱</button>
    </div>
  </form>

  <ul class="subscribe-perks">
    <li>每週浪況精選整理，不用自己每天查</li>
    <li>新浪點文章上架第一時間通知</li>
    <li>偶爾才有的裝備開箱／優惠資訊</li>
  </ul>

  <p class="form-note">這裡目前只是畫面樣式，按「訂閱」還不會真的收集 email。
  正式上線前需要接一個電子報服務（例如 Mailchimp、Buttondown、電子豹），
  或至少先串一個 Google 表單頂著用，我可以幫你接好。</p>
</div>

{footer("./")}'''

with open(f"{ROOT}/subscribe.html", "w") as f:
    f.write(head("./", "訂閱最新浪況", "訂閱浪誌 TIDELOG 最新浪況與文章通知") + subscribe_body + FOOT)

print("contact.html + subscribe.html written")
