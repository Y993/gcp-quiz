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
    # --- intro 0:00-0:40 ---
    dict(id="L00", bg="title", bgargs=dict(main="人間失格", sub="太宰治　なぜ今も刺さるのか"),
         narr="太宰治、人間失格。", telop=None),
    dict(id="L01", bg="mask", bgargs=dict(crack=0.5),
         narr="「恥の多い生涯を送って来ました」。この一文だけで、自分の人生を要約できてしまう。そう感じてしまう人は、決して少なくありません。",
         telop="「恥の多い生涯を送って来ました」", pos="bottom"),
    dict(id="L02", bg="mask", bgargs=dict(crack=0.7),
         narr="人間失格は、八十年以上前に書かれた小説です。けれど、そこに描かれた生きづらさは、色あせるどころか、むしろ今のほうが、多くの人の胸に刺さっている。",
         telop="80年前の小説が、今こそ刺さる", pos="bottom"),
    dict(id="L03", bg="dark", bgargs=dict(),
         narr="多くの人は、これを暗い私小説のひとことで片づけてしまいます。でも、その奥にある本当の怖さと、本当のやさしさを、見落としているのです。",
         telop="「暗い私小説」では片づかない", pos="bottom"),
    dict(id="L04", bg="dark", bgargs=dict(tint=(20,28,40)),
         narr="この動画では、物語の構造、あらすじ、三つの読み解き、そして現代との接続、という順番で見ていきます。最後に、なぜこの失格が、現代でむしろ増えているのかを話します。",
         telop="構造→あらすじ→3つの読み解き→現代", pos="bottom"),

    # --- framing device: three photographs (はしがき) ---
    dict(id="L05", bg="title", bgargs=dict(main="三葉の写真", sub="物語を縁取る、はしがき"),
         narr="まず、この小説の、巧みな仕掛けから。", telop=None),
    dict(id="L06", bg="manuscript", bgargs=dict(),
         narr="人間失格は、いきなり主人公が語り出すのではありません。冒頭で、ある人物が、男の三枚の写真を眺める場面から始まります。",
         telop="物語は「3枚の写真」から始まる", pos="bottom"),
    dict(id="L07", bg="manuscript", bgargs=dict(),
         narr="幼い子どもの写真、美しい学生の写真、そして、年齢も表情も読み取れない、不気味な最後の写真。語り手は言います。こんなに奇妙な男の顔を、見たことがない、と。この三枚が、これから読む手記の、額縁になります。",
         telop="子ども→学生→不気味な顔", pos="bottom"),

    # --- synopsis / three notebooks ---
    dict(id="L08", bg="title", bgargs=dict(main="あらすじ", sub="道化を演じた男の、三つの手記"),
         narr="では、その男の手記、あらすじです。", telop=None),
    dict(id="L09", bg="crowd", bgargs=dict(),
         narr="主人公の名は、大庭葉蔵。裕福な家に生まれながら、彼は幼いころから、人間というものが、どうしても理解できませんでした。人が何を考え、なぜ怒り、なぜ笑うのか。それが分からず、ただ、恐ろしかった。",
         telop="人間が、理解できない・怖い", pos="bottom"),
    dict(id="L10", bg="crowd", bgargs=dict(),
         narr="そこで葉蔵が編み出したのが、道化を演じることでした。わざとおどけ、ふざけて、人を笑わせる。そうやって、自分を世界のすみに、そっと滑り込ませようとしたのです。",
         telop="編み出した「道化」という生存戦略", pos="bottom"),
    dict(id="L11", bg="crowd", bgargs=dict(),
         narr="ところが学生時代、竹一という同級生だけが、その芝居を見抜きます。鉄棒でわざと失敗した葉蔵に、竹一はこうささやく。わざ、と。わざとだろう、と。完璧だったはずの仮面に、初めて、ひびが入った瞬間でした。",
         telop="竹一だけが見抜いた「わざ、と」", pos="bottom"),
    dict(id="L12", bg="dark", bgargs=dict(tint=(34,22,22)),
         narr="やがて彼は、堀木という遊び仲間に引きずられ、酒と、煙草と、女性の世界へ落ちていきます。心中事件を起こし、女性だけが死に、自分は生き残る。その罪の意識が、さらに彼をむしばんでいく。",
         telop="酒・女性・心中、そして罪", pos="bottom"),
    dict(id="L13", bg="dark", bgargs=dict(tint=(28,20,30)),
         narr="一度は、ヨシ子という、人を疑うことを知らない若い妻と出会い、彼は救われかけます。けれど、その純粋なヨシ子が、ある事件で傷つけられたとき、葉蔵の心は、決定的に壊れてしまう。",
         telop="信じる妻・ヨシ子との破局", pos="bottom"),
    dict(id="L14", bg="mask", bgargs=dict(crack=0.9),
         narr="アルコール、そして薬物。彼はついに精神の病院へ入れられ、人間としての一切を、奪われたと感じます。そして、自らにこう烙印を押すのです。もはや、自分は人間ではない。人間、失格だ、と。",
         telop="自らに押す「人間、失格」の烙印", pos="bottom"),

    # --- peak1 25% ---
    dict(id="L15", bg="dark", bgargs=dict(tint=(10,10,16)),
         narr="さて、ここからが本題です。多くの人が見落とすのは、葉蔵が本当に怖がっていたのは、失敗そのものではない、ということです。",
         telop="彼が怖れたのは「失敗」ではない", pos="center", telop_px=72),

    # --- reading1 道化 ---
    dict(id="L16", bg="title", bgargs=dict(main="読み解き①", sub="“道化”の正体"),
         narr="読み解きの、一つめ。道化の正体です。", telop=None),
    dict(id="L17", bg="crowd", bgargs=dict(),
         narr="葉蔵にとっての道化は、ただのお調子者ではありません。それは、人間が怖いからこそ、攻撃される前に先回りして、相手を笑わせておく。必死の、防衛本能でした。",
         telop="道化＝必死の防衛本能", pos="bottom"),
    dict(id="L18", bg="crowd", bgargs=dict(),
         narr="嫌われる前に、笑わせて、無害な存在になる。怒られる前に、自分から滑稽になって、相手の警戒を解いてしまう。つまり彼の笑顔は、笑顔のかたちをした、分厚い防具だったのです。",
         telop="その笑顔は「防具」だった", pos="bottom"),
    dict(id="L19", bg="mask", bgargs=dict(crack=0.3),
         narr="ここに、人間失格の本当の怖さがあります。彼は、嘘をついて人をだまして楽しんでいるのではない。むしろ、本当の自分を見せたら、必ず拒絶される、という確信に、生まれたときから、ずっと怯えている。",
         telop="本当の自分を見せたら、拒絶される", pos="bottom"),
    dict(id="L20", bg="mask", bgargs=dict(crack=0.5),
         narr="だからこそ彼は、誰よりも他人に気をつかい、誰よりも空気を読み、そして、誰よりも深く疲れていく。やさしさと、生きづらさは、しばしば、まったく同じ根っこから生えているのです。",
         telop="やさしさと生きづらさは同じ根", pos="bottom"),

    # --- peak2 50% + midroll ---
    dict(id="L21", bg="dark", bgargs=dict(),
         narr="さて、ここで物語は、大きく折り返します。",
         telop=None, pos="center"),

    # --- reading2 失格 ---
    dict(id="L22", bg="title", bgargs=dict(main="読み解き②", sub="“失格”とは何か"),
         narr="読み解きの、二つめ。失格とは、いったい何か。", telop=None),
    dict(id="L23", bg="crowd", bgargs=dict(),
         narr="人間、失格。これは、とても残酷な言葉です。なぜなら、これは他人が下した判定ではなく、葉蔵が、自分自身に向かって下した、有罪判決だからです。",
         telop="「失格」は自分が自分に下した判決", pos="bottom"),
    dict(id="L24", bg="crowd", bgargs=dict(),
         narr="社会にうまく馴染めない。人とまっすぐ向き合えない。お金のことも、世間の常識も、よく分からない。そんな自分を、彼は欠陥品とみなし、人間の資格がない、と断じてしまう。",
         telop="馴染めない自分＝欠陥品、と断じる", pos="bottom"),
    dict(id="L25", bg="dark", bgargs=dict(tint=(28,20,34)),
         narr="でも、ここで一度、立ち止まって考えてみてください。馴染めないことは、本当に、失格なのでしょうか。そして、その失格という判定を、いったい、誰が決めたのでしょうか。",
         telop="その「失格」を、誰が決めた?", pos="bottom"),
    dict(id="L26", bg="dark", bgargs=dict(tint=(20,20,28)),
         narr="本当は、誰も決めていません。葉蔵を失格にしたのは、世間ではなく、世間という名を借りた、彼自身の、きびしすぎるまなざしでした。私たちもまた、誰に言われたわけでもないのに、自分で自分を、裁いてしまうことがあります。",
         telop="裁いているのは、自分のまなざし", pos="bottom"),

    # --- peak3 75% ---
    dict(id="L27", bg="phone", bgargs=dict(),
         narr="そして、ここで、はっと気づくはずです。これは、八十年前の他人の話ではなく、今の、私たちの話ではないか、と。",
         telop="これ、今の私たちと同じでは?", pos="center", telop_px=72),

    # --- reading3 現代 ---
    dict(id="L28", bg="title", bgargs=dict(main="読み解き③", sub="現代との接続"),
         narr="読み解きの、三つめ。現代との接続です。", telop=None),
    dict(id="L29", bg="phone", bgargs=dict(),
         narr="私たちは毎日、いいねをもらうための自分を演じています。波風を立てないように空気を読み、嫌われないように、笑顔の絵文字を足す。それは、葉蔵が演じた道化と、驚くほど、構造がそっくりです。",
         telop="“いいね”用の自分＝現代の道化", pos="bottom"),
    dict(id="L30", bg="phone", bgargs=dict(),
         narr="そして、仮面をかぶり続けた人ほど、ある日ふと、こう思ってしまうのです。みんなに合わせている、この自分。本当の自分は、いったい、どこにあるのか、もう分からない、と。",
         telop="本当の自分が、分からない", pos="bottom"),
    dict(id="L31", bg="dark", bgargs=dict(tint=(18,22,32)),
         narr="八十年前、太宰はこの感覚を、命をかけて、言葉にしました。人間失格は、暗い過去の小説ではありません。むしろ、つながりすぎて、誰もが演技を強いられる現代を、先回りして予言していた、一冊なのです。",
         telop="つながりすぎた時代を予言した一冊", pos="bottom"),

    # --- Dazai biography ---
    dict(id="L32", bg="title", bgargs=dict(main="太宰治という人", sub="物語の外側にある、本物の痛み"),
         narr="ここで、作者、太宰治自身に、目を向けてみましょう。", telop=None),
    dict(id="L33", bg="manuscript", bgargs=dict(),
         narr="太宰治もまた、生涯にわたって生きづらさを抱え、何度も、死の淵に立った人でした。人間失格を書き上げたその年、彼は、玉川上水に身を投げ、三十八歳で、この世を去ります。",
         telop="人間失格を書いた年に、世を去る", pos="bottom"),
    dict(id="L34", bg="manuscript", bgargs=dict(),
         narr="だからこの物語の痛みは、つくりものではありません。葉蔵の手記は、太宰自身の、血のにじむような自己告白でもある。それが、八十年たっても、読む人の心を、まっすぐに撃ち抜く理由です。",
         telop="作り物ではない、本物の痛み", pos="bottom"),

    # --- the ending reframe (the madam's words) ---
    dict(id="L35", bg="dark", bgargs=dict(tint=(24,20,28)),
         narr="そして、物語の最後。葉蔵を知るバーのマダムが、ぽつりと、こう漏らします。私たちの知っている葉ちゃんは、とても素直で、よく気がきいて、お酒さえ飲まなければ、いえ、飲んでも、神様みたいに、いい子でした、と。",
         telop="マダム「神様みたいに、いい子でした」", pos="bottom"),
    dict(id="L36", bg="mask", bgargs=dict(crack=0.2),
         narr="自分を、人間失格だと断じた男。でも、他人の目には、神様みたいに、いい子に映っていた。この、決定的なすれ違いこそが、この小説の、最後の、そして最大の問いかけなのです。",
         telop="本人の評価と、他人の評価のすれ違い", pos="bottom"),

    # --- summary ---
    dict(id="L37", bg="mask", bgargs=dict(crack=0.4),
         narr="最初の問いに戻りましょう。なぜ、この失格が、現代でむしろ増えているのか。それは、私たちが、かつてないほど多くの仮面を、たくさんの画面の向こうで、同時にかぶらされているからです。",
         telop="今こそ、仮面が増えている", pos="bottom"),
    dict(id="L38", bg="dark", bgargs=dict(tint=(26,22,30)),
         narr="でも、どうか、忘れないでください。あなたが失格かどうかを決める資格は、本当は、世間にも、他の誰にも、ありません。あなたを失格にできるのは、たった一人、あなた自身の、まなざしだけなのです。",
         telop="あなたを失格にできるのは、あなただけ", pos="bottom"),

    # --- CTA ---
    dict(id="L39", bg="dark", bgargs=dict(tint=(22,20,28)),
         narr="あなたにも、ふと、道化を演じてしまう瞬間が、ありますか。よかったら、コメントで、教えてください。",
         telop="あなたも“道化”を演じてる瞬間、ある?", pos="bottom"),
    dict(id="L40", bg="title", bgargs=dict(main="次は『走れメロス』", sub="チャンネル登録で次の解説を"),
         narr="次回は、太宰治、走れメロスの、知られざる裏の顔を、解説します。チャンネル登録をして、お待ちください。最後まで見てくれて、ありがとうございました。",
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
