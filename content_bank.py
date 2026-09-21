"""30-day rotating content bank + festival specials for Shabnal Perfumes.

- hook/sub  -> printed ON the image (plain text only, no emoji)
- caption   -> Instagram caption (Hinglish + emojis OK)
- hashtags auto-appended by daily.py (3 rotating sets)
"""

HASHTAG_SETS = [
    "#ShabnalPerfumes #OudRose #EternalRomance #ExtraitDeParfum #LongLastingPerfume #PerfumeLovers #FragranceAddict #DesiLuxury #VaranasiShopping #PerfumeCollection #LuxuryPerfumeIndia #AttarLovers #SmellGoodFeelGood #NicheFragrance #PerfumeGram",
    "#PerfumeReels #FragranceLovers #PerfumeAddictIndia #GoodVibeOnly #FeelTheGlow #DailyPerfume #PocketPerfume #TravelFriendly #ComboOffer #GiftIdeasIndia #OnlineShoppingIndia #SmallBusinessIndia #SupportSmallBusiness #ReelsIndia #FragranceCommunity",
    "#FestiveSeasonIndia #WeddingSeasonReady #GiftForHim #GiftForHer #ShaadiSeason #IndianFestivals #PerfumeGiftSet #GiftingIdeas #FestiveVibes #EthnicWearLove #CelebrationTime #FestivalOfLights #PoojaVibes #DiwaliGifts2026 #PerfumeLoversIndia",
]

