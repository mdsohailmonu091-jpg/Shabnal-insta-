# 📱 Shabnal Perfumes — Instagram Automation Setup (Hindi Guide)

Ye system **roz automatically** karta hai:
1. 📝 **Script likhta hai** — product + festival/season ke hisab se (30 din ka bank + Diwali/Eid/Navratri specials)
2. 🖼️ **Post image banata hai** — aapki real photos, gold-black brand design (1080x1350)
3. 🎬 **Reel video banata hai** — 15 sec vertical video, slow-zoom + text (1080x1920)
4. 📤 **Post karta hai** — ya draft folder me save karta hai

**Kharcha: ₹0** — GitHub free + Cloudinary free + content bank free. (AI captions optional, paid.)

---

## LEVEL 1 — Abhi yahi se chalao (2 minute, koi setup nahi)

Jab bhi content chahiye, bas mujhse (Arena assistant se) kaho **"aaj ka Insta content bana do"** —
mai `outbox/2026-09-21/` jaisi folder me tayaar karke de dunga:
- `post_4x5.jpg` — feed post image
- `reel_9x16.mp4` — reel video
- `caption.txt` + `reel_caption.txt` — copy-paste captions with hashtags

Phir aap Instagram app se manually post kar do (2 minute ka kaam).

> Manual posting ka FAYDA: app me **trending audio** laga sakte ho = zyada reach! 🚀

---

## LEVEL 2 — GitHub par FREE daily automation (RECOMMENDED ⭐)

Ek baar 20 minute setup → phir **roz subah 9 baje** content khud ban jayega.

