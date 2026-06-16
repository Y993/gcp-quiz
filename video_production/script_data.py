# -*- coding: utf-8 -*-
"""
script_data.py — narration + telop + visual spec for the 『人間失格』 videos.
Public-domain work (太宰治, d.1948). Narration is original analysis; only the
famous opening phrase is quoted briefly.

Each scene: dict(id, narr=<spoken>, telop=<on-screen>, bg=<callable name>,
bgargs=<dict>, pos=<telop position>, telop_px=<optional>)
"""

# ----------------------------------------------------------------------------
# LONG-FORM (約9分・16:9)
# ----------------------------------------------------------------------------
LONG = [
    # --- intro 0:00-0:30 ---
    dict(id="L00", bg="title", bgargs=dict(main="人間失格", sub="太宰治　なぜ今も刺さるのか"),
         narr="太宰治、人間失格。", telop=None),
    dict(id="L01", bg="mask", bgargs=dict(crack=0.5),
         narr="「恥の多い生涯を送って来ました」。この一文だけで、自分の人生を要約できてしまう。そう感じる人は、決して少なくありません。",
         telop="「恥の多い生涯を送って来ました」", pos="bottom"),
    dict(id="L02", bg="mask", bgargs=dict(crack=0.7),
         narr="人間失格は、八十年以上前に書かれた小説です。けれど、そこに描かれた生きづらさは、むしろ今のほうが多くの人に刺さっている。",
         telop="80年前の小説が、今刺さる", pos="bottom"),
    dict(id="L03", bg="dark", bgargs=dict(),
         narr="多くの人は、これを暗い私小説のひとことで片づけてしまう。でも、その奥にある本当の怖さを見落としています。",
         telop="「暗い私小説」では片づかない", pos="bottom"),
    dict(id="L04", bg="dark", bgargs=dict(tint=(20,28,40)),
         narr="この動画では、あらすじ、三つの読み解き、そして現代との接続、という順番で見ていきます。最後に、なぜこの失格が、現代でむしろ増えているのかを話します。",
         telop="あらすじ→3つの読み解き→現代", pos="bottom"),

    # --- synopsis 0:30-2:20 ---
    dict(id="L05", bg="title", bgargs=dict(main="あらすじ", sub="道化を演じた男の手記"),
         narr="まず、あらすじです。", telop=None),
    dict(id="L06", bg="crowd", bgargs=dict(),
         narr="主人公の名は、大庭葉蔵。彼は幼いころから、人間というものが、どうしても理解できませんでした。人が何を考え、なぜ怒り、なぜ笑うのか。それが分からず、ただ恐ろしかった。",
         telop="人間が、理解できない・怖い", pos="bottom"),
    dict(id="L07", bg="crowd", bgargs=dict(),
         narr="そこで葉蔵が選んだのが、道化を演じることでした。わざとおどけて、人を笑わせる。そうやって、自分を世界に滑り込ませようとした。",
         telop="選んだのは「道化」を演じること", pos="bottom"),
    dict(id="L08", bg="dark", bgargs=dict(tint=(34,22,22)),
         narr="けれど、その仮面はしだいに彼自身を追い詰めていきます。酒、女性、そして薬物。葉蔵はあらゆるものに溺れ、転落していきます。",
         telop="酒・女性・薬物へ転落", pos="bottom"),
    dict(id="L09", bg="mask", bgargs=dict(crack=0.9),
         narr="そして最後、彼は自らにこう烙印を押すのです。もはや、自分は人間ではない。人間、失格だ、と。",
         telop="自らに押す「人間、失格」の烙印", pos="bottom"),

    # --- peak1 25% ---
    dict(id="L10", bg="dark", bgargs=dict(tint=(10,10,16)),
         narr="さて、ここからが本題です。多くの人が見落とすのは、葉蔵が怖がっていたのは、失敗ではない、ということです。",
         telop="彼が怖れたのは「失敗」ではない", pos="center", telop_px=72),

    # --- reading1 道化 2:20-4:20 ---
    dict(id="L11", bg="title", bgargs=dict(main="読み解き①", sub="“道化”の正体"),
         narr="読み解きの一つめ。道化の正体です。", telop=None),
    dict(id="L12", bg="crowd", bgargs=dict(),
         narr="葉蔵にとっての道化は、ただのお調子者ではありません。それは、人間が怖いからこそ、先回りして相手を笑わせる、必死の防衛本能でした。",
         telop="道化＝必死の防衛本能", pos="bottom"),
    dict(id="L13", bg="crowd", bgargs=dict(),
         narr="嫌われる前に、笑わせて、無害な存在になる。攻撃される前に、自分から道化になって、相手の警戒を解く。つまり彼の笑顔は、笑顔のかたちをした、防具だったのです。",
         telop="その笑顔は「防具」だった", pos="bottom"),
    dict(id="L14", bg="mask", bgargs=dict(crack=0.3),
         narr="ここに、人間失格の本当の怖さがあります。彼は、嘘をついて人をだましているのではない。むしろ、本当の自分を見せたら拒絶される、という確信に、ずっと怯えている。",
         telop="本当の自分を見せたら、拒絶される", pos="bottom"),
    dict(id="L15", bg="mask", bgargs=dict(crack=0.5),
         narr="だから彼は、誰よりも他人に気をつかい、誰よりも空気を読み、そして誰よりも疲れていく。やさしさと、生きづらさは、しばしば同じ根っこから生えています。",
         telop="やさしさと生きづらさは同じ根", pos="bottom"),

    # --- peak2 50% + midroll ---
    dict(id="L16", bg="dark", bgargs=dict(),
         narr="ここで、いったん区切ります。",
         telop=None, pos="center"),

    # --- reading2 失格 4:20-6:20 ---
    dict(id="L17", bg="title", bgargs=dict(main="読み解き②", sub="“失格”とは何か"),
         narr="読み解きの二つめ。失格とは、いったい何か。", telop=None),
    dict(id="L18", bg="crowd", bgargs=dict(),
         narr="人間、失格。これは、とても残酷な言葉です。なぜなら、これは他人が下した判定ではなく、葉蔵が、自分自身に下した判決だからです。",
         telop="「失格」は自分が自分に下した判決", pos="bottom"),
    dict(id="L19", bg="crowd", bgargs=dict(),
         narr="社会にうまく馴染めない。人とまっすぐ向き合えない。その自分を、彼は欠陥品とみなし、人間の資格がない、と断じてしまう。",
         telop="馴染めない自分＝欠陥品、と断じる", pos="bottom"),
    dict(id="L20", bg="dark", bgargs=dict(tint=(28,20,34)),
         narr="でも、ここで立ち止まって考えてみてください。馴染めないことは、本当に失格なのでしょうか。そして、その失格を、いったい誰が決めたのでしょうか。",
         telop="その「失格」を、誰が決めた?", pos="bottom"),
    dict(id="L21", bg="dark", bgargs=dict(tint=(20,20,28)),
         narr="本当は、誰も決めていません。葉蔵を失格にしたのは、世間ではなく、世間という名の、彼自身のまなざしでした。私たちもまた、自分で自分を裁いてしまうことがあります。",
         telop="裁いているのは、自分のまなざし", pos="bottom"),

    # --- peak3 75% ---
    dict(id="L22", bg="phone", bgargs=dict(),
         narr="そして、ここで気づくはずです。これ、今の私たちと、同じではないか、と。",
         telop="これ、今の私たちと同じでは?", pos="center", telop_px=72),

    # --- reading3 現代 6:20-7:50 ---
    dict(id="L23", bg="title", bgargs=dict(main="読み解き③", sub="現代との接続"),
         narr="読み解きの三つめ。現代との接続です。", telop=None),
    dict(id="L24", bg="phone", bgargs=dict(),
         narr="私たちは毎日、いいねをもらうための自分を演じています。波風を立てないように、空気を読み、嫌われないように、笑顔の絵文字を足す。それは、葉蔵の道化と、構造がそっくりです。",
         telop="“いいね”用の自分＝現代の道化", pos="bottom"),
    dict(id="L25", bg="phone", bgargs=dict(),
         narr="そして、仮面をかぶり続けた人ほど、ある日ふと、こう思うのです。本当の自分が、どこにあるのか、もう分からない、と。",
         telop="本当の自分が、分からない", pos="bottom"),
    dict(id="L26", bg="dark", bgargs=dict(tint=(18,22,32)),
         narr="八十年前、太宰はこの感覚を、命をかけて言葉にしました。人間失格は、暗い過去の小説ではありません。むしろ、つながりすぎた現代を、先に予言していた一冊なのです。",
         telop="つながりすぎた時代を予言した一冊", pos="bottom"),

    # --- summary 7:50-8:30 ---
    dict(id="L27", bg="manuscript", bgargs=dict(),
         narr="太宰治自身もまた、生涯にわたって生きづらさを抱え、何度も死の淵に立った人でした。だからこそ、この物語には、つくりものではない痛みが宿っています。",
         telop="作り物ではない、本物の痛み", pos="bottom"),
    dict(id="L28", bg="mask", bgargs=dict(crack=0.4),
         narr="最初の問いに戻りましょう。なぜ、この失格が、現代でむしろ増えているのか。それは、私たちが、かつてないほど多くの仮面を、同時にかぶらされているからです。",
         telop="今こそ仮面が増えている", pos="bottom"),
    dict(id="L29", bg="dark", bgargs=dict(tint=(26,22,30)),
         narr="でも、忘れないでください。失格かどうかを決める資格は、本当は、世間にも、誰にもありません。あなたを失格にできるのは、あなた自身の、まなざしだけです。",
         telop="あなたを失格にできるのは、あなただけ", pos="bottom"),

    # --- CTA 8:30-9:00 ---
    dict(id="L30", bg="dark", bgargs=dict(tint=(22,20,28)),
         narr="あなたにも、道化を演じてしまう瞬間が、ありますか。よかったら、コメントで教えてください。",
         telop="あなたも“道化”を演じてる瞬間、ある?", pos="bottom"),
    dict(id="L31", bg="title", bgargs=dict(main="次は『走れメロス』", sub="チャンネル登録で次の解説を"),
         narr="次回は、太宰治、走れメロスの、裏の顔を解説します。チャンネル登録で、お待ちください。",
         telop=None),
]