# ---------------------------------------------------------------- POSTS (30)
POSTS = [
 {"product": "oud_rose", "hook": "OUD ROSE", "sub": "Eternal Romance - Extrait de Parfum",
  "caption": "Jab baat ho ROYAL mehke ki... 👑🌹\n\nOUD ROSE - Eternal Romance. Shahi oud + romantic gulab ka woh blend jo logon ko majboor kar de poochne par - \"yeh khushboo kaunsi hai?\" 😍\n\n✨ Extrait de Parfum (sabse strong)\n⏰ 12+ ghante long lasting\n🎁 Gifting ke liye perfect\n\n📩 Order: DM ya WhatsApp 90263 99218"},

 {"product": "good_vibe", "hook": "GOOD VIBE", "sub": "Feel The Glow - Daily Freshness",
  "caption": "Monday ho ya Sunday... VIBE hamesha GOOD rakho! ✨😎\n\nGOOD VIBE - Feel The Glow. Fresh, halki aur positive energy wali khushboo - roz college, office ya outing ke liye best! 🌞\n\n💫 Fresh citrus + floral glow\n⏰ Subah se shaam tak saath\n💰 Pocket-friendly luxury\n\n📩 Order: DM ya WhatsApp 90263 99218"},

 {"product": "all_mine", "hook": "ALL MINE", "sub": "Keep It Close - Pocket Luxury 20ml",
  "caption": "Badi khushboo, chhoti bottle! 😍\n\nALL MINE - Keep It Close. 20ml pocket spray jo jeep, bag ya car me aasani se fit. Kahin bhi, kabhi bhi - ek spray aur fresh! 💨\n\n👝 Travel + office friendly\n⚡ Instant freshness on-the-go\n🎁 Combo me aur bhi best deal\n\n📩 Order: DM ya WhatsApp 90263 99218"},

 {"product": "combo", "hook": "COMBO SET", "sub": "Oud Rose 50ml + All Mine 20ml",
  "caption": "SMART log COMBO lete hain! 🧠🎁\n\nOUD ROSE (50ml) ghar ke liye + ALL MINE (20ml) safar ke liye = COMPLETE luxury ritual! Gifting ke liye toh isse best kuch nahi 💛\n\n🏠 Badi bottle - dressing table ke liye\n👝 Chhoti bottle - pocket ke liye\n💝 Elegant gift-ready packing\n\n📩 Combo order: DM ya WhatsApp 90263 99218"},

 {"product": "oud_rose", "hook": "12+ GHANTE?", "sub": "Asli Extrait de Parfum ki pehchan",
  "caption": "Normal perfume 2-3 ghante... Shabnal 12+ GHANTE?! 🤯\n\nRaaz hai EXTRAIT DE PARFUM - sabse zyada oil concentration. Matlab gehra, ameer aur lambe samay tak rehne wali mehak! 💪\n\n👔 Kapdon par: 12+ ghante\n🤵 Skin par: 6-8 ghante\n💧 Sirf 2-3 spray kaafi\n\n📩 Try karo: DM / WhatsApp 90263 99218"},

 {"product": "oud_rose", "hook": "SHAHI OUD", "sub": "Royal oud + Taif rose ka sangam",
  "caption": "Oud - duniya ka sabse KEEMTI khushboo wala lakda 🪵👑 Aur usme mile romantic rose... = OUD ROSE, Eternal Romance 🌹\n\nYeh sirf perfume nahi, ek EHSAAS hai. Shaadi, party ya special dinner - jahan jao, mehak pehle pahunche! ✨\n\n📩 Order: DM ya WhatsApp 90263 99218"},

 {"product": "combo", "hook": "GIFTING SEASON", "sub": "Kya gift dein? Tension khatam!",
  "caption": "Gift me kya dein - yeh sawaal ab khatam! 🎁😌\n\nShabnal COMBO SET - elegant packing, royal khushboo, aur budget me luxury. Rishtedaar ho ya dost, boss ho ya partner - sab khush! 💛\n\n💒 Shaadi / Engagement\n🎂 Birthday / Anniversary\n🪔 Festivals\n\n📩 Gift order: DM / WhatsApp 90263 99218"},

 {"product": "good_vibe", "hook": "MORNING RITUAL", "sub": "2 spray = poore din ka confidence",
  "caption": "Successful logon ki ek aadat: subah ka SIGNATURE SCENT! ☀️💼\n\nGOOD VIBE lagao aur niklo - fresh, confident aur positive. Pehla impression hi LASTING impression banta hai! 😎\n\n🎯 Office / College / Business\n💫 Halki, fresh, kabhi tez nahi\n⏰ Din bhar saath\n\n📩 Order: DM ya WhatsApp 90263 99218"},

 {"product": "all_mine", "hook": "POCKET ME RAKHO", "sub": "Bag, car, office drawer - kahin bhi",
  "caption": "Meeting se pehle? Date se pehle? Selfie se pehle? 📸😉\n\nALL MINE pocket spray - 2 second me freshness wapas! Chhoti bottle, bada confidence 💪\n\n🚗 Car dashboard me rakho\n💼 Office drawer me rakho\n👝 Har bag me ek hona chahiye\n\n📩 Order: DM ya WhatsApp 90263 99218"},

 {"product": "oud_rose", "hook": "LOG POOCHENGE", "sub": "\"Yeh perfume kaunsa hai?!\"",
  "caption": "\"Bhai, yeh khushboo KAUNSI hai?!\" 😍 - yeh sunne ke liye ready ho jao!\n\nOUD ROSE pehen ne walon se aksar log poochte hain. Kyunki yeh bheed wali mehak NAHI hai - yeh SIGNATURE hai! 👑🌹\n\n📩 Apna signature banao: DM / WhatsApp 90263 99218"},

 {"product": "good_vibe", "hook": "SUMMER FRESH", "sub": "Paseene ki tension? Bhool jao!",
  "caption": "Garmi + paseena = embarrassment? 😓 NOT ANYMORE!\n\nGOOD VIBE ki fresh khushboo paseene ki smell ko door rakhe aur aapko cool-confident! Roz nahao, spray karo, niklo! 🚿✨\n\n🌞 Garmi ka best dost\n💨 Freshness lock\n😎 Confidence unlock\n\n📩 Order: DM ya WhatsApp 90263 99218"},

 {"product": "combo", "hook": "2 BOTTLES", "sub": "1 price me double khushi!",
  "caption": "1+1 = DOUBLE KHUSHI! 🎁🎁\n\nCOMBO SET: Oud Rose 50ml (ghar) + All Mine 20ml (safar). Alag-alag lene se behtar - COMBO me lo aur smart bano! 🧠\n\n✅ Dono bestsellers ek saath\n✅ Gift-ready packing\n✅ Best value deal\n\n📩 DM / WhatsApp: 90263 99218"},

 {"product": "oud_rose", "hook": "NIGHT PARTY?", "sub": "Raat ko mehakna hai toh Oud Rose",
  "caption": "Shaadi, reception ya night party... 🌙✨ Raat ki mehfil me OUD ROSE jaisa koi nahi!\n\nGehra oud + gulab - andhere me bhi aapki presence chamke! Log bhool jayenge sab, aapki khushboo NAHI! 😍\n\n📩 Party ready? DM / WhatsApp 90263 99218"},

 {"product": "good_vibe", "hook": "DAILY WEAR", "sub": "Roz ka perfume, roz ka glow",
  "caption": "Kuch perfumes roz nahi lagaye ja sakte... GOOD VIBE unme se NAHI! 🌞\n\nHalka, fresh, sweet - roz lagao, roz glow karo. College ho ya office, yeh kabhi over-powering nahi lagta! 💛\n\n📩 Roz ka saathi: DM / WhatsApp 90263 99218"},

 {"product": "oud_rose", "hook": "PERFUME TIPS", "sub": "Pulse points par lagao - 3x lasting!",
  "caption": "PERFUME HACK jo 90% log nahi jaante! 🤯👇\n\n1️⃣ Gardan ke sides (neck)\n2️⃣ Kalai (wrists) - ragdo MAT!\n3️⃣ Kaan ke peeche\n4️⃣ Kapdon par halka spray\n\nPulse points ki garmi khushboo ko dheere-dheere failati hai = 3X zyada lasting! 🔥\n\n📩 Shabnal order: DM / WhatsApp 90263 99218"},

 {"product": "all_mine", "hook": "TRAVEL BESTIE", "sub": "Safar me freshness ka saathi",
  "caption": "Train ho ya flight, bus ho ya bike... 🏍️✈️ Safar me ALL MINE saath = hamesha fresh!\n\n20ml - airport security friendly, leak-proof, pocket size. Smart travellers ka secret! 😉👝\n\n📩 Travel buddy: DM / WhatsApp 90263 99218"},

 {"product": "combo", "hook": "COUPLE GOALS?", "sub": "His + Hers - ek combo, do dil!",
  "caption": "Couple ho? Toh yeh combo TUMHARE liye! 💑💛\n\nOud Rose (bold & royal) + All Mine (fresh & sweet) - dono ki pasand ek pack me! Anniversary gift ke liye PERFECT 🎁\n\n📩 DM / WhatsApp: 90263 99218"},

 {"product": "oud_rose", "hook": "UNISEX LUXURY", "sub": "Uske liye bhi, uske liye bhi!",
  "caption": "Khushboo ka koi GENDER nahi hota! 💛\n\nOUD ROSE - mardon par royal, auraton par elegant. Unisex luxury jo har kisi par jache! 👔👗🌹\n\n📩 Order: DM ya WhatsApp 90263 99218"},

 {"product": "good_vibe", "hook": "MOOD BOOSTER", "sub": "Stress? Ek spray aur smile!",
  "caption": "Science kehta hai: achchi khushboo MOOD behtar karti hai! 🧠✨\n\nGOOD VIBE - naam hi kaafi hai! Stressful din me ek spray = instant positivity 😊💫\n\n📩 Good mood order karo: DM / WhatsApp 90263 99218"},

 {"product": "combo", "hook": "CUSTOMER LOVE", "sub": "Subah lagaya, shaam tak mehak!",
  "caption": "⭐⭐⭐⭐⭐ CUSTOMER REVIEW:\n\n\"Oud Rose ki khushboo LAJAWAB! Subah lagaya, shaam tak kapdon me mehak rahi. Pure paise vasool!\" - Arif K. 🙏\n\nAap bhi try karo - nirasha NAHI hogi, guarantee! 💛\n\n📩 Order: DM / WhatsApp 90263 99218"},

 {"product": "oud_rose", "hook": "ROYAL WEDDINGS", "sub": "Dulha ho ya mehmaan - chamko!",
  "caption": "Shaadi season aa raha hai! 💒✨ Dulha ho, dulhan ho ya BARAATI - OUD ROSE ke bina look ADHOORA!\n\nSherwani ho ya lehenga, royal khushboo se hi baat banti hai! 👑🌹\n\n📩 Shaadi shopping: DM / WhatsApp 90263 99218"},

 {"product": "all_mine", "hook": "OFFICE SECRET", "sub": "Promotion khushboo se? Try karo!",
  "caption": "Fun fact: achchi khushboo wale log zyada CONFIDENT aur SUCCESSFUL lagte hain! 💼📈\n\nALL MINE desk me rakho - har meeting se pehle ek spray. Small habit, BIG impression! 😉\n\n📩 Office essential: DM / WhatsApp 90263 99218"},

 {"product": "good_vibe", "hook": "COLLEGE STAR", "sub": "Campus me sabse alag dikho!",
  "caption": "College me 500 students... par khushboo sirf TUMHARI yaad rahe! 🎓✨\n\nGOOD VIBE - fresh, cool aur budget-friendly. Doston me trend-setter bano! 😎🔥\n\n📩 Student special: DM / WhatsApp 90263 99218"},

 {"product": "combo", "hook": "FAMILY PACK?", "sub": "Ghar me sabke liye kuch!",
  "caption": "Papa ko oud pasand, bhai ko fresh? 🤔 Dono khush - COMBO SET se! 👨‍👩‍👦💛\n\nEk pack, do khushboo, poora parivaar khush. Ghar-ghar ki pasand - SHABNAL! 🏠\n\n📩 Family order: DM / WhatsApp 90263 99218"},

 {"product": "oud_rose", "hook": "ATTAR VS SPRAY?", "sub": "Dono ka best - Extrait de Parfum!",
  "caption": "Attar lagana pasand par spray ki aasani chahiye? 🤔\n\nShabnal EXTRAIT DE PARFUM = attar jaisa gehra oil + spray ki aasani! Dono jahan ka best! 🪔💨👌\n\n📩 Best of both: DM / WhatsApp 90263 99218"},

 {"product": "good_vibe", "hook": "GYM FRESH?", "sub": "Workout ke baad bhi fresh!",
  "caption": "Gym bag me kya hai? Dumbbells? Towel? ...aur GOOD VIBE? 💪😉\n\nWorkout ke baad ek spray = paseene ki smell GONE, freshness ON! Gym buddies bhi poochenge! 🏋️✨\n\n📩 Gym essential: DM / WhatsApp 90263 99218"},

 {"product": "all_mine", "hook": "DATE NIGHT?", "sub": "Pehli mulaqat, lasting yaad!",
  "caption": "Date par ja rahe ho? 💘 Suno - log CHEHRA bhool sakte hain, KHUSHBOO nahi!\n\nALL MINE pocket me rakho - mulaqat se pehle ek spray. Pehla impression = BEST impression! 😍✨\n\n📩 Date ready: DM / WhatsApp 90263 99218"},

 {"product": "combo", "hook": "BESTSELLER", "sub": "Sabse zyada bikne wala combo!",
  "caption": "🔥 SABSE ZYADA BIKNE WALA COMBO! 🔥\n\nOud Rose 50ml + All Mine 20ml - hazaaron khush customers ki pasand! Stock limited, demand HIGH! ⏰\n\nDer mat karo - aaj hi order karo! 👇\n📩 DM / WhatsApp: 90263 99218"},

 {"product": "oud_rose", "hook": "SMELL RICH", "sub": "Luxury ab har pocket me!",
  "caption": "5000 wale perfume wali FEEL... pocket-friendly price me?! 🤯💛\n\nOUD ROSE - premium oud-rose luxury jo har kisi ke budget me! SMELL RICH, spend smart! 👑🌹\n\n📩 Price jaanne ke liye: DM / WhatsApp 90263 99218"},

 {"product": "good_vibe", "hook": "THANK YOU!", "sub": "Aapke pyaar ke liye shukriya!",
  "caption": "30 din, 30 khushboo... aur HAZAARON muskaan! 🙏💛\n\nShabnal parivaar ka hissa banne ke liye SHUKRIYA! Aapka pyaar hi hamari asli kamai hai. Comment me batao - aapki favourite kaunsi? 👇\n\n🌹 Oud Rose | ✨ Good Vibe | 👝 All Mine\n\n📩 Order: DM / WhatsApp 90263 99218"},
]