### Step 1: GitHub account banao
1. [github.com](https://github.com) par free account banao (email se).
2. **New repository** → naam: `shabnal-insta` → **Public** → Create.

### Step 2: Ye folder upload karo
1. Repo me **"uploading an existing file"** par click karo.
2. Is `instagram-automation` folder ki **saari files** drag-drop karo (assets/ + outbox khaali bhi chalega, `.github/` zaroor!).
3. **Commit changes** dabao.

### Step 3: Daily schedule ON
- Bas! `.github/workflows/daily-post.yml` pehle se andar hai.
- Roz subah 9 baje GitHub khud `daily.py` chalayega.
- Bane hue files: repo → **Actions** tab → aaj ka run → neeche **Artifacts → todays-content** → Download.
- Download karke Instagram app se post karo + trending audio lagao. 🎵

> Manual check: Actions tab → "Daily Instagram Content" → **Run workflow** button se kabhi bhi turant bana sakte ho.

---

## LEVEL 3 — 100% Auto-Post (bina haath lagaye Instagram par post)

Iske liye 2 free cheezein chahiye: **Meta token** + **Cloudinary link**.

### A. Instagram ko taiyaar karo (5 min)
1. Instagram app → apna Shabnal account → **Settings → Account type → Switch to Professional → Business**.
2. Facebook par ek **Page** banao (naam: Shabnal Perfumes).
3. IG app → Settings → **Business tools → Facebook Page se link** karo (wahi Page select karo).

### B. Meta access token banao (10 min)
1. Computer par [developers.facebook.com](https://developers.facebook.com) kholo → **Get Started** → Developer account banao.
2. **Create App** → type **Business** → naam `Shabnal Auto Post` → Create.
3. Left menu → **App settings → Basic** → neeche apna App ID/Secret dikhega (likh lo).
4. [Graph API Explorer](https://developers.facebook.com/tools/explorer/) kholo:
   - Apna App select karo → **Generate Access Token** → apna Facebook account → apne **Page** ko saare rights de do.
   - **Permissions** me ye add karo: `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`.
5. Explorer me query chalao: `me/accounts` → apne Page ka **ID** note karo.
6. Query: `{PAGE-ID}?fields=instagram_business_account` → **IG_USER_ID** note karo. (e.g. `1784140...`)
7. Token ko 60-din wala (long-lived) banao — browser me ye link kholo (APP-ID/SECRET/TOKEN badal kar):
   `https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id=APP-ID&client_secret=APP-SECRET&fb_exchange_token=TOKEN`
   - Jo `access_token` mile, wahi asli token hai. Notepad me save karo.

### C. Cloudinary free account (3 min)
1. [cloudinary.com](https://cloudinary.com) → free Sign Up.
2. **Dashboard** par `CLOUDINARY_URL` dikhega: `cloudinary://API_KEY:API_SECRET@CLOUD_NAME` — poora copy karo.
3. (Ye sirf photo/video ko public link dene ke liye hai — Instagram API ko public link chahiye hota hai.)

### D. GitHub Secrets me dalo (3 min)
Repo → **Settings → Secrets and variables → Actions → New repository secret**:
- `IG_USER_ID` = Step B ka number
- `IG_ACCESS_TOKEN` = Step B ka token
- `CLOUDINARY_URL` = Step C ka link

Bas! Agli subah 9 baje se **post + reel dono khud Instagram par publish** honge. 🎉
Test karne ke liye: **Actions → Run workflow** dabao aur 5 min me apna Instagram check karo!

### ⚠️ Token renew (har 60 din, 5 min kaam)
Meta ka token ~60 din me expire hota hai. Phone me reminder lagao: **"Insta token renew"**.
Renew: Step B-7 wali link dobara kholo (naya short token lekar) → GitHub Secret update karo. Bas.

---

## 📅 Festival calendar (pehle se andar!)

System in dates par **khud special festive post+reel** banata hai:
| Date | Festival | Date | Festival |
|---|---|---|---|
| 25 Sep 2026 | Ganpati Visarjan | 8 Nov 2026 | **Diwali** 🪔 |
| 11 Oct 2026 | Navratri start | 11 Nov 2026 | Bhai Dooj |
| 20 Oct 2026 | Dussehra | 15 Nov 2026 | Chhath Puja |
| 29 Oct 2026 | Karwa Chauth | 25 Dec 2026 | Christmas |
| 6 Nov 2026 | Dhanteras | 31 Dec 2026 | New Year |

*(Diwali 8 Nov, Dussehra 20 Oct 2026 — confirmed festival calendar.)*
Naya festival jodna ho to `content_bank.py` → `FESTIVALS` me date + script add karo (ya mujhse bol do!).

## 🎵 Trending audio ka funda (reach badhane ke liye)
- **Auto-posted reels me trending music NAHI lagta** (Meta ka rule) — isliye video me awaaz nahi hoti.
- **Best strategy (hybrid):** Auto-post ON rakho + hafte me 2 reels app se khud trending audio lagakar post karo.
- Har hafte `trends.txt` ki pehli line me trending audio ka naam likh do — system use reel-caption me jod dega.

## 🕚 Best posting time
- Feed post: **11am–1pm** | Reel: **7–9pm** (IST)
- Schedule badalna ho: `.github/workflows/daily-post.yml` me `cron` line badlo (UTC time me).

## 🛠️ Problems? (Troubleshooting)
| Problem | Solution |
|---|---|
| `ffmpeg not found` | `pip install imageio-ffmpeg` chalao |
| Photo post hui, reel fail | Video bada tha — 1-2 min baad Run workflow dobara karo |
| Error `#190` / token invalid | Token expire — Step B-7 se renew karo |
| Caption me ajeeb boxes | Image-text me emoji mat likho (caption me OK) |
| GitHub Action hi nahi chala | Repo **Public** hona chahiye; Actions tab me enable karo |

## 📁 Files ka matlab
| File | Kaam |
|---|---|
| `daily.py` | Roz ka engine — sab kuch yahi se chalta hai |
| `content_bank.py` | 30 din ki scripts + captions + festivals (edit kar sakte ho!) |
| `designer.py` | Post image banata hai (PIL) |
| `reel_maker.py` | Reel video banata hai (ffmpeg) |
| `publisher.py` | Instagram par post karta hai |
| `ai_writer.py` | (Optional) AI se roz naye captions — `AI_API_KEY` secret chahiye |
| `trends.txt` | Hafte ka trending audio yahan likho |
| `assets/` | Aapki product photos + backgrounds |
| `outbox/` | Roz ka tayaar maal (date-wise folder) |

**Naya product aaye?** Uski photo `assets/` me dalo + `content_bank.py` me 2-4 scripts add karo (ya mujhse bol do — mai kar dunga! 😊)