# ----------------------------------------------------------------------------
# SHORTS (各30-40秒・9:16)
# ----------------------------------------------------------------------------
SHORT1 = [
    dict(id="S1a", bg="mask", bgargs=dict(crack=0.6),
         narr="この一文で始まる小説、知ってる?",
         telop="恥の多い生涯を送って来ました", pos="bottom", telop_px=64),
    dict(id="S1b", bg="crowd", bgargs=dict(),
         narr="太宰治、人間失格。人間が怖くて、道化を演じ続けた男の手記。",
         telop="道化を演じた男", pos="bottom", telop_px=76),
    dict(id="S1c", bg="mask", bgargs=dict(crack=0.9),
         narr="酒、女性、薬に溺れ、最後は人間、失格と、自らに烙印を押す。",
         telop="失格の烙印", pos="bottom", telop_px=76),
    dict(id="S1d", bg="phone", bgargs=dict(),
         narr="でもこの生きづらさ、今のSNS時代に、むしろ増えてる。",
         telop="80年後の私たち", pos="bottom", telop_px=76),
    dict(id="S1e", bg="mask", bgargs=dict(crack=0.5),
         narr="なぜ刺さるのか、フル解説は長尺で。",
         telop="続きは長尺で →", pos="center", telop_px=80),
]