# ---------------------------------------------------------------- REELS (30)
REELS = [
 {"title": "Oud Rose reveal", "product": "oud_rose",
  "scenes": [{"img": "oud_rose", "text": "OUD ROSE", "sub": "Eternal Romance"},
             {"img": "bg_rose", "text": "Shahi Oud + Gulab", "sub": "Royal blend"},
             {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "POV: Tumne OUD ROSE lagaya aur poora room mehke gaya! 🌹👑 #POV #PerfumeReveal\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending luxury/love audio"},

 {"title": "Good Vibe energy", "product": "good_vibe",
  "scenes": [{"img": "good_vibe", "text": "GOOD VIBE", "sub": "Feel The Glow"},
             {"img": "bg_smoke", "text": "Fresh All Day", "sub": "Subah se shaam"},
             {"img": "good_vibe", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Good Vibe lagao, glow karo! ✨ Morning routine ka hero 🌞 #GoodVibesOnly\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending morning-aesthetic audio"},

 {"title": "Pocket spray hack", "product": "all_mine",
  "scenes": [{"img": "all_mine", "text": "ALL MINE", "sub": "Keep It Close"},
             {"img": "bg_smoke", "text": "Pocket Me Rakho", "sub": "20ml travel spray"},
             {"img": "all_mine", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Bag me yeh nahi hai toh kya hai?! 👝 20ml pocket luxury ✨ #PocketPerfume #TravelHack\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending hack/transition audio"},

 {"title": "Combo unboxing feel", "product": "combo",
  "scenes": [{"img": "combo", "text": "COMBO SET", "sub": "50ml + 20ml"},
             {"img": "oud_rose", "text": "Oud Rose", "sub": "Eternal Romance"},
             {"img": "all_mine", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Unboxing happiness! 🎁 Oud Rose + All Mine combo = double khushi 💛 #Unboxing #ComboOffer\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending unboxing audio"},

 {"title": "12 hour challenge", "product": "oud_rose",
  "scenes": [{"img": "oud_rose", "text": "12+ GHANTE?", "sub": "Challenge accepted"},
             {"img": "bg_rose", "text": "Subah Lagao", "sub": "Shaam tak mehak"},
             {"img": "oud_rose", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "12-HOUR perfume challenge! ⏰ Subah 8 baje lagaya... raat 8 baje bhi mehak! 🤯 #Challenge #LongLasting\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending challenge audio"},

 {"title": "Shahi oud story", "product": "oud_rose",
  "scenes": [{"img": "bg_smoke", "text": "SHAHI OUD", "sub": "Duniya ka keemti itra"},
             {"img": "oud_rose", "text": "OUD ROSE", "sub": "+ Romantic gulab"},
             {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Oud = liquid gold! 🪵👑 Jaano shahi khushboo ka raaz #OudLovers #LuxuryPerfume\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending royal/Arabic audio"},

 {"title": "Gift idea reel", "product": "combo",
  "scenes": [{"img": "bg_festive", "text": "GIFT KYA DEIN?", "sub": "Tension khatam!"},
             {"img": "combo", "text": "COMBO SET", "sub": "Gift-ready packing"},
             {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Best gift idea under budget! 🎁 Koi occasion ho - yeh combo sab khush 💛 #GiftIdeas #GiftingSeason\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending gifting audio"},

 {"title": "Morning routine", "product": "good_vibe",
  "scenes": [{"img": "good_vibe", "text": "MORNING RITUAL", "sub": "2 spray daily"},
             {"img": "bg_rose", "text": "Fresh + Confident", "sub": "Poore din glow"},
             {"img": "good_vibe", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "My 10-second morning glow-up! ☀️✨ #MorningRoutine #GlowUp\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending GRWM audio"},

 {"title": "Before After fresh", "product": "all_mine",
  "scenes": [{"img": "bg_smoke", "text": "BEFORE: Thaka hua", "sub": "After dekho..."},
             {"img": "all_mine", "text": "1 SPRAY", "sub": "All Mine magic"},
             {"img": "all_mine", "text": "AFTER: Fresh!", "sub": "DM 90263 99218"}],
  "caption": "Before vs After - 1 spray ka kamaal! 😱✨ #BeforeAfter #Transformation\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending transition audio"},

 {"title": "People ask me", "product": "oud_rose",
  "scenes": [{"img": "oud_rose", "text": "\"Perfume Kaunsa Hai?\"", "sub": "Sab poochte hain!"},
             {"img": "bg_rose", "text": "OUD ROSE", "sub": "Shabnal Perfumes"},
             {"img": "oud_rose", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "\"Bhai perfume kaunsa hai?!\" - roz sunne ko milta hai 😍🌹 #Compliments #Signature scent\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending confident audio"},

 {"title": "Summer saviour", "product": "good_vibe",
  "scenes": [{"img": "bg_smoke", "text": "GARMI + PASEENA?", "sub": "No tension!"},
             {"img": "good_vibe", "text": "GOOD VIBE", "sub": "Freshness lock"},
             {"img": "good_vibe", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Garmi ka tod! 🌞 Paseene ki smell ko bolo BYE 👋 #SummerEssentials #Freshness\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending summer audio"},

 {"title": "1+1 combo", "product": "combo",
  "scenes": [{"img": "oud_rose", "text": "1. OUD ROSE 50ml", "sub": "Ghar ke liye"},
             {"img": "all_mine", "text": "2. ALL MINE 20ml", "sub": "Safar ke liye"},
             {"img": "combo", "text": "COMBO = SMART!", "sub": "DM 90263 99218"}],
  "caption": "Smart buyers combo lete hain! 🧠🎁 #SmartShopping #ComboDeal\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending shopping audio"},

 {"title": "Night party scent", "product": "oud_rose",
  "scenes": [{"img": "bg_smoke", "text": "NIGHT PARTY?", "sub": "Scent ready?"},
             {"img": "oud_rose", "text": "OUD ROSE", "sub": "Raat ki shaan"},
             {"img": "oud_rose", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Night-out essential! 🌙✨ Bheed me bhi alag dikho #NightParty #PartyReady\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending party audio"},

 {"title": "Daily wear fav", "product": "good_vibe",
  "scenes": [{"img": "good_vibe", "text": "ROZ LAGAO", "sub": "Roz glow karo"},
             {"img": "bg_rose", "text": "GOOD VIBE", "sub": "Daily wear hero"},
             {"img": "good_vibe", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Roz lagane wala perfume mil gaya! 🙌 #DailyWear #EverydayPerfume\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending daily-vlog audio"},

 {"title": "Perfume hack", "product": "oud_rose",
  "scenes": [{"img": "bg_rose", "text": "PERFUME HACK!", "sub": "90% log nahi jaante"},
             {"img": "oud_rose", "text": "Pulse Points", "sub": "3x lasting!"},
             {"img": "oud_rose", "text": "Follow for more", "sub": "DM 90263 99218"}],
  "caption": "Yeh hack try karo - perfume 3X zyada chalega! 🤯 #PerfumeHacks #TipsAndTricks\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending tips audio"},

 {"title": "Travel essential", "product": "all_mine",
  "scenes": [{"img": "all_mine", "text": "TRAVEL ME?", "sub": "Yeh mat bhoolna!"},
             {"img": "bg_smoke", "text": "ALL MINE 20ml", "sub": "Pocket friendly"},
             {"img": "all_mine", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Travel packing me sabse pehle yeh! ✈️👝 #TravelEssentials #PackWithMe\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending travel audio"},

 {"title": "Couple combo", "product": "combo",
  "scenes": [{"img": "oud_rose", "text": "HIS: Oud Rose", "sub": "Bold + Royal"},
             {"img": "good_vibe", "text": "HERS: Good Vibe", "sub": "Fresh + Sweet"},
             {"img": "combo", "text": "Couple Combo!", "sub": "DM 90263 99218"}],
  "caption": "Couple perfume challenge! 💑 Dono ki pasand ek combo me #CoupleGoals #HisAndHers\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending couple audio"},

 {"title": "Unisex luxury", "product": "oud_rose",
  "scenes": [{"img": "oud_rose", "text": "FOR HIM", "sub": "Royal + Bold"},
             {"img": "bg_rose", "text": "FOR HER", "sub": "Elegant + Soft"},
             {"img": "oud_rose", "text": "UNISEX!", "sub": "DM 90263 99218"}],
  "caption": "Khushboo ka gender nahi hota! 💛 #UnisexPerfume #ForEveryone\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending inclusive audio"},

 {"title": "Mood booster", "product": "good_vibe",
  "scenes": [{"img": "bg_smoke", "text": "STRESSED?", "sub": "Try this..."},
             {"img": "good_vibe", "text": "1 SPRAY", "sub": "Good Vibe"},
             {"img": "good_vibe", "text": "MOOD FIXED!", "sub": "DM 90263 99218"}],
  "caption": "Stress ka 10-second ilaaj! 😊✨ #MoodBooster #SelfCare\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending selfcare audio"},

 {"title": "Review reel", "product": "combo",
  "scenes": [{"img": "combo", "text": "5 STAR REVIEW", "sub": "Real customer"},
             {"img": "oud_rose", "text": "\"Pure paise vasool!\"", "sub": "- Arif K."},
             {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Real review, real love! ⭐⭐⭐⭐⭐ #CustomerReview #Testimonial\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending review audio"},

 {"title": "Wedding scent", "product": "oud_rose",
  "scenes": [{"img": "bg_festive", "text": "SHAADI SEASON", "sub": "Scent ready?"},
             {"img": "oud_rose", "text": "OUD ROSE", "sub": "Royal choice"},
             {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Shaadi me dulha-dulhan se zyada mehakna hai? 😜💒 #WeddingSeason #ShaadiReady\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending wedding audio"},

 {"title": "Office hack", "product": "all_mine",
  "scenes": [{"img": "bg_smoke", "text": "MEETING SE PEHLE?", "sub": "1 kaam zaroor karo"},
             {"img": "all_mine", "text": "1 SPRAY", "sub": "Confidence ON"},
             {"img": "all_mine", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Corporate girlie/boy essential! 💼 #OfficeLife #CorporateLife\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending corporate audio"},

 {"title": "College fav", "product": "good_vibe",
  "scenes": [{"img": "good_vibe", "text": "COLLEGE STAR", "sub": "Kaise bano?"},
             {"img": "bg_rose", "text": "GOOD VIBE", "sub": "Signature scent"},
             {"img": "good_vibe", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Campus ka trend-setter! 🎓🔥 #CollegeLife #StudentLife\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending college audio"},

 {"title": "Family pack", "product": "combo",
  "scenes": [{"img": "oud_rose", "text": "PAPA: Oud pasand", "sub": "Royal choice"},
             {"img": "good_vibe", "text": "BHAI: Fresh pasand", "sub": "Cool choice"},
             {"img": "combo", "text": "COMBO = Dono khush!", "sub": "DM 90263 99218"}],
  "caption": "Ghar me sabki pasand - ek combo! 👨‍👩‍👦 #Family #DesiFamily\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending family audio"},

 {"title": "Attar vs spray", "product": "oud_rose",
  "scenes": [{"img": "bg_smoke", "text": "ATTAR vs SPRAY?", "sub": "Confusion khatam!"},
             {"img": "oud_rose", "text": "EXTRAIT = Dono!", "sub": "Oil + Spray"},
             {"img": "oud_rose", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Attar lovers vs Spray lovers - FIGHT! 😂 Best of both worlds 👇 #AttarVsPerfume\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending debate audio"},

 {"title": "Gym fresh", "product": "good_vibe",
  "scenes": [{"img": "bg_smoke", "text": "GYM KE BAAD?", "sub": "Smell check!"},
             {"img": "good_vibe", "text": "GOOD VIBE", "sub": "Freshness ON"},
             {"img": "good_vibe", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
  "caption": "Gym bag essential! 💪 Paseene ko bolo bye #GymLife #Fitness\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending gym audio"},

 {"title": "Date ready", "product": "all_mine",
  "scenes": [{"img": "bg_rose", "text": "DATE PAR JA RAHE?", "sub": "1 cheez mat bhoolna"},
             {"img": "all_mine", "text": "ALL MINE", "sub": "Pocket me rakho"},
             {"img": "all_mine", "text": "Good luck!", "sub": "DM 90263 99218"}],
  "caption": "Date-night non-negotiable! 💘 #DateNight #DatingTips\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending romantic audio"},

 {"title": "Bestseller alert", "product": "combo",
  "scenes": [{"img": "combo", "text": "BESTSELLER!", "sub": "Sabse zyada bikta hai"},
             {"img": "oud_rose", "text": "OUD ROSE", "sub": "+ All Mine FREE feel"},
             {"img": "combo", "text": "ORDER NOW!", "sub": "DM 90263 99218"}],
  "caption": "Restock alert! 🔥 Sabse zyada bikne wala combo #Bestseller #Restock\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending hype audio"},

 {"title": "Smell rich", "product": "oud_rose",
  "scenes": [{"img": "oud_rose", "text": "SMELL RICH", "sub": "Spend smart!"},
             {"img": "bg_rose", "text": "Luxury Feel", "sub": "Budget price"},
             {"img": "oud_rose", "text": "DM for Price", "sub": "WhatsApp 90263 99218"}],
  "caption": "POV: 5000 wali feel, pocket-friendly price 🤯💛 #LuxuryOnBudget #SmellRich\n\n📩 Price: DM / WhatsApp 90263 99218",
  "audio": "Trending luxury audio"},

 {"title": "Thank you fam", "product": "combo",
  "scenes": [{"img": "combo", "text": "THANK YOU!", "sub": "Shabnal family"},
             {"img": "craft", "text": "Aapka Pyaar", "sub": "Hamari kamai"},
             {"img": "combo", "text": "Comment Favourite!", "sub": "Rose? Vibe? Mine?"}],
  "caption": "Thank you Shabnal family! 🙏💛 Comment me batao favourite 👇 #ThankYou #Grateful\n\n📩 Order: DM / WhatsApp 90263 99218",
  "audio": "Trending grateful audio"},
]

# ------------------------------------------------------- FESTIVAL SPECIALS
FESTIVALS = {
 "2026-09-25": {"name": "Ganpati Visarjan",
  "post": {"product": "good_vibe", "hook": "FESTIVE FRESH", "sub": "Visarjan look, complete with Good Vibe",
   "caption": "Bappa ka farewell... fresh mehak ke saath! 🙏✨\n\nVisarjan ke din bheed me bhi fresh raho - GOOD VIBE lagao aur blessings + compliments dono pao! 🌸\n\nGanpati Bappa Morya! 🙏\n\n📩 Order: DM / WhatsApp 90263 99218"},
  "reel": {"title": "Visarjan fresh", "product": "good_vibe",
   "scenes": [{"img": "bg_festive", "text": "VISARJAN DAY", "sub": "Fresh raho!"},
              {"img": "good_vibe", "text": "GOOD VIBE", "sub": "Festive fresh"},
              {"img": "good_vibe", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
   "caption": "Visarjan look complete! 🙏✨ #GanpatiVisarjan #FestiveFresh\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending devotional audio"}},

 "2026-10-11": {"name": "Navratri Day 1",
  "post": {"product": "oud_rose", "hook": "NAVRATRI NIGHTS", "sub": "9 raatein, 9 looks, 1 signature scent",
   "caption": "Navratri ki 9 raatein... 🪔💃 Garba-dandiya me nacho, par mehak aisi ki sab poochen!\n\nOUD ROSE - festive nights ka royal saathi! 👑🌹\n\nShubh Navratri! 🙏\n\n📩 Order: DM / WhatsApp 90263 99218"},
  "reel": {"title": "Navratri nights", "product": "oud_rose",
   "scenes": [{"img": "bg_festive", "text": "NAVRATRI!", "sub": "9 nights ready?"},
              {"img": "oud_rose", "text": "OUD ROSE", "sub": "Garba nights scent"},
              {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
   "caption": "Navratri fit + Oud Rose = UNSTOPPABLE! 💃🪔 #Navratri2026 #GarbaNights\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending garba audio"}},

 "2026-10-20": {"name": "Dussehra",
  "post": {"product": "combo", "hook": "VIJAYADASHAMI", "sub": "Burai par achchai ki jeet!",
   "caption": "Burai par ACHCHAI ki jeet! 🏹✨\n\nIs Dussehra apne andar ka best nikalo - aur bahar se Oud Rose ki royal mehak! Shubh Vijayadashami! 🙏🌹\n\n📩 Festive order: DM / WhatsApp 90263 99218"},
  "reel": {"title": "Dussehra vibes", "product": "combo",
   "scenes": [{"img": "bg_festive", "text": "HAPPY DUSSEHRA!", "sub": "Shubh Vijayadashami"},
              {"img": "combo", "text": "FESTIVE COMBO", "sub": "Gift + glow"},
              {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
   "caption": "Dussehra glow loading... 🏹✨ #Dussehra2026 #Vijayadashami\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending festive audio"}},

 "2026-10-29": {"name": "Karwa Chauth",
  "post": {"product": "combo", "hook": "KARWA CHAUTH", "sub": "Unke liye best gift - Shabnal Combo",
   "caption": "Karwa Chauth par UNKO kya gift dein? 🤔💝\n\nShabnal COMBO SET - elegant, royal aur dil choo lene wala! Patni khush = zindagi khush 😉🌙\n\n📩 Gift order (jaldi karo!): DM / WhatsApp 90263 99218"},
  "reel": {"title": "Karwa Chauth gift", "product": "combo",
   "scenes": [{"img": "bg_festive", "text": "KARWA CHAUTH", "sub": "Gift ready?"},
              {"img": "combo", "text": "COMBO SET", "sub": "Perfect gift"},
              {"img": "combo", "text": "ORDER NOW!", "sub": "DM 90263 99218"}],
   "caption": "Husbands, suno! 👂 Best Karwa Chauth gift idea 💝 #KarwaChauth #GiftForWife\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending romantic audio"}},

 "2026-11-06": {"name": "Dhanteras",
  "post": {"product": "combo", "hook": "SHUBH DHANTERAS", "sub": "Shubh kharidari - luxury gifting",
   "caption": "Shubh Dhanteras! 🪔✨ Aaj ke din shubh cheez kharido - apne liye AUR apno ke liye!\n\nShabnal COMBO - luxury jo budget me! Diwali gifting ki shopping aaj se shuru karo 🎁\n\n📩 Shubh order: DM / WhatsApp 90263 99218"},
  "reel": {"title": "Dhanteras shopping", "product": "combo",
   "scenes": [{"img": "bg_festive", "text": "DHANTERAS!", "sub": "Shubh kharidari"},
              {"img": "combo", "text": "LUXURY GIFTING", "sub": "Budget me!"},
              {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
   "caption": "Dhanteras shopping list me yeh ADD karo! 🪔✅ #Dhanteras2026 #ShubhKharidari\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending Diwali audio"}},

 "2026-11-08": {"name": "Diwali",
  "post": {"product": "oud_rose", "hook": "HAPPY DIWALI", "sub": "Roshni + khushboo = perfect Diwali",
   "caption": "🪔 SHUBH DEEPAVALI! 🪔\n\nDiyon ki roshni + OUD ROSE ki mehak = PERFECT Diwali! 🌹✨ Naye kapde, mithaas aur royal khushboo - taiyaari complete!\n\nShabnal parivaar ki taraf se Diwali ki dher saari shubhkamnayein! 🙏💛\n\n📩 Diwali order: DM / WhatsApp 90263 99218"},
  "reel": {"title": "Diwali glow", "product": "oud_rose",
   "scenes": [{"img": "bg_festive", "text": "HAPPY DIWALI!", "sub": "Shubh Deepavali"},
              {"img": "oud_rose", "text": "OUD ROSE", "sub": "Diwali glow"},
              {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
   "caption": "Diwali fit check + scent check! 🪔🌹 #Diwali2026 #HappyDiwali #Deepavali\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending Diwali audio"}},

 "2026-11-11": {"name": "Bhai Dooj",
  "post": {"product": "combo", "hook": "BHAI DOOJ", "sub": "Behen ko do khushboo wala pyaar!",
   "caption": "Behen ne tilak lagaya... bhai ne kya diya? 🤔💝\n\nIs Bhai Dooj GIFT me do Shabnal COMBO - behen khush, tikka vasool! 😄🎁\n\nShubh Bhai Dooj! 🙏\n\n📩 Gift order: DM / WhatsApp 90263 99218"},
  "reel": {"title": "Bhai Dooj gift", "product": "combo",
   "scenes": [{"img": "bg_festive", "text": "BHAI DOOJ!", "sub": "Gift socha?"},
              {"img": "combo", "text": "COMBO SET", "sub": "Behen ke liye"},
              {"img": "combo", "text": "ORDER NOW!", "sub": "DM 90263 99218"}],
   "caption": "Brothers, gift sorted! 🎁 #BhaiDooj #SiblingLove\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending sibling audio"}},

 "2026-11-15": {"name": "Chhath Puja",
  "post": {"product": "good_vibe", "hook": "CHHATH PUJA", "sub": "Surya dev ko pranam - fresh mann!",
   "caption": "Chhath Maiya ki kripa sab par bani rahe! 🙏🌅\n\nGhaat par subah ki aarti - fresh hawa, fresh mann, fresh mehak! GOOD VIBE ke saath pavitra din ki shuruaat 🌸\n\nJai Chhathi Maiya! 🙏\n\n📩 Order: DM / WhatsApp 90263 99218"},
  "reel": {"title": "Chhath morning", "product": "good_vibe",
   "scenes": [{"img": "bg_festive", "text": "JAI CHHATHI MAIYA", "sub": "Shubh Chhath"},
              {"img": "good_vibe", "text": "GOOD VIBE", "sub": "Fresh morning"},
              {"img": "good_vibe", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
   "caption": "Chhath morning vibes! 🌅🙏 #ChhathPuja2026 #ChhathiMaiya\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending Chhath audio"}},

 "2026-12-25": {"name": "Christmas",
  "post": {"product": "combo", "hook": "MERRY CHRISTMAS", "sub": "Santa se pehle, Shabnal combo!",
   "caption": "Merry Christmas! 🎄🎅 Secret Santa gift me kya dein? Shabnal COMBO - jo mile, woh khush!\n\nWinter + Oud Rose = PERFECT combo! ❄️🌹\n\n📩 Christmas order: DM / WhatsApp 90263 99218"},
  "reel": {"title": "Christmas gift", "product": "combo",
   "scenes": [{"img": "bg_festive", "text": "MERRY CHRISTMAS!", "sub": "Gift ready?"},
              {"img": "combo", "text": "COMBO SET", "sub": "Secret Santa pick"},
              {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"}],
   "caption": "Secret Santa gift SORTED! 🎄🎁 #Christmas2026 #SecretSanta\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending Christmas audio"}},

 "2026-12-31": {"name": "New Year Eve",
  "post": {"product": "oud_rose", "hook": "HAPPY NEW YEAR", "sub": "2027 - nayi shuruaat, nayi mehak!",
   "caption": "2027 ki pehli mehak - OUD ROSE! 🎉🌹\n\nNaya saal, naya confidence, naya signature scent! Party night ke liye royal taiyaari 👑✨\n\nHappy New Year 2027! 🥳\n\n📩 Party order: DM / WhatsApp 90263 99218"},
  "reel": {"title": "New Year party", "product": "oud_rose",
   "scenes": [{"img": "bg_smoke", "text": "2027 LOADING...", "sub": "Party ready?"},
              {"img": "oud_rose", "text": "OUD ROSE", "sub": "New Year scent"},
              {"img": "combo", "text": "HAPPY NEW YEAR!", "sub": "DM 90263 99218"}],
   "caption": "2027 glow-up starts NOW! 🎉 #NewYear2027 #PartyReady\n\n📩 Order: DM / WhatsApp 90263 99218", "audio": "Trending New Year audio"}},
}

WEEKEND_LINE = "\n\n🎁 WEEKEND SPECIAL: Aaj order karo - DM / WhatsApp 90263 99218!"

START_DATE = "2026-09-21"