SHORT2 = [
    dict(id="S2a", bg="phone", bgargs=dict(),
         narr="その笑顔、防具になってない?",
         telop="その笑顔、防具じゃない?", pos="center", telop_px=84),
    dict(id="S2b", bg="crowd", bgargs=dict(),
         narr="人間失格の葉蔵は、人間が怖いから、先回りして笑わせる、道化を演じた。",
         telop="怖いから、笑わせる", pos="bottom", telop_px=72),
    dict(id="S2c", bg="phone", bgargs=dict(),
         narr="これ、SNSでいいねされる自分を演じるのと、ほぼ同じ構造。",
         telop="“いいね”用の自分", pos="bottom", telop_px=76),
    dict(id="S2d", bg="mask", bgargs=dict(crack=0.6),
         narr="八十年前に太宰は、この仮面の苦しさを書いていた。",
         telop="80年前に予言", pos="bottom", telop_px=76),
    dict(id="S2e", bg="mask", bgargs=dict(crack=0.4),
         narr="本当の自分って何? 続きは長尺で。",
         telop="続きは長尺で →", pos="center", telop_px=80),
]

SHORT3 = [
    dict(id="S3a", bg="mirror", bgargs=dict(),
         narr="本当の自分が分からない。それ、八十年前に書かれてた。",
         telop="本当の自分、分かる?", pos="top", telop_px=80),
    dict(id="S3b", bg="crowd", bgargs=dict(),
         narr="人間失格の核心は、社会に馴染めない自分を、失格と断じる残酷さ。",
         telop="誰が失格を決める?", pos="bottom", telop_px=72),
    dict(id="S3c", bg="dark", bgargs=dict(tint=(20,20,30)),
         narr="でも、馴染めないイコール失格なんて、本当は誰も決めてない。",
         telop="それ、本当?", pos="center", telop_px=84),
    dict(id="S3d", bg="manuscript", bgargs=dict(),
         narr="太宰はその問いを、命がけで書き残した。",
         telop="命がけの問い", pos="bottom", telop_px=76),
    dict(id="S3e", bg="mirror", bgargs=dict(),
         narr="全部の読み解きは、長尺で。",
         telop="続きは長尺で →", pos="center", telop_px=80),
]

SHORTS = {"short1": SHORT1, "short2": SHORT2, "short3": SHORT3}
